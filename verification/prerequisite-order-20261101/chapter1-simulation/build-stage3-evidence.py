from pathlib import Path
import json,hashlib,datetime
root=Path(r'C:\dev\clsc\burak-papers\guide')
folder=root/'verification/prerequisite-order-20261101/chapter1-simulation'
packet=json.loads((folder/'concept-index-final.json').read_text(encoding='utf-8-sig'))
passages={p['id']:p for p in packet['passages']}
relations=[]
def rel(cid,pid,role,start='',stop='',why=''):
    p=passages[pid];a=p['text'].index(start) if start else 0;b=p['text'].index(stop,a) if stop else len(p['text'])
    assert 0<=a<b<=len(p['text']), (pid,start,stop)
    r=dict(concept_id=cid,passage_id=pid,role=role,span=[a,b],status='reviewed',review='chapter1-simulation/stage3',evidence=why)
    r.update({'adequacy':'adequate'} if role=='teach' else {'need':'required'})
    relations.append(r)
rel('ring-preferred-angle','ch:FOUNDATIONS/p272','teach','In the ring example',' [An ','Expected-rate maximum defines assigned preferred-angle labels before ordering or angle readout depends on them.')
rel('ring-preferred-angle','ch:FOUNDATIONS/p272','use','The ring describes',' The published','Ordering meaning follows the inline label definition.')
rel('ring-preferred-angle','ch:FOUNDATIONS/p288','use','At each step',' The authors','Angle readout uses defined neuron labels and expected-rate peak.')
rel('firing-rate-bump','ch:FOUNDATIONS/p272','teach','[An ',' The ring','Defines localized peak across neuron rates and its position as represented angle, distinct from activation and single spikes.')
rel('firing-rate-bump','ch:FOUNDATIONS/p272','use','The chosen connection','', 'Persistence and random peak displacement refer to the rate pattern already defined in this paragraph.')
rel('simulated-activation-state','ch:FOUNDATIONS/p270','teach','The computer stores',' The connections','One activation per neuron is the computer state; inputs/rates calculated from those activations.')
rel('simulated-activation-state','ch:FOUNDATIONS/p278','use','','','Computing all rates from current activations uses defined state and previously taught weighted-input/transfer equations.')
rel('recurrent-spike-coupling','ch:FOUNDATIONS/p100','teach','A spike from cell',' Thus the weights','Unit activation increase, weighted receiving input, transfer response and later spikes teach complete physical coupling.')
rel('recurrent-spike-coupling','ch:FOUNDATIONS/p274','use','A spike in cell','','Simulation explanation applies previously taught one-event pathway and feedback.')
rel('conditional-spike-draw','ch:FOUNDATIONS/p253','teach','The useful independence statement',' The changing state','Independence is conditional on present modeled state and local elementary noise; whole trains may be dependent.')
rel('conditional-spike-draw','ch:FOUNDATIONS/p279','use','Draw a spike indicator','','Independent draws depend on current rates, consistent with prior conditional rule.')
rel('ring-spike-indicator','ch:FOUNDATIONS/p279','teach','Draw a spike indicator',' independently','X is defined by0/1 values and r*h probability before displayed update uses it.')
rel('ring-spike-indicator','ch:FOUNDATIONS/p286','use','The one-spike draw',' The authors','Small r*h and population caveat apply the previously stated one-event draw; equation283 separately checked.')
rel('euler-activation-step','ch:FOUNDATIONS/p286','teach','This [**Euler update**]',' The one-spike','Names current-derivative-times-duration approximation after the explicit decay/addition operation and directly checked update.')
rel('euler-activation-step','ch:SIMULATING-MEMORY/p24','use','For decay alone','','Later simulation chapter applies earlier step; its local reminder still makes remote reading usable.')
sections={s['id']:'reviewed' for s in packet['sections'] if s['chapter_id']=='ch:FOUNDATIONS'}
assert set(sections)=={f'ch:FOUNDATIONS/s{i}' for i in range(7)}
concepts=[{'id':c,'aliases':[]} for c in dict.fromkeys(r['concept_id'] for r in relations)]
judgments=dict(concepts=concepts,sections=sections,relations=relations,teaching_sets=[])
(folder/'concept-judgments.json').write_text(json.dumps(judgments,indent=2)+'\n',encoding='utf-8')
files=['content/chapters/01-foundations.md','content/chapters/01-foundations.yaml','plan/chapter-plan.yaml','content/chapters/01b-persistence.md','content/chapters/11-simulating-memory.md']
hashes={p:hashlib.sha256((root/p).read_bytes()).hexdigest() for p in files}
for p in files[:2]:
    assert packet['source_sha256'][p]==hashes[p],f'Stale packet {p}'
