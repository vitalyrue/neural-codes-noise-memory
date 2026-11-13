"""Serialize the separate current source and connection recheck."""
import json, pathlib, hashlib, sys, datetime, os
P=pathlib.Path(__file__).resolve().parent
ROOT=P.parent.parent
sys.path.insert(0, r'C:/dev/NBIS/publisher-releases/0.8.23/skills/course-quality-gate/scripts')
import orchestrate_pedagogy_reviews as gate
def load(n): return json.loads((P/n).read_text(encoding='utf8'))
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
prep=load('review-reuse-preparation.json'); current=load('current-place-input.json'); flow=load('final-place-stage3.json')
old=load('final-place-input.json'); snap=P/'final-snapshot'; csnap=P/'current-snapshot'
contract=gate._review_contract_hash()
assert contract==current['review_contract_hash']==flow['review_contract_hash']
def records(root):
    files=gate.discover_source_files(root)
    scopes=gate._expected_review_scopes(root,files)
    return gate._input_hash(root,files), {u:r for scope in scopes.values() for u,r in scope['unit_records'].items()}
oh,orec=records(snap);nh,nrec=records(ROOT)
assert oh==old['input_hash']==prep['before_input_hash']
assert nh==current['input_hash']==prep['current_input_hash']
binding=[];runs=[]
for c in prep['calls']:
    if not c['run_id'].startswith('final-place-'):continue
    cp=pathlib.Path(c['original_call_path']);assert sha(cp)==c['original_call_sha256']
    w=json.loads(cp.read_text(encoding='utf8'));a=pathlib.Path(w['source_artifact']);assert sha(a)==w['source_artifact_sha256']
    r=json.loads(a.read_text(encoding='utf8'));run=w['runs'][0]
    for key in ['run_id','reviewer_id','stage','context','started_at','completed_at','input_hash','review_contract_hash']:
        assert run[key]==r[key]
    assert run['input_hash']==oh and run['review_contract_hash']==contract
    assert {x['unit_id'] for x in run['assessments']}==set(current['units'])
    for ra,wa in zip(r['assessments'],run['assessments']):
        assert ra['unit_id']==wa['unit_id'] and ra['status']==wa['status'] and ra['unresolved']==wa['unresolved']
        assert [(q['question'],q['answer']) for q in ra['questions']]==[(q['question'],q['answer']) for q in wa['questions']]
        assert not wa['unresolved']
    assert set(current['units'])<=set(c['eligible_assessments'])
    binding.append({'run_id':run['run_id'],'call_path':str(cp),'call_sha256':sha(cp),'original_report':str(a),'original_report_sha256':sha(a),'started_at':run['started_at'],'completed_at':run['completed_at'],'snapshot_input_hash':oh,'review_contract_hash':contract})
    runs.append(run['run_id'])
assert len(runs)==2
unit_signatures={}
for uid in current['units']:
    a=gate._review_input_signature(snap,orec[uid]);b=gate._review_input_signature(ROOT,nrec[uid]);assert a==b
    assert old['units'][uid]==current['units'][uid]
    unit_signatures[uid]=a
source_hashes=load('accept-place-stage1-source-hashes.json')['files']
for path,digest in source_hashes.items():
    assert sha(ROOT/path)==sha(snap/path)==sha(csnap/path)==digest
assets=load('reuse-snapshot-assets.json');asset_verified=[]
for a in assets['assets']:
    path=a['path'];assert sha(ROOT/path)==sha(snap/path)==a['sha256'];asset_verified.append(path)
