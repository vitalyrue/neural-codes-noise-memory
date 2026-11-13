from pathlib import Path
from datetime import datetime, timezone
import json,csv,yaml,hashlib
from book_runtime.compiler.loader import load_book
from book_runtime.semantic_review import record_accepted_review
from book_runtime.release_audit import build_structure_lock,write_structure_lock

root=Path(__file__).resolve().parents[2];task=Path(__file__).resolve().parent
ids=['ch:SIMULATING-MEMORY','ch:SIMULATING-EYE','ch:SIMULATING-PLACE','ch:SIMULATION-TOOLS']
for name in ['memory','eye','place']:
    d=json.loads((task/f'review-{name}-stage3.json').read_text(encoding='utf-8'))
    assert str(d.get('verdict',d.get('status'))).lower().startswith('pass'),(name,d.get('verdict',d.get('status')))
check=json.loads((task/'concept-check.json').read_text(encoding='utf-8'))
assert check['clear'] and not check['findings']
book=load_book(root/'guide-project.yaml')
record_accepted_review(book,root/'verification/semantic-review-ledger.yaml',ids,
    reviewer='/root/sim_sources_memory; /root/sim_sources_eye; /root/sim_sources_place: independent separate truth, wording and reader-flow calls',
    evidence='verification/part4-simulations-20261030/RESULTS.md; review-*-stage1/2/3.json and separate repair rechecks; concept-check.json. New Part IV text and changed Part openings only. Previous whole-guide and figure holds remain.')
baseline=yaml.safe_load((task/'baseline/plan/structural-locks/current.yaml').read_text(encoding='utf-8'))
new=build_structure_lock(book)
# Only the requested Part opening prose changed in the original Parts.
for a,b in zip(baseline['parts'],new['parts'][:3]):
    for k in ['id','title','chapters']:
        if k=='chapters':
            assert [(c['id'],c['title']) for c in a[k]]==[(c['id'],c['title']) for c in b[k]]
        else:assert a[k]==b[k],k
write_structure_lock(root/'guide-project.yaml','plan/structural-locks/current.yaml')
p=root/'source-maps/source-coverage.csv'
with p.open(encoding='utf-8',newline='') as f:r=csv.DictReader(f);fields=r.fieldnames;rows=list(r)
count=0
for row in rows:
    if row['source_unit_id'].startswith('SIM-'):
        count+=1;row['review_status']='accepted'
        row['reviewer']='/root/sim_sources_memory; /root/sim_sources_eye; /root/sim_sources_place'
        row['review_evidence']='verification/part4-simulations-20261030/RESULTS.md; independent stage1/2/3 records'
        row['reason']='Selected simulation method source verified and taught in the reviewed new Part IV. Full source simulations were not rerun.'
with p.open('w',encoding='utf-8',newline='') as f:w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(rows)
p=root/'source-maps/research-ledger.csv'
with p.open(encoding='utf-8',newline='') as f:r=csv.DictReader(f);fields=r.fieldnames;rows=list(r)
for row in rows:
    if row['claim_id'].startswith('SIM-'):row['status']='source verified and independently reviewed in Part IV; see verification/part4-simulations-20261030/RESULTS.md'
with p.open('w',encoding='utf-8',newline='') as f:w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(rows)
preserved={}
for name in ['source-inventory.csv','source-coverage.csv','research-ledger.csv']:
    with (task/'baseline/source-maps'/name).open(encoding='utf-8',newline='') as f:old=list(csv.DictReader(f))
    with (root/'source-maps'/name).open(encoding='utf-8',newline='') as f:current=list(csv.DictReader(f))
    preserved[name]=old==current[:len(old)];assert preserved[name],name
(task/'scoped-acceptance.json').write_text(json.dumps({'at':datetime.now(timezone.utc).isoformat(),'book_model_hash':book.content_hash(),'accepted_chapters':ids,'existing_chapter_ids_titles_order_preserved':True,'old_source_rows_unchanged':preserved,'new_source_groups':count,'scope':'New Part IV text and changed Part introductions. Existing full-guide and figure holds remain.'},indent=2),encoding='utf-8')
print('Accepted four new chapters and',count,'selected method groups. Original chapters and source rows preserved.')
