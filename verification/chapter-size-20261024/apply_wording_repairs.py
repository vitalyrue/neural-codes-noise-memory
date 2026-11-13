from pathlib import Path
from datetime import datetime
import json,hashlib
OUT=Path(__file__).resolve().parent;ROOT=OUT.parents[1]
read=lambda p:p.read_text(encoding='utf-8')
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
repairs=[]
for name in ['stage2-foundations-memory.json','stage2-place-synthesis.json']:
 report=json.loads(read(OUT/name))
 for finding in report['findings']:
  p=ROOT/finding['file'];before=finding.get('quoted_passage',finding.get('original'))
  after=finding.get('replacement',finding.get('proposed'))
  if finding['id']=='S2-PS-2':before=' '+before;after=''
  text=read(p);assert text.count(before)==1,finding['id']
  oldhash=sha(p);text=text.replace(before,after);p.write_text(text,encoding='utf-8',newline='\n')
  repairs.append({'id':finding['id'],'file':finding['file'],'before':before,'after':after,'before_sha256':oldhash,'after_sha256':sha(p),'review_record':name})
for filename,collection in [('integration.json','chapters'),('selected-plan.json','originals')]:
 data=json.loads(read(OUT/filename))
 rows=data[collection] if collection=='chapters' else [g for o in data[collection] for g in o['groups']]
 for row in rows:
  file=row['file'] if row['file'].startswith('content/') else 'content/chapters/'+row['file']
  for repair in repairs:
   if file==repair['file']:row['opening']=[p.replace(repair['before'],repair['after']) for p in row['opening']]
 (OUT/filename).write_text(json.dumps(data,indent=2,ensure_ascii=False),encoding='utf-8')
(OUT/'wording-repairs.json').write_text(json.dumps({'at':datetime.now().astimezone().isoformat(),'repairs':repairs},indent=2),encoding='utf-8')
print('Applied three exact wording repairs in chapter openings.')
