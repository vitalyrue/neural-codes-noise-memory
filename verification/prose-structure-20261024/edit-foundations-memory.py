from pathlib import Path
import hashlib, json, datetime

task=Path(__file__).parent
chapters=['01-foundations.md','01b-persistence.md','02-memory-dynamics.md','02b-memory-long-delays.md']
records=[]
texts={}
for name in chapters:
    path=task/'baseline/content/chapters'/name
    raw=path.read_bytes()
    texts[name]=raw.decode('utf-8')
    records.append({'source_path':f'content/chapters/{name}','baseline_path':str(path),'baseline_sha256':hashlib.sha256(raw).hexdigest(),'edits':[]})

def edit(name, section, old, new, kind, why, preserve, question=None):
    text=texts[name]
    nl='\r\n' if '\r\n' in text else '\n'
    old=old.replace('\n',nl); new=new.replace('\n',nl)
    assert text.count(old)==1,(name,old[:90],text.count(old))
    rec=next(x for x in records if x['source_path'].endswith(name))
    rec['edits'].append({'section':section,'paragraph_start':old.split(nl)[0], 'old':old,'new':new,'kind':kind,'rationale':why,'preserved_premise_or_limit':preserve,'source_or_meaning_question':question,'recorded_at':datetime.datetime.now().astimezone().isoformat()})
    # Save the exact ledger before applying this individual change to the proposed text.
    (task/'changes-foundations-memory.json').write_text(json.dumps({'chapters':records},ensure_ascii=False,indent=2),encoding='utf-8')
    texts[name]=text.replace(old,new,1)

edit('01-foundations.md','sec:FOUNDATIONS-SPIKES',
'''Neurons affect one another through connections called [**synapse**]{.definition-term custom-style="Definition Term"}s. In the models used here, an excitatory input increases a receiving neuron's tendency to fire and an inhibitory input reduces it. The effect of a spike can last beyond the spike itself because synaptic input decays over time. When neurons send signals back into the same population, the circuit has [**recurrent connectivity**]{.definition-term custom-style="Definition Term"}. Such feedback can maintain activity after an external signal disappears.''',
'''Neurons affect one another through connections called [**synapse**]{.definition-term custom-style="Definition Term"}s. In the models used here, inputs have two contrasting effects:

- An [**excitatory input**]{.definition-term custom-style="Definition Term"} increases a receiving neuron's tendency to fire.
- An [**inhibitory input**]{.definition-term custom-style="Definition Term"} reduces it.

The effect of a spike can last beyond the spike itself because synaptic input decays over time. When neurons send signals back into the same population, the circuit has [**recurrent connectivity**]{.definition-term custom-style="Definition Term"}. Such feedback can maintain activity after an external signal disappears.''',
'list','Expose the two input effects as a comparison and mark their existing explanations in blue. The following prose still connects decay to recurrent activity.','The effects remain limited to the models used here; feedback can, rather than must, maintain activity.')

edit('01-foundations.md','sec:FOUNDATIONS-SPIKES',
'Establishing a population pattern from an input is encoding.',
'Establishing a population pattern from an input is [**encoding**]{.definition-term custom-style="Definition Term"}.',
'definition','Mark the existing explanation paired with decoding.','No change to the definition or claim.')

edit('01-foundations.md','sec:FOUNDATIONS-SPIKES',
'''The hippocampal areas CA3 and CA1 contain place cells. CA3 supplies major input to CA1 and has substantial recurrent excitation. CA1 also receives input from entorhinal cortex and has much less local recurrent excitation. A [**grid cell**]{.definition-term custom-style="Definition Term"}, found in entorhinal cortex, has repeated spatial fields that often form an approximately hexagonal pattern in a two-dimensional arena. These repeated grid fields and a place cell's irregular multiple fields should be kept distinct. A model explaining CA1's output maps need not identify where the animal's position estimate is maintained.[^f-anatomy]''',
'''The hippocampal areas CA3 and CA1 contain place cells, but their connections differ:

- CA3 supplies major input to CA1 and has substantial recurrent excitation.
- CA1 also receives input from entorhinal cortex and has much less local recurrent excitation.

A [**grid cell**]{.definition-term custom-style="Definition Term"}, found in entorhinal cortex, has repeated spatial fields that often form an approximately hexagonal pattern in a two-dimensional arena. These repeated grid fields and a place cell's irregular multiple fields should be kept distinct. A model explaining CA1's output maps need not identify where the animal's position estimate is maintained.[^f-anatomy]''',
'list','Make the anatomical comparison visible before the explanation distinguishes grid fields and output maps.','Preserve both input pathways, the relative amount of local recurrent excitation, often and approximately, and the limit on inferring memory location.')

