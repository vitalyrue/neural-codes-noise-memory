from pathlib import Path
from datetime import datetime
import hashlib,json
from book_runtime.release_audit import load_book,audit_release
OUT=Path(__file__).resolve().parent;ROOT=OUT.parents[1]
load=lambda p:json.loads(p.read_text(encoding='utf-8'));sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
for name in ['draft-check.json','rendered-check.json','browser-check.json','pixel-review.json']:assert load(OUT/name)['status']=='pass',name
accept=load(OUT/'acceptance.json')
for rel,digest in accept['source_bindings'].items():assert sha(ROOT/rel)==digest,rel
book=load_book(ROOT/'guide-project.yaml');manifest=load(OUT/'raw-build-manifest.json')
assert book.content_hash()==manifest['book_model_hash']
html=audit_release(ROOT/'guide-project.yaml')['artifacts']['html']
manifest['artifacts']={'html':{k:html[k] for k in ['path','kind','bytes','file_count','sha256']}}
manifest['finalized_at']=datetime.now().astimezone().isoformat()
manifest['quarto_build_manifest']={'path':(OUT/'raw-build-manifest.json').relative_to(ROOT).as_posix(),'sha256':sha(OUT/'raw-build-manifest.json')}
manifest['postprocess_evidence']=['verification/publication/paper-assets.json']
manifest['checks']=[(OUT/name).relative_to(ROOT).as_posix() for name in ['acceptance.json','review-bindings.json','draft-check.json','rendered-check.json','browser-check.json','pixel-review.json']]
manifest['review_scope']=accept['scope']
(ROOT/'verification/manifests/build-manifest.json').write_text(json.dumps(manifest,indent=2),encoding='utf-8')
audit=audit_release(ROOT/'guide-project.yaml');(OUT/'release-audit.json').write_text(json.dumps(audit,indent=2),encoding='utf-8');assert audit['status']=='passed',audit.get('findings')
now=datetime.now().astimezone();start=datetime.fromisoformat('2026-10-24T21:32:54.8366363+03:00')
render=load(OUT/'rendered-check.json');draft=load(OUT/'draft-check.json')
delivery={'completed_at':now.isoformat(),'started_at':start.isoformat(),'wall_elapsed_seconds':round((now-start).total_seconds(),1),'awake_execution_time':'unverified','token_stats':'unavailable','teaching_chapters':13,'changed_reader_files':15,'recorded_exact_edits':draft['recorded_edits'],'added_lists':sum(r['after']['lists']-r['before']['lists'] for r in render['list_and_definition_changes']),'new_first_definition_terms':24,'total_first_definition_terms':draft['definition_terms'],'matching_glossary_entries':97,'figures_preserved':22,'tables_preserved':4,'optional_notes_preserved':10,'screen_body_font_px':11.9,'preview':'http://127.0.0.1:8765/guide/site/chapters/ch-synthesis.html','book_model_hash':book.content_hash(),'html':manifest['artifacts']['html'],'standard_release_audit':'pass','browser_scope':load(OUT/'browser-check.json')['scope'],'limits':accept['limits']}
for p in [OUT/'DELIVERY.json',ROOT/'verification/DELIVERY.json']:p.write_text(json.dumps(delivery,indent=2),encoding='utf-8')
print(json.dumps(delivery,indent=2))
