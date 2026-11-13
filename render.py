"""Backwards-compatible wrapper. The renderer now lives in tools/render.py (system Chrome, font + overflow checks).
usage: python3 render.py <template.html> <out.jpg> [feed|story]"""
import os, runpy, sys
sys.argv[0] = os.path.join(os.path.dirname(os.path.abspath(__file__)), "tools", "render.py")
runpy.run_path(sys.argv[0], run_name="__main__")
