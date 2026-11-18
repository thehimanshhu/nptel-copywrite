"""Render a page in headless Chromium and save the hydrated DOM.

Run via tools/render.sh, not directly. Usage inside the container:
  python render.py <url> <out.html> [--click "CSS selector"]...
Each --click clicks every element matching the selector (in order), waiting
for the network to settle after each, so content behind tabs/accordions is
present in the saved DOM. Progress is logged unbuffered.
"""
import sys
from playwright.sync_api import sync_playwright

url, out = sys.argv[1], sys.argv[2]
clicks = [sys.argv[i + 1] for i, a in enumerate(sys.argv) if a == '--click']
print(f'[render] {url}', flush=True)
with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page(viewport={'width': 1440, 'height': 1000})
    pg.goto(url, wait_until='networkidle', timeout=120000)
    pg.wait_for_timeout(1500)
    for sel in clicks:
        els = pg.query_selector_all(sel)
        print(f'[render] click {sel!r}: {len(els)} element(s)', flush=True)
        for e in els:
            try:
                e.click(timeout=5000); pg.wait_for_load_state('networkidle', timeout=30000); pg.wait_for_timeout(300)
            except Exception as ex:
                print(f'[render]   click failed: {ex.__class__.__name__}', flush=True)
    html = pg.content()
    open(out, 'w', encoding='utf-8').write(html)
    print(f'[render] saved {len(html)} bytes -> {out}', flush=True)
    b.close()
