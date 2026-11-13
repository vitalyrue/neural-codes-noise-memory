from pathlib import Path
import re,json,hashlib
from datetime import datetime
import yaml
TASK=Path(__file__).resolve().parents[1]
P=TASK/'proposed'/'content'/'chapters'
now=datetime.now().astimezone()
start=datetime.fromisoformat('2026-10-24T18:54:22.5524387+03:00')
stage_start=datetime.fromisoformat('2026-10-24T19:03:51.8226140+03:00')
def sha(b): return hashlib.sha256(b).hexdigest()
sources={}
for stem in ['03-memory-information','04-eye-drift']:
    for ext in ['md','yaml']:
        q=P/(stem+'.'+ext);sources[q.name]=dict(path=str(q),sha256=sha(q.read_bytes()))

text=(P/'04-eye-drift.md').read_text(encoding='utf-8')
quote='Substituting $B=-A$ gives $A(1/\\tau_- -1/\\tau_+)=1/m$, hence $A=\\tau_+\\tau_-/[m(\\tau_+-\\tau_-)]$. Making the response zero before the spike gives'
assert quote in text
line=text[:text.index(quote)].count('\n')+1
finding=dict(id='S1-IE-01',priority=3,kind='incomplete moved-proof connection',file='04-eye-drift.md',section='sec:EYE-INVERSE-FILTER',line=line,quote=quote,passage_sha256=sha(quote.encode('utf-8')),failed_check='Expanded proof must connect its last inference to the displayed result after a result-before-proof move.',reason='The fold ends immediately after the word gives. Its promised expression has moved above the fold, so an expanded derivation ends with a missing object even though the correct response formula remains visible earlier. The closed reading path is mathematically intact.',repair='Replace the final sentence with: Making the response zero before the spike gives the impulse response displayed above.',impact='Small local connection repair; no equation or mathematical claim needs changing.',prerequisites_checked=['Visible distinct positive decay times and the h0 expression in the same section.','Causality definition and Theta(u) before this fold.'])

fold_checks=[]
for stem in ['03-memory-information','04-eye-drift']:
    t=(P/(stem+'.md')).read_text(encoding='utf-8')
    for m in re.finditer(r'^::: \{[^\n]+title="([^"]+)"[^\n]*\}\n\n(.*?)\n\n:::',t,re.M|re.S):
        title,body=m.groups(); ln=t[:m.start()].count('\n')+1
        detail={
        'Check: equality can also hold with a linear transfer rule':'The visible proportional-vector condition and the statement that an exponential rule is sufficient rather than necessary preserve the conclusion. The fold supplies a counterexample using Chapter 2 mutual excitation; theta, rates and the 2DJ product match that earlier model.',
        'Check: the residual matrix proves the lower bound':'The matrix inequality, positive-semidefinite meaning, invertible-information condition and U/V identities are visible. The residual Q proof contains no later-needed first definition.',
        'Derivation: the weights of the two decaying responses':'The h0 formula, distinct positive roots, causality, units, neural lead and convolution are visible. Pulse matching supplies its constants inside the fold. Only the final promised-result connector needs S1-IE-01.',
        'Check: static gain and coincident decay times':'The visible example already checks kernel area equals 1/k and identifies it as a constructed example. The repeated-root limit and further normalization argument are optional; later covariance and circuit reasoning use calibrated degree units taught visibly.'}[title]
        fold_checks.append(dict(file=stem+'.md',line=ln,title=title,body_sha256=sha(body.encode('utf-8')),assessment=detail,first_definition_term_inside='definition-term' in body,block_reference_inside='{{block:' in body))
assert len(fold_checks)==4

checks=[
dict(area='Initial open assessment',assessment='Chapter 3 adds a local information measure, a diffusion constraint and a readout cost to the preceding projection model. Chapter 4 needs this only after its separate recording/calibration evidence has established what movement can reveal. Keeping theory before the application gives meaning to the later integrator calculation. An experiment-first order is plausible but would require moving the projection and diffusion prerequisites into the application. No chapter swap is warranted by the connected text.'),
dict(area='Audience and earlier teaching',assessment='The baseline is undergraduate calculus, probability and linear algebra. Earlier proposed foundations teaches spikes/rates, conditional Poisson noise, covariance, CV, a continuous attractor and Brownian displacement. Proposed Chapter 2 teaches tangent/left projection, 2D=sum(v_i^2 r_i), u=tau r-prime, and both two-cell examples. Chapter 3 teaches likelihood, score and information before using them; Chapter 4 teaches the physiological pathway and filtering before covariance and MSD tests.'),
dict(area='New title claims',assessment='All 23 chapter/section headings were read with their complete sections and sidecar titles. Chapter 3 titles keep the bound as a lower bound, comparisons conditional on fixed quantities, additive errors conditional on assumptions, and the readout limit distinct from abrupt stopping. Chapter 4 titles use points to, challenges, estimates, and can reproduce, matching inferential rather than unique-cause claims. Its measurement-error heading is qualified visibly to positive lags and errors independent of movement and uncorrelated across sampled times; the filtering heading is qualified visibly to stable decaying kernels and nonzero static gain.'),
dict(area='Information and equality reasoning',assessment='Cauchy-Schwarz uses the preceding projected diffusion and tangent normalization. Equality is a proportionality condition at the current state. The exponential rule is visibly sufficient, and the linear counterexample does not alter the inequality. The matrix claim requires invertibility and keeps coupled directions distinct from scalar coordinate checks.'),
dict(area='Readout scope',assessment='Storage time T and observation time L remain separate. Zero cross covariance follows from local unbiasedness and future-noise independence; translation invariance supplies one readout variance. Independent Gaussian observation and transition noises are visibly identified as an approximation. Naive averaging, backward precision, ideal asymptote, full/partial access and the printed inequality caution remain inside that declared model.'),
dict(area='Eye inference and mechanism',assessment='One-neuron-at-a-time recordings are distinguished from simultaneous neuronal covariance. R squared is a fitted linear explanatory fraction; the common fraction uses calibrated unit gain and approximately uncorrelated contributions. The chapter retains the order-1/N private cross term, two-animal/horizontal/350 ms scope and uncertainty limits. Filtered white input and Brownian position are compared under the same one-pole teaching filter before the fuller model. Upstream localization remains separate from proof that integrator neurons are the unique generator.'),
dict(area='Figure/caption connections',assessment='All nine guide figure and table sidecar entries were read against their source leads and interpretations. Chapter 3 captions separate readout from storage, preserve the positive-rate range and show that a lower bound can fall while actual diffusion stays fixed. Chapter 4 captions separate the physical pathway from analysis, common from predictor noise, positive-lag measurement offsets from zero lag, and independently normalized model shapes from fitted data. No figure or block is inside a fold. This is a content/caption check, not a pixel inspection.'),
dict(area='Original paper calculations',assessment='Unchanged full paper calculations and empirical estimates were not rerun. The stage checks the mathematical meaning and conditions of the proposed teaching path and its changes; it does not certify raw-data reproduction or resolve every existing source-paper claim.'),
]

