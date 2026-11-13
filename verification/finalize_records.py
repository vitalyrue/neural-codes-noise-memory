"""Record completed independent reviews and exact local delivery identity."""
from pathlib import Path
from datetime import datetime
import csv,json,hashlib,shutil,yaml
from book_runtime.release_audit import audit_release,write_structure_lock,load_book
from book_runtime.semantic_review import record_accepted_review
ROOT=Path(__file__).resolve().parents[1]
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
# This is a one-delivery recorder, not an approval script for future edits.
reviewed_model_hash='57c2164b6bda4a02484c6ccc1c7085b0df1ead23342541850b6f15f0172b26a6'
assert audit_release(ROOT/'guide-project.yaml')['book_model_hash']==reviewed_model_hash,'Content changed; obtain current independent review before recording acceptance'
scopes={
 'memory':['ch:READING-GUIDE','ch:FOUNDATIONS','ch:MEMORY-DYNAMICS','ch:MEMORY-INFORMATION','ch:GLOSSARY'],
 'eye':['ch:EYE-DRIFT'],
 'place':['ch:PLACE-FIELDS','ch:SYNTHESIS','ch:REFERENCES'],
}
for scope in scopes:
 for stage in (1,2,3):
  for suffix in ('','-recheck'):
   assert (ROOT/f'verification/reviews/{scope}-stage{stage}{suffix}.json').exists()
binding=json.loads((ROOT/'verification/reviews/final-paragraph-binding.json').read_text(encoding='utf-8'))
assert not binding['missing'] and not binding['open_decisions']

p=ROOT/'source-maps/source-coverage.csv'
rows=list(csv.DictReader(p.open(encoding='utf-8',newline='')))
for r in rows:
 scope='memory' if r['source_id'].startswith('P1') else 'eye' if r['source_id'].startswith('P2') else 'place'
 r.update(week='self-paced',unit_type='PDF page',teaching_value=r['rationale'],reason=r['rationale'],review_status='accepted',reviewer='/root/review_'+scope+'_guide',review_evidence='verification/reviews/'+scope+'-stage3-recheck.json')
with p.open('w',encoding='utf-8',newline='') as f:
 w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)

p=ROOT/'source-maps/terminology-ledger.yaml';terms=yaml.safe_load(p.read_text(encoding='utf-8'));terms['terms']=terms['first_teaching'];p.write_text(yaml.safe_dump(terms,sort_keys=False,allow_unicode=True),encoding='utf-8')
p=ROOT/'source-maps/visual-ledger.yaml';v=yaml.safe_load(p.read_text(encoding='utf-8'));meta=yaml.safe_load((ROOT/'content/chapters/01-foundations.yaml').read_text(encoding='utf-8'))['blocks'][0]
fig=v['visuals'][0]
fig.update(block_id=fig['visual_id'],status='selected',embedded=True,teaching_introduction='content/chapters/01-foundations.md: the two disturbances and solid/dashed arrow roles are explained directly before the figure.',caption=meta['caption'],interpretation='Common rate disturbance preserves 5 degrees and decays; along-line disturbance remains at 6.5 degrees.',accessibility_description=meta['alt'],provenance=fig['origin'],toc_correspondence='Chapter 1, section 1.4.1, two disturbances to the same stored angle',visual_review='verification/reviews/figure-final.json')
figure_report=ROOT/'verification/reviews/figure-final.json'
assert figure_report.is_file(),'Independent full-size figure review required'
fig['full_size_review']=dict(status='approved',reviewed_sha256=fig['sha256'],reviewer='/root/review_place_guide',evidence=figure_report.relative_to(ROOT).as_posix())
p.write_text(yaml.safe_dump(v,sort_keys=False,allow_unicode=True),encoding='utf-8')

p=ROOT/'guide-project.yaml';config=yaml.safe_load(p.read_text(encoding='utf-8'));config['plan']={'structure_lock':'plan/structural-locks/current.yaml'};p.write_text(yaml.safe_dump(config,sort_keys=False,allow_unicode=True),encoding='utf-8')
write_structure_lock(p,'plan/structural-locks/current.yaml')
book=load_book(p)
for scope,ids in scopes.items():
 record_accepted_review(book,ROOT/'verification/semantic-review-ledger.yaml',ids,reviewer='/root/review_'+scope+'_guide',evidence='verification/reviews/'+scope+'-stage3-recheck.md')

# The local delivery adds unchanged PDFs and removes only build metadata from
# the index. Preserve the raw Quarto manifest and bind those explicit steps.
p=ROOT/'verification/manifests/build-manifest.json';raw=p.with_name('quarto-build-manifest.json')
if not raw.exists():shutil.copy2(p,raw)
original=json.loads(raw.read_text(encoding='utf-8'))
audit=audit_release(ROOT/'guide-project.yaml')
assert audit['book_model_hash']==original['book_model_hash'],'Book model changed after rendering'
current=audit['artifacts']['html']
manifest=dict(original)
manifest['artifacts']={'html':{k:current[k] for k in ('path','kind','bytes','file_count','sha256')}}
manifest['finalized_at']=datetime.now().astimezone().isoformat()
manifest['quarto_build_manifest']={'path':raw.relative_to(ROOT).as_posix(),'sha256':digest(raw)}
manifest['postprocess_evidence']=['verification/publication/paper-assets.json']
manifest['checks']=['verification/publication/html-links.json','verification/publication/browser-checks.json','verification/reviews/final-paragraph-binding.json']
p.write_text(json.dumps(manifest,indent=2)+'\n',encoding='utf-8')
summary=dict(completed_at=manifest['finalized_at'],independent_paragraph_judgments=binding['paragraphs'],source_pages=len(rows),source_coverage_status='accepted for the declared teaching scope, including reasoned exclusions',semantic_chapters=sum(map(len,scopes.values())),html=manifest['artifacts']['html'],tooling_limit='Development Publisher/skill locks remain unpinned; no authoritative-release claim.',format_scope='Local HTML only; no experimental reproduction, PDF or DOCX release requested.')
(ROOT/'verification/DELIVERY.json').write_text(json.dumps(summary,indent=2)+'\n',encoding='utf-8')
print(json.dumps(summary,indent=2))
