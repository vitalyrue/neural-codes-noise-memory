"""Apply only the four individually reviewed Stage 2 repairs and their metadata mirrors."""
from pathlib import Path
from datetime import datetime
import ast, hashlib, json, yaml
OUT = Path(__file__).resolve().parent
ROOT = OUT.parents[1]
report = json.loads((OUT / 'stage2-review.json').read_text(encoding='utf-8'))
packets = {}
for filename in ['foundation-information-integration.json','eye-place-integration.json']:
    packets[filename] = json.loads((OUT / filename).read_text(encoding='utf-8'))
repairs = []
for finding in report['required_repairs']:
    filename, row = next((name,r) for name, rows in packets.items() for r in rows if r['id'] == finding['figure'])
    old = row[finding['field']]
    assert old.count(finding['original']) == 1, finding['id']
    new = old.replace(finding['original'], finding['replacement'], 1)
    repairs.append({**finding, 'packet': filename, 'full_original': old, 'full_replacement': new})
(OUT / 'stage2-application.json').write_text(json.dumps({'at': datetime.now().astimezone().isoformat(), 'repairs': repairs}, ensure_ascii=False, indent=2), encoding='utf-8')
for change in repairs:
    row = next(r for r in packets[change['packet']] if r['id'] == change['figure'])
    assert row[change['field']] == change['full_original']
    row[change['field']] = change['full_replacement']
    generator = ROOT / row['review_contract']['vector_spec']
    text = generator.read_text(encoding='utf-8')
    nodes = [node for node in ast.walk(ast.parse(text)) if isinstance(node, ast.Constant) and node.value == change['full_original']]
    assert len(nodes) == 1, (change['id'], 'generator literal')
    segment = ast.get_source_segment(text, nodes[0])
    assert text.count(segment) == 1
    generator.write_text(text.replace(segment, repr(change['full_replacement']), 1), encoding='utf-8', newline='\n')
    bp = OUT / f"{change['figure']}-brief.yaml"
    brief = yaml.safe_load(bp.read_text(encoding='utf-8'))
    if 'language_contract' in brief:
        key = {'intro':'teaching_introduction','alt':'alt_text','interpretation':'conclusion'}.get(change['field'], change['field'])
        assert brief['language_contract'][key] == change['full_original']
        brief['language_contract'][key] = change['full_replacement']
        bp.write_text(yaml.safe_dump(brief, allow_unicode=True, sort_keys=False, width=84), encoding='utf-8')
for name, rows in packets.items():
    (OUT / name).write_text(json.dumps(rows, ensure_ascii=False, indent=2), encoding='utf-8')
for filename in ['pending-ledger-foundations-information.yaml','pending-ledger-eye-place.yaml']:
    path = OUT / filename
    ledger = yaml.safe_load(path.read_text(encoding='utf-8'))
    for change in repairs:
        row = next((r for r in ledger['visuals'] if r['visual_id'] == next(x['visual_id'] for x in packets[change['packet']] if x['id'] == change['figure'])), None)
        if row is None: continue
        key = {'intro':'teaching_introduction','alt':'accessibility_description'}.get(change['field'], change['field'])
        if key in row:
            assert row[key] == change['full_original']
            row[key] = change['full_replacement']
    path.write_text(yaml.safe_dump(ledger, allow_unicode=True, sort_keys=False, width=84), encoding='utf-8')
print(json.dumps({'applied_findings': [r['id'] for r in repairs], 'image_changes': 0}))
