#!/usr/bin/env python3
"""Trace LinkWin's official transparent logo files into clean single-colour SVG marks.

Sources (official, from https://www.linkwinco.com/assets/img/, saved in brand/mark/):
  source-seal-light.png       -> brand/mark/linkwin-seal.svg        (seal: frame + 赢)
  source-logo-full-light.png  -> brand/mark/linkwin-logo-full.svg   (seal + 链赢贸易 + LinkWin Trading)
The trace follows the official artwork's alpha channel exactly (4x Lanczos upsample, 50 % threshold, potrace curves);
nothing is redrawn. Output paths use fill="currentColor" so templates colour them with CSS (`color:#AC3E33`).
usage: python3 tools/trace_logo.py
"""
import os, numpy as np, potrace
from PIL import Image
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
JOBS = [("source-seal-light.png", "linkwin-seal.svg"), ("source-logo-full-light.png", "linkwin-logo-full.svg")]
UP = 4

def trace(src, dst):
    a = Image.open(src).convert("RGBA").getchannel("A")
    w, h = a.size
    a = a.resize((w * UP, h * UP), Image.LANCZOS)
    bm = potrace.Bitmap(np.array(a) <= 127)  # potracer traces the False/dark side; invert so the opaque artwork is the shape
    path = bm.trace(turdsize=8, turnpolicy=potrace.POTRACE_TURNPOLICY_MINORITY, alphamax=1.0, opticurve=True, opttolerance=0.2)
    d = []
    for curve in path:
        s = curve.start_point
        d.append(f"M{s.x/UP:.2f},{s.y/UP:.2f}")
        for seg in curve.segments:
            if seg.is_corner:
                d.append(f"L{seg.c.x/UP:.2f},{seg.c.y/UP:.2f}L{seg.end_point.x/UP:.2f},{seg.end_point.y/UP:.2f}")
            else:
                d.append(f"C{seg.c1.x/UP:.2f},{seg.c1.y/UP:.2f} {seg.c2.x/UP:.2f},{seg.c2.y/UP:.2f} {seg.end_point.x/UP:.2f},{seg.end_point.y/UP:.2f}")
        d.append("Z")
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}">'
           f'<path fill="currentColor" fill-rule="evenodd" d="{"".join(d)}"/></svg>\n')
    open(dst, "w").write(svg)
    print(dst, w, h, len(svg) // 1024, "KB")

# crops of the full-logo trace (same paths, different viewBox): measured from the source alpha rows
CROPS = {"linkwin-wordmark-cn.svg": "9 352 623 134", "linkwin-wordmark-en.svg": "172 508 301 40"}

if __name__ == "__main__":
    for s, d in JOBS:
        trace(os.path.join(ROOT, "brand/mark", s), os.path.join(ROOT, "brand/mark", d))
    import re
    full = open(os.path.join(ROOT, "brand/mark/linkwin-logo-full.svg")).read()
    for name, vb in CROPS.items():
        w, h = vb.split()[2:]
        out = re.sub(r'viewBox="[^"]+" width="\d+" height="\d+"', f'viewBox="{vb}" width="{w}" height="{h}"', full)
        open(os.path.join(ROOT, "brand/mark", name), "w").write(out); print(name, vb)
