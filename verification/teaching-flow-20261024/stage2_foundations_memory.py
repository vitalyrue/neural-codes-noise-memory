from pathlib import Path
import re,json,hashlib,datetime,yaml
T=Path('C:/dev/clsc/burak-papers/guide/verification/teaching-flow-20261024'); P=T/'proposed/content/chapters'
def sha(b):return hashlib.sha256(b).hexdigest()
files=['01-foundations.md','01-foundations.yaml','02-memory-dynamics.md','02-memory-dynamics.yaml']
src={f:(P/f).read_text(encoding='utf-8') for f in files}
hashes={f:sha((P/f).read_bytes()) for f in files}
judgments={
'ch:FOUNDATIONS':('Retain. Removing the distinction between continued activity and accurate memory would lose the chapter question.','Persistent and error have ordinary meanings here; the opening immediately separates represented value from activities.'),
'sec:FOUNDATIONS-SPIKES':('Retain. The rate-pattern statement gives the point of the coming cell-level definitions.','Firing rate is defined in the first paragraph; population code and decoding follow the explicit rate vector. A title preview does not require extra jargon before this explanation.'),
'sec:FOUNDATIONS-POISSON':('Retain. Fixed rate with variable count is the needed observation that motivates the Poisson model.','Poisson process is the exact model name and is immediately given its count law, duration and expected count. Replacing it with random firing would erase the model assumptions.'),
'sec:FOUNDATIONS-COVARIANCE':('Retain. The title states why variance alone may not account for displacement; deleting mean motion would hide the later bias distinction.','Mean, variance and covariance belong to the audience probability baseline. The chapter gives subject-specific displacement and covariance meanings before using them for neural or eye signals.'),
'sec:FOUNDATIONS-ATTRACTOR':('Retain. The short value-versus-activity contrast is the concrete reason for the attractor example.','Stable is explained as decay in a direction; vulnerable is ordinary wording for a value that can change. Continuous attractor and neutral direction receive exact definitions before the example depends on them.'),
'sec:FOUNDATIONS-DIFFUSION':('Retain the repaired title. Its duration and variance conditions earn their words because deleting either would broaden the mathematical claim.','Steps is ordinary language for the defined interval increments. Equal variance is appropriate for the probability baseline, and the body immediately identifies the shared 2D Delta t value.'),
'sec:FOUNDATIONS-RANDOMNESS':('Retain. The contrast prevents using random spatial shape as evidence of temporal memory loss.','Fixed refers to the expected spatial function for a cell/environment, not invariant observed spikes; the first paragraph makes that meaning explicit.'),
'ch:MEMORY-DYNAMICS':('Retain. The title identifies the specific state direction in which spike noise accumulates.','Spiking and attractor are taught in Chapter 1. Diffusion has its variance-growth meaning there; the Chapter 2 notation paragraph recalls its convention before calculation.'),
'sec:MEMORY-SPIKES':('Retain. Renew connects the decaying activation to the recurrent cause that can sustain it.','Recurrent means a circuit sends signals back into its population, defined in Chapter 1. The present first paragraph explains the full cycle rather than relying on that label.'),
'sec:MEMORY-LINEARIZATION':('Retain. Return flow distinguishes the required projection from a perpendicular geometric shortcut; deleting it loses the section result.','Flow is used concretely as the state returning toward the fixed-point family. Linearization and both zero eigenvectors are defined with equations and purposes before the lasting-displacement result.'),
'sec:MEMORY-DIFFUSION':('Retain. The title names the calculation the reader can now perform from projected fluctuations.','Projecting has the specific left-vector meaning just taught. Diffusion coefficient is already defined and is now matched explicitly to increment variance.'),
'sec:MEMORY-SYMMETRIC':('Retain. The symmetry condition earns its place because it makes a tuning-based expression possible; removing it suggests the same formula works for all networks.','Symmetric weights are given as W_ij=W_ji in the opening. Tuning curves were introduced in Chapter 1, and their input/rate derivatives are defined before the formula.'),
'sec:MEMORY-LONG-TIME':('Retain. Boundaries and state dependence explain why a local coefficient cannot alone fix all delay errors.','Local means evaluated near the current represented value, as stated in the preceding section. Probability density is from the probability baseline, and p is assigned its memory-trial meaning before the equation.'),
'sec:MEMORY-DRIFT-SCOPE':('Retain. The title preserves a needed limit on the preceding variance calculation.','Systematic drift is explained first as reproducible mean movement, then defined as nonzero mean velocity. Ito and Stratonovich retain their exact names because they describe different coefficient-evaluation rules.'),
'sec:MEMORY-FIGURES':('Retain. Memory motion, readout uncertainty and simulation tests are different contributions; the heading helps the reader keep them apart.','Readout error is explained in the figure paragraph as finite-spike uncertainty about current location. Activity bump is defined when first needed, and all empirical-versus-simulation labels remain precise.')
}
answers=[]
for f in ['01-foundations.md','02-memory-dynamics.md']:
    for n,line in enumerate(src[f].splitlines(),1):
        m=re.match(r'^#+ (.*?) \{#([^}]+)\}$',line)
        if m:
            deletion,terms=judgments[m[2]]
            answers.append(dict(file=f,line=n,id=m[2],passage=line,passage_sha256=sha(line.encode()),deletion_test=deletion,terminology_answer=terms,decision='retain'))
