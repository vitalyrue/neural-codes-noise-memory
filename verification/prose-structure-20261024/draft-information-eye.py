from pathlib import Path
import hashlib, json, re
from datetime import datetime

root=Path('C:/dev/clsc/burak-papers/guide')
task=root/'verification/prose-structure-20261024'
names=['03-memory-information.md','03b-memory-readout.md','04-eye-drift.md','04b-eye-timing.md','04c-eye-circuit.md']
original={n:(task/'baseline/content/chapters'/n).read_bytes() for n in names}
texts={n:b.decode('utf-8').replace('\r\n','\n') for n,b in original.items()}
baselines=dict(texts)
changes={n:[] for n in names}
def para(n,prefix):
    found=[p for p in texts[n].split('\n\n') if p.startswith(prefix)]
    assert len(found)==1,(n,prefix,len(found))
    return found[0]
def edit(n,prefix,after,kind,reason,limits):
    before=para(n,prefix)
    if callable(after): after=after(before)
    assert before!=after
    pos=texts[n].index(before)
    prior=texts[n][:pos]
    section=re.findall(r'^## (.+)$',prior,re.M)
    entry={'section':section[-1] if section else 'Chapter opening','paragraph_prefix':prefix,
        'before':before,'after':after,'kind':kind,'rationale':reason,
        'preserved_premise_or_limit':limits,'source_or_meaning_question':None}
    changes[n].append(entry)
    texts[n]=texts[n].replace(before,after,1)

n=names[0]
edit(n,'The volume element contributes',r'''Two factors determine how information changes with tuning width:

- The volume element contributes $w^d$ because broader fields recruit more neurons.
- The squared slope contributes $w^{-2}$ because broader curves change more slowly.

Under these assumptions $J\propto w^{d-2}$. In an equality achieving isotropic exponential network, diffusion in each coordinate consequently scales as $D\propto w^{2-d}$. The resulting comparisons are:

- Narrower curves help in $d=1$.
- Width has no leading effect in $d=2$.
- Broader curves help in $d=3$.''','list','Expose the two parallel factors in the scaling and the three dimensional outcomes, keeping the calculation and conditions before its interpretation.','Fixed peak rate, density and shape remain in the preceding setup; equality achieving, isotropic and exponential conditions remain beside the diffusion claim.')
edit(n,'These conclusions change under another resource constraint.',lambda p:p.replace('Saturating the inequality identifies efficient self tracking for a given information rate; minimizing diffusion still requires deciding how much information the allowed architecture and firing budget can supply.','Attaining equality identifies a network that tracks its own state efficiently for a given information rate. Minimizing diffusion still requires deciding how much information the allowed architecture and firing budget can supply.'),'wording','Explain what self tracking describes and replace the compressed semicolon with the two separate conclusions.','All alternative resource constraints and failure conditions remain; efficient tracking still differs from minimizing diffusion across architectures.')
edit(n,'The matrix statement',lambda p:p.replace('The matrix statement $2D\\succeq\\tau^{-2}J^{-1}$ means','The matrix bound $2D\\succeq\\tau^{-2}J^{-1}$ means'),'wording','Use the direct mathematical name for the inequality.','The order definition, all coordinate directions and matrix construction are unchanged.')
edit(n,'If an external stimulus produces',lambda p:p.replace("This is the paper's reason for suggesting that one circuit could serve both functions.","This is why the paper suggests that one circuit could support both sensory estimation and memory storage."),'wording','State which two functions are connected so the conclusion can be read without recovering them from the previous sentence.','Same sensory and internal tuning, symmetric exponential model and the biological limit remain.')

