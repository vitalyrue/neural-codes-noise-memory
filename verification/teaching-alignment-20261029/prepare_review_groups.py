from pathlib import Path
import argparse
import json
import sys

ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).resolve().parent
SKILL = Path('C:/dev/NBIS/publisher-releases/0.8.23/skills/course-quality-gate/scripts')
sys.path.insert(0, str(SKILL))
import orchestrate_pedagogy_reviews as review

parser = argparse.ArgumentParser()
parser.add_argument('--packet-dir', default='pedagogy-initial')
parser.add_argument('--prefix', default='')
args = parser.parse_args()
discovered = review.discover_source_files(ROOT)
scopes = review._expected_review_scopes(ROOT, discovered)
paragraphs = json.loads((OUT / args.packet_dir / 'PARAGRAPH_REVIEW.json').read_text())
groups = {name: {'units': {}, 'paragraphs': []} for name in ('memory', 'eye', 'place')}

def group_for(unit_id):
    if unit_id.startswith('part:MECHANISMS'):
        return 'memory'
    if unit_id.startswith('part:OBSERVATIONS'):
        return 'eye'
    filename = unit_id.split('::')[0].split('/')[-1]
    if filename.startswith(('01', '02', '03')):
        return 'memory'
    if filename.startswith(('00', '04')):
        return 'eye'
    return 'place'

for scope in scopes.values():
    for unit_id, record in scope['unit_records'].items():
        groups[group_for(unit_id)]['units'][unit_id] = record
for paragraph in paragraphs['paragraphs']:
    groups[group_for(paragraph['unit_id'])]['paragraphs'].append(paragraph)
for name, group in groups.items():
    group['input_hash'] = paragraphs['input_hash']
    group['review_contract_hash'] = paragraphs['review_contract_hash']
    group['review_fields'] = review.REVIEW_FIELDS
    (OUT / f'{args.prefix}{name}-input.json').write_text(json.dumps(group, indent=2, ensure_ascii=False, default=lambda value: sorted(value) if isinstance(value, set) else str(value)), encoding='utf-8')
    print(name, len(group['units']), 'units;', len(group['paragraphs']), 'paragraphs;', sum(len(x['claims']) for x in group['units'].values()), 'claims')
