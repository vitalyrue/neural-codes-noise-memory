from pathlib import Path
from datetime import datetime,timezone
import json,csv,yaml
from book_runtime.compiler.loader import load_book
from book_runtime.semantic_review import record_accepted_review
from book_runtime.release_audit import build_structure_lock,write_structure_lock

root=Path(__file__).resolve().parents[2]; task=Path(__file__).resolve().parent
for name in ['memory','systems','tests']:
 d=json.loads((task/f'review-{name}-stage3.json').read_text(encoding='utf-8'))
 assert str(d['verdict']).lower().startswith('pass'),(name,d['verdict'])
check=json.loads((task/'concept-check.json').read_text(encoding='utf-8'))
assert check['clear'] and not check['findings']
book=load_book(root/'guide-project.yaml')
ids=['ch:HARDWARE-MEMORY','ch:HARDWARE-DYNAMICS','ch:NEUROMORPHIC-SYSTEMS','ch:HARDWARE-TESTS']
record_accepted_review(book,root/'verification/semantic-review-ledger.yaml',ids,
 reviewer='/root/part3_review_memory; /root/part3_review_systems; /root/part3_review_tests: independent separate truth, wording, and reader-flow calls',
 evidence='verification/part3-neuromorphic-20261030/RESULTS.md; review-*-stage1/2/3.json; concept-check.json; footnote-spacing-reuse.json; table-format-reuse.json; rebind-locators.json. New Part III text only; prior whole-guide and figure holds unchanged.')
baseline=yaml.safe_load((task/'baseline/plan/structural-locks/current.yaml').read_text(encoding='utf-8'))
new=build_structure_lock(book)
assert baseline['parts']==new['parts'][:2]
write_structure_lock(root/'guide-project.yaml','plan/structural-locks/current.yaml')
source_ids={'VN1958','IntelLoihi2-2021','Pehle2022','Scholze2026','LeGallo2023','Sun2026','Seung1996','Massoud2011','Giulioni2012','Kleyko2025','Aitsam2026','Ortner2025','Wang2026','Ilmberger2025'}
p=root/'source-maps/source-coverage.csv'
with p.open(encoding='utf-8',newline='') as f:r=csv.DictReader(f);fields=r.fieldnames;rows=list(r)
for row in rows:
 if row['source_id'] in source_ids:
  row['review_status']='accepted'
  row['reviewer']='/root/part3_review_memory; /root/part3_review_systems; /root/part3_review_tests'
  row['review_evidence']='verification/part3-neuromorphic-20261030/RESULTS.md; independent stage1/2/3 records; selected-passage scope only'
  row['reason']='Selected source passage taught at the corrected guide locus and checked in independent staged review. Other source sections are outside this extension.'
with p.open('w',encoding='utf-8',newline='') as f:w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(rows)
p=root/'source-maps/research-ledger.csv'
with p.open(encoding='utf-8',newline='') as f:r=csv.DictReader(f);fields=r.fieldnames;rows=list(r)
for row in rows:
 if any(s in row['claim_id'] for s in source_ids):
  row['status']='source-verified and independently reviewed in new Part III text; see verification/part3-neuromorphic-20261030/RESULTS.md'
with p.open('w',encoding='utf-8',newline='') as f:w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(rows)
preserved={}
for name in ['source-inventory.csv','source-coverage.csv','research-ledger.csv']:
 with (task/'baseline/source-maps'/name).open(encoding='utf-8',newline='') as f:old=list(csv.DictReader(f))
 with (root/'source-maps'/name).open(encoding='utf-8',newline='') as f:current=list(csv.DictReader(f))
 preserved[name]=old==current[:len(old)]
 assert preserved[name],name
(task/'scoped-acceptance.json').write_text(json.dumps({'at':datetime.now(timezone.utc).isoformat(),'book_model_hash':book.content_hash(),'accepted_chapters':ids,'old_parts_unchanged':True,'old_source_rows_unchanged':preserved,'scope':'New Part III semantic acceptance, with inherited whole-guide/figure/output holds unchanged.'},indent=2),encoding='utf-8')
print('Accepted four new chapters and 14 selected source groups. Old Part structure and source rows preserved.')
