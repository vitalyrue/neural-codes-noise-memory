import json, hashlib, sys
from pathlib import Path
p=Path(__file__).parent
g=p.parent.parent
L=lambda n: json.loads((p/n).read_text(encoding='utf-8'))
H=lambda f: hashlib.sha256(Path(f).read_bytes()).hexdigest()
cur=L('current-eye-input.json'); old=L('final-eye-input.json'); prep=L('review-reuse-preparation.json')
s1=L('final-eye-stage1.json'); s2=L('final-eye-stage2.json'); freeze=L('current-source-freeze.json')
errors=[]; checks={}; wrappers=[]
sys.path.insert(0,str(p))
import prepare_review_reuse as prep_module
for c in prep['calls']:
    if c['run_id'] not in ['final-eye-truth-20261029-01','final-eye-language-20261029-02']: continue
    wp=Path(c['original_call_path']); w=json.loads(wp.read_text(encoding='utf-8')); r=w['runs'][0]
    good=H(wp)==c['original_call_sha256'] and H(w['source_artifact'])==w['source_artifact_sha256']
    original=s1 if 'truth' in c['run_id'] else s2
    good=good and r['run_id']==original.get('run_id',original.get('local_request_id')) and r['started_at']==original['started_at'] and r['completed_at']==original.get('completed_at',original.get('ended_at'))
    good=good and w['input_hash']==old['input_hash'] and w['review_contract_hash']==cur['review_contract_hash']
    good=good and r==prep_module.actual_run(original)
    if not good: errors.append(str(wp))
    wrappers.append({'path':str(wp),'sha256':H(wp),'report':w['source_artifact'],'report_sha256':H(w['source_artifact']),'verified':good})
raw_checks={uid:u==old['units'][uid] for uid,u in cur['units'].items()}
for uid,u in cur['units'].items(): checks[uid]=(prep_module.gate._review_input_signature(g,u)==prep_module.gate._review_input_signature(p/'final-snapshot',old['units'][uid]))
if sum(checks.values())!=24: errors.append('unit equality count')
source_checks=[]
for rel,h in freeze['source_hashes'].items():
    f=g/rel; snap=p/'current-snapshot'/rel
    ok=H(f)==h and H(snap)==h
    source_checks.append({'path':rel,'sha256':h,'current_and_snapshot_match':ok})
    if not ok and rel!='plan/structural-locks/current.yaml': errors.append(rel)
original_checks=[]
for row in s2['source_snapshot_verification']:
    f=Path(row['path']); rel=f.relative_to(g); h=row['hash']
    ok=H(p/'final-snapshot'/rel)==h
    original_checks.append({'path':str(rel),'sha256':h,'snapshot_matches_review':ok})
    if not ok: errors.append(str(rel))
rules=[]
for fp,h in s1['source_file_sha256'].items():
    if '/.codex/skills/' not in fp.replace('\\','/'): continue
    ok=H(fp)==h; rules.append({'path':fp,'sha256':h,'unchanged':ok})
    if not ok: errors.append(fp)
assets=[]
for row in L('reuse-snapshot-assets.json')['assets']:
    rel=row['path']; h=row['sha256']
    ok=all(H(root/rel)==h for root in [g,p/'final-snapshot'])
    assets.append({'path':rel,'sha256':h,'unchanged':ok})
    if not ok: errors.append(rel)
vale=H(g/'.vale.ini')==H(p/'final-snapshot/.vale.ini')==H(p/'current-snapshot/.vale.ini')
if not vale: errors.append('vale config')
before=(p/'final-snapshot/content/chapters/04b-eye-timing.md').read_text(encoding='utf-8')
now=(g/'content/chapters/04b-eye-timing.md').read_text(encoding='utf-8')
deleted='The common variance calculation uses one interval length. To learn what kind of process drives motion, the authors next compare displacements at many time separations. '
repair=(before.replace(deleted,'',1)==now and before.count(deleted)==1)
if not repair: errors.append('exact body deletion')
narrow=[]
for n in ['current-eye-noise-stage1.json','current-eye-noise-stage2.json']:
    r=L(n); ok=r['input_hash']==cur['input_hash'] and r['review_contract_hash']==cur['review_contract_hash']
    narrow.append({'path':n,'sha256':H(p/n),'current_hashes_match':ok})
    if not ok: errors.append(n)
flow=L('final-eye-stage3.json')
override=next(a for a in flow['assessments'] if a['unit_id'].endswith('::sec:READING-START'))['fields']['Expert objection']
lock=L('structure-lock-refresh.json')
if H(g/'plan/structural-locks/current.yaml')!=lock['current_sha256']: errors.append('refreshed lock binding')
e={'unit_signature_equality':checks,'raw_packet_equality':raw_checks,'raw_container_difference':'Timing opening and filtered-MSD have unchanged source/metadata/assets, but review_asset_definitions stores the whole chapter Markdown, including the repaired other unit. Pinned signature extracts actual image definitions rather than hashing that whole container.','wrappers':wrappers,'current_sources':source_checks,'original_source_bindings':original_checks,'teaching_rules':rules,'assets':assets,'vale_configuration_unchanged':vale,'exact_two_sentence_deletion':repair,'narrow_calls':narrow,'structural_lock_refresh':lock,'expert_override_path':'assessments[unit_id=content/chapters/00-reading-guide.md::sec:READING-START].fields.Expert objection','expert_override_disposition':override['disposition'],'errors':errors}
(p/'final-eye-recheck-evidence.json').write_text(json.dumps(e,indent=2),encoding='utf-8')
print(json.dumps({'errors':errors,'unchanged_units':sum(checks.values()),'sources':len(source_checks),'old_source_bindings':len(original_checks),'rules':len(rules),'assets':len(assets),'repair':repair,'override':override['disposition']}))

