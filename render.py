"""Render an HTML template to a JPEG for Instagram.
usage: python3 render.py <template.html> <out.jpg> [feed|story]
feed = 1080x1350 (4:5 portrait), story = 1080x1920 (9:16)."""
import sys, os
from playwright.sync_api import sync_playwright
src, out = os.path.abspath(sys.argv[1]), sys.argv[2]
mode = sys.argv[3] if len(sys.argv) > 3 else "feed"
h = 1920 if mode == "story" else 1350
with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page(viewport={"width": 1080, "height": h}, device_scale_factor=1)
    pg.goto("file://" + src)
    if mode == "story":
        pg.evaluate("document.documentElement.classList.add('story')")
    pg.evaluate("document.fonts.ready")
    pg.wait_for_timeout(500)
    pg.screenshot(path=out, type="jpeg", quality=93)
    b.close()