assert len(answers)==15
folds=[
 dict(file='01-foundations.md',lines=[44,54],title='Derivation: why a Poisson count has variance equal to its mean',
 deletion_test='Retain the exact calculation as optional depth. Deleting it would remove the count-variance derivation; leaving it visible is not required to understand the result already stated before it.',
 terminology='Poisson count and variance/mean are the exact concepts being derived. Factorial moments occurs inside the proof and is immediately shown as the sums of k and k(k-1), so no additional unexplained concept drives the result.',
 connected_text='The visible E[K]=Var(K)=lambda result comes first. After the fold, relative standard deviation and the silent-cell example use that visible result without referencing hidden proof notation.'),
 dict(file='02-memory-dynamics.md',lines=[304,326],title='Derivation: from random increments to the memory density equation',
 deletion_test='Retain the proof as optional depth because it connects local increments to density evolution. The visible first-pass solution and ring-limit discussion do not need its test-function algebra.',
 terminology='Random increments has its interval-change meaning from Chapter 1. Memory density here refers to p(theta,t), already defined for repeated trials in this section. Ito, Fokker Planck and Dirac delta are retained exact terms with local meanings supplied before later reasoning.',
 connected_text='The repaired first sentence states its purpose directly. The last sentence names the Fokker Planck equation explicitly. The later state-dependent-moment paragraph independently states its boundary condition and explains integration by parts; it does not rely on an unexplained object hidden in this fold.')]
side=[]
for f in ['01-foundations.yaml','02-memory-dynamics.yaml']:
    d=yaml.safe_load(src[f]); side.append(dict(file=f,
 purpose_answer='Retain the opening summary: it establishes the biological question and chapter contribution without replacing its teaching. It matches the actual chapter opening.',
 section_summaries_answer='Read all section titles and summaries. They retain the actual section openings and match the new headings without adding claims or alternate terminology.',
 figures_answer='Read all four captions and alt texts in this sidecar. Their construction/simulation/data labels and units serve interpretation rather than decorative commentary. None is moved inside a fold. No caption deletion is needed for this title/depth/order change.'))
now=datetime.datetime.now().astimezone(); start=datetime.datetime.fromisoformat('2026-10-24T19:07:36.5166502+03:00'); root=datetime.datetime.fromisoformat('2026-10-24T18:54:22.5524387+03:00')
r=dict(stage='2. Necessity and terminology only',local_request_id='/root/teach_information_eye/stage2-foundations-memory-20261024',reviewer='/root/teach_information_eye; GPT-6.1-sol/high allocation',
 started=start.isoformat(),completed=now.isoformat(),root_wall_seconds=(now-root).total_seconds(),stage_wall_seconds=(now-start).total_seconds(),awake_execution='unverified',
 scope='Frozen-v2 Chapters 1 and 2 titles, two fold titles and moved proof paragraphs, their connected explanations and reader-facing sidecar fields. No writer defenses read and no edits.',source_hashes=hashes,
 audience='Undergraduate calculus, basic probability and linear algebra; needed neural/stochastic meanings taught in the reading path.',
 heading_answers=answers,fold_and_moved_passage_answers=folds,sidecar_answers=side,
 defects=[],optional_preferences=[],
 verdict='No required necessity or terminology repair found in this scope. Retain the current wording. This is separate from the Stage 1/recheck evidence and does not complete Stage 3 or approve the whole book.',token_stats='unavailable')
(T/'stage2-foundations-memory.json').write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
(T/'stage2-foundations-memory.md').write_text(f'''# Stage 2: necessity and terminology, Chapters 1 and 2

Completed {now.isoformat()}. Reviewer /root/teach_information_eye, GPT-6.1-sol/high allocation. Frozen-v2 source hashes and 15 heading judgments are in stage2-foundations-memory.json.

No required repair or optional wording preference found. Retain the current wording. The titles state useful distinctions without dropping the conditions needed by their sections. In the repaired diffusion title, equal duration and variance are necessary words, so shortening it would lose its mathematical limit.

Both fold titles identify the exact proof offered. The Poisson result precedes its factorial-moment calculation. The density equation, initial state, line/ring result and boundary meaning remain visible before its test-function proof. The moved proof's opening and closing identify its purpose and result directly. The later moment equations do not need hidden definitions.

Exact terms earn their place: firing rate, tuning curve, covariance, continuous attractor, diffusion coefficient, the two zero eigenvectors, Ito and Fokker Planck have meanings supplied before the reasoning that uses them. Removing them would weaken the model distinctions. Reader-facing sidecar summaries and all eight captions/alt texts were read; no inconsistent terms or extra claims were found in this scope.

No edits made. Stage 1 and its recheck remain separate records. Stage 3 is pending. Wall elapsed since root start {r['root_wall_seconds']:.1f}s; stage elapsed {r['stage_wall_seconds']:.1f}s; awake execution unverified. Token stats unavailable.
''',encoding='utf-8')
print(json.dumps(dict(completed=now.isoformat(),root_wall_seconds=r['root_wall_seconds'],stage_wall_seconds=r['stage_wall_seconds'],heading_answers=len(answers),required_defects=0,optional_preferences=0),indent=2))
