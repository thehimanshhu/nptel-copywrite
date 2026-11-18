#!/usr/bin/env python3
"""Word-level diff between a live nptel.ac.in page and its markdown transcription.

  python3 -I tools/verify.py <url-or-saved-html> <file.md>

Live text = server-rendered <body>, minus the site-wide <header>/<footer>
(the direct children of SvelteKit's root <div style="display: contents">,
plus any nested copy of those same components, matched by class),
minus the site-wide div.migration-notice banner, minus <script>/<style>/<svg>/<noscript>.
Pass a file saved by tools/render.sh to check client-rendered content.

Markdown text = the file, minus front matter, markdown syntax, link targets,
and placeholder tag lines (lines starting "> **[").

Output: every non-matching span. "insert" = only in the markdown (expected for
text that appears only after a click, e.g. non-default tabs or modals);
"delete" = only on the live page (must be either transcribed or covered by
a placeholder); "replace" = wording differs (should not happen).
"""
import html, re, sys, difflib, urllib.request
from html.parser import HTMLParser

VOID = {'area','base','br','col','embed','hr','img','input','link','meta','source','track','wbr'}
SKIP = {'script','style','svg','noscript','template'}

class Text(HTMLParser):
    def __init__(self, chrome=()):
        super().__init__(convert_charrefs=True)
        self.chrome = set(chrome)  # (tag, class) of the shared Header/Footer components
        self.stack = []          # tag names
        self.root_depth = None   # depth of SvelteKit's display:contents div
        self.drop_depth = None   # depth at which we started dropping
        self.out = []
        self.found = set()
    def handle_starttag(self, tag, attrs):
        if tag in VOID:
            if tag == 'br' and self.drop_depth is None: self.out.append('\n')
            return
        self.stack.append(tag)
        d = len(self.stack)
        a = dict(attrs)
        if self.root_depth is None and tag == 'div' and 'display: contents' in (a.get('style') or ''):
            self.root_depth = d
        if self.drop_depth is None:
            cls = (a.get('class') or '').split()
            top = tag in ('header', 'footer') and self.root_depth and d == self.root_depth + 1
            if top: self.found.add((tag, a.get('class') or ''))
            if (tag in SKIP or 'migration-notice' in cls       # site-wide notice banner
                    or top or (tag, a.get('class') or '') in self.chrome):   # shared header/footer, even nested
                self.drop_depth = d
    def handle_endtag(self, tag):
        if tag in VOID or tag not in self.stack: return
        while self.stack:
            t = self.stack.pop()
            if self.drop_depth and len(self.stack) < self.drop_depth: self.drop_depth = None
            if t == tag: break
    def handle_data(self, data):
        if self.drop_depth is None and 'body' in self.stack:
            self.out.append(data)

def fetch(src):
    if src.startswith('http'):
        req = urllib.request.Request(src, headers={'User-Agent': 'Mozilla/5.0 (transcription check)'})
        return urllib.request.urlopen(req, timeout=60).read().decode('utf-8', 'replace')
    return open(src, encoding='utf-8').read()

def chrome_classes():
    # /aboutus always has the shared Header and Footer at top level; learn their
    # (build-specific) svelte classes there so nested copies can be dropped too.
    # Cached for an hour (classes change only when the site is redeployed).
    import json, os, time, tempfile
    cache = os.path.join(tempfile.gettempdir(), 'nptel-copywrite-chrome.json')
    try:
        if time.time() - os.path.getmtime(cache) < 3600:
            return {tuple(x) for x in json.load(open(cache))}
    except OSError:
        pass
    for attempt in range(3):
        try:
            p = Text(); p.feed(fetch('https://nptel.ac.in/aboutus')); break
        except OSError:
            if attempt == 2: raise
            time.sleep(5)
    json.dump(sorted(p.found), open(cache, 'w'))
    return p.found

def live_text(src):
    p = Text(chrome_classes()); p.feed(fetch(src))
    return ' '.join(p.out)

def md_text(path):
    md = open(path, encoding='utf-8').read()
    md = re.sub(r'\A---\n.*?\n---\n', '', md, flags=re.S)
    keep = []
    for l in md.splitlines():
        s = re.sub(r'^(\s*>)+\s?', '', l)
        if re.match(r'^\s*>\s*\*\*\[[A-Z][A-Za-z0-9 ·/&_+-]*\]\*\*', l): continue   # placeholder tag line
        if re.match(r'^\s*\|?\s*:?-{3,}', s): continue         # table rule
        keep.append(s)
    t = '\n'.join(keep)
    t = re.sub(r'!\[[^\]]*\]\([^)]*\)', ' ', t)                # images
    t = re.sub(r'\]\([^)]*\)', ']', t)                         # link targets
    t = re.sub(r'\*\((button|link|tab|opens [^)]*)\)\*', ' ', t)
    t = re.sub(r'^\s*(#{1,6}|[*+-]|\d+[.)])\s+', '', t, flags=re.M)
    t = re.sub(r'^\s*---\s*$', '', t, flags=re.M)
    t = t.replace('**', '').replace('|', ' ').replace('`', '')
    t = re.sub(r'(?<!\w)\[|\](?!\w)', '', t)
    t = re.sub(r'<br\s*/?>', ' ', t)
    return html.unescape(t)

def norm(s):
    return [w for w in s.replace(' ', ' ').split() if w]

if __name__ == '__main__':
    a, b = norm(live_text(sys.argv[1])), norm(md_text(sys.argv[2]))
    print(f'live words: {len(a)}   markdown words: {len(b)}')
    sm = difflib.SequenceMatcher(None, a, b, autojunk=False)
    matched = sum(bl.size for bl in sm.get_matching_blocks())
    print(f'live words matched in markdown: {matched}/{len(a)} ({100*matched/max(len(a),1):.1f}%)')
    for op, i1, i2, j1, j2 in sm.get_opcodes():
        if op != 'equal':
            print(f'{op:8} LIVE: {" ".join(a[i1:i2])[:300]!r}\n         MD:   {" ".join(b[j1:j2])[:300]!r}')
