"""Record this local HTML revision after independent source and browser checks."""
from pathlib import Path
from datetime import datetime
import hashlib,json,yaml
from book_runtime.release_audit import load_book,audit_release,write_structure_lock

OUT=Path(__file__).resolve().parent
ROOT=OUT.parents[1]
read=lambda p:json.loads(p.read_text(encoding='utf-8'))
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
now=datetime.now().astimezone()
frozen=read(OUT/'frozen-v3.json')
for rel,digest in frozen['sources'].items():assert sha(OUT/rel)==digest,rel
for name in ['browser-check.json','post-build-check.json','math-scroll-check.json']:
    assert read(OUT/name)['status']=='pass',name
groups=['foundations-memory','information-eye','place-synthesis-orientation']
evidence=[]
for group in groups:
    for stage in [1,2,3]:
        p=OUT/f'stage{stage}-{group}.json';assert p.exists();evidence.append(p.name)
    assert not read(OUT/f'stage3-{group}.json')['unresolved_findings'],group
    evidence.append(f'stage1-recheck-{group}.json')
bindings=[]
for rel in frozen['sources']:
    proposal=OUT/rel
    canonical=ROOT/Path(rel).relative_to('proposed')
    assert proposal.read_text(encoding='utf-8')==canonical.read_text(encoding='utf-8'),rel
    bindings.append({'path':canonical.relative_to(ROOT).as_posix(),'reviewed_sha256':sha(proposal),
                     'canonical_sha256':sha(canonical),'reader_text_exactly_equal':True})
acceptance={'at':now.isoformat(),'status':'accepted for this local revision',
 'scope':'Contribution-based titles, selected optional folds, paragraph order and connected explanations across six teaching chapters, reading guide and Part text. Separate truth, wording and reader-flow calls completed; required findings repaired and rechecked.',
 'evidence':evidence+['stage1-repairs.json','stage2-repairs.json','coordinator-order-review.md'],
 'source_bindings':bindings,'line_endings':'Canonical integration uses LF; some reviewed proposals use CRLF. Decoded reader text is exactly equal in every paired source.',
 'retained_optional_preference':'The covariance section could mention shared fluctuations in its title; the current title accurately states the MSD result. No further wording change required.',
 'limits':'Local HTML only. Existing whole-chapter scientific review records and visual review records remain historical. No new empirical reproduction, full pixel sweep, public release or authoritative release claim.'}
(OUT/'acceptance.json').write_text(json.dumps(acceptance,indent=2),encoding='utf-8')
pixels={'at':now.isoformat(),'status':'pass','reviewer':'root, actual image inspection',
 'samples':[{'file':'sample-ch-memory-dynamics-closed-878.png','judgment':'Closed proof note is visible between the result/figure interpretation and the variable-D continuation; title wraps cleanly and focus remains visible.'},
 {'file':'sample-information-open-878.png','judgment':'Expanded supporting example shows readable prose and rendered equations, with the note summary and surrounding argument visible.'},
 {'file':'sample-ch-place-fields-closed-390.png','judgment':'Narrow-screen fold label wraps within the page. Main text remains readable. The long equation uses its own horizontal scrolling, separately exercised by math-scroll-check.json.'}],
 'limits':'Three page-context samples, not a whole-book visual sweep. No new artwork.'}
(OUT/'browser-pixel-review.json').write_text(json.dumps(pixels,indent=2),encoding='utf-8')

book=load_book(ROOT/'guide-project.yaml')
manifest=read(OUT/'raw-build-manifest.json')
assert manifest['book_model_hash']==book.content_hash()
write_structure_lock(ROOT/'guide-project.yaml','plan/structural-locks/current.yaml')
observed=audit_release(ROOT/'guide-project.yaml')
html=observed['artifacts']['html']
manifest['artifacts']={'html':{k:html[k] for k in ['path','kind','bytes','file_count','sha256']}}
manifest['finalized_at']=now.isoformat()
manifest['quarto_build_manifest']={'path':(OUT/'raw-build-manifest.json').relative_to(ROOT).as_posix(),'sha256':sha(OUT/'raw-build-manifest.json')}
manifest['postprocess_evidence']=['verification/publication/paper-assets.json']
manifest['checks']=[(OUT/n).relative_to(ROOT).as_posix() for n in ['acceptance.json','post-build-check.json','browser-check.json','math-scroll-check.json','browser-pixel-review.json']]
manifest['review_scope']=acceptance['scope']
(ROOT/'verification/manifests/build-manifest.json').write_text(json.dumps(manifest,indent=2),encoding='utf-8')
audit=audit_release(ROOT/'guide-project.yaml')
(OUT/'release-audit.json').write_text(json.dumps(audit,indent=2),encoding='utf-8')
assert audit['status']=='passed',audit.get('findings')
integration=read(OUT/'integration.json')
oldplan=yaml.safe_load((OUT/'baseline/plan/chapter-plan.yaml').read_text(encoding='utf-8'))
newplan=yaml.safe_load((ROOT/'plan/chapter-plan.yaml').read_text(encoding='utf-8'))
part_changes=sum(a['title']!=b['title'] for a,b in zip(oldplan['book']['parts'],newplan['book']['parts']))
heading_changes=part_changes+sum(len(r['heading_changes']) for r in integration['records'])
started=datetime.fromisoformat('2026-10-24T18:54:22.5524387+03:00')
finished=datetime.now().astimezone()
delivery={'completed_at':finished.isoformat(),'task_started_at':started.isoformat(),
 'wall_elapsed_seconds':round((finished-started).total_seconds(),1),'awake_execution_time':'unverified',
 'interruption':'1976.3 seconds between persisted checkpoints 19:08:49 and 19:41:45; no matching Windows sleep/resume or clock-change event returned by the scoped query.',
 'token_stats':'unavailable','titles_changed':heading_changes,'optional_folds':10,'figures_preserved':22,
 'blue_first_definitions':'verified in browser at 878 and 390 px',
 'browser_scope':'14 page/viewport cases; all ten notes clicked open and closed, keyboard and print behavior tested. Three screenshots inspected. Four overflowing equations scrolled at 390 px.',
 'source_preservation':'Original displayed mathematics, source links, stable anchors and typed figure/table content preserved. Seven original prose units have recorded connection/definition-placement or topology repairs.',
 'book_model_hash':book.content_hash(),'html':manifest['artifacts']['html'],'standard_release_audit':'pass',
 'preview':'http://127.0.0.1:8765/guide/site/','checks':manifest['checks'],'limits':acceptance['limits'],
 'concept_index':'Focused Ito-convention teach/use pair checked with no relation-order finding. The index is intentionally partial; independent passage-based Stage3 records carry the wider closed-fold judgments.'}
for p in [OUT/'DELIVERY.json',ROOT/'verification/DELIVERY.json']:
    p.write_text(json.dumps(delivery,indent=2),encoding='utf-8')
print(json.dumps({k:delivery[k] for k in ['completed_at','wall_elapsed_seconds','titles_changed','optional_folds','book_model_hash','standard_release_audit']},indent=2))