CONNECTIONS={
'ch:GLOSSARY':'The current glossary still describes lookup after the main teaching. Its Gaussian-process, covariance, diffusion, critical-point and size-law entries preserve the distinctions used in the place path; it is not used to supply a missing earlier explanation.',
'ch:REFERENCES':'The bibliography still distinguishes the main Mainali paper with supplement from the separate author notes. The current chapter source notes lead to those identities, so the scientific and language answers retain their intended source scope.',
'ch:PLACE-FIELDS':'The opening moves from tunnel, floor and room observations to thresholded input and upcrossing counts, then explicitly fixes the map in space. That final distinction remains the prerequisite for the covariance section and for the later time-dependent synthesis.',
'sec:PLACE-GP':'The preceding fixed-map problem still motivates spatial dependence. Map roles, stationarity, isotropy, smoothness, normalization, connected fields and the local slope scale still lead to the crossing argument; the formal fold does not replace their visible physical meanings.',
'sec:PLACE-KAC-RICE':'The map assumptions still support the local band-width count, slope weighting and Gaussian independence step. The endpoint correction remains explicit before field and gap means are inferred, so the old exact-count and wording judgments keep the same conditions.',
'sec:PLACE-INFERENCE':'The exact crossing intensity still combines with occupied and inactive fractions to separate threshold and scale. The numerical round trip, rare-event qualification and silent-cell correction retain distinct jobs before the next chapter asks for full size distributions.',
'ch:PLACE-SIZES':'The opening still states the missing task after exact means: a whole distribution. It restores the symbols and dimension before the high-peak argument, so the reader is not asked to infer the limiting law from the earlier exact mean alone.',
'sec:PLACE-RARE-PEAKS':'The smooth high-threshold assumptions still precede the conditional Hessian, parabola, radius and exponential excess law. Full width is distinguished from radius before geometry converts that radius into length, area or volume.',
'sec:PLACE-SIZE-LAW':'The preceding radius law still feeds the dimensional volume conversion and density. Mean, units, distribution-family interpretation and finite-threshold error remain visible; the printed-source check preserves the limits of what its corrections establish before slices test more than volume.',
'sec:PLACE-SLICES':'The size-law result still motivates an independent question about internal arrangement. Gaussian restriction, measured slice components and hit bias precede the sphere counterexample; boundary slope selection then follows as a different sampling question.',
'sec:PLACE-SLOPES':'The earlier crossing weighting still supplies the boundary-sampled derivative law. The exact threshold cancellation and rate gain remain separate from the optional high-threshold width check, and the next chapter can ask about holes without confusing these scopes.',
'ch:PLACE-TESTS':'The opening still explains why sizes and counts leave holes unresolved, then distinguishes testing spatial statistics from identifying a circuit. The restored notation separates spatial dimension from the earlier diffusion coefficient before the topology calculation.',
'sec:PLACE-TOPOLOGY':'The dimension-specific connected-component and hole examples still teach the signs before the signed critical-point formula. Box boundaries, negative Euler characteristic and the high-threshold component approximation remain explicit before comparison with measured rate maps.',
'sec:PLACE-DATA':'The current topology result still leads into what the recordings measure and what parameters were fitted. Added statistics, processing choices, sampling limits and shared cell thresholds retain their roles before the following circuit construction; a fitted statistic is not silently converted into a new test.',
'sec:PLACE-WIRING':'The preceding evidence still leaves a mechanism question. Fixed input profiles and random weights, finite-vector Gaussian conditions, overlap covariance and the width example support a sufficient construction; its nonunique biological interpretation still leads into the synthesis.',
'ch:SYNTHESIS':'The place sequence still ends with a statistical map and an unresolved maintenance question. The synthesis opening preserves that difference and sets up the map, motion and downstream-observation comparison before proposing any joint calculation.',
'sec:SYNTHESIS-QUESTIONS':'The current list and comparison still distinguish represented coordinate, internal command, eye angle and physical position. The closing requirement to specify movement of the represented position still directly sets up the next hypothetical fixed-map plus moving-state model.',
'sec:SYNTHESIS-JOINT-CALCULATION':'The previous missing movement law is still supplied as a local shared displacement of fixed expected-rate functions. The variance and slope-product covariance, approximation range and omitted noise sources remain visible before the optional numerical example.',
'sec:SYNTHESIS-COVARIANCE-EXAMPLE':'The visible general covariance formula still precedes the folded two-cell calculation. The conclusion after the fold keeps the one-direction rate-change result and the need to measure alignment with tuning curves, providing the premise for the evidence comparison.',
'sec:SYNTHESIS-EVIDENCE':'The preceding proposed alignment test still leads into the exact scope of the place fit, eye-noise evidence and memory bound. The eye deletion removed repeated wording in another unit; the current synthesis retains the required calibration, stationarity and model-interpretation limits.',
'sec:SYNTHESIS-RELATED':'The preceding evidence limits still motivate each related study by the assumption or open question it addresses. Path integration and dendrites are defined before their local explanatory use, and benefit for vision remains separate from identifying the generator of eye movement.',
'sec:SYNTHESIS-NEXT':'The related-work limits still motivate measuring maps and fluctuations in the same population. The sequence retains tuning uncertainty, weak correction, alignment, a valid local diffusion range and conditional downstream filters; it ends with a proposed test, not a claim that the joint experiment has occurred.'}
assessments=[]
for a in flow['assessments']:
    uid=a['unit_id'];short=uid.split('::')[-1];assert short in CONNECTIONS
    refs=list(dict.fromkeys([uid]+a['questions'][0]['source_refs']+a['questions'][1]['source_refs']))
    questions=[
      {'kind':'reuse_sources','question':'Do the saved calls and their source snapshot match the actual earlier review, and is the complete current unit unchanged?','answer':f'Yes. Both saved call wrappers match their recorded SHA256 hashes and the original reports, including actual run identity, times, questions and answers. The original packet and current packet have identical complete records for {short}; independently recomputed review-input signatures match across the original snapshot and current source, including companion metadata and referenced assets. All 12 assigned source files also match the original reviewer hashes and both snapshots. Asset copies are byte bindings, not pixel approval.'},
      {'kind':'reuse_rules','question':'Do the original and current rules match, and does the current scope still permit the old judgment?','answer':f'Yes. The current pinned review-contract hash was recomputed from the actual tool and contract files and equals both saved calls: {contract}. The {short} review still covers the same scientific and reader-text scope. No required open finding is converted to a pass. The four conditional synthesis metadata notes remain conditional because the current renderer does not present section summaries as standalone reader text.'},
      {'kind':'reuse_connections','question':'Do the current preceding and following explanations and prerequisites still support the adopted answers?','answer':CONNECTIONS[short]}
    ]
    for q in questions:q.update({'source_refs':refs,'original_run_ids':runs[:]})
    assessments.append({'unit_id':uid,'status':'pass','unresolved':[],'questions':questions})
