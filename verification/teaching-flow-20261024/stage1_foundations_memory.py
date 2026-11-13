from pathlib import Path
import hashlib,json,datetime,re,yaml
TASK=Path('C:/dev/clsc/burak-papers/guide/verification/teaching-flow-20261024')
P=TASK/'proposed/content/chapters'
def sha(b): return hashlib.sha256(b).hexdigest()
files=['01-foundations.md','01-foundations.yaml','02-memory-dynamics.md','02-memory-dynamics.yaml']
hashes={f:sha((P/f).read_bytes()) for f in files}
texts={f:(P/f).read_text(encoding='utf-8') for f in files}
verdicts={
'ch:FOUNDATIONS':'Supported by the two-activity example: an along-family disturbance changes the angle from 5 to 6.5 degrees while activity stays on the fixed-point line. Can preserves the possibility rather than making all persistent activity fail.',
'sec:FOUNDATIONS-SPIKES':'The tuning vector explicitly maps each represented angle to a rate pattern. The text distinguishes rate expectation from particular spike times and a neuron index from physical position.',
'sec:FOUNDATIONS-POISSON':'A fixed modeled rate gives a Poisson count with variable outcomes. The mean/variance formula and zero-count example establish the title directly.',
'sec:FOUNDATIONS-COVARIANCE':'The displayed identity adds displacement variance and squared mean displacement. Combines does not claim the unsquared mean is added. The preceding covariance/correlation identities support the later eye inference.',
'sec:FOUNDATIONS-ATTRACTOR':'The fixed-point and restoring/neutral definitions are followed by two disturbances that separate activity restoration from value restoration. The example is labeled a teaching model.',
'sec:FOUNDATIONS-DIFFUSION':'Needs the fixed variance-per-time condition in its answer title. Independence and zero mean alone allow variance growth at other rates; see defect FM-TRUTH-01.',
'sec:FOUNDATIONS-RANDOMNESS':'The text distinguishes a random function drawn over locations from noise accumulating over time, while allowing visit-to-visit spikes to remain variable. It does not claim place-cell firing is deterministic.',
'ch:MEMORY-DYNAMICS':'Supported within the explicitly tuned continuous-attractor, weak-fluctuation model. The chapter states the large-population and local-state limits and checks systematic drift separately.',
'sec:MEMORY-SPIKES':'The jump/decay equation, summed input and transfer function show how recurrent spikes replenish decaying activation. Can in the opening correctly avoids claiming arbitrary recurrence suffices.',
'sec:MEMORY-LINEARIZATION':'The left zero vector removes decaying modes and preserves the tangent displacement. The tilted example demonstrates why return flow can differ from perpendicular projection.',
'sec:MEMORY-DIFFUSION':'The projected Brownian increment covariance gives 2D=sum(v_i squared r_i). The text limits the formula to local weak noise and does not equate high rate with greater damage under arbitrary retuning.',
'sec:MEMORY-SYMMETRIC':'Under symmetric W, g prime is a left zero vector and normalization gives the displayed tuning formula. Stable-family and noise conditions remain explicit, with invertibility needed only when replacing input by the inverse transfer relation.',
'sec:MEMORY-LONG-TIME':'The line/ring comparison and state-dependent moment equation show exactly how boundaries and local D alter delay errors. The title does not promise all state dependence curves the variance.',
'sec:MEMORY-DRIFT-SCOPE':'The text explicitly separates variance growth from mean velocity and states why the leading noise projection does not determine exact noise-induced drift. Correlated-noise extension is kept distinct from a proved general information result.',
'sec:MEMORY-FIGURES':'The figure account separates displacement of the latent coordinate from finite-spike readout uncertainty, and treats network simulations as model tests rather than direct animal measurements.'
}
headings=[]
for f in ['01-foundations.md','02-memory-dynamics.md']:
    for i,line in enumerate(texts[f].splitlines(),1):
        m=re.match(r'^#+ (.*?) \{#([^}]+)\}$',line)
        if m: headings.append(dict(file=f,line=i,id=m[2],title=m[1],passage_sha256=sha(line.encode()),answer=verdicts[m[2]],verdict='repair needed' if m[2]=='sec:FOUNDATIONS-DIFFUSION' else 'supported in context'))
assert len(headings)==15
f='01-foundations.md'; lines=texts[f].splitlines()
defect=dict(id='FM-TRUTH-01',kind='required title qualification',severity='minor',file=f,line=159,anchor='sec:FOUNDATIONS-DIFFUSION',
 passage=lines[158],passage_sha256=sha(lines[158].encode()),
 literal_claim='Independent increments with mean zero give variance that grows linearly with elapsed time.',
 likely_reader_inference='The two listed conditions are sufficient for the advertised result.',
 failed_check='Necessary condition omitted from a result title.',
 evidence='The following paragraph at line 161 also assumes every equal-duration increment has variance 2D Delta t with the same D. Only then does the displayed sum become 2D n Delta t.',
 counterexample='Let independent increments have mean zero and variance j in equal-duration interval j. Their cumulative variance is n(n+1)/2, not linear in n. No research-source claim is needed for this direct variance identity.',
 prerequisites_checked=['01-foundations.md covariance sum rule and zero-mean MSD decomposition','01-foundations.md lines 159-181, including the fixed-D increment variance','02-memory-dynamics.md state-dependent-D discussion lines 328-343'],
 proposed_repair='Independent changes with fixed variance per time give linear variance growth',
 sidecar_action='Match sec:FOUNDATIONS-DIFFUSION section_list title. Body already supplies the missing condition and does not need changing.')