n=names[1]
edit(n,'The first term comes from storage.',r'''The two terms describe different sources of error:

- $2DT$ comes from storage.
- $V_{\mathrm{read}}(L)$ concerns estimation of $\theta(T)$ from spikes after $T$.

The supplement derives this decomposition for a locally translation invariant diffusion and readout model; state dependence, boundaries, informative priors, or uncertain initial encoding require corresponding changes.[^p1-read-setup]''','list','Make the two parallel error sources easy to compare after the decomposition, with its conditions kept visible.','All four limits and the supplement attribution remain after the list.')
edit(n,'Assume the readout is locally unbiased',lambda p:p.replace('Translation invariance makes the readout variance the same at every $x$','[**Translation invariance**]{.definition-term custom-style="Definition Term"} makes the readout variance the same at every $x$'),'definition','Mark the existing first explanation of the invariance used in this readout model.','The independence, local unbiasedness, zero covariance and constant-variance assumptions remain intact.')
edit(n,'The hyperbolic tangent is',lambda p:p.replace('The hyperbolic tangent is','The [**hyperbolic tangent**]{.definition-term custom-style="Definition Term"} is').replace('Its inverse on $(-1,1)$ is','Its [**inverse hyperbolic tangent**]{.definition-term custom-style="Definition Term"} on $(-1,1)$ is'),'definition','Mark the formulas that first explain the functions needed to solve the precision equation.','Domain, derivative, initial condition and both competing terms of the precision dynamics are retained.')
edit(n,'Here $\\coth z=1/\\tanh z$.',lambda p:p.replace('Here $\\coth z=1/\\tanh z$.','The [**hyperbolic cotangent**]{.definition-term custom-style="Definition Term"} is $\\coth z=1/\\tanh z$.'),'definition','Give the function its name at the existing first explanation.','The reciprocal identity, teaching reconstruction and equivalence to the supplement remain.')
edit(n,'The ideal observer keeps improving,',r'''The ideal observer keeps improving, but the improvement becomes small. Its variance relative to the limiting variance is:

- $1.313$ at $L=L^*$.
- $1.037$ at $2L^*$.
- $1.005$ at $3L^*$.

These are variances, so their ratios are not ratios of standard deviations.''','list','Expose three parallel quantitative comparisons without presenting them as method steps.','Every duration and ratio remains; variance is still distinguished from standard deviation.')
edit(n,'Figure 3 isolates readout uncertainty,',r'''Figure 3 isolates readout uncertainty, rescaling variance by $\sqrt{2D/J}$ and duration by $L^*$. In these axes the ideal curve is $\coth z$ and the naive curve is $z/3+1/z$. Both diverge like $1/z$ at short durations because too few spikes are available. The plotted features are:

- The ideal solid curve approaches one.
- The naive dashed curve reaches $2/\sqrt3$ at $z=\sqrt3$, then rises because its equal weighting gives increasing importance to displaced states.
- The dotted vertical line marks that naive optimum.

The storage delay contribution $2DT$ is not part of these rescaled curves. Figure S2 repeats the comparison for partial access, showing the rightward and upward shifts when $\alpha=0.1$.[^p1-fig3]''','list','Separate the parallel figure features while leaving the scaling and common short-duration behavior in prose.','Exact formulas, optimum, physical cause, omitted storage term and partial-access comparison remain.')
edit(n,'Finally, the short readout interval',lambda p:p.replace('Finally, the short readout interval','The short readout interval'),'wording','Remove a sequence marker that adds no reason for the important distinction between observation duration and integrator lifetime.','Mean retention, growing variance, leak distinction and all requirements for animal comparisons remain.')

n=names[2]
edit(n,'There are three possible contributions',r'''There are three possible contributions to an observed drift:

- A changing shared command sent to many OMNs.
- Private spike variability in individual OMNs.
- Variability after those neurons, including muscle and measurement noise.

Private spike fluctuations can partly cancel when many neurons act together. A common command survives this averaging. This is why the noisy activity of one neuron can reveal a source that dominates the much smoother eye movement.''','list','Show the three candidate sources as parallel alternatives before explaining why averaging affects them differently.','Possible contributions remain possible; partial cancellation and shared survival retain their original strength.')
edit(n,'The large movements have a useful role',lambda p:p.replace('an incorrect [**gain**]{.definition-term custom-style="Definition Term"} during drift','an incorrect gain during drift').replace('Gain is the scale','[**Gain**]{.definition-term custom-style="Definition Term"} is the scale'),'definition','Put blue emphasis on the sentence that explains gain, keeping its earlier mention within the same paragraph.','Calibration transfer remains an assumption; the dependence of inferred common variance on gain remains.')
edit(n,'where $C=\\delta E_C$',r'''where $C=\delta E_C$ is the common upstream contribution, $\eta$ combines motor neuron, muscle, and measurement contributions to measured displacement, and $\epsilon$ is the prediction error from the individual cell. All are displacement variables in degrees. The calculation assumes:

- The common contribution enters both signals with unit gain, meaning the same one-for-one displacement scale.
- $C,\eta,\epsilon$ are pairwise uncorrelated to the required accuracy.''','list','Expose the two distinct assumptions behind the covariance estimate, after defining every variable.','Unit gain, pairwise uncorrelated contributions and required-accuracy qualification are unchanged.')
edit(n,'Expanding the covariance shows exactly',lambda p:p.replace('shows exactly what those assumptions buy','shows why those assumptions matter'),'wording','Replace a trading metaphor with a direct link from the assumptions to the expansion.','The covariance expansion and approximate equality are untouched.')

