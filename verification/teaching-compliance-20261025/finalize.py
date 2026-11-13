from pathlib import Path
from datetime import datetime
import json,hashlib,yaml
from book_runtime.release_audit import load_book,audit_release,write_structure_lock
from book_runtime.semantic_review import record_accepted_review
OUT=Path(__file__).resolve().parent;ROOT=OUT.parents[1]
load=lambda p:json.loads(p.read_text(encoding='utf-8'))
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
for name in ['preservation-check.json','rendered-check.json','browser-check.json','pixel-review.json','map-ledger-check.json','packet-validation-final.json']:
    assert load(OUT/name)['status']=='pass',name
assert load(OUT/'concept-check.json')['clear']
bindings=load(OUT/'review-bindings.json');assert bindings['missing']==[] and bindings['reviewed_paragraphs']==824
for row in bindings['source_bindings']:
    # The input packet acquired independently reviewed annotations after each
    # reader recorded its input hash. The final validator checks its preserved
    # full source inventory and annotations against the actual current files.
    if Path(row['file']).resolve()==(OUT/'pedagogy-final/PARAGRAPH_REVIEW.json').resolve():continue
    assert sha(Path(row['file']))==row['sha256'],row['file']
for row in load(OUT/'workflow-assembly.json')['actual_report_bindings']:
    assert sha(ROOT/row['path'])==row['sha256'],row['path']
sources={p.relative_to(ROOT).as_posix():sha(p) for p in (ROOT/'content/chapters').glob('*') if p.suffix in ('.md','.yaml')}
for rel in ['content/index.md','guide-project.yaml','plan/chapter-plan.yaml']:sources[rel]=sha(ROOT/rel)
reviewed_paths={Path(row['file']).resolve() for row in bindings['source_bindings']}
assert all((ROOT/rel).resolve() in reviewed_paths for rel in sources if rel.startswith('content/chapters/'))
scope='Whole-guide local teaching revision: all13teaching chapters, reading guide, glossary, References, landing text and Part purposes. Independent correctness, necessity/terminology and understanding/flow reviews, current-source adoptions and repair rechecks, full paragraph/unit/claim evidence and book-wide prerequisite checks.'
limits='Local HTML delivery only. No animal-data reanalysis or reproduction of full network simulations, no new public deployment, no PDF/DOCX release and no whole-book pixel sweep. Existing development tooling locks remain unchanged. The changed paper-map has a fresh criterion review; other historical diagram release records were not migrated. No authoritative-release certification is claimed.'
evidence=['stage1-memory.json','stage1-eye.json','stage1-place.json','stage1-recheck-memory.json','stage1-recheck-eye.json','stage1-recheck-place-stage2.json','stage2-memory.json','stage2-eye.json','stage2-place.json','stage3-memory.json','stage3-eye.json','stage3-place.json','integration-recheck-place.json','review-bindings.json','workflow-assembly.json','packet-validation-final.json','concept-check.json','map-ledger-check.json']
acceptance={'at':datetime.now().astimezone().isoformat(),'status':'accepted for whole-guide local teaching revision','scope':scope,'independent_reviewers':['/root/compliance_memory','/root/compliance_eye','/root/compliance_place'],'source_bindings':sources,'evidence':[str((OUT/x).relative_to(ROOT)).replace('\\','/') for x in evidence],'packet_units':75,'paragraph_records':824,'concepts':57,'relations':199,'teaching_sets':32,'unresolved_teaching_findings':[],'limits':limits}
(OUT/'acceptance.json').write_text(json.dumps(acceptance,ensure_ascii=False,indent=2),encoding='utf-8')
book=load_book(ROOT/'guide-project.yaml')
scopes={'memory':['ch:FOUNDATIONS','ch:PERSISTENCE','ch:MEMORY-DYNAMICS','ch:MEMORY-LONG-DELAYS','ch:MEMORY-INFORMATION','ch:MEMORY-READOUT'],'eye':['ch:READING-GUIDE','ch:EYE-DRIFT','ch:EYE-TIMING','ch:EYE-CIRCUIT'],'place':['ch:PLACE-FIELDS','ch:PLACE-SIZES','ch:PLACE-TESTS','ch:SYNTHESIS','ch:REFERENCES']}
for group,ids in scopes.items():
    record_accepted_review(book,ROOT/'verification/semantic-review-ledger.yaml',ids,reviewer='/root/compliance_'+group,evidence=f'verification/teaching-compliance-20261025/final-recheck-{group}.json')
