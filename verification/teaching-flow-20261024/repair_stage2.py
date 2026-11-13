from pathlib import Path
from datetime import datetime
import hashlib,json,yaml
OUT=Path(__file__).resolve().parent
PROP=OUT/'proposed/content/chapters'
changes=[
 ('04-eye-drift.md','Check: static gain and coincident decay times','Check: static gain and equal decay times',
  'Use the familiar word equal in the expandable-note title; the scientific condition is unchanged.'),
 ('05-place-fields.md','Why rare high fields are nearly parabolic','Near a high peak, the input is nearly parabolic',
  'The local input profile is parabolic; a field was defined as a connected region, whose high-peak boundary is nearly round. Name the object the calculation actually approximates.'),
]
records=[]
for name,old,new,reason in changes:
    p=PROP/name;text=p.read_text(encoding='utf-8')
    assert text.count(old)==1
    before=hashlib.sha256(p.read_bytes()).hexdigest()
    p.write_text(text.replace(old,new),encoding='utf-8')
    side=p.with_suffix('.yaml')
    meta=yaml.safe_load(side.read_text(encoding='utf-8'))
    changed=False
    for row in meta['section_list']:
        if row['title']==old:row['title']=new;changed=True
    if changed:side.write_text(yaml.safe_dump(meta,allow_unicode=True,sort_keys=False,width=84),encoding='utf-8')
    records.append({'file':name,'before':old,'after':new,'reason':reason,
                    'before_sha256':before,'after_sha256':hashlib.sha256(p.read_bytes()).hexdigest()})
now=datetime.now().astimezone().isoformat()
(OUT/'stage2-repairs.json').write_text(json.dumps({'at':now,'changes':records},indent=2,ensure_ascii=False),encoding='utf-8')
units=json.loads((OUT/'changed-prose-units.json').read_text(encoding='utf-8'))
count=sum(len(r['changed_original_units']) for r in units)
with (OUT/'RUN.md').open('a',encoding='utf-8') as f:
    f.write(f'\n{now}: Correction to the 19:08:49 checkpoint: the mechanical comparison contains {count} changed original prose units, not eight. All are accounted for by the recorded connection/definition-placement repairs and topology correction.\n')
print(json.dumps({'at':now,'repairs':len(records),'changed_original_prose_units':count}))
