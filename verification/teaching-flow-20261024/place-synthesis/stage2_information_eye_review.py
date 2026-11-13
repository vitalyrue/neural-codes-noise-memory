from pathlib import Path
import re,json,hashlib,yaml
from datetime import datetime
TASK=Path(__file__).resolve().parents[1]; P=TASK/'proposed'/'content'/'chapters'
now=datetime.now().astimezone();root=datetime.fromisoformat('2026-10-24T18:54:22.5524387+03:00');start=datetime.fromisoformat('2026-10-24T19:07:32.6172750+03:00')
def sha(t): return hashlib.sha256(t.encode('utf-8')).hexdigest()
R={
'ch:MEMORY-INFORMATION':'Spike information connects distinguishable current states to memory diffusion and recall error; the opening explains spikes and moving rates before formal information. Keeping the heading gives the chapter its shared question.',
'sec:MEMORY-FI':'Rate slopes and spike variability are the numerator and denominator in the taught Poisson information expression. The opening gives the neighboring-value discrimination problem before likelihood, score and Fisher information definitions.',
'sec:MEMORY-BOUND':'Lower bound is the exact direction needed to distinguish permitted stability from achieved stability. Diffusion and the projection formula were taught in Chapters 1 and 2, and information immediately above.',
'sec:MEMORY-COMPARISONS':'What is held fixed is the question governing the N, rate, time-constant and width comparisons. Removing this emphasis would encourage incompatible parameter comparisons; no specialist shorthand is needed in the title.',
'sec:MEMORY-READOUT-SETUP':'Storage loss and readout error are explained through s and e in the next two paragraphs; specific assumptions correctly warn that their variances add only after the cross term vanishes. The visible equations make the quantity precise. Variances could sharpen the heading, but the existing connected prose is sufficient.',
'sec:MEMORY-NAIVE':'Equal weighting identifies the cause of the error increase rather than implying that every long readout is harmful. The opening explains the averaging and movement conflict before its calculation.',
'sec:MEMORY-IDEAL':'Accounting for diffusion is the needed contrast with equal weighting; toward a limit preserves continuing diminishing benefit. Precision is defined before the backward recursion uses it.',
'sec:MEMORY-PARTIAL':'The following text explains limited access as missing spikes, and slower as a longer useful observation interval. The unchanged heading is sufficient with that immediate explanation and the exact alpha scaling; no rewrite is required for this local revision.',
'sec:MEMORY-EXTENSIONS':'Time scales and noise laws identify the two assumptions whose changes matter. The section separately derives the sum of time constants and changes to the equality condition, so no extra technical label belongs in the heading.',
'sec:MEMORY-FIG3-AND-CAUTION':'Saturates summarizes the limiting improvement just derived. Printed error bound needs qualification points to the actual algebraic caution while keeping its apparent, not author-confirmed, status in the text.',
'ch:EYE-DRIFT':'Points to conveys inference rather than unique circuit identification. The opening defines fixational drift and immediately separates shared upstream evidence from the proposed storage mechanism.',
'sec:EYE-PATHWAY':'Stored eye position to muscle action is the section purpose. Oculomotor integrator, motoneurons and plant are each explained before later filtering and covariance reasoning relies on them.',
'sec:EYE-RECORDINGS':'One motor neuron at a time states the recording limitation needed for later covariance interpretation. The full section directly distinguishes repeated paired recordings from simultaneous neural recording.',
'sec:EYE-FORWARD-FIT':'Fitted model and movement-to-rate direction keep the calibration distinct from inverse prediction. Position, velocity and acceleration are motivated before the equation, and the parameter units are then given.',
'sec:EYE-INVERSE-FILTER':'Calibrated filter states the retained physical gain and one-cell input. Causal filter and impulse response are defined before the h0 expression; convolution is explained before later degrees-based comparisons.',
'sec:EYE-SHARED-VARIANCE':'Challenges independent noise alone is needed to keep the first statistical inference weaker than locating a specific integrator. Correlation and coefficient of determination have the needed definitions before population bounds.',
'sec:EYE-CHI':'Calibrated covariance distinguishes this estimate from raw correlation. Common share of movement variance identifies the quantity in the numerator/denominator; gain is defined earlier and unit common gain is explained again before use.',
'sec:EYE-MEASUREMENT-NOISE':'Constant offset identifies the useful consequence of temporally independent error. MSD is already taught in Chapter 1 and repeated at section start; positive-lag and covariance conditions are taught visibly before subtraction.',
'sec:EYE-FILTERED-MSD':'The plateau/growth contrast gives the reader the model-discriminating result. White noise, low pass filtering and stationarity are defined before the overlap calculation; diffusion is earlier background.',
'sec:EYE-CIRCUIT-MODEL':'Can reproduce keeps a sufficient model distinct from uniquely measured cause. Noisy integrator and muscle filtering have both been taught before this more detailed mechanism.',
'sec:EYE-SCALING':'Spike regularity and circuit parameters state what controls the modeled amplitude. CV, sub-Poisson spiking and renewal-process assumptions are supplied before their scaling roles.',
'sec:EYE-FIGURES':'The three tested claims give a useful reading purpose. The table distinguishes empirical drive evidence, simulated diffusion and the full model comparison; no heading-only technical claim is left unexplained.',
'sec:EYE-LIMITS':'Upstream drive and no unique circuit summarize the distinction needed for the final interpretation. All components of this distinction have already been taught; the section retains animal, movement-axis and task limits.',
}
rows=[];sources={};fields=[]
for stem in ['03-memory-information','04-eye-drift']:
    for ext in ['md','yaml']:
        f=P/(stem+'.'+ext);sources[f.name]=dict(path=str(f),sha256=hashlib.sha256(f.read_bytes()).hexdigest())
    t=(P/(stem+'.md')).read_text(encoding='utf-8');y=yaml.safe_load((P/(stem+'.yaml')).read_text(encoding='utf-8'))
    for m in re.finditer(r'^#{1,6} (.+) \{#([^}]+)\}$',t,re.M):
        title,ident=m.groups();rows.append(dict(file=stem+'.md',line=t[:m.start()].count('\n')+1,id=ident,quote=title,passage_sha256=sha(m.group(0)),decision='retain',deletion_and_terminology_test=R[ident]))
    fields.append(dict(file=stem+'.yaml',fields='chapter title, purpose, all section titles/summaries, figure captions/alts and table cells',assessment='The title fields match the actual source headings. The existing purpose/summary openings still describe their sections. Figure/table fields retain the units, inferred-versus-measured distinctions and model/example labels used in the prose; no new undefined term or changed claim was introduced through these reader fields.'))

