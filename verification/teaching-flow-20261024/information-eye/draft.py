from pathlib import Path
import json, re, hashlib, datetime, difflib

BASE=Path('C:/dev/clsc/burak-papers/guide')
TASK=BASE/'verification/teaching-flow-20261024'
OUT=TASK/'proposed/content/chapters'
GROUP=TASK/'information-eye'
OUT.mkdir(parents=True,exist_ok=True)
def sha(s): return hashlib.sha256(s.encode('utf-8')).hexdigest()
now=datetime.datetime.now().astimezone().isoformat()
assessment=GROUP/'initial-assessment.md'
assessment.write_text(assessment.read_text(encoding='utf-8').replace('2026-10-24T19:00:00+03:00 (actual timestamp stored in status.json by the author script)',now),encoding='utf-8')

# Each row is an individual title judgment made after reading the whole chapter.
TITLES={
'03-memory-information':[
('ch:MEMORY-INFORMATION','How spike information limits memory stability and recall','Connects local spike information to memory diffusion and finite recall accuracy.','Opening; scalar bound; ideal and partial readout results.'),
('sec:MEMORY-FI','Rate slopes and spike variability determine local information','Explains what makes nearby internal states distinguishable.','J=sum(r prime squared/r); positive-rate, local Poisson assumptions remain visible.'),
('sec:MEMORY-BOUND','Spike information sets a lower bound on memory diffusion','Derives a lower bound rather than identifying actual diffusion with that bound.','Cauchy Schwarz proof, equality condition and strictness example.'),
('sec:MEMORY-COMPARISONS','Improving persistence depends on what a comparison holds fixed','Explains why rate, time constant and tuning-width effects require controlled comparisons.','Population, rate, time-constant, width and firing-budget paragraphs.'),
('sec:MEMORY-READOUT-SETUP','Storage loss and readout error add under specific assumptions','Separates unrecoverable storage displacement from cue-state estimation error.','Zero cross-covariance argument and translation-invariance limits.'),
('sec:MEMORY-NAIVE','Equal weighting becomes harmful when observation lasts too long','Equal weighting has a finite best observation interval.','Opposing 2DL/3 and 1/(JL) terms; the answer title states their resulting tradeoff.'),
('sec:MEMORY-IDEAL','Accounting for diffusion makes readout improve toward a limit','Distinguishes diminishing improvement from the worsening of equal averaging.','Backward precision recursion and coth curve; local Gaussian assumptions already visible.'),
('sec:MEMORY-PARTIAL',None,'Reduced observed information can lengthen useful recall.','Random thinning and caveat for selected subsets; existing can qualification is accurate.'),
('sec:MEMORY-EXTENSIONS','Time scales and noise laws change the bound and its equality condition','Separates a two-stage dynamical change from a different observation-noise law.','tau plus tau_m formula and constant-q equality calculation.'),
('sec:MEMORY-FIG3-AND-CAUTION','Readout saturates, and one printed error bound needs qualification','Connects the curve comparison to the guide algebra checking a printed lower bound.','Normalized figure, inequality direction, saturation condition and explicit strict case.')],
'04-eye-drift':[
('ch:EYE-DRIFT','Eye drift points to a shared neural drive','Frames the result as evidence about upstream drive without promising a uniquely identified circuit.','Recorded correlations, calibrated covariance and final localization limits.'),
('sec:EYE-PATHWAY',None,'Explains the physical stages between a stored command and movement.','Integrator, OMNs and plant definitions; existing transformation title is sufficient.'),
('sec:EYE-RECORDINGS','The recordings pair one motor neuron with movement at a time','Explains the paired recording design and its limits.','57 cells in two animals, no simultaneous motor-neuron pair; the title gives the key design limit.'),
('sec:EYE-FORWARD-FIT','A fitted model links movement to firing rate','Shows why position alone is insufficient and how movement calibrates the neural signal.','Position, velocity, acceleration and delay fit; active-rate and held-out-trial qualifications.'),
('sec:EYE-INVERSE-FILTER',"A calibrated filter predicts eye position from one cell's spikes",'Puts neural and movement signals on the same calibrated degree scale.','Inverse relationship, kernel, units and constructed gain example support the conversion.'),
('sec:EYE-SHARED-VARIANCE','The measured correlation challenges independent motor noise alone','Makes the inference and rejected restricted hypothesis explicit.','R squared bound, representativeness and private-noise independence premises remain visible.'),
('sec:EYE-CHI','Calibrated covariance estimates the common share of movement variance','Separates a common variance fraction from correlation or distance traveled.','Unit gain and pairwise covariance assumptions, 0.82 weighted estimate and uncertainty limits.'),
('sec:EYE-MEASUREMENT-NOISE','Independent measurement error adds a constant offset to the MSD','States the statistical effect that makes noise subtraction possible.','Positive-lag 2 sigma squared result; temporal correlation and subtraction-uncertainty caveats.'),
('sec:EYE-FILTERED-MSD','The MSD plateaus for filtered white noise but grows for filtered diffusion','States the model distinction tested by timing statistics.','Stable decaying filter; white-input covariance plateau and filtered Brownian growth.'),
('sec:EYE-CIRCUIT-MODEL','A noisy integrator can reproduce drift after muscle filtering','Keeps the circuit as a possible explanation of the measured pattern.','Approximate fixed-point model, motor output and feedback; can avoids unique localization.'),
('sec:EYE-SCALING',"Spike regularity and circuit parameters set the model's drift scale",'Shows which changes alter the model drift scale and what must stay fixed.','CV squared, neuron count, absolute versus fractional sensitivity and tau_s; the title limits the result to the model.'),
('sec:EYE-FIGURES','The figures test shared drive, diffusion, and the full circuit model','Keeps the three different evidence steps separate.','Existing figure table and supplementary controls, without changing table content.'),
('sec:EYE-LIMITS','The evidence places shared drive upstream without identifying one circuit','Makes the remaining localization limit clear at chapter close.','No integrator recordings or selective perturbation; upstream alternatives and empirical scope.')]
}