now=datetime.datetime.now().astimezone()
record=dict(stage='1. Truth and reasoning only',local_request_id='/root/teach_information_eye/stage1-foundations-memory-20261024',
 reviewer='/root/teach_information_eye; GPT-6.1-sol/high allocation',
 initial_context='Neutral assignment, actual proposed reader sources and sidecars, proposed reading-guide audience/path paragraphs. No target writer decisions, defenses or earlier verdicts read.',
 started='2026-10-24T19:04:34.4353335+03:00',completed=now.isoformat(),root_start='2026-10-24T18:54:22.5524387+03:00',
 wall_elapsed_seconds=(now-datetime.datetime.fromisoformat('2026-10-24T18:54:22.5524387+03:00')).total_seconds(),awake_execution='unverified',source_hashes=hashes,
 scope='Full proposed Chapters 1 and 2, including sidecar purpose/section summaries, eight figure captions and alt text; connected reading-guide audience and first-pass instructions.',
 initial_open_assessment='Chapter 1 separates represented values from neural activity and supplies count/covariance/attractor/diffusion meanings. Chapter 2 turns that geometry into a noise projection and distinguishes local from long-delay and mean-drift claims. This order supplies the assumptions needed by Chapter 3 without treating the three papers as one established circuit. The title changes mostly make those contributions explicit.',
 title_answers=headings,
 closed_fold_answers=[
 dict(file='01-foundations.md',lines=[44,54],title='Derivation: why a Poisson count has variance equal to its mean',
 answer='The Poisson model, expected count and E[K]=Var(K)=lambda are visible before the fold. Later relative-error arithmetic and the concrete count example need that result, not factorial moments. The fold retains the exact moment calculation and introduces no visible dependent notation.'),
 dict(file='02-memory-dynamics.md',lines=[304,326],title='Derivation: from random increments to the memory density equation',
 answer='The visible path defines density, zero-drift Ito convention and initial point mass before the density equation, then gives its line/ring solutions and limiting error. Later state-dependent moments use the visible density equation and explicitly explain integration by parts. The folded test-function proof supplies its derivation without hiding a needed first definition or boundary assumption; conditions that remove boundary terms remain visible at line 328.')],
 figure_caption_answers=[
 dict(chapter='01-foundations',answer='All four captions match their surrounding equations and illustrative status: Poisson rate SD falls from 20 to 4.47 Hz; attractor disturbances give 5 versus 6.5 degrees; bias and RMS scales meet at 0.40 degrees and 4 seconds; the paper map compares different questions without claiming one circuit.'),
 dict(chapter='02-memory-dynamics',answer='All four captions match their surrounding examples: spike activation jumps by one and decays; a/lambda=1/2 maps the vertical jump of 2 to a lasting shift of 1; b=20 and tau=0.1 give D=100; constant-D angular reporting tends to pi squared over 3. The long-time figure stays outside the density-proof fold and is introduced and interpreted visibly.')],
 cross_chapter_answers=[
 'Chapter 1 teaches conditional spike-generation independence without treating complete recurrent spike trains as independent; Chapter 2 repeats that distinction where correlated input would alter the projection.',
 'The Chapter 1 fixed-point example explicitly defers tilted return flow to Chapter 2; Chapter 2 defines both zero vectors and demonstrates the missing perpendicular-projection correction before using it.',
 'Both chapters use variance=2Dt for one coordinate under fixed D and appropriate boundaries. Chapter 2 distinguishes ring saturation, state-dependent diffusion and systematic drift; moving the density proof does not erase these limits.',
 'Neither optional fold hides a figure, a first definition used by later visible prose, or the conditions needed to apply its displayed result.'
 ],defects=[defect],optional_preferences=[],
 limits=['No manuscript edits.','No Stage 2 wording or Stage 3 reader-flow verdict is implied.','This scoped check did not revalidate every unchanged research finding against the original papers or inspect all image pixels. It read the equations and reader-facing caption connections, not a whole-book release.'],
 verdict='One narrow heading condition needs repair; no other evidenced truth/reasoning defect found in the assigned changed reading path. Whole-book approval not given.',tokens='unavailable')
(TASK/'stage1-foundations-memory.json').write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
md=f'''# Stage 1: truth and reasoning, Chapters 1 and 2

Completed {now.isoformat()}. Reviewer: /root/teach_information_eye, GPT-6.1-sol/high allocation. Actual source hashes and passage-level answers are in stage1-foundations-memory.json. No writer decisions or prior verdicts were read.

The two chapters supply a coherent chain: distinguish neural activity from its represented value, define random spike counts and covariance, show neutral versus restoring directions, then derive the lasting displacement and its diffusion coefficient. Both optional folds keep the needed result and conditions visible. The figure captions match the surrounding illustrative calculations and preserve the distinction between model checks and animal measurements.

## Required repair

FM-TRUTH-01, 01-foundations.md:159, sec:FOUNDATIONS-DIFFUSION. “Independent, unbiased changes give linear variance growth” omits the fixed variance per time condition in its next paragraph. Independence and zero mean alone are insufficient. Independent zero-mean increments with variance j in interval j have cumulative variance n(n+1)/2. Suggested title: “Independent changes with fixed variance per time give linear variance growth”. Match the sidecar title. The body already has the correct condition.

No other evidenced defect found in this scope. No optional preferences recorded in Stage 1. This is not a wording, reader-flow, image-pixel or whole-book approval.

Wall elapsed since root start: {record['wall_elapsed_seconds']:.1f}s. Awake execution unverified. Stage start: 19:04:34.4353335. Token stats unavailable.
'''
(TASK/'stage1-foundations-memory.md').write_text(md,encoding='utf-8')
print(json.dumps(dict(completed=now.isoformat(),root_wall_seconds=record['wall_elapsed_seconds'],heading_answers=len(headings),required_defects=1,files=['stage1-foundations-memory.json','stage1-foundations-memory.md']),indent=2))
