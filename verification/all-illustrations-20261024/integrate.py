"""Insert only images whose frozen candidate bytes passed independent review."""
from pathlib import Path
from datetime import datetime
import hashlib, json, re, shutil, yaml
ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).resolve().parent
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
rows = json.loads((OUT / 'integration.json').read_text(encoding='utf-8'))
approved = json.loads((OUT / 'stage1-approved.json').read_text(encoding='utf-8'))
assert approved['reviewer'] not in {'/root', '/root/all_draw_foundations_information', '/root/all_draw_eye_place'}
assert len(approved['figures']) == 9
ledger_path = ROOT / 'source-maps/visual-ledger.yaml'
assert sha(ledger_path) == sha(OUT / 'baseline/source-maps/visual-ledger.yaml')
ledger = yaml.safe_load(ledger_path.read_text(encoding='utf-8'))
old_ids = {r['visual_id'] for r in ledger['visuals']}
chapters = sorted({r['chapter'] for r in rows})
for cp in chapters:
    for rel in [Path(cp), Path(cp).with_suffix('.yaml')]:
        assert sha(ROOT / rel) == sha(OUT / 'baseline' / rel), f'Changed reader source: {rel}'
for r in rows:
    candidate = ROOT / r['candidate']
    decision = approved['figures'][r['id']]
    assert decision['decision'] == 'pass'
    assert decision['png_sha256'] == sha(candidate / 'figure.png')
    assert decision['svg_sha256'] == sha(candidate / 'figure.svg')
    qa = json.loads((candidate / 'qa.json').read_text(encoding='utf-8'))
    assert qa['status'] == 'pass' and qa['png_sha256'] == sha(candidate / 'figure.png')
    png = ROOT / r['asset']
    assert not png.exists() and not png.with_suffix('.svg').exists()
    assert r['visual_id'] not in old_ids
for cp in chapters:
    for rel in [Path(cp), Path(cp).with_suffix('.yaml')]:
        shutil.copy2(OUT / 'proposed' / rel, ROOT / rel)
new = []
for r in rows:
    candidate = ROOT / r['candidate']
    png = ROOT / r['asset']
    shutil.copy2(candidate / 'figure.png', png)
    shutil.copy2(candidate / 'figure.svg', png.with_suffix('.svg'))
    row = {'visual_id': r['visual_id'], 'block_id': r['visual_id'], 'asset': r['asset'],
      'status': 'selected', 'embedded': True, 'sha256': sha(png),
      'vector_source': png.with_suffix('.svg').relative_to(ROOT).as_posix(),
      'caption_and_alt': Path(r['chapter']).with_suffix('.yaml').as_posix(),
      'caption': r['caption'], 'accessibility_description': r['alt'],
      'teaching_introduction': r['intro'], 'interpretation': r['interpretation'],
      'source_status': r['source_locator'], 'placement': r['placement'],
      'origin': 'Original analytic or simulated teaching construction; not experimental data.',
      'rights': 'Original guide figure', 'toc_correspondence': r['placement'],
      'content_review': approved['figures'][r['id']]['report'],
      'visual_review': approved['figures'][r['id']]['report'],
      'review_contract': r['review_contract'], 'diagram_review': {'schema_version': 1, 'status': 'pending'}}
    ledger['visuals'].append(row)
    new.append(row)
ledger_path.write_text(yaml.safe_dump(ledger, allow_unicode=True, sort_keys=False, width=84), encoding='utf-8')
(OUT / 'new-visual-ledger.yaml').write_text(yaml.safe_dump({'schema_version': 1, 'visuals': new}, allow_unicode=True, sort_keys=False, width=84), encoding='utf-8')
tp = ROOT / 'source-maps/terminology-ledger.yaml'
terms = yaml.safe_load(tp.read_text(encoding='utf-8'))
updated = []
for cp in chapters:
    loci, section = {}, None
    for number, line in enumerate((ROOT / cp).read_text(encoding='utf-8').splitlines(), start=1):
        found = re.search(r'\{#(sec:[^}]+)\}', line)
        if found: section = found.group(1)
        for term in re.findall(r'\[\*\*(.*?)\*\*\]\{\.definition-term', line):
            loci[term] = (number, section)
    for term in terms['first_teaching']:
        if term['source'] == cp:
            number, section = loci[term['term']]
            term.update(line=number, guide_location=section)
            updated.append(term['term'])
tp.write_text(yaml.safe_dump(terms, allow_unicode=True, sort_keys=False, width=84), encoding='utf-8')
for cp in chapters:
    reverse = (ROOT / cp).read_text(encoding='utf-8')
    for item in reversed(json.loads((OUT / 'insertions.json').read_text(encoding='utf-8'))):
        if item['chapter'] == cp:
            assert reverse.count(item['after']) == 1
            reverse = reverse.replace(item['after'], item['before'])
    assert reverse == (OUT / 'baseline' / cp).read_text(encoding='utf-8')
print(json.dumps({'at': datetime.now().astimezone().isoformat(), 'inserted': len(rows), 'chapters': len(chapters), 'original_recovers_exactly': True, 'updated_term_locations': len(updated)}))
