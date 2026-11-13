"""Record this scoped delivery; never renew historical chapter acceptance."""
from pathlib import Path
from datetime import datetime
import hashlib,json,shutil,sys,yaml
from book_runtime.release_audit import audit_release
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,'C:/Users/vital/.codex/skills/course-diagram-builder/scripts')
from visual_review import audit_ledger

def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()

ledger=yaml.safe_load((ROOT/'source-maps/visual-ledger.yaml').read_text(encoding='utf-8'))
newrows=[r for r in ledger['visuals'] if 'review_contract' in r]
newaudit=audit_ledger({'visuals':newrows},ROOT)
assert newaudit['status']=='pass' and newaudit['reviewed_figures']==9
allaudit=audit_ledger(ledger,ROOT)
assert allaudit['findings']==[{'rule':'visual-acceptance-missing','location':'fig:FOUNDATIONS-ATTRACTOR','reason':'Selected technical figure requires review_contract and criterion-level diagram_review; a generic approved flag is insufficient'}]
allaudit['scope_note']='The unchanged original SVG retains its earlier independent full-size review. Only its older record format lacks the newer criterion schema; this task did not migrate that historical asset or claim a full-book release.'
for name,data in [('new-figures-review-audit',newaudit),('all-figures-review-audit',allaudit)]:
    (ROOT/f'verification/illustrations/{name}.json').write_text(json.dumps(data,indent=2),encoding='utf-8')

for check in ['html-links','illustrations-browser','illustrations-map-links','all-reader-tables']:
    data=json.loads((ROOT/f'verification/publication/{check}.json').read_text(encoding='utf-8'))
    assert data['status']=='pass',(check,data)
assert digest(ROOT/'assets/approved/visuals/attractor-directions.svg')=='42be8b1bee6869b3f2218d8b7618c30c7ad59986f14a2ed994094c7fadb93fe9'

oldbindings=json.loads((ROOT/'verification/illustrations/source-bindings-reviewed.json').read_text(encoding='utf-8'))
current=json.loads((ROOT/'verification/illustrations/current-bindings.json').read_text(encoding='utf-8'))
assert oldbindings['figures']==current['figures']

raw=ROOT/'verification/manifests/illustrations-20261023-quarto-manifest.json'
manifest_path=ROOT/'verification/manifests/build-manifest.json'
if not raw.exists():shutil.copy2(manifest_path,raw)
manifest=json.loads(raw.read_text(encoding='utf-8'))
audit=audit_release(ROOT/'guide-project.yaml')
assert manifest['book_model_hash']==current['book_model_hash']==audit['book_model_hash']
html=audit['artifacts']['html']
manifest['artifacts']={'html':{k:html[k] for k in ['path','kind','bytes','file_count','sha256']}}
manifest['finalized_at']=datetime.now().astimezone().isoformat()
manifest['quarto_build_manifest']={'path':raw.relative_to(ROOT).as_posix(),'sha256':digest(raw)}
manifest['postprocess_evidence']=['verification/publication/paper-assets.json']
manifest['checks']=['verification/publication/html-links.json','verification/publication/all-reader-tables.json','verification/publication/illustrations-browser.json','verification/publication/illustrations-map-links.json','verification/illustrations/new-figures-review-audit.json']
manifest['review_scope']='Nine new images and their connected inserted text; no renewal of historical whole-chapter review records.'
manifest_path.write_text(json.dumps(manifest,indent=2),encoding='utf-8')

summary={
 'completed_at':manifest['finalized_at'],'task_started_at':'2026-10-23T21:56:31.9322700+03:00',
 'approved_plan':'plan/illustrations/PLAN.md','plan_additions_completed':8,'new_image_assets':9,
 'original_attractor_preserved':True,'all_reader_figures':10,
 'html':manifest['artifacts']['html'],'book_model_hash':current['book_model_hash'],
 'review_scope':manifest['review_scope'],
 'independent_stages':['truth/reasoning and exact images','necessity and wording with repairs rechecked','connected reader understanding and flow'],
 'checks':manifest['checks'],
 'browser_scope':'18 figure checks at desktop and narrow widths; two representative figure contexts visually sampled; two real map-link clicks verified.',
 'legacy_limit':'Existing original attractor has its historical review format; modern full-ledger audit has that one schema hold. All nine new criterion records pass.',
 'tooling_limit':'Development/unpinned tool locks and historical whole-chapter review state are not renewed. Local HTML only; no authoritative or public release claim.',
 'editable_vectors':'assets/approved/visuals/*.svg; generators in verification/illustrations/',
 'awake_execution_time':'unverified','token_stats':'unavailable',
}
(ROOT/'verification/DELIVERY.json').write_text(json.dumps(summary,indent=2),encoding='utf-8')
(ROOT/'verification/illustrations/DELIVERY.json').write_text(json.dumps(summary,indent=2),encoding='utf-8')
print(json.dumps({k:summary[k] for k in ['completed_at','plan_additions_completed','new_image_assets','all_reader_figures','html','book_model_hash']},indent=2))
