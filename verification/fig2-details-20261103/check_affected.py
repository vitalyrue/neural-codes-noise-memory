"""Check the three affected HTML pages, source scope and served bytes."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote
from urllib.request import urlopen
from datetime import datetime, timezone
import hashlib, json, re, difflib

TASK = Path(__file__).resolve().parent
ROOT = TASK.parents[1]
SITE = ROOT / 'site'

class Page(HTMLParser):
    def __init__(self, text):
        super().__init__()
        self.ids, self.links = set(), []
        self.feed(text)
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if 'id' in attrs:
            self.ids.add(attrs['id'])
        if tag == 'a' and attrs.get('href'):
            self.links.append(attrs['href'])
        if attrs.get('src'):
            self.links.append(attrs['src'])

def bad_links(page_path, page):
    failures = []
    for target in page.links:
        url = urlsplit(target)
        if url.scheme or target.startswith('//'):
            continue
        dest = ((SITE / unquote(url.path.lstrip('/'))) if url.path.startswith('/')
                else page_path.parent / unquote(url.path)).resolve() if url.path else page_path
        if dest.is_dir():
            dest /= 'index.html'
        if not dest.exists():
            failures.append(target)
        elif url.fragment and dest.suffix == '.html':
            if unquote(url.fragment) not in Page(dest.read_text(encoding='utf-8')).ids:
                failures.append(target)
    return failures

paths = ['chapters/ch-memory-long-delays.html', 'chapters/ch-simulating-memory.html',
         'chapters/ch-eye-drift.html']
records = []
for rel in paths:
    path = SITE / rel
    body = path.read_bytes()
    markup = body.decode('utf-8')
    page = Page(markup)
    failures = bad_links(path, page)
    assert not failures, failures
    assert not re.search(r'\[\^[^\]\n]+\]', markup), 'Unresolved footnote'
    assert 'mjx-container' in markup or 'class="math' in markup
    served = urlopen('https://vrdell15.tail8b993e.ts.net/burak/' + rel, timeout=20).read()
    assert served == body, 'Served bytes differ: ' + rel
    records.append({'page': rel, 'checked_targets': len(page.links), 'bad_links': failures,
                    'sha256': hashlib.sha256(body).hexdigest(), 'served_bytes_match': True})

# Confirm the link checker rejects the failure it is meant to find.
assert bad_links(SITE / paths[0], Page('<a href="__missing_fig2_check__.html">bad</a>'))

state = json.loads((TASK / 'STATE.json').read_text(encoding='utf-8'))
changes = []
for record in state['source_baseline']:
    path = ROOT / record['path']
    before = (TASK / path.name).read_text(encoding='utf-8')
    after = path.read_text(encoding='utf-8')
    assert re.findall(r'(?m)^#{1,6} .*', before) == re.findall(r'(?m)^#{1,6} .*', after)
    changes.append({'path': record['path'], 'before_sha256': record['sha256'],
                    'after_sha256': hashlib.sha256(path.read_bytes()).hexdigest(),
                    'headings_unchanged': True,
                    'diff': list(difflib.unified_diff(before.splitlines(), after.splitlines(),
                               fromfile='before/'+path.name, tofile='after/'+path.name, lineterm=''))})
(TASK / 'CHANGES.json').write_text(json.dumps(changes, indent=2)+'\n', encoding='utf-8')

prior = json.loads((ROOT/'verification/nemotron-review-20261103/MANIFEST.json').read_text(encoding='utf-8'))
changed = [f['source'] for f in prior['source_files']
           if hashlib.sha256(Path(f['source']).read_bytes()).hexdigest() != f['sha256']]
assert set(map(lambda x: Path(x).resolve(), changed)) == {
    (ROOT/r['path']).resolve() for r in state['source_baseline']}, changed

figure = ROOT/'assets/approved/visuals/paper-excerpts/memory-fig-2.png'
assert figure.read_bytes() == (SITE/'assets/fig-paper-memory-2.png').read_bytes()
result = {'completed_utc': datetime.now(timezone.utc).isoformat(), 'status': 'pass',
          'scope': 'Three affected pages, outgoing targets, source scope, exact served bytes and Figure 2 copy',
          'pages': records, 'checker_planted_missing_link_rejected': True,
          'changed_source_files': changed, 'source_headings_unchanged': True,
          'figure2_published_bytes_match_source': True,
          'full_figure_acceptance': 'pending; no new figure audit'}
(TASK/'FINAL_CHECKS.json').write_text(json.dumps(result, indent=2)+'\n', encoding='utf-8')
print(json.dumps({k:v for k,v in result.items() if k != 'pages'}, indent=2))
