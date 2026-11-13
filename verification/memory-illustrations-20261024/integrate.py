"""Insert independently checked candidate images and reviewed Chapter 2 text."""
from pathlib import Path
from datetime import datetime
import hashlib, json, re, shutil, yaml

ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).resolve().parent
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
review = (OUT / 'stage1-review.md').read_text(encoding='utf-8')
assert 'pass' in review.lower(), 'Read the independent Stage 1 decision before running this script.'
rows = yaml.safe_load((OUT / 'integration-rows.yaml').read_text(encoding='utf-8'))['visuals']
chapter = ROOT / 'content/chapters/02-memory-dynamics.md'
sidecar = chapter.with_suffix('.yaml')
for p in [chapter, sidecar]:
    baseline = OUT / 'baseline' / p.relative_to(ROOT)
    assert sha(p) == sha(baseline), 'Reader source changed while candidates were prepared'
shutil.copy2(OUT / 'proposed-chapter.md', chapter)
shutil.copy2(OUT / 'proposed-chapter.yaml', sidecar)
ledger_path = ROOT / 'source-maps/visual-ledger.yaml'
ledger = yaml.safe_load(ledger_path.read_text(encoding='utf-8'))
old_ids = {r['visual_id'] for r in ledger['visuals']}
for index, row in enumerate(rows, start=1):
    assert row['visual_id'] not in old_ids
    candidate = ROOT / f'candidate-content/visuals/candidates/20261024/M0{index}'
    qa = json.loads((candidate / 'qa.json').read_text(encoding='utf-8'))
    assert qa['status'] == 'pass' and qa['png_sha256'] == sha(candidate / 'figure.png')
    png = ROOT / row['asset']
    svg = png.with_suffix('.svg')
    assert not png.exists() and not svg.exists(), 'Do not overwrite an existing approved image'
    shutil.copy2(candidate / 'figure.png', png)
    shutil.copy2(candidate / 'figure.svg', svg)
    row.update(status='selected', embedded=True, sha256=sha(png),
               vector_source=svg.relative_to(ROOT).as_posix(),
               caption_and_alt=sidecar.relative_to(ROOT).as_posix(),
               origin='Original analytic teaching plot; not paper simulation or experimental data.',
               rights='Original guide figure',
               content_review='verification/memory-illustrations-20261024/stage1-review.md',
               visual_review='verification/memory-illustrations-20261024/stage1-review.md',
               toc_correspondence=row['placement'])
    ledger['visuals'].append(row)
ledger['visual_ledger_version'] = max(4, ledger.get('visual_ledger_version', 1))
ledger_path.write_text(yaml.safe_dump(ledger, allow_unicode=True, sort_keys=False, width=84), encoding='utf-8')
(OUT / 'new-visual-ledger.yaml').write_text(yaml.safe_dump({'schema_version': 1, 'visuals': rows}, allow_unicode=True, sort_keys=False, width=84), encoding='utf-8')

# The first-use locations move when the figures are inserted. Keep other chapters intact.
term_path = ROOT / 'source-maps/terminology-ledger.yaml'
terms = yaml.safe_load(term_path.read_text(encoding='utf-8'))
text = chapter.read_text(encoding='utf-8')
term_loci = {}
section = None
for number, line in enumerate(text.splitlines(), start=1):
    found = re.search(r'\{#(sec:[^}]+)\}', line)
    if found: section = found.group(1)
    for term in re.findall(r'\[\*\*(.*?)\*\*\]\{\.definition-term', line):
        term_loci[term] = (number, section)
updated = []
for row in terms['first_teaching']:
    if row['source'] == chapter.relative_to(ROOT).as_posix():
        number, section = term_loci[row['term']]
        row.update(line=number, guide_location=section)
        updated.append(row['term'])
term_path.write_text(yaml.safe_dump(terms, allow_unicode=True, sort_keys=False, width=84), encoding='utf-8')

changes = json.loads((OUT / 'insertions.json').read_text(encoding='utf-8'))
reverse = text
for item in reversed(changes):
    assert reverse.count(item['after']) == 1
    reverse = reverse.replace(item['after'], item['before'])
assert reverse == (OUT / 'baseline/content/chapters/02-memory-dynamics.md').read_text(encoding='utf-8')
result = {'at': datetime.now().astimezone().isoformat(), 'inserted_figures': 3,
          'pdf_links_in_source': 48, 'original_content_recovers_exactly': True,
          'terminology_locations_updated': updated, 'chapter_sha256': sha(chapter),
          'sidecar_sha256': sha(sidecar), 'scope': 'Chapter 2 only; final connected reviews pending.'}
(OUT / 'insertion-record.json').write_text(json.dumps(result, indent=2), encoding='utf-8')
print(json.dumps(result, indent=2))
