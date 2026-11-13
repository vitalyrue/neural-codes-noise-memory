from pathlib import Path
from datetime import datetime
import hashlib,json
from book_runtime.release_audit import load_book,write_structure_lock
OUT=Path(__file__).resolve().parent;ROOT=OUT.parents[1]
load=lambda p:json.loads(p.read_text(encoding='utf-8'));sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
assert load(OUT/'draft-check.json')['status']=='pass'
evidence=[];review_bindings=[];covered=set()
for group in ['foundations-synthesis','information-eye','place']:
 for stage in [1,2,3]:
  p=OUT/f'stage{stage}-{group}.json';report=load(p);evidence.append(p.name)
  if stage in [1,3]:
   for key in ['findings','defects','unresolved_questions','unresolved_findings']:assert not report.get(key),(p,key)
  if stage==3:
   for name,digest in report['source_bindings'].items():
    rel='content/chapters/'+Path(name).name
    assert sha(ROOT/rel)==digest.lower(),(p,rel)
    review_bindings.append({'review':p.name,'file':rel,'sha256':digest.lower(),'matches_current':True});covered.add(Path(name).name)
assert covered=={p.name for p in (OUT/'proposed/content/chapters').glob('*.md')},covered
recheck=load(OUT/'stage1-recheck-information-eye.json');assert not recheck['unresolved_questions'];evidence.append('stage1-recheck-information-eye.json')
repairs=load(OUT/'review-repairs.json');assert len(repairs['edits'])==6
source_bindings={p.relative_to(ROOT).as_posix():sha(p) for p in (ROOT/'content/chapters').glob('*') if p.suffix in ['.md','.yaml']}
source_bindings['plan/chapter-plan.yaml']=sha(ROOT/'plan/chapter-plan.yaml')
acceptance={'at':datetime.now().astimezone().isoformat(),'status':'accepted for local paragraph structure revision','scope':'All thirteen teaching chapters plus reading guide: visible lists for parallel points and ordered steps, actual first definitions in blue, matching glossary entries, concrete transitions and individual wording repairs. Separate independent truth, wording and connected reading stages; six exact wording repairs, including focused correctness rechecks for the two explanatory replacements.','evidence':evidence+['review-repairs.json','draft-check.json'],'source_bindings':source_bindings,'limits':'Scoped prose and paragraph structure review; no new whole-paper scientific audit, empirical reproduction, artwork review, full pixel sweep, public or authoritative release. Historical scientific/visual records and development locks retained.'}
(OUT/'acceptance.json').write_text(json.dumps(acceptance,indent=2),encoding='utf-8')
(OUT/'review-bindings.json').write_text(json.dumps(review_bindings,indent=2),encoding='utf-8')
write_structure_lock(ROOT/'guide-project.yaml','plan/structural-locks/current.yaml')
print(json.dumps({'accepted_files':len(covered),'review_bindings':len(review_bindings),'book_model_hash':load_book(ROOT/'guide-project.yaml').content_hash()}))