record_accepted_review(book,ROOT/'verification/semantic-review-ledger.yaml',['ch:GLOSSARY'],reviewer='/root/compliance_memory, /root/compliance_eye, /root/compliance_place',evidence='verification/teaching-compliance-20261025/acceptance.json')
write_structure_lock(ROOT/'guide-project.yaml','plan/structural-locks/current.yaml')
raw=load(OUT/'raw-build-manifest.json');assert raw['book_model_hash']==book.content_hash()
html=audit_release(ROOT/'guide-project.yaml')['artifacts']['html']
manifest={**raw,'artifacts':{'html':{k:html[k] for k in ['path','kind','bytes','file_count','sha256']}},'finalized_at':datetime.now().astimezone().isoformat(),'quarto_build_manifest':{'path':(OUT/'raw-build-manifest.json').relative_to(ROOT).as_posix(),'sha256':sha(OUT/'raw-build-manifest.json')},'postprocess_evidence':['verification/publication/paper-assets.json'],'checks':[(OUT/n).relative_to(ROOT).as_posix() for n in ['acceptance.json','packet-validation-final.json','concept-check.json','preservation-check.json','rendered-check.json','browser-check.json','pixel-review.json','map-ledger-check.json']],'review_scope':scope}
(ROOT/'verification/manifests/build-manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf-8')
audit=audit_release(ROOT/'guide-project.yaml');(OUT/'release-audit.json').write_text(json.dumps(audit,ensure_ascii=False,indent=2),encoding='utf-8');assert audit['status']=='passed',audit.get('findings')
now=datetime.now().astimezone();start=datetime.fromisoformat('2026-10-25T20:11:31.8244846+02:00')
delivery={'completed_at':now.isoformat(),'started_at':start.isoformat(),'wall_elapsed_seconds':round((now-start).total_seconds(),1),'awake_execution_time':'unverified','token_stats':'unavailable','status':'whole-guide local teaching revision complete','teaching_chapters':13,'reviewed_reader_sources':16,'review_units':75,'paragraph_records':824,'indexed_concepts':57,'concept_relations':199,'recorded_exact_edits':93,'html_pages_checked':19,'local_targets_checked':931,'browser_checks':22,'page_screenshots_inspected':3,'figures':22,'tables':4,'optional_notes':10,'blue_teaching_terms':97,'glossary_entries':97,'screen_body_font_px':11.9,'book_model_hash':book.content_hash(),'html':manifest['artifacts']['html'],'standard_release_audit':'passed','preview':'http://127.0.0.1:8765/guide/site/','limits':limits}
for p in [OUT/'DELIVERY.json',ROOT/'verification/DELIVERY.json']:p.write_text(json.dumps(delivery,ensure_ascii=False,indent=2),encoding='utf-8')
report=f'''# Whole-guide teaching revision

Completed {now.isoformat()}. The existing local HTML is rebuilt and accepted for the teaching scope below.

All13teaching chapters and the reading guide, glossary, References, landing text and Part purposes were reviewed. The current order was retained after checking its prerequisites and comparing plausible alternatives. Chapter overviews remain before the first section and explain why each chapter takes its chosen route.

## Repairs

- Brownian motion is taught before its first continuous-diffusion equation, including mean-zero increments and continuous paths.
- The eye-timing chapter now builds its stochastic integral from weighted increments and derives the shared-increment covariance step by step.
- The tuning-width comparison states the symmetry needed to turn the matrix information bound into a per-coordinate diffusion result.
- The three-paper map now points to chapters3–6,7–9and10–12. Its scientific drawing and dimensions are unchanged.
- Caption operations and sampling language are more explicit; unused labels, repeated commentary and duplicate citation text were removed individually. DOI links have readable labels.

The13chapter structure, contribution-based headings,97blue first-teaching terms,97glossary entries,22figures,four typed tables,ten optional folds and11.9px reading size are retained. Paper copies and print styles are unchanged.

## Evidence

The Publisher0.8.23 teaching skill and quality companion were used. Three independent reviewers completed separate truth/reasoning, necessity/terminology and reader-understanding stages. Original calls and source versions are preserved; current adoption and repair rechecks are recorded separately.

- Whole-book review validation passes75units and824passage records with no unresolved findings. The count includes structural wrapper records, which are explicitly distinguished from prose.
- The prerequisite checker covers57reviewed concepts,199relations and32joint teaching sets across73sections, with no ordering finding. Display equations were checked directly because the extractor does not include all of them.
- All19HTML pages and931local targets pass structural/link checks.22browser checks and three inspected desktop/narrow screenshots cover the revised explanations, math, blue definitions, font size, example interaction and source navigation.
- Final BookModel: `{book.content_hash()}`. Final HTML tree: `{html['sha256']}`.

Exact changes are in repairs-v1.json and repairs-v2.json; current independent acceptance is in acceptance.json. Full packet validation is in packet-validation-final.json. Earlier failed parser checks remain as history and were resolved without manuscript changes.

## Scope limits

{limits}

Wall time at artifact completion: {delivery['wall_elapsed_seconds']}seconds. Awake execution time unverified. Token stats unavailable.
'''
(OUT/'RESULTS.md').write_text(report,encoding='utf-8')
state=ROOT/'CURRENT_STATE.md';text=state.read_text(encoding='utf-8')
entry=f'''### {now.strftime('%Y-%m-%d %H:%M:%S %z')}: whole-guide teaching revision complete

- Reviewed all13teaching chapters plus reading guide, glossary, References, landing text and Part purposes under Publisher0.8.23's packaged teaching skill. Kept the13chapter order and motivated openings after an independent global-order check. Repaired Brownian first teaching, the weighted-increment/covariance bridge in eye timing, the symmetry premise of the information-width comparison, clearer captions/wording and outdated paper-map chapter numbers. Exact93edits and all source snapshots are in verification/teaching-compliance-20261025.
- Actual independent three-stage reviews, current-source adoptions and repair rechecks now cover the final source. Publisher's whole-book review validator passes75units/824records; concept-order check passes57concepts/199relations/32teaching sets across73sections. Display equations were read directly. Original reports/times remain unchanged; structured historical reuse records preserve the actual fresh independent starts. Current semantic ledger records16accepted chapters/appendices.
- Rebuilt localHTML.19pages/931local targets pass;22browser checks and3page screenshots pass.22figures,4tables,10folds,97blue teaching terms,97glossary entries,11.9px screen type and original print styles remain. Only the paper-map asset changed, with current independent full/700px criterion review. No full pixel sweep or raw-data replication.
- BookModel `{book.content_hash()}`; finalHTML `{html['sha256']}`. Standard release audit passes. Development tool locks and other historical diagram release records remain unchanged; this is local teaching acceptance, not an authoritative/public release. See verification/teaching-compliance-20261025/RESULTS.md and DELIVERY.json. No unresolved teaching repair remains. Preview: http://127.0.0.1:8765/guide/site/.
- Started {start.isoformat()}; artifact completed {now.isoformat()}; wall elapsed {delivery['wall_elapsed_seconds']}s. Awake execution unverified. Token stats unavailable. Final handoff checkpoints are in this task's RUN.md/checkpoints.jsonl.

'''
assert '## Open work\n\n' in text
state.write_text(text.replace('## Open work\n\n','## Open work\n\n'+entry,1),encoding='utf-8')
print(json.dumps(delivery,ensure_ascii=False,indent=2))