edit('01-foundations.md','sec:FOUNDATIONS-POISSON',
'Even when the represented value stays fixed, the spikes need not repeat from trial to trial. The 2012 model starts with a tractable description of this variability: a [**Poisson process**]{.definition-term custom-style="Definition Term"}.',
'A tuning curve describes expected activity, but a brief spike observation can differ each time the same value is represented. The 2012 model describes this variability with a [**Poisson process**]{.definition-term custom-style="Definition Term"}.',
'transition','Connect the rate representation to the unresolved problem of observing variable spikes; remove tractable, which adds no needed explanation.','The value is held fixed across observations; this remains the 2012 model rather than a claim that all spikes are Poisson.')

edit('01-foundations.md','sec:FOUNDATIONS-POISSON',
'''Other measurements describe other aspects of variability. The [**coefficient of variation**]{.definition-term custom-style="Definition Term"}, or CV, of interspike intervals is their standard deviation divided by their mean. A homogeneous Poisson process has exponential intervals and CV equal to one. More regular firing can have CV below one, as in the ocular motor neurons analyzed in 2022. The count variance divided by mean count is the [**Fano factor**]{.definition-term custom-style="Definition Term"}; its value also depends on the counting interval. CV and Fano factor cannot be substituted for one another without additional assumptions.''',
'''Two other measurements describe different aspects of variability:

- The [**coefficient of variation**]{.definition-term custom-style="Definition Term"}, or CV, of interspike intervals, the times between successive spikes, is their standard deviation divided by their mean. A homogeneous Poisson process has exponential intervals and CV equal to one. More regular firing can have CV below one, as in the ocular motor neurons analyzed in 2022.
- The count variance divided by mean count is the [**Fano factor**]{.definition-term custom-style="Definition Term"}; its value also depends on the counting interval.

CV and Fano factor cannot be substituted for one another without additional assumptions.''',
'list','Separate interval variability from count variability and explain interspike intervals in place.','Preserve homogeneous Poisson scope, the example of below-one CV, counting-interval dependence and the warning against substitution.','The added explanation of interspike intervals is a short definition implicit in the existing term; correctness review should confirm it.')

edit('01b-persistence.md','sec:FOUNDATIONS-ATTRACTOR',
r'''At $\theta=5$ degrees, the rates are $(50,30)$. A disturbance of $(+3,+3)$ changes them to $(53,33)$. It creates $x=3$ but leaves the represented angle at 5 degrees. The restoring dynamics return to $(50,30)$. A disturbance of $(+3,-3)$ instead gives $(53,27)$, with $x=0$ and angle $26/(2\times2)=6.5$ degrees. This state lies on the fixed-point line, so there is no restoring response. The circuit remains coherent while holding the wrong angle.''',
r'''At $\theta=5$ degrees, the rates are $(50,30)$. Compare two disturbances from this same state:

- A disturbance of $(+3,+3)$ changes the rates to $(53,33)$. It creates $x=3$ but leaves the represented angle at 5 degrees. The restoring dynamics return to $(50,30)$.
- A disturbance of $(+3,-3)$ gives $(53,27)$, with $x=0$ and angle $26/(2\times2)=6.5$ degrees. This state lies on the fixed-point line, so there is no restoring response.

In the second case, the circuit remains coherent while holding the wrong angle.''',
'list','Let the reader compare the same starting state under two directions of disturbance; retain the conclusion after both cases.','All values, units, restoring behavior and the wrong-angle interpretation are unchanged.')

edit('01b-persistence.md','sec:FOUNDATIONS-DIFFUSION',
r'''If persistent angular changes arrive repeatedly, their errors accumulate. Divide time into intervals of length $\Delta t$. Let $\xi_j$ be the change in the represented coordinate during interval $j$. Assume independent increments with mean zero and variance $2D\Delta t$, where $D$ has units coordinate squared per time. After $n$ intervals,''',
r'''If persistent angular changes arrive repeatedly, their errors accumulate. Divide time into intervals of length $\Delta t$. Let $\xi_j$ be the change in the represented coordinate during interval $j$. The calculation assumes:

- increments are independent;
- each increment has mean zero;
- each increment has variance $2D\Delta t$, where $D$ has units coordinate squared per time.

After $n$ intervals,''',
'list','Keep the three assumptions visible beside the variance sum that needs them.','Equal interval duration, independence, zero mean, equal variance and units remain explicit.')

