from pathlib import Path
from datetime import datetime
import hashlib,json,re,yaml
OUT=Path(__file__).resolve().parent
PROP=OUT/'proposed'
for group in ['foundations-memory','information-eye','place-synthesis-orientation']:
    assert (OUT/f'stage1-{group}.json').exists(),group
changes=[
 ('01-foundations.md','Independent, unbiased changes give linear variance growth',
  'Independent steps with equal duration and variance give linear variance growth',
  'The new title must carry the fixed variance-per-time condition. Independence and zero mean alone do not imply linear growth.'),
 ('04-eye-drift.md','Making the response zero before the spike gives\n\n:::',
  'Making the response zero before the spike gives the impulse response $h_0(u)$.\n\n:::',
  'The result now precedes the optional proof; complete its ending by referring to the defined response explicitly.'),
 ('05-place-fields.md','To test this part of the geometry, raise the activity threshold and watch how regions split, join, appear, and disappear.',
  'As the activity threshold rises, active regions shrink and can split or disappear. The numbers of components and holes can change.',
  'Raising the threshold removes points from the active set, so it cannot join separate components. This also aligns the prose with the figure caption.'),
]
records=[]
for name,old,new,reason in changes:
    p=PROP/'content/chapters'/name
    text=p.read_text(encoding='utf-8')
    before=hashlib.sha256(p.read_bytes()).hexdigest()
    assert text.count(old)==1,(name,old)
    line=text[:text.index(old)].count('\n')+1
    text=text.replace(old,new)
    p.write_text(text,encoding='utf-8')
    side=p.with_suffix('.yaml')
    meta=yaml.safe_load(side.read_text(encoding='utf-8'))
    for m in re.finditer(r'^## (.+) \{#([^}]+)\}\n\n',text,re.M):
        row=next(r for r in meta['section_list'] if r['id']==m.group(2))
        row['title']=m.group(1)
        row['summary']=text[m.end():].split('\n\n',1)[0]
    side.write_text(yaml.safe_dump(meta,allow_unicode=True,sort_keys=False,width=84),encoding='utf-8')
    records.append({'path':p.relative_to(OUT).as_posix(),'line':line,'before':old,'after':new,'reason':reason,
                    'before_source_sha256':before,'after_source_sha256':hashlib.sha256(p.read_bytes()).hexdigest()})
path=PROP/'plan/chapter-plan.yaml'
plan=yaml.safe_load(path.read_text(encoding='utf-8'))
part=plan['book']['parts'][0]
old=part['title'];new='Noise limits memory accuracy in continuous attractor models'
assert old=='Persistent activity has a limit on memory accuracy'
part['title']=new
path.write_text(yaml.safe_dump(plan,allow_unicode=True,sort_keys=False,width=84),encoding='utf-8')
records.append({'path':'proposed/plan/chapter-plan.yaml','before':old,'after':new,
 'reason':'Name the model family in the Part title so the result is not read as a limit for every persistent-memory mechanism.'})
(OUT/'stage1-repairs.json').write_text(json.dumps({'at':datetime.now().astimezone().isoformat(),'changes':records},indent=2,ensure_ascii=False),encoding='utf-8')
print(json.dumps({'at':datetime.now().astimezone().isoformat(),'repairs':len(records)}))
