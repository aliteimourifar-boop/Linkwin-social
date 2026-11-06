import sys
from playwright.sync_api import sync_playwright
src, out = sys.argv[1], sys.argv[2]
h = int(sys.argv[3]) if len(sys.argv) > 3 else 1350
with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page(viewport={"width":1080,"height":h}, device_scale_factor=1)
    pg.goto("file://" + src); pg.wait_for_timeout(400)
    pg.screenshot(path=out, type="jpeg", quality=93, full_page=False)
    b.close()
