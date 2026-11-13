#!/usr/bin/env python3
"""Render a LinkWin post HTML template to an Instagram-ready JPEG with headless Chrome.

usage:
  python3 tools/render.py <template.html> <out.jpg> [feed|story] [--quality 92]

  feed  = 1080x1350 (4:5)   story = 1080x1920 (9:16; adds class="story" to <html>)

What it does
  * opens the template from disk (file://, so ../brand, ../fonts, ../photos resolve),
  * waits for document.fonts.ready and for every <img> / CSS background to load,
  * fails loudly if a required web font did not load (Arabic-script text would fall back to a
    system face and look wrong), or if any element with text spills outside the canvas,
  * screenshots at device_scale_factor 1 and writes a baseline JPEG (sRGB, 4:4:4 chroma).

Shaping: Chrome uses HarfBuzz, so Persian/Arabic joining, lam-alef ligatures, kashida-free RTL and
Cyrillic all render correctly as long as the template sets dir="rtl" (FA/AR) and loads an
Arabic-script face (Vazirmatn, IBM Plex Sans Arabic, Noto Naskh/Kufi Arabic, Lalezar) from brand/fonts.css.

Requirements: pip install --user --break-system-packages playwright pillow
              Chrome at /usr/bin/google-chrome (override with $CHROME). No playwright browser download needed.
"""
import argparse, io, os, sys
from playwright.sync_api import sync_playwright
from PIL import Image

SIZES = {"feed": (1080, 1350), "story": (1080, 1920)}
CHROME = os.environ.get("CHROME", "/usr/bin/google-chrome")

CHECK_JS = r"""
() => {
  const W = innerWidth, H = innerHeight, bad = [];
  for (const el of document.querySelectorAll('body *')) {
    const own = [...el.childNodes].some(n => n.nodeType === 3 && n.textContent.trim());
    if (!own) continue;
    const r = el.getBoundingClientRect();
    if (r.width === 0 && r.height === 0) continue;
    if (r.left < -1 || r.top < -1 || r.right > W + 1 || r.bottom > H + 1)
      bad.push(`${el.tagName}.${el.className}: ${Math.round(r.left)},${Math.round(r.top)},${Math.round(r.right)},${Math.round(r.bottom)}`);
    if (el.scrollWidth > el.clientWidth + 2 && getComputedStyle(el).overflow === 'hidden')
      bad.push(`${el.tagName}.${el.className}: clipped horizontally`);
  }
  const fonts = [...document.fonts].filter(f => f.status === 'error').map(f => f.family + ' ' + f.weight);
  const imgs = [...document.images].filter(i => !i.complete || i.naturalWidth === 0).map(i => i.src);
  return {bad, fonts, imgs};
}
"""

def render(src, out, mode="feed", quality=92, strict=True):
    w, h = SIZES[mode]
    src = os.path.abspath(src)
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path=CHROME, args=["--font-render-hinting=none", "--force-color-profile=srgb"])
        pg = b.new_page(viewport={"width": w, "height": h}, device_scale_factor=1)
        pg.goto("file://" + src, wait_until="networkidle")
        if mode == "story":
            pg.evaluate("document.documentElement.classList.add('story')")
        pg.evaluate("document.fonts.ready.then(() => true)")
        pg.evaluate("Promise.all([...document.fonts].filter(f=>f.status==='unloaded').map(f=>f.load().catch(()=>null)))")
        pg.wait_for_timeout(400)
        res = pg.evaluate(CHECK_JS)
        png = pg.screenshot(type="png", full_page=False)
        b.close()
    Image.open(io.BytesIO(png)).convert("RGB").save(out, "JPEG", quality=quality, subsampling=0, optimize=True)
    problems = res["bad"] + [f"font failed: {f}" for f in res["fonts"]] + [f"image failed: {i}" for i in res["imgs"]]
    for pr in problems:
        print("  ! " + pr, file=sys.stderr)
    print(f"{out}  {w}x{h}  {os.path.getsize(out)//1024} KB  {'OK' if not problems else str(len(problems)) + ' problem(s)'}")
    if problems and strict:
        sys.exit(2)
    return problems

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("template"); ap.add_argument("out")
    ap.add_argument("mode", nargs="?", default="feed", choices=list(SIZES))
    ap.add_argument("--quality", type=int, default=92)
    ap.add_argument("--no-strict", action="store_true", help="write the JPEG even if checks fail")
    a = ap.parse_args()
    render(a.template, a.out, a.mode, a.quality, not a.no_strict)