end=os.environ['PLACE_RECHECK_END'];start='2026-10-29T14:08:04.6026280+02:00'
elapsed=(datetime.datetime.fromisoformat(end)-datetime.datetime.fromisoformat(start)).total_seconds()
prep_elapsed=(datetime.datetime.fromisoformat(end)-datetime.datetime.fromisoformat('2026-10-29T13:05:39.8301214+02:00')).total_seconds()
report={'run_id':'final-place-recheck-20261029-04','run_id_type':'local request ID','reviewer_id':'/root/accept_place','assigned_model':'GPT-6 Astra','assigned_reasoning':'high','stage':'recheck','context':'reviewer_continuation','started_at':start,'completed_at':end,'input_hash':nh,'review_contract_hash':contract,'status':'pass for source/rule reuse and current text connections within the assigned scope','assessments':assessments,'findings':[],'unresolved':[],'bindings':binding,'unit_signatures':unit_signatures,'verification':{'current_source_input_hash':nh,'original_snapshot_input_hash':oh,'original_reports_and_wrappers':'Exact saved hashes, identities, times, questions and answers verified','assigned_source_files':12,'asset_bytes_verified':len(asset_verified),'asset_copy_record':'reuse-snapshot-assets.json','asset_copy_time':assets['prepared_at'],'actual_rule_hash_recomputed':True,'current_connection_basis':'Separate bounded current opening/ending checks plus the completed current connected Stage3 reading; the unit-specific answers above are current adoption judgments.'},'preserved_limits':['Four conditional internal section-summary notes remain in Stage2; no current reader defect established by them.','Guide figure pixels remain deferred.','No new claim to have reviewed all unassigned chapters.','No manuscript, tool, rule or earlier report changed.'],'timing':{'stage_wall_seconds':elapsed,'preparation_wall_seconds':prep_elapsed,'measured_checkpoints':[start,'2026-10-29T14:08:42.0371888+02:00',end],'awake_execution':'unverified','token_stats':'unavailable'}}
assert len(assessments)==22 and sum(len(a['questions']) for a in assessments)==66
(P/'final-place-recheck.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
md=f'''# Place group separate reuse recheck

Actual request `final-place-recheck-20261029-04`, reviewer `/root/accept_place`, context `reviewer_continuation`.

Started {start}. Completed {end}. Wall time {elapsed:.2f} seconds; since preparation {prep_elapsed:.2f} seconds. Awake execution unverified. Token stats unavailable.

All 22 units pass the bounded source, rule and current connection check. The 66 answers preserve the three reuse kinds and exact original run IDs `final-place-truth-20261029-01` and `final-place-language-20261029-02`. No new required defect found.

Original report and call-wrapper hashes, identities, times, questions and answers match. Complete current unit signatures match the original snapshot, including companion metadata and referenced assets. All 12 assigned source files also match the earlier review hashes and both snapshots. The 52 copied assets match the saved asset binding and current files; that copy is not pixel approval.

Current source hash: `{nh}`. Original snapshot hash: `{oh}`. Recomputed current contract hash: `{contract}`.

The current connection check preserves the progression from spatial map roles through exact crossings, limiting size laws, additional geometry and empirical tests, then the qualified circuit construction and proposed shared-position calculation. Glossary and references remain lookup aids. Four conditional internal-metadata notes remain preserved in Stage2. The only intervening eye deletion does not remove an assumption needed by this group's synthesis.

Figure pixels and release acceptance remain deferred. No manuscript or earlier review artifact changed.
'''
(P/'final-place-recheck.md').write_text(md,encoding='utf8')
print(json.dumps({'units':22,'questions':66,'wall_seconds':elapsed,'completed_at':end,'source_hash':nh,'contract_hash':contract}))