edit('01b-persistence.md','sec:FOUNDATIONS-DIFFUSION',
'Removing systematic drift is therefore a substantive assumption in a theory devoted to random diffusion.',
'A theory of random diffusion must therefore account for systematic drift separately.',
'wording','Replace substantive assumption and devoted to with the concrete consequence of the bias calculation.','The preceding example still shows the bias overtaking random spreading; the theory must still treat drift rather than ignore it.')

edit('02-memory-dynamics.md','sec:MEMORY-DIFFUSION',
'''The result is local in state and leading order in weak noise. A short interval must be long enough for the coarse description of many spike contributions to apply, yet short enough that the coefficients do not change substantially as the memory moves. Systematic drift requires a [separate check in the next chapter](ch-memory-long-delays.html#sec-memory-drift-scope).''',
'''The result is local in state and leading order in weak noise. The time interval must satisfy two conditions:

- It must be long enough for the approximation based on many spike contributions to apply.
- It must be short enough that the coefficients do not change substantially as the memory moves.

These conditions justify a local spreading rate. Systematic drift requires a [separate check in the next chapter](ch-memory-long-delays.html#sec-memory-drift-scope).''',
'list','Expose the competing time requirements and replace coarse description with what is being approximated.','Keep local and leading-order scope, many spike contributions, slow coefficient change and the separate drift check.')

edit('02-memory-dynamics.md','sec:MEMORY-SYMMETRIC',
'The result requires symmetric weights, a stable continuous family, and the noise assumptions already introduced; translation symmetry is unnecessary.[^p1-symmetric]',
'''The result requires:

- symmetric weights;
- a stable continuous family;
- the noise assumptions already introduced.

Translation symmetry is unnecessary.[^p1-symmetric]''',
'list','Make the three assumptions easy to check without hiding the distinction between symmetric weights and translation symmetry.','Every assumption and the explicit lack of a translation-symmetry requirement are retained.')

edit('02b-memory-long-delays.md','sec:MEMORY-LONG-TIME',
r'For completeness, multiply the density equation by $\theta$ or $(\theta-\Theta)^2$, integrate over $\theta$, and integrate by parts twice.',
r'To obtain these identities, multiply the density equation by $\theta$ or $(\theta-\Theta)^2$, integrate over $\theta$, and integrate by parts twice.',
'wording','Explain why the following calculation is here rather than label it for completeness.','The functions, integration steps and preceding boundary condition remain unchanged.')

edit('02b-memory-long-delays.md','sec:MEMORY-FIGURES',
r'''In Fig. 1B, an [**activity bump**]{.definition-term custom-style="Definition Term"} is a localized peak of population firing rates across the neurons' preferred angles. Its location has moved away from its initial value $\Theta$ during storage. At the later time, an observer has additional uncertainty about the bump's current location because it sees only a finite sample of spikes. The [information calculation](ch-memory-information.html#sec-memory-fi) measures this second uncertainty and relates it to diffusion; the [readout chapter](ch-memory-readout.html) then follows observation of the moving state.[^p1-fig1]''',
r'''In Fig. 1B, an [**activity bump**]{.definition-term custom-style="Definition Term"} is a localized peak of population firing rates across the neurons' preferred angles. The figure separates two sources of error:

- During storage, the bump's location has moved away from its initial value $\Theta$.
- At the later time, an observer has additional uncertainty about the bump's current location because it sees only a finite sample of spikes.

The [information calculation](ch-memory-information.html#sec-memory-fi) measures this second uncertainty and relates it to diffusion; the [readout chapter](ch-memory-readout.html) then follows observation of the moving state.[^p1-fig1]''',
'list','Make the stored-value change and finite-observation uncertainty separately visible before linking the second to information.','Preserve the activity-bump definition, initial value, finite sample limit and the difference between movement and readout uncertainty.')

edit('02b-memory-long-delays.md','sec:MEMORY-FIGURES',
r'''Panel C compares simulated mean squared angular displacements with the prediction from the tuning curves and transfer function. The gray exponential case and black sigmoidal, or S-shaped, case have different transfer functions. The dashed bound is a lower limit for the sigmoidal case, not a separate fitted trajectory. A model can lie above its information bound while still agree with the derived diffusion formula. Panel D follows angular error to longer intervals; its flattening uses angular wrapping, not a disappearance of noise. The expected limiting value with the caption's error convention is $\pi^2/3$.''',
r'''Panels C and D test different parts of the prediction:

- Panel C compares simulated mean squared angular displacements with the prediction from the tuning curves and transfer function. The gray exponential case and black sigmoidal, or S-shaped, case have different transfer functions. The dashed bound is a lower limit for the sigmoidal case, not a separate fitted trajectory. A model can lie above its information bound while still agreeing with the derived diffusion formula.
- Panel D follows angular error to longer intervals; its flattening uses angular wrapping, not a disappearance of noise. The expected limiting value with the caption's error convention is $\pi^2/3$.''',
'list','Separate the diffusion comparison from the long-delay wrapping test while preserving the interpretation of each plotted line.','Keep transfer-function differences, sigmoidal bound scope, distinction from fitted trajectories, continued noise and the caption-dependent limiting value.')