n=names[3]
edit(n,'The mean squared displacement measures',lambda p:p.replace('The next comparison follows two possible inputs through a decaying muscle response: fluctuations that do not accumulate and a position that wanders by diffusion.','To test whether the command accumulates changes, we compare two possible inputs after a decaying muscle response: fluctuations that do not accumulate and a position that wanders by diffusion.'),'transition','Tie the comparison directly to the unresolved question about accumulation, rather than announcing the next topic.','Measurement-error removal still precedes interpretation; both candidate inputs and the common filter remain.')
edit(n,'At short lags, the displacement can',r'''At short lags, the displacement can be smaller than the search coil's measurement error. Suppose its reading is $E_{\rm obs}(t)=E(t)+\nu(t)$. The measurement error is assumed to have:

- Zero mean and variance $\sigma_m^2$.
- Independence from true movement.
- No correlation between distinct sampled times.

For a positive lag,''','list','Expose the separate error assumptions needed to remove the mixed term and cross-time covariance.','Zero mean, finite variance, independence, distinct sampled times and positive-lag restriction are preserved.')
edit(n,'Now suppose the input is a stored position',lambda p:p.replace('Now suppose the input is a stored position','Filtered white noise cannot explain continued long-lag growth. Suppose instead the input is a stored position'),'transition','Use the plateau result to motivate the alternative accumulating input.','The claim concerns the stable decaying filter just derived; nonzero static gain and the teaching-example limit remain in the paragraph.')

n=names[4]
edit(n,'Doubling $N$ halves this diffusion scale;',r'''At fixed network geometry and under the noise assumptions above, the scale changes as follows:

- Doubling $N$ halves it.
- Doubling CV multiplies it by four.
- Doubling $\tau_s$ divides it by four.
- Doubling the absolute slope at fixed rate also divides it by four.

Increasing rate reduces diffusion when the fractional slope is fixed, because more spikes then also supply a proportionally steeper absolute slope. Increasing rate at fixed absolute slope is a different comparison and increases the scale in the first formula. A rate change alone does not specify which comparison is intended.''','list','Make the four parallel parameter comparisons visible while retaining the different rate constraints in connected prose.','The controlled geometry and noise assumptions are repeated locally; fixed-rate slope and fixed-fractional-slope rate comparisons remain distinct.')
edit(n,'The data and model answer different localization questions.',r'''The data and model answer different questions about where the drive originates:

- The common variance estimate supports a drive upstream of OMNs, given the calibration and noise assumptions.
- The MSD comparison supports a command that accumulates variation over the measured interval, rather than stationary white noise passed through a decaying muscle filter.
- The circuit model shows that integrator noise with plausible parameters can generate such a command and explain its filtered amplitude and timing.''','list','Separate the three kinds of evidence so the model demonstration cannot be mistaken for direct recording-based localization.','Calibration and noise assumptions, measured interval, white-noise comparator, and possible model explanation all remain.')
edit(n,'Those results do not uniquely locate',r'''Those results do not uniquely locate the noise inside integrator neurons. Two missing tests limit that conclusion:

- No integrator neurons were recorded in this study.
- No selective change of that circuit tested whether it was necessary for drift.

Noisy inputs to the integrator, or an already diffusive upstream signal, remain possible. The authors make this distinction in the Discussion and explicitly in their peer review response. Several combinations of neuron count, variability, and synaptic time constant can also fit an amplitude, so matching one curve does not uniquely recover those parameters.[^p2-localization]''','list','Expose the two separate gaps in direct circuit evidence, then retain alternative sources and parameter uncertainty as their consequences.','Neither lack of recordings nor lack of intervention is treated as disproof; both upstream alternatives and all parameter ambiguity remain.')