assert packet['plan_sha256']==hashes['plan/chapter-plan.yaml'],'Stale plan'
now=datetime.datetime.now(datetime.timezone.utc)
report={
'stage':'3 connected reading and prerequisite order',
'status':'pass for Chapter1 addition and connected handoffs',
'completed_utc':now.strftime('%Y-%m-%dT%H:%M:%SZ'),
'review_start_utc':'2026-11-01T19:34:41Z',
'extension_start_utc':'2026-11-01T19:23:52Z',
'original_start_utc':'2026-11-01T13:32:42Z',
'extension_wall_seconds':int((now-datetime.datetime(2026,11,1,19,23,52,tzinfo=datetime.timezone.utc)).total_seconds()),
'original_wall_seconds':int((now-datetime.datetime(2026,11,1,13,32,42,tzinfo=datetime.timezone.utc)).total_seconds()),
'awake_execution_time':'unverified',
'file_hashes':hashes,
'scope':'Chapter1 full connected path, changed sidecar/PartI map, Chapter2 opening and Chapter18 backward teaching link. Unrelated unchanged sections adopted only after exact section-byte comparison; no broad scientific/figure/simulation acceptance.',
'unchanged_section_adoption':json.loads((folder/'unchanged-section-hashes.json').read_text()),
'ordering_verdict':'Retain the single new section after spike-count conditions and before covariance. The reader first learns neural signals and dynamics, population representation, and conditional randomness; the simulation then combines them into operations and an evidence comparison. Covariance/MSD afterward equips the reader to interpret shared changes and bias in eye recordings. Retain existing Part/chapter order; neither moving the simulation into Chapter2 nor importing Chapter18 numerical detail would improve this prerequisite path.',
'reader_can_describe':[
{'question':'What system is simulated?','sites':'48-104 earlier neural model,270 current computer state,272 rate-pattern coordinate','answer':'One decaying activation per modeled neuron, fixed weights/bias/transfer/time constant; current activations determine inputs/rates; a rate-pattern peak represents an angle.'},
{'question':'How do neurons depend on each other?','sites':'80-104 earlier weight direction and one-event feedback,254 conditional independence,272 inhibitory ring,274 simulation consequence','answer':'One spike changes its outgoing activation; weights change receiving inputs; transfer function changes later spike probabilities. Elementary draws are independent only conditional on current state.'},
{'question':'What does the computer update?','sites':'276 duration h;278 current inputs/rates;279 definition of X;280 decay/addition;283 display;286 Euler and small-probability caveat','answer':'Calculate rates, generate0/1 spikes from current rates, apply approximate decay and unit spike additions, then use updated activations for next step. All local symbols have prior meanings.'},
{'question':'What data comparison is established?','sites':'268 test question,288 measurement versus theoretical prediction,290 second model,292 biological evidence limit','answer':'Squared changes of the simulated represented coordinate agree with theoretical model predictions without fitting a diffusion parameter. Figure2 does not report fitting an animal memory-error dataset.'}
],
'paragraph_purposes':[
{'lines':[9,9],'purpose':'Maps simulation to the components just promised; now includes both implementation and meaning of agreement.'},
{'lines':[48,54],'purpose':'Defines activation, time derivative, decay time, spike index/time and delta pulse before Eq7, then interprets addition and removal.'},
{'lines':[80,104],'purpose':'Defines input/weight direction/bias before Eq8 and transfer/rate units before Eq9; one-spike trace supplies causal action.'},
{'lines':[108,131],'purpose':'Tuning and population vector explain how patterns refer to angle/location, so later ring peak is a representation rather than a physical cell movement.'},
{'lines':[135,264],'purpose':'Poisson counts teach rate versus observed event variation. Main conditional-independence qualification at254 precedes dependent simulation draws; folds contain proof/examples, not the only needed conditions.'},
{'lines':[268,270],'purpose':'States test question and computer state; prevents confusing constant bias with an angle-anchoring signal or model spikes with muscle/voltage simulation.'},
{'lines':[272,274],'purpose':'Defines preferred-angle label and rate bump, describes inhibitory interaction, then follows one spike through the network. No prior attractor-manifold proof is required to understand these model operations.'},
{'lines':[276,286],'purpose':'Combines existing model with event generation. h and X introduced before display; Euler label follows an already stated operation and before any reasoning requiring its name. Small-r*h condition and population caution are visible.'},
{'lines':[288,292],'purpose':'Describes observed collective coordinate, statistic and independent theoretical calculation. Short/long-lag behavior is qualified and biological scope explicit. Diffusion parameter here is an orienting label for spreading, not an unexplained calculation using D.'},
{'lines':[294,308],'purpose':'Transitions from modeled spreading to recorded shared movement and introduces covariance before formal use.'},
{'lines':[347,385],'purpose':'Defines displacement/MSD, distinguishes random movement from bias and measurement noise, then motivates Chapter2 persistence mechanism.'}
],
'handoffs':[
{'to':'Chapter2 opening and eye mechanics','evidence':'01b-persistence.md1-11 rechecked. It recalls firing-rate code and eye holding, then asks which activity disturbances restore and which change represented value. New simulation offers an example to explain, without replacing Chapter2 geometry or relying on it prematurely.'},
{'to':'PartI Chapter1 map','evidence':'Current map identifies supporting simulation test by recurrent networks and keeps background/model status. It previews result without asking reader to calculate diffusion or interpret bound before Chapters2-6.'},
{'to':'Chapter18 backward teaching link','evidence':'11-simulating-memory.md5-24 rechecked. Link to Ch1 sec-memory-spikes still reaches symbol/model teaching; Ch1 now also supplies simple event update before Chapter18 adds full settings, resolution cautions and model comparisons.'}
],
'direct_equation_review':[
'01-foundations.md51 Eq7: s,derivative,tau,alpha,t_i^alpha,delta defined in48 before use.',
'01-foundations.md83 Eq8: W_ij,b_i,g_i defined in80; s_j already taught; standard sum/index notation assumed from undergraduate maths.',
'01-foundations.md89 Eq9: phi,r_i and spikes/second units defined in86.',
'01-foundations.md283 update: s_i and tau earlier; h introduced276; X_i introduced279. h/tau dimensionless and X unit activation event; no new operator lesson needed.'
],
'concept_packet':'concept-index-final.json',
'concept_judgments':'concept-judgments.json',
'catalog_counts':{'concepts':len(concepts),'relations':len(relations),'sections':len(sections)},
'packet_limit':'Extractor omits display math; exact prose spans organize dependencies while equations were read directly. No bare equation lead-in is declared to teach a missing formula.',
'remaining_findings':[],'required_repairs':[],'source_edits_made':False,'token_stats':'unavailable'
}
(folder/'stage3.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:report[k] for k in ['completed_utc','extension_wall_seconds','original_wall_seconds','catalog_counts','status']},indent=2))