FOLDS={
'03-memory-information':[
dict(title='Check: equality can also hold with a linear transfer rule',start=129,end=137,
visible='Scalar inequality and pointwise proportionality condition at original lines 106-127, including the explicit sufficient-not-necessary qualification.',
dependent='The visible strictness example uses mutual inhibition, not this optional mutual-excitation counterexample. The Gaussian-noise extension refers to the counterexample, but also states the general pointwise condition visibly and does not use its numbers.',
reason='The closed path preserves the limit on the exponential claim and a separate short strictness example; this check supplies the deeper counterexample in full.'),
dict(title='Check: the residual matrix proves the lower bound',start=179,end=184,move_after=186,
visible='Matrix information, the meaning of positive semidefinite order, the matrix bound and U/V identities at original lines 165-177. Invertibility and coupled-direction interpretation remain at line 186.',
dependent='Later scalar width and eye-drift calculations do not use Q or this residual expansion. Q exists only in the hidden algebra.',
reason='Readers can retain the multidimensional result, its meaning and conditions while opening the exact nonnegative-residual calculation if wanted.')],
'04-eye-drift':[
dict(title='Derivation: the weights of the two decaying responses',start=94,end=107,move_after=122,
visible='Causal filter and impulse-response definitions, differential relation, decay times and their conditions at original lines 65-91. The complete response formula remains visible at 109-113, followed by causality, delay, convolution and units.',
dependent='The common variance and circuit arguments require the calibrated filter and its gain, all visible. The temporary coefficients A and B occur only inside this calculation.',
reason='The closed path still teaches the filter and gives its full normalized formula; only the initial-condition calculation of its coefficients is optional.'),
dict(title='Check: static gain and coincident decay times',start=124,end=132,move_after=141,
visible='The normalized kernel, delay and units remain at original lines 109-122; the numerical example at 134-141 visibly checks area 1/k and steady-rate gain.',
dependent='No later passage needs the repeated-pole limit. The 82 percent inference needs calibrated gain, which the visible numerical example and kernel still explain.',
reason='The closed path retains the shortest concrete gain check; this fold keeps the symbolic area calculation and special equal-time-constant case available.')]
}