assessments={
'01-foundations.md':{'retained':'The opening motivates rate representation before spike noise. Tuning notation, Poisson moments and covariance identities remain connected prose because each sentence supplies the next calculation. The conditional-independence qualification remains a paragraph so its present-state condition stays attached to its warning about full spike trains.','rejected':[{'candidate':'Turn the chapter route paragraph into a numbered procedure.','reason':'It is a learning path, not a method the reader performs; numbering would suggest compulsory operational steps.'},{'candidate':'List every fact about rate maps.','reason':'The calculation of a rate map explains why sampling and processing change measured fields. Keeping that causal link in prose is easier to follow.'}]},
'01b-persistence.md':{'retained':'The state, fixed-point and attractor definitions lead directly into the two-activity construction. Equations and their interpretation remain in order. Brownian covariance stays in prose because its dependence argument is sequential. The final map-versus-motion comparison already motivates the different paper models.','rejected':[{'candidate':'Bullet the Brownian motion properties.','reason':'The short definition already fits one sentence and is immediately interpreted; a second assumptions list here would interrupt the derivation.'},{'candidate':'Bullet finite range, periodic coordinate, feedback and variable diffusion.','reason':'These are a brief scope warning rather than four explained cases. The following ring example is the important connection.'}]},
'02-memory-dynamics.md':{'retained':'The chapter follows spike activation, mean dynamics, linearization, surviving projection and diffusion. Left/right vector teaching, the tilted-decay example and symmetric-weight derivation remain prose around intact equations because the reasoning is sequential. No formula, source note or figure changes.','rejected':[{'candidate':'Bullet the mean and variance scaling in the large-population explanation.','reason':'The common scaling explains why noise shrinks while mean dynamics stay fixed; splitting it would obscure that connection.'},{'candidate':'Number the projection derivation.','reason':'Each equation already follows the preceding equality and its explanation; added step labels would not reveal a hidden list.'}]},
'02b-memory-long-delays.md':{'retained':'The line/ring comparison, density equation, variable-diffusion identities and systematic-drift scope remain connected derivations. The drift-convention and correlated-noise paragraphs retain their limits and source distinctions. Figure guidance now exposes the actual comparisons while the closing transition still motivates the information bound.','rejected':[{'candidate':'Turn the Itô/Stratonovich discussion into a short two-item comparison.','reason':'The conversion term and the distinction between an estimated drift scale and exact microscopic drift require the full connected explanation.'},{'candidate':'List each source discrepancy as a warning box.','reason':'The discrepancies belong beside their calculations; moving them would separate the convention from the result being checked.'}]}}
for rec in records:
    name=Path(rec['source_path']).name
    rec['full_chapter_assessment']=assessments[name]['retained']
    rec['possible_but_rejected_edits']=assessments[name]['rejected']
    rec['proposed_sha256']=hashlib.sha256(texts[name].encode('utf-8')).hexdigest()
    output=task/'proposed/content/chapters'/name
    output.parent.mkdir(parents=True,exist_ok=True)
    output.write_bytes(texts[name].encode('utf-8'))
result={'created_at':datetime.datetime.now().astimezone().isoformat(),'task_started_at':'2026-10-24T21:32:54.8366363+03:00','awake_execution':'unverified','writer_model':'GPT-6.1-sol/high','scope':'Four proposed chapter copies only; independent acceptance pending.','chapters':records,'new_glossary_terms':['excitatory input','inhibitory input','encoding'],'meaning_review_notes':['The brief explanation of interspike intervals is added inside the existing CV definition.','The drift wording now says account for systematic drift separately; the worked bias calculation and all limits remain visible.'],'token_stats':'unavailable'}
(task/'changes-foundations-memory.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
for rec in records:
    raw=Path(rec['baseline_path']).read_bytes().decode('utf-8')
    for change in rec['edits']:
        assert raw.count(change['old'])==1
        raw=raw.replace(change['old'],change['new'],1)
    assert raw==texts[Path(rec['source_path']).name]
print(json.dumps({'files':len(records),'edits':sum(len(r['edits']) for r in records),'by_chapter':{Path(r['source_path']).name:len(r['edits']) for r in records},'reconstruction':'passed','finished_at':result['created_at']},indent=2))