headings=[]
for stem in ['03-memory-information','04-eye-drift']:
    t=(P/(stem+'.md')).read_text(encoding='utf-8'); d=yaml.safe_load((P/(stem+'.yaml')).read_text(encoding='utf-8'))
    alltitles={d['chapter_id']:d['title'],**{s['id']:s['title'] for s in d['section_list']}}
    for m in re.finditer(r'^#{1,6} (.+) \{#([^}]+)\}$',t,re.M):
        title,ident=m.groups();assert alltitles[ident]==title
        headings.append(dict(file=stem+'.md',line=t[:m.start()].count('\n')+1,id=ident,title=title,truth_verdict='supported by the complete section under its visibly taught assumptions'))

report=dict(stage=1,scope='Independent truth and reasoning only; no edits or whole-book acceptance',reviewer='GPT-6.1-sol/high, teach_place_synthesis',local_request_id='root-to-teach_place_synthesis-stage1-information-eye',platform_call_id='not exposed',timestamp=now.isoformat(),root_wall_elapsed_seconds=(now-start).total_seconds(),stage_elapsed_seconds=(now-stage_start).total_seconds(),awake_execution_time='unverified',fresh_context='No target author decision ledger, defense, handoff or prior verdict was read. The review began from the neutral task and actual source text. Earlier authored Chapters 5/6 were not used as authority for these judgments.',sources=sources,initial_and_scope_checks=checks,heading_checks=headings,fold_checks=fold_checks,findings=[finding],optional_preferences=[],verdict='No new mathematical or empirical overclaim found in the scoped changes. One required local connection repair remains; recheck that sentence after repair. Later wording and reader-flow stages remain separate and pending.',token_stats='unavailable')
(TASK/'stage1-information-eye.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
md=f'''# Independent Stage 1: Chapters 3 and 4 truth and reasoning

Recorded {now.isoformat()}. GPT-6.1-sol/high. Root wall elapsed {(now-start).total_seconds()/60:.2f} minutes; this stage {(now-stage_start).total_seconds()/60:.2f} minutes. Awake execution time unverified. Token stats unavailable.

No new mathematical or empirical overclaim was found in the scoped changes. One small moved-proof connection repair remains. No target author ledger, defense or prior verdict was read. No source edits were made, and this is not whole-book acceptance.

## Required repair

**S1-IE-01, priority 3.** `04-eye-drift.md`, line {line}, `sec:EYE-INVERSE-FILTER`. The impulse-response fold ends: “Making the response zero before the spike gives”. The expression it promises is now above the fold. The closed path still has the correct formula; the expanded proof ends without its promised object. Change that final sentence to “Making the response zero before the spike gives the impulse response displayed above.” No equation needs changing.

Passage SHA256: `{finding['passage_sha256']}`. Source SHA256: `{sources['04-eye-drift.md']['sha256']}`.

## Checked reasoning

'''
for c in checks: md+=f"- **{c['area']}:** {c['assessment']}\n\n"
md+='## Four fold boundaries\n\n'
for c in fold_checks:md+=f"- `{c['file']}:{c['line']}`, **{c['title']}**: {c['assessment']}\n\n"
md+='Optional preferences: none. Exact source hashes and all heading checks are in the accompanying JSON. Wording and reader-flow stages were not performed in this call.\n'
(TASK/'stage1-information-eye.md').write_text(md,encoding='utf-8')
print(json.dumps({'timestamp':now.isoformat(),'root_wall_minutes':(now-start).total_seconds()/60,'stage_minutes':(now-stage_start).total_seconds()/60,'headings':len(headings),'folds':len(fold_checks),'findings':1,'finding_line':line}))