repairs=[
dict(file='03-memory-information.md',quote='The matrix inequality applies when every independent small coordinate change can be distinguished through a change in rates, so $J$ is invertible. It also explains why a scalar bound in each coordinate separately would miss coupled directions.[^p1-matrix]',decision='retain',deletion_test='Removing this paragraph would hide invertibility and the reason for a matrix result from the closed reading path. Applies is appropriate before the proof; This proves would falsely point back to proof steps now below it.',terminology='Independent coordinate change is explained by changes in rates. The U,V symbols and positive-semidefinite meaning are visible before the fold.'),
dict(file='04-eye-drift.md',quote='Substituting $B=-A$ gives $A(1/\\tau_- -1/\\tau_+)=1/m$, hence $A=\\tau_+\\tau_-/[m(\\tau_+-\\tau_-)]$. Making the response zero before the spike gives the impulse response $h_0(u)$.',decision='retain',deletion_test='The first sentence solves the pulse-matching constants; the final sentence connects them and the causal condition to the response. Deleting it would leave the coefficient calculation without its link to the response being derived.',terminology='Impulse response and h0 were defined before the visible formula. The repaired wording uses that exact term rather than adding a new label.'),
dict(file='04-eye-drift.md',quote='For a constructed example, take $k=4$ spikes/(s deg), $\\tau_+=0.120$ s, and $\\tau_-=0.005$ s.',decision='retain at its moved visible position',deletion_test='The example converts the formula into decay coefficients, area 1/k and a rate-to-position gain. Removing it would remove the shortest physical-units check from the visible route. Placing it before the optional general area/repeated-root check is sufficient.',terminology='Constructed marks the illustrative values; the paper data comparison that follows is separately labeled.'),
]
for r in repairs:
    t=(P/r['file']).read_text(encoding='utf-8');assert r['quote'] in t;r['line']=t[:t.index(r['quote'])].count('\n')+1;r['passage_sha256']=sha(r['quote'])

