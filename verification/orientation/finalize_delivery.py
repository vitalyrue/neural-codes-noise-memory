"""Record the scientific-opening revision without renewing other chapter reviews."""
from pathlib import Path
from datetime import datetime
import hashlib,json,shutil,yaml
from book_runtime.release_audit import audit_release,write_structure_lock

ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'verification/orientation'
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def read(p):return json.loads((ROOT/p).read_text(encoding='utf-8'))

checks=['verification/publication/html-links.json','verification/publication/orientation-browser.json']
for p in checks:
    assert read(p)['status']=='pass',p
stage3=read('verification/orientation/stage3.json')
assert stage3['status']=='pass','Reader-understanding review must pass before recording delivery'
for row in stage3['source_hashes']+stage3['rule_hashes']:
    assert digest(Path(row['path'])).lower()==row['sha256'].lower(),row['path']

# The earlier illustration review binds to its own unchanged chapter inputs.
bindings=read('verification/illustrations/current-bindings.json')
preserved={}
for fig,row in bindings['figures'].items():
    for name,sha in row['input_sha256'].items():
        if name.startswith('content/chapters/'):
            actual=digest(ROOT/name)
            assert actual==sha,(fig,name)
            preserved[name]=actual

write_structure_lock(ROOT/'guide-project.yaml','plan/structural-locks/current.yaml')
before=yaml.safe_load((OUT/'baseline/current.yaml').read_text(encoding='utf-8'))
after=yaml.safe_load((ROOT/'plan/structural-locks/current.yaml').read_text(encoding='utf-8'))
for key in ['parts','appendices']:
    assert before[key]==after[key],key
old_ids=[s['id'] for s in before['front_matter'][0]['sections']]
new_ids=[s['id'] for s in after['front_matter'][0]['sections']]
assert all(i in new_ids for i in old_ids)
(OUT/'preservation.json').write_text(json.dumps({
    'at':datetime.now().astimezone().isoformat(),
    'unchanged_illustration_chapter_inputs':preserved,
    'all_main_chapter_and_appendix_structure_unchanged':True,
    'old_frontmatter_section_ids_retained':old_ids,
    'added_frontmatter_section_ids':[i for i in new_ids if i not in old_ids],
    'note':'Reading paths, paper-copy text and reproduction/literature boundary are checked against the saved baseline by update_metadata.py. Figures and typed tables were not edited.',
},indent=2),encoding='utf-8')

mp=ROOT/'verification/manifests/build-manifest.json'
raw=ROOT/'verification/manifests/orientation-20261023-quarto-manifest.json'
assert not raw.exists(),'Preserve the original build record'
shutil.copy2(mp,raw)
manifest=read(raw.relative_to(ROOT))
audit=audit_release(ROOT/'guide-project.yaml')
assert manifest['book_model_hash']==audit['book_model_hash']
manifest['artifacts']={'html':{k:audit['artifacts']['html'][k] for k in ['path','kind','bytes','file_count','sha256']}}
manifest['finalized_at']=datetime.now().astimezone().isoformat()
manifest['quarto_build_manifest']={'path':raw.relative_to(ROOT).as_posix(),'sha256':digest(raw)}
manifest['postprocess_evidence']=['verification/publication/paper-assets.json']
manifest['checks']=checks
manifest['review_scope']='Scientific opening and retained reading guide only. Other chapter and illustration acceptances remain historical.'
mp.write_text(json.dumps(manifest,indent=2),encoding='utf-8')
audit=audit_release(ROOT/'guide-project.yaml')
(OUT/'release-audit.json').write_text(json.dumps(audit,indent=2),encoding='utf-8')
now=datetime.now().astimezone()
start=datetime.fromisoformat('2026-10-23T22:54:03.8209459+03:00')
summary={
    'completed_at':now.isoformat(),'task_started_at':start.isoformat(),
    'wall_elapsed_seconds':round((now-start).total_seconds()),
    'changed_reader_files':['content/chapters/00-reading-guide.md','content/chapters/00-reading-guide.yaml','source-maps/terminology-ledger.yaml'],
    'change':'Added field and shared problem, then motivation, methods, results, implications and limits for each paper before the reading paths and source copies. Clarified scope and notation.',
    'book_model_hash':manifest['book_model_hash'],'html':manifest['artifacts']['html'],
    'review_scope':manifest['review_scope'],
    'independent_reviews':['verification/orientation/stage1.json','verification/orientation/stage1-recheck.json','verification/orientation/stage2.json','verification/orientation/stage2-recheck.json','verification/orientation/stage2-recheck-followup.json','verification/orientation/stage3.json'],
    'checks':checks+['verification/orientation/preservation.json','verification/orientation/release-audit.json'],
    'browser_scope':'Desktop, original comment viewport and narrow width; two representative screenshots and one real table-of-contents click. No whole-book visual sweep.',
    'limits':'No new whole-book acceptance or authoritative/public release. Existing development locks and historical review limits remain.',
    'awake_execution_time':'unverified','token_stats':'unavailable',
}
(ROOT/'verification/DELIVERY.json').write_text(json.dumps(summary,indent=2),encoding='utf-8')
(OUT/'DELIVERY.json').write_text(json.dumps(summary,indent=2),encoding='utf-8')
print(json.dumps({'book_model_hash':summary['book_model_hash'],'html':summary['html'],'release_audit_status':audit.get('status'),'release_findings':len(audit.get('findings',[]))},indent=2))
