"""Bind actual independent paragraph judgments to the final UTF-8 inventory."""
from pathlib import Path
from datetime import datetime
import json,re,hashlib
ROOT=Path(__file__).resolve().parents[1]
path=ROOT/'verification/pedagogy/PARAGRAPH_REVIEW.json'
d=json.loads(path.read_text(encoding='utf-8'))
names=['memory-stage3-paragraphs.json','eye-stage3-paragraphs.json','place-stage3-paragraphs.json','memory-stage3-recheck-paragraphs.json','eye-stage3-recheck-paragraphs.json']
def normalize(text):return re.sub(r'\s+',' ',text).strip()
lookup={};evidence=[]
for name in names:
 p=ROOT/'verification/reviews'/name
 old=json.loads(p.read_text(encoding='utf-8'))
 evidence.append(dict(path=p.relative_to(ROOT).as_posix(),sha256=hashlib.sha256(p.read_bytes()).hexdigest(),original_input_hash=old.get('input_hash'),paragraphs=len(old['paragraphs'])))
 for row in old['paragraphs']:
  key=(row['source'],row['unit_id'],normalize(row['text']))
  lookup[key]=(row['review'],name,row['id'])
missing=[]; open_rows=[]
for row in d['paragraphs']:
 key=(row['source'],row['unit_id'],normalize(row['text']))
 if key not in lookup:missing.append(row['id']);continue
 review,name,old_id=lookup[key]
 row['review']=review
 row['judgment_evidence']={'path':'verification/reviews/'+name,'original_id':old_id,'binding':'Same actual paragraph text and unit; final line IDs may shift. Focused rechecks assess changed connections.'}
 if review['decision']!='retain':open_rows.append(row['id'])
d['independent_paragraph_evidence']=evidence
d['binding_checked_at']=datetime.now().astimezone().isoformat()
path.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
report=dict(checked_at=d['binding_checked_at'],final_input_hash=d['input_hash'],paragraphs=len(d['paragraphs']),bound=len(d['paragraphs'])-len(missing),missing=missing,open_decisions=open_rows,evidence=evidence,limits='Actual paragraph judgments are bound here. Formal packet/workflow validation is separate; no missing generic packet field is auto-filled or declared passed.')
(ROOT/'verification/reviews/final-paragraph-binding.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in report.items() if k!='evidence'},indent=2))
raise SystemExit(bool(missing or open_rows))