folds=[
dict(title='Check: equality can also hold with a linear transfer rule',decision='retain',deletion_test='The fold adds the constructive counterexample supporting sufficient rather than necessary. The visible qualification already teaches the result, so it is optional depth rather than the first use of that limit.',terms='Equality refers to the immediately preceding diffusion bound; linear transfer rule was taught in Chapter 2.'),
dict(title='Check: the residual matrix proves the lower bound',decision='retain',deletion_test='The fold adds a compact proof of the visible matrix result; the difference Q and its squared norm show what residual means. The matrix construction and invertibility remain visible.',terms='Residual is a standard linear-algebra remainder, displayed immediately as Q=V-U(U-transpose U) inverse. Replacing the technical term is unnecessary.'),
dict(title='Derivation: the weights of the two decaying responses',decision='retain',deletion_test='Weights identifies the A/B coefficients solved by pulse matching, after the response and decay times have been shown. Removing that purpose would leave a generic derivation label.',terms='Decay times, causality and impulse response are already taught; the fold has no new required biological term.'),
dict(title='Check: static gain and coincident decay times',decision='retain as sufficient; optional simpler word below',deletion_test='Static gain and equal-root behavior are the two actual checks. Both add depth after a visible gain example, and neither is needed for the next statistical inference.',terms='Gain was defined in the recording section. Coincident means equal here and is explained by the repeated-time condition inside the fold.'),
]
optional=[dict(id='S2-IE-OPT-01',file='04-eye-drift.md',line=139,quote='Check: static gain and coincident decay times',suggestion='Check: static gain and equal decay times',reason='Equal is the everyday word for the same repeated-time condition. The existing title is mathematically sufficient and the body explains it, so this is optional and does not block the scoped review.')]
report=dict(stage=2,reviewer='GPT-6.1-sol/high, teach_place_synthesis',local_request_id='root-to-teach_place_synthesis-stage2-information-eye',platform_call_id='not exposed',timestamp=now.isoformat(),root_wall_elapsed_seconds=(now-root).total_seconds(),stage_elapsed_seconds=(now-start).total_seconds(),awake_execution_time='unverified',source_hashes=sources,scope='Necessity and terminology in current frozen-v2 titles, fold titles, moved/repaired paragraphs, connected teaching and reader fields. No paper audit, manuscript edits or whole-book verdict.',method='Read actual current sources and baseline source text, not author defenses. Applied deletion tests before considering changes. Retained sufficient wording and exact scientific terms. Stage 1 remains separate evidence.',title_checks=rows,reader_field_checks=fields,moved_repaired_paragraph_checks=repairs,fold_title_checks=folds,defects=[],optional_preferences=optional,verdict='No required wording or terminology repair in the scoped current text. One optional simpler fold-title word is recorded separately. Reader-flow Stage 3 remains pending.',token_stats='unavailable')
(TASK/'stage2-information-eye.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
md=f'''# Independent Stage 2: Chapters 3 and 4 necessity and terminology

Recorded {now.isoformat()}. GPT-6.1-sol/high. Root wall elapsed {(now-root).total_seconds()/60:.2f} minutes; stage {(now-start).total_seconds()/60:.2f} minutes. Awake execution time unverified. Token stats unavailable.

No required wording or terminology repair was found in the current scoped text. The accompanying JSON contains passage-based deletion/terminology judgments for all 23 headings, four fold titles, the moved/repaired paragraphs and connected reader fields, bound to actual source hashes. No target author defense was read and no source was edited. Stage 1 and its recheck remain separate evidence.

The scientific terms carry needed distinctions: lower bound versus achieved diffusion, conditional Poisson information versus the Gaussian readout model, calibrated covariance versus correlation, and inferred upstream drive versus a unique circuit. Their required meanings precede later reasoning. The visible invertibility paragraph and the repaired h0 proof sentence supply needed connections and should stay.

The moved impulse-response example earns its visible space by converting decay times into a coefficient, kernel area and a rate-to-position gain. The optional static-gain algebra repeats the general check at greater depth, while the equal-time limit extends the result. No new required term is hidden by these folds.

Optional preference, not a defect: at `04-eye-drift.md:139`, “Check: static gain and coincident decay times” could use “equal decay times”. Both mean the same mathematical condition; the body already explains it. No blanket wording change is suggested.

This is the local wording stage only. Reader-flow Stage 3 remains pending; there is no whole-book acceptance claim.
'''
(TASK/'stage2-information-eye.md').write_text(md,encoding='utf-8')
print(json.dumps({'timestamp':now.isoformat(),'root_wall_minutes':(now-root).total_seconds()/60,'stage_minutes':(now-start).total_seconds()/60,'title_checks':len(rows),'defects':0,'optional_preferences':1}))
