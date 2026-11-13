"""Merge the three independent reviewers' unchanged figure judgments."""
from pathlib import Path
import json,sys,yaml
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,'C:/Users/vital/.codex/skills/course-diagram-builder/scripts')
from visual_review import validate_visual_review
old=json.loads((ROOT/'verification/illustrations/source-bindings-reviewed.json').read_text(encoding='utf-8'))
new=json.loads((ROOT/'verification/illustrations/current-bindings.json').read_text(encoding='utf-8'))
assert old['figures']==new['figures'],'Navigation must not change any reviewed figure input or chapter scope'
records={}
for area in ['memory','eye','place-orientation']:
    data=json.loads((ROOT/f'verification/illustrations/diagram-review-{area}.json').read_text(encoding='utf-8'))
    records.update(data)
path=ROOT/'source-maps/visual-ledger.yaml'
ledger=yaml.safe_load(path.read_text(encoding='utf-8'))
modern=[]
for row in ledger['visuals']:
    ident=row['visual_id']
    if ident not in records:continue
    row['diagram_review']=records[ident]
    errors=validate_visual_review(row,ROOT)
    assert not errors,(ident,errors)
    modern.append(row)
assert len(modern)==9
path.write_text(yaml.safe_dump(ledger,sort_keys=False,allow_unicode=True),encoding='utf-8')
(ROOT/'verification/illustrations/new-visual-ledger.yaml').write_text(yaml.safe_dump({'schema_version':1,'visual_ledger_version':3,'visuals':modern},sort_keys=False,allow_unicode=True),encoding='utf-8')
print(json.dumps({'independent_reviews_merged':len(modern),'all_validated':True,
    'navigation_only_model_change':{'reviewed':old['book_model_hash'],'current':new['book_model_hash'],'all_nine_figure_bindings_identical':True},
    'old_attractor':'Original asset and historical acceptance retained unchanged.'},indent=2))
