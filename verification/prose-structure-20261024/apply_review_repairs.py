from pathlib import Path
from datetime import datetime
import hashlib,json,sys
OUT=Path(__file__).resolve().parent;P=OUT/'proposed/content/chapters'
load=lambda p:json.loads(p.read_text(encoding='utf-8'));sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
ledger=load(OUT/'review-repairs.json') if (OUT/'review-repairs.json').exists() else {'edits':[]}
for group in sys.argv[1:]:
 review=load(OUT/f'stage2-{group}.json')
 for repair in review.get('repairs',review.get('proposed_repairs',review.get('small_repairs',[]))):
  repair['before']=repair.get('before',repair.get('old'));repair['after']=repair.get('after',repair.get('new'))
  file=Path(repair['file']).name;p=P/file;before=p.read_text(encoding='utf-8')
  assert before.count(repair['before'])==1,(file,repair['before'][:90])
  oldsha=sha(p);p.write_text(before.replace(repair['before'],repair['after']),encoding='utf-8',newline='\n')
  ledger['edits'].append({'file':'content/chapters/'+file,'before':repair['before'],'after':repair['after'],'kind':'independent-review-repair','reason':repair['reason'],'review':f'stage2-{group}.json','before_sha256':oldsha,'after_sha256':sha(p),'at':datetime.now().astimezone().isoformat()})
(OUT/'review-repairs.json').write_text(json.dumps(ledger,indent=2,ensure_ascii=False),encoding='utf-8')
print(json.dumps({'recorded_repairs':len(ledger['edits']),'groups':sys.argv[1:]}))
