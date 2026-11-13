"""Apply the two specific Stage 1 caption findings, preserving their earlier text."""
from pathlib import Path
from datetime import datetime
import json, yaml
OUT = Path(__file__).resolve().parent
packet_path = OUT / 'foundation-information-integration.json'
rows = json.loads(packet_path.read_text(encoding='utf-8'))
repairs = {
 'A01': ('Estimates above 100 Hz are outside the displayed range.', 'Only estimates through 100 Hz are drawn.', 'Axis ends at 103 Hz; stems stop at 100 Hz.'),
 'A03': (r'$(r_i\prime)^2/r_i$', r'$(r_i^{\prime})^2/r_i$', 'Attach the derivative prime as a superscript.'),
}
record = []
for row in rows:
    if row['id'] not in repairs: continue
    before, after, reason = repairs[row['id']]
    assert row['caption'].count(before) == 1
    record.append({'id': row['id'], 'field': 'caption', 'original': row['caption'], 'replacement': row['caption'].replace(before, after), 'reason': reason})
(OUT / 'caption-repairs.json').write_text(json.dumps({'at': datetime.now().astimezone().isoformat(), 'reviewer': '/root/all_draw_eye_place', 'repairs': record}, ensure_ascii=False, indent=2), encoding='utf-8')
for item in record:
    row = next(r for r in rows if r['id'] == item['id'])
    row['caption'] = item['replacement']
    bp = OUT / f"{item['id']}-brief.yaml"
    brief = yaml.safe_load(bp.read_text(encoding='utf-8'))
    assert brief['language_contract']['caption'] == item['original']
    brief['language_contract']['caption'] = item['replacement']
    bp.write_text(yaml.safe_dump(brief, allow_unicode=True, sort_keys=False, width=84), encoding='utf-8')
lp = OUT / 'pending-ledger-foundations-information.yaml'
ledger = yaml.safe_load(lp.read_text(encoding='utf-8'))
for item in record:
    row = next(r for r in ledger['visuals'] if r['id'] == item['id'])
    assert row['caption'] == item['original']
    row['caption'] = item['replacement']
packet_path.write_text(json.dumps(rows, ensure_ascii=False, indent=2), encoding='utf-8')
lp.write_text(yaml.safe_dump(ledger, allow_unicode=True, sort_keys=False, width=84), encoding='utf-8')
print('Applied two caption repairs; image pixels unchanged.')