changes=[]; titles=[]; folds=[]; hashes={}
for stem, rows in TITLES.items():
    src=BASE/'content/chapters'/f'{stem}.md'; old=src.read_text(encoding='utf-8'); text=old
    ysrc=src.with_suffix('.yaml'); yold=ysrc.read_text(encoding='utf-8'); ytext=yold
    for anchor, proposed, contribution, support in rows:
        pattern=re.compile(r'^(#+) (.*?) \{#'+re.escape(anchor)+r'\}$',re.M)
        m=pattern.search(old); assert m,anchor
        previous=m.group(2); new=proposed or previous
        titles.append(dict(chapter=stem,id=anchor,old=previous,new=new,decision='change' if proposed else 'retain',contribution=contribution,support=support))
        if proposed:
            before=m.group(0); after=f'{m.group(1)} {new} {{#{anchor}}}'
            assert text.count(before)==1
            text=text.replace(before,after,1)
            changes.append(dict(file=f'{stem}.md',kind='title',id=anchor,before=before,after=after,reason=contribution))
            # Only the matching title row is edited; block captions stay unchanged.
            if anchor.startswith('ch:'):
                needle=f'title: {previous}\n'; replacement=f'title: {new}\n'
            else:
                needle=f'- id: {anchor}\n  title: {previous}\n'; replacement=f'- id: {anchor}\n  title: {new}\n'
            assert ytext.count(needle)==1,(anchor,needle)
            ytext=ytext.replace(needle,replacement,1)
            changes.append(dict(file=f'{stem}.yaml',kind='sidecar-title',id=anchor,before=needle,after=replacement,reason='Match the individually reviewed source title. Opening summary remains accurate because prose is unchanged.'))
    original_lines=old.splitlines()
    for f in FOLDS[stem]:
        span='\n'.join(original_lines[f['start']-1:f['end']]); assert text.count(span)==1
        assert '{{block:' not in span and '.definition-term' not in span and not re.search(r'^#',span,re.M)
        wrapped=f'::: {{.publisher-clarification-note .publisher-fold-always title="{f["title"]}"}}\n\n{span}\n\n:::'
        if 'move_after' in f:
            before='\n'.join(original_lines[f['start']-1:f['move_after']])
            tail='\n'.join(original_lines[f['end']:f['move_after']]).strip('\n')
            after=tail+'\n\n'+wrapped
        else:
            before=span; after=wrapped
        assert text.count(before)==1
        text=text.replace(before,after,1)
        entry=dict(chapter=stem,original_lines=[f['start'],f['end']],hidden_text=span,hidden_sha256=sha(span),**f)
        folds.append(entry)
        changes.append(dict(file=f'{stem}.md',kind='move-and-fold' if 'move_after' in f else 'fold',locus=f'original lines {f["start"]}-{f["end"]}',before=before,after=after,reason=f['reason']))
    # Minimal local connections required by putting results before optional proofs.
    if stem=='03-memory-information':
        before='This proves the matrix inequality when every independent small coordinate change can be distinguished through a change in rates, so $J$ is invertible.'
        after='The matrix inequality applies when every independent small coordinate change can be distinguished through a change in rates, so $J$ is invertible.'
        reason='The condition now precedes its optional proof; remove the backward reference to an algebraic step that follows it.'
    else:
        before='$$\nh_0(u)=\\frac{\\Theta(u)}{m}\\,'
        after='The corresponding impulse response is\n\n'+before
        reason='Introduce the visible response formula after moving its optional coefficient derivation below the formula and interpretation.'
    assert text.count(before)==1
    text=text.replace(before,after,1)
    changes.append(dict(file=f'{stem}.md',kind='connection-repair',before=before,after=after,reason=reason))
    (OUT/f'{stem}.md').write_text(text,encoding='utf-8')
    (OUT/f'{stem}.yaml').write_text(ytext,encoding='utf-8')
    hashes[stem]=dict(source_md=sha(old),proposed_md=sha(text),source_yaml=sha(yold),proposed_yaml=sha(ytext))
    # Exact text reversibility and preservation checks.
    restored=text
    for c in reversed([x for x in changes if x['file']==f'{stem}.md']):
        assert restored.count(c['after'])==1
        restored=restored.replace(c['after'],c['before'],1)
    assert restored==old
    assert re.findall(r'\{#([^}]+)\}',old)==re.findall(r'\{#([^}]+)\}',text)
    assert re.findall(r'\{\{block:[^}]+\}\}',old)==re.findall(r'\{\{block:[^}]+\}\}',text)
    # No math, prose or links removed: removing wrappers and restoring titles recovers every character.
    (GROUP/f'{stem}.diff').write_text(''.join(difflib.unified_diff(old.splitlines(True),text.splitlines(True),fromfile=f'canonical/{stem}.md',tofile=f'proposed/{stem}.md')),encoding='utf-8')

for name,data in [('exact-changes.json',changes),('title-decisions.json',titles),('fold-decisions.json',folds),('hashes.json',hashes)]:
    (GROUP/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
(GROUP/'status.json').write_text(json.dumps(dict(timestamp=now,root_start='2026-10-24T18:54:22.5524387+03:00',model='GPT-6.1-sol/high allocation',stage='draft written; paragraph ledger and connected check pending',awake_execution='unverified',tokens='unavailable'),indent=2)+'\n',encoding='utf-8')
print(json.dumps(dict(timestamp=now,titles=len(titles),changed_titles=sum(t['decision']=='change' for t in titles),folds=len(folds),exact_change_rows=len(changes),checks='reverse changes recover source exactly; stable IDs, typed-block references, math, prose and links retained'),indent=2))
