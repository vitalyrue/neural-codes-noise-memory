from pathlib import Path
from datetime import datetime
import hashlib,json
from book_runtime.release_audit import load_book,write_structure_lock
OUT=Path(__file__).resolve().parent;ROOT=OUT.parents[1]
read=lambda p:json.loads(p.read_text(encoding='utf-8'))
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
groups=['foundations-memory','information-eye','place-synthesis'];evidence=[]
for group in groups:
 for stage in [1,2,3]:
  p=OUT/f'stage{stage}-{group}.json';r=read(p);evidence.append(p.name)
  if stage in [1,3]:
   for k in ['defects','findings','unresolved_questions','unresolved_findings']:
    assert not r.get(k),f'{p.name}: {k}'
for group in ['foundations-memory','place-synthesis']:
 p=OUT/f'stage1-recheck-{group}.json';r=read(p);evidence.append(p.name)
 for k in ['defects','findings','unresolved_questions','unresolved_findings']:assert not r.get(k),(p,k)
repairs=read(OUT/'wording-repairs.json')['repairs']
assert {r['id'] for r in repairs}=={'NM1','S2-PS-1','S2-PS-2'}
for r in repairs:assert sha(ROOT/r['file'])==r['after_sha256']
bindings={p.relative_to(ROOT).as_posix():sha(p) for p in (ROOT/'content/chapters').glob('*') if p.suffix in ['.md','.yaml']}
bindings['plan/chapter-plan.yaml']=sha(ROOT/'plan/chapter-plan.yaml')
acceptance={'at':datetime.now().astimezone().isoformat(),'status':'accepted for this local structure and opening revision','scope':'Thirteen chapters with retained complete sections; motivated chapter openings, continuation reminders, reading paths and necessary cross-references. Separate independent truth, wording and flow calls; three exact wording repairs and focused meaning rechecks.','evidence':evidence+['wording-repairs.json','source-check.json'],'source_bindings':bindings,'limits':'No new whole-paper scientific audit, empirical reproduction, artwork review, full pixel sweep, public release or authoritative release claim. Historical whole-chapter scientific and visual records are retained unchanged.'}
(OUT/'acceptance.json').write_text(json.dumps(acceptance,indent=2),encoding='utf-8')
write_structure_lock(ROOT/'guide-project.yaml','plan/structural-locks/current.yaml')
print(json.dumps({'status':acceptance['status'],'book_model_hash':load_book(ROOT/'guide-project.yaml').content_hash()}))
