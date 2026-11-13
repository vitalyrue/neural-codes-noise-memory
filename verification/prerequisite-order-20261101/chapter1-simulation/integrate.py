from pathlib import Path
from datetime import datetime, timezone
import json, yaml, hashlib, csv, io
from book_runtime.compiler.loader import load_book
from book_runtime.release_audit import build_structure_lock, write_structure_lock
root=Path('.').resolve();task=root/'verification/prerequisite-order-20261101';ext=task/'chapter1-simulation'
review=json.loads((ext/'stage3.json').read_text(encoding='utf-8'))
assert review['status'].startswith('pass') and not review.get('remaining_findings') and not review.get('required_repairs')
old=json.loads((task/'concept-index-reviewed.json').read_text(encoding='utf-8'))
new=json.loads((ext/'concept-index-final.json').read_text(encoding='utf-8'))
assert old['chapter_order']==new['chapter_order']
oldp={x['id']:x for x in old['passages']};newp={x['id']:x for x in new['passages']}
base=json.loads((task/'concept-judgments-merged.json').read_text(encoding='utf-8'))
for rel in base['relations']:
 assert oldp[rel['passage_id']]['text']==newp[rel['passage_id']]['text'],rel['passage_id']
add=json.loads((ext/'concept-judgments.json').read_text(encoding='utf-8'))
assert not set(c['id'] for c in base['concepts']) & set(c['id'] for c in add['concepts'])
for key in ['concepts','relations','teaching_sets']:base[key].extend(add.get(key,[]))
base['sections'].update(add['sections'])
base['review_scope']+=' Chapter1 simulation introduction and symbol-before-equation moves separately reviewed in chapter1-simulation/stage1.json, stage1-addendum.json, stage2.json, recheck.json and stage3.json; retained old relation passages were checked identical.'
(ext/'whole-book-judgments.json').write_text(json.dumps(base,indent=2),encoding='utf-8')
# Refresh first-teaching locations; existing late references remain valid.
p=root/'source-maps/terminology-ledger.yaml';terms=yaml.safe_load(p.read_text(encoding='utf-8'));lines=(root/'content/chapters/01-foundations.md').read_text(encoding='utf-8').splitlines();seen=set()
for key in ['first_teaching','terms']:
 rows=terms[key]
 if id(rows) in seen:continue
 seen.add(id(rows))
 for term in ['preferred angle','activity bump','Euler update']:
  found=[x for x in rows if x.get('term')==term and x.get('source')!='content/chapters/glossary.md']
  record={'term':term,'source':'content/chapters/01-foundations.md','line':next(i for i,s in enumerate(lines,1) if '**'+term+'**' in s),'guide_location':'sec:FOUNDATIONS-SIMULATION'}
  if found:
   for row in found:row.update(record)
  else: rows.append(record)
 for row in rows:
  if row.get('source')=='content/chapters/01-foundations.md':
   matches=[i for i,s in enumerate(lines,1) if '**'+row['term']+'**' in s]
   if matches:row['line']=matches[0]
p.write_text(yaml.safe_dump(terms,sort_keys=False,allow_unicode=True,width=100),encoding='utf-8')
p=root/'source-maps/source-coverage.csv';rows=list(csv.DictReader(io.StringIO(p.read_text(encoding='utf-8'))));fields=list(rows[0])
for row in rows:
 if row['source_unit_id'] in ['P1-p03','P1-p06']:
  row['review_status']='accepted';row['reviewer']='/root/prereq_memory';row['review_evidence']='verification/prerequisite-order-20261101/chapter1-simulation/source-review.json; verification/prerequisite-order-20261101/chapter1-simulation/stage3.json'
with p.open('w',encoding='utf-8',newline='') as f:
 w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(rows)
# Preserve previous outline, allowing exactly the requested new section.
book=load_book(root/'guide-project.yaml');before=yaml.safe_load((ext/'baseline/plan/structural-locks/current.yaml').read_text(encoding='utf-8'));after=build_structure_lock(book)
def ids(obj):
 result=[]
 if isinstance(obj,dict):
  if 'id' in obj:result.append(obj['id'])
  for v in obj.values():result.extend(ids(v))
 elif isinstance(obj,list):
  for v in obj:result.extend(ids(v))
 return result
oldids=ids(before);newids=ids(after);missing=[x for x in oldids if x not in newids];added=[x for x in newids if x not in oldids]
assert not missing,missing
assert added==['sec:FOUNDATIONS-SIMULATION'],added
write_structure_lock(root/'guide-project.yaml','plan/structural-locks/current.yaml')
p=root/'plan/change-ledger.yaml';ledger=yaml.safe_load(p.read_text(encoding='utf-8'));ledger['changes'].append({'date':'2026-11-01','scope':'Chapter1 network simulation foundation','disposition':'added requested section; reordered local symbol definitions','guide_locus':'sec:FOUNDATIONS-SIMULATION; sec:MEMORY-SPIKES','reason':'Explain the simulated circuit, neuron interdependence and simulation-versus-theory evidence before later derivations. Put model symbols before Eqs.7–9.','retained':'All prior chapters, sections, equations, figures, typography and print rules; detailed simulation implementation remains in Chapter18.','evidence':'verification/prerequisite-order-20261101/chapter1-simulation/reader.diff','review':'verification/prerequisite-order-20261101/chapter1-simulation/stage3.json'})
p.write_text(yaml.safe_dump(ledger,sort_keys=False,allow_unicode=True,width=100),encoding='utf-8')
report={'at_utc':datetime.now(timezone.utc).isoformat(),'chapter_order_unchanged':True,'retained_old_outline_ids':len(oldids),'added_section_ids':added,'missing_ids':missing,'old_relation_passages_identical':len(base['relations'])-len(add['relations']),'current_book_model_hash':book.content_hash(),'concept_count':len(base['concepts']),'relations':len(base['relations']),'reviewed_sections':len(base['sections'])}
(ext/'integration.json').write_text(json.dumps(report,indent=2),encoding='utf-8');print(json.dumps(report))