assessments={
 names[0]:'Retained the likelihood-to-score derivation, Cramer Rao argument, projection inequality, equality qualification, numerical examples and all folds. Lists clarify two scaling factors and three dimensional outcomes; population, firing-rate and time-constant comparisons remain separate causal paragraphs.',
 names[1]:'Retained the storage/readout covariance argument, Gaussian approximation limits, equal-weight double integral, backward precision recursion, partial-access calculation, two-time-constant matrix and printed-bound caution. Lists expose parallel error terms, saturation values and figure features; derivations stay connected.',
 names[2]:'Retained the physical pathway, recording design, calibration and inverse-filter derivation, independent-noise bound and common-fraction estimate. Lists identify candidate sources and necessary covariance assumptions; gain emphasis moves to its actual explanation.',
 names[3]:'Retained the measurement-noise subtraction, white-input covariance argument and full filtered Brownian derivation. The assumptions become visible before the calculation, and the plateau result motivates the accumulating-input alternative.',
 names[4]:'Retained all circuit, plant and feedback equations, recurrence and near-neutrality conditions, CV construction, dimensional scaling caution and measured-CV check. Lists compare parameters and distinguish inference, model demonstration and missing direct evidence.'}
rejected={
 names[0]:['Do not bullet the Cramer Rao proof or equality derivation: each sentence supplies the premise needed by the next calculation.','Do not remove the folded linear-family counterexample: it preserves a necessary limit on the source converse.'],
 names[1]:['Do not turn the backward precision recursion into an isolated numbered recipe: its equations and surrounding reasoning teach why each step works.','Do not shorten the printed-bound caution: direction of the inequality and saturation condition are essential.'],
 names[2]:['Do not shorten the one-neuron-at-a-time limitation: it limits every later shared-source inference.','Do not list every chronological sample-processing detail: the existing connected paragraph explains one data-selection process and retains all numbers.'],
 names[3]:['Do not replace technical stationary process or white noise with approximate everyday synonyms: the precise assumptions explain the plateau.','Do not move nonzero static gain to a fold: it is needed for continued displacement growth.'],
 names[4]:['Do not list the circuit equations as independent components without their causal links: recurrence and muscle filtering depend on their sequence.','Do not combine absolute and fractional slope comparisons: their rate dependence differs.']}
out=task/'proposed/content/chapters';out.mkdir(parents=True,exist_ok=True)
records=[]
for n in names:
    reconstructed=baselines[n]
    for i,e in enumerate(changes[n],1):
        assert reconstructed.count(e['before'])==1
        e['edit_order']=i
        # Locate in frozen baseline where possible, also retaining the exact sequential patch.
        e['baseline_line']=baselines[n][:baselines[n].find(e['before'])].count('\n')+1 if e['before'] in baselines[n] else None
        reconstructed=reconstructed.replace(e['before'],e['after'],1)
    assert reconstructed==texts[n]
    newline='\r\n' if b'\r\n' in original[n] else '\n'
    output=texts[n].replace('\n',newline).encode('utf-8')
    (out/n).write_bytes(output)
    records.append({'source_path':str(root/'content/chapters'/n),'baseline_path':str(task/'baseline/content/chapters'/n),'baseline_sha256':hashlib.sha256(original[n]).hexdigest(),'proposed_sha256':hashlib.sha256(output).hexdigest(),'newline':repr(newline),'edits':changes[n],'full_chapter_assessment':assessments[n],'possible_but_rejected_edits':rejected[n]})
ledger={'created_at':datetime.now().astimezone().isoformat(),'group':'information-eye','model':'GPT-6.1-sol/high','task_wall_start':'2026-10-24T21:32:54.8366363+03:00','awake_execution':'unverified','reconstruction':'Decode original UTF-8 baseline, normalize CRLF to LF, apply each exact before/after once in edit_order, restore recorded newline; no other changes.','new_glossary_candidates':[{'term':'translation invariance','meaning':'In this readout model, the readout variance is the same at every cue state x.','location':'03b-memory-readout.md, sec:MEMORY-READOUT-SETUP','note':'Existing explanation newly emphasized; keep distinct from spatial stationarity.'},{'term':'hyperbolic tangent, inverse hyperbolic tangent, hyperbolic cotangent','meaning':'Definitions by the displayed exponential, logarithmic and reciprocal formulas in the ideal readout derivation.','location':'03b-memory-readout.md, sec:MEMORY-IDEAL','note':'Existing formulas newly emphasized; these function names can share one short lookup entry.'}],'files':records,'token_stats':'unavailable'}
(task/'changes-information-eye.json').write_text(json.dumps(ledger,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'chapters':len(names),'edits':sum(map(len,changes.values())),'counts':{n:len(v) for n,v in changes.items()},'created_at':ledger['created_at']}))
