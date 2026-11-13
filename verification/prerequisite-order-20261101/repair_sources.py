from pathlib import Path
from datetime import datetime, timezone
import hashlib, json

ROOT=Path(__file__).resolve().parents[2]
TASK=Path(__file__).resolve().parent
changes=[]

def edit(name,old,new,reason):
    changes.append({'file':'content/chapters/'+name,'old':old,'new':new,'reason':reason})

# Brownian meaning belongs on the main reading path; the step calculation stays folded.
name='01b-persistence.md'
old=r'''Writing $t=n\Delta t$ gives linear variance growth $2Dt$. [To describe this limit with a continuous path, use [**Brownian motion**]{.definition-term custom-style="Definition Term"} $W(t)$. It starts at zero, has continuous paths and independent Gaussian increments with mean zero, and satisfies $\operatorname{Var}[W(t)-W(s)]=t-s$ for $t\geq s$.]{.definition-explanation} It describes the limit of many small, suitably independent fluctuations. A physical network need only approach this description over the time and noise scales relevant to the calculation.'''
edit(name,old,r'''Writing $t=n\Delta t$ gives linear variance growth $2Dt$. The continuous approximation expresses this accumulated change through Brownian motion.''','Move the needed process meaning out of the optional derivation; retain the variance calculation.')
old='::: {.publisher-clarification-note .publisher-fold-always title="Mathematical model: independent steps and Brownian motion"}'
new=r'''[**Brownian motion**]{.definition-term custom-style="Definition Term"} [$W(t)$ models the accumulated effect of many small fluctuations. It starts at zero, has continuous paths and independent Gaussian increments with mean zero, and satisfies $\operatorname{Var}[W(t)-W(s)]=t-s$ for $t\geq s$.]{.definition-explanation} The independence concerns changes over disjoint time intervals. A physical network need only approach this description over the time and noise scales relevant to the calculation.

'''+old
edit(name,old,new,'Make Brownian paths and their increment scale available before later stochastic equations.')

name='02-memory-dynamics.md'
edit(name,'Conditioned on the present rates, spike counts over a short interval $dt$ are independent Poisson variables. Thus',r'Conditioned on the present rates, spike counts over a short interval $dt$ are independent Poisson variables. Let $\delta_{ij}$ be one when $i=j$ and zero otherwise. Thus','Introduce the index-matching symbol before the count-covariance equation.')
edit(name,r'The symbol $\delta_{ij}$ is one when $i=j$ and zero otherwise. Splitting the count into its mean and fluctuation gives',r'Write $dM_i=dN_i-r_i\,dt$ for the spike count minus its conditional mean: the surplus or deficit of spikes in this interval. Splitting the count into its mean and this fluctuation gives','Define the centered count rather than asking the reader to infer it from moment conditions.')
old=r'''ds_i=F_i(\mathbf s)dt+\sqrt{r_i}\,dB_i,
\qquad
F_i(\mathbf s)=-s_i/\tau+\phi\!\left(\sum_jW_{ij}s_j+b_i\right),'''
# Add a lead-in immediately before this existing display, retaining its algebra.
needle='$$\n'+old
new=r'''Let $F_i(\mathbf s)$ be the mean rate of change of neuron $i$'s activation. Let $B_i$ be independent standard [Brownian motions](ch-persistence.html#sec-foundations-diffusion). The increment $dB_i=B_i(t+dt)-B_i(t)$ has mean zero and variance $dt$. Multiplying it by $\sqrt{r_i}$ gives the same leading variance $r_i\,dt$ as the centered spike count. The stochastic equation is

$$
'''+old
edit(name,needle,new,'Explain what changes, the Brownian increment and its noise scale before the first stochastic equation.')
edit(name,'where the $B_i$ are independent standard Brownian processes. The noise coefficient has units','The noise coefficient has units','Remove the now-redundant post-equation introduction.')
edit(name,r'The constant terms cancel because $\bar{\mathbf s}$ is a fixed point. Therefore',r'The constant terms cancel because $\bar{\mathbf s}$ is a fixed point. Let $K$ be the linear response matrix: $K\delta\mathbf s$ is the mean rate of change of the activation disturbance. Let $R$ be the diagonal matrix of spike-count variance rates, evaluated at that fixed point. Then','State the physical roles of K and R before their matrix equation.')
edit(name,r'[We also need a [**left zero eigenvector**]{.definition-term custom-style="Definition Term"}, a vector $\mathbf v$ satisfying]{.definition-explanation}',r'[To extract the lasting memory displacement from a general perturbation, we need a [**left zero eigenvector**]{.definition-term custom-style="Definition Term"}, a vector $\mathbf v$ satisfying]{.definition-explanation}','Place the existing purpose of v before its defining equations.')
edit(name,'Its purpose is to extract the lasting memory displacement from a general perturbation. The normalization makes','The normalization makes','The purpose has moved to the introduction; retain the normalization argument.')

name='03-memory-information.md'
old='::: {.publisher-clarification-note .publisher-fold-always title="Derivation: likelihood, score, and Fisher information"}'
new=r'''To compare possible angles, hold the observed spike counts fixed and vary the proposed $\theta$. [A [**likelihood**]{.definition-term custom-style="Definition Term"} compares proposed parameter values by the probability each assigns to those observations.]{.definition-explanation} It is not, by itself, a probability distribution over the proposed angles.

'''+old
edit(name,old,new,'Make likelihood meaning available before later main-text Gaussian readout; keep score algebra folded.')
old=r'''Here the parameter being estimated is $\theta$ during the short observation. [A [**likelihood**]{.definition-term custom-style="Definition Term"} compares proposed parameter values by the probability each assigns to the observations already obtained.]{.definition-explanation} Suppose four spikes were recorded. A candidate angle predicting four spikes on average and one predicting sixteen assign different probabilities to that same count. Evaluating those probabilities as the proposed angle changes gives the likelihood. It is not, by itself, a probability distribution over the proposed angles.'''
new=r'''Suppose four spikes were recorded during the short observation. A candidate angle predicting four spikes on average and one predicting sixteen assign different probabilities to that same count. Evaluating those probabilities as the proposed angle changes gives the likelihood.'''
edit(name,old,new,'Retain the concrete count comparison in the derivation after moving its general definition.')

name='03b-memory-readout.md'
old=r'''To solve the readout problem, the supplement approximates the likelihood from each short bin of duration $h$ as Gaussian. Let $x=\theta(T)$ and index subsequent bins by $k$. The equivalent observation model is'''
new=r'''To solve the readout problem, the supplement approximates the [likelihood](ch-memory-information.html#sec-memory-fi) from each short bin of duration $h$ as Gaussian. Let $x=\theta(T)$ and index subsequent bins by $k$, starting with $\theta_0=x$. The increment $\eta_k$ is the change in the stored value between bins. The observation $y_k$ summarizes the bin's population spikes as an estimate of $\theta_k$, and $\epsilon_k$ is its estimation error. In this approximation, these increments and errors are independent, zero-mean Gaussian variables. The equivalent observation model is'''
edit(name,old,new,'Name the state change and readout error before they enter the bin equations.')
old="The Gaussian increments and observation errors are independent in this approximation. The value $y_k$ summarizes information about the state from that bin's population spikes. It is not an additional directly measured physical coordinate."
edit(name,old,'The value $y_k$ is inferred from spikes, not an additional directly measured physical coordinate.','Retain the measurement distinction without repeating the moved variable roles.')
formula=r'''$$
\boxed{V_{\mathrm{ideal}}(L)
=\sqrt{\frac{2D}{J}}\coth(\sqrt{2DJ}\,L).}
$$'''
edit(name,formula,'Taking the reciprocal of $P(L)$ gives the displayed finite-time readout variance.','Move the result before the optional integration details.')
old='::: {.publisher-clarification-note .publisher-fold-always title="Mathematical solution: hyperbolic functions and finite-time readout error"}'
new=r'''The solution gives the readout variance at any observation duration $L>0$:

'''+formula+r'''

[The [**hyperbolic cotangent**]{.definition-term custom-style="Definition Term"} is $\coth z=(e^{2z}+1)/(e^{2z}-1)$.]{.definition-explanation} For positive $z$, it falls from large values toward one. This function describes how the extra error from limited observation decreases toward the diffusion-limited value.

'''+old
edit(name,old,new,'Expose the finite-time result and function meaning before numerical ratios and figure interpretation.')
edit(name,r'[The [**hyperbolic cotangent**]{.definition-term custom-style="Definition Term"} is $\coth z=1/\tanh z$.]{.definition-explanation} This backward precision derivation',r'The identity $\coth z=1/\tanh z$ connects this result to the finite-time variance. This backward precision derivation','Keep the proof identity, with the main definition now before use.')
old=r'''In the basic model, the firing rate changes immediately when the summed input changes. Assume symmetric weights. The extension instead lets $r_i$ approach $\phi(g_i)$ gradually, with time constant $\tau_m$, while synaptic activation still decays with time constant $\tau$:'''
new=r'''In the basic model, the firing rate changes immediately when the summed input changes. Assume symmetric weights. The extension instead lets $r_i$ approach $\phi(g_i)$ gradually, with time constant $\tau_m$, while synaptic activation still decays with time constant $\tau$.

The symbol $\xi_i$ writes the spike fluctuation as a drive in a rate-of-change equation. [[**White noise**]{.definition-term custom-style="Definition Term"} is an ideal zero-mean input whose fluctuations at different times are uncorrelated. Its continuous-time strength is defined through a delta-function covariance, rather than a finite variance at an individual time.]{.definition-explanation} In the Gaussian approximation used here, $\xi_i\,dt=\sqrt{r_i}\,dB_i$, with independent Brownian increments $dB_i$. Conditional on the current rates, its contribution over $dt$ has variance $r_i\,dt$, the same spike-count variance as in the basic model. The two dynamical equations are'''
edit(name,old,new,'Teach the white-noise notation as the same already-taught random increment before using xi in a derivative equation.')
edit(name,"Here $\\xi_i$ is the zero mean noise from variable spike generation, with the same Poisson strength as in the basic model.\n\n",'','Replace the vague strength reminder with the explicit preceding increment bridge.')
edit(name,r'Figure 3 isolates readout uncertainty, rescaling variance by $\sqrt{2D/J}$ and duration by $L^*$. In these axes the ideal curve is $\coth z$',r'Figure 3 isolates readout uncertainty, rescaling variance by $\sqrt{2D/J}$ and duration by $L^*$. Write $z=L/L^*=\sqrt{2DJ}\,L$ for this dimensionless observation duration. In these axes the ideal curve is $\coth z$','Define the figure coordinate z before using it in its curves.')

name='04b-eye-timing.md'
old=r'''[[**White noise**]{.definition-term custom-style="Definition Term"} here is an ideal zero mean input whose fluctuations at different times are uncorrelated. In continuous time its strength is defined by an intensity multiplying a delta function, rather than a finite variance at an individual time.]{.definition-explanation}'''
new=r'''The input is idealized as [white noise](ch-memory-readout.html#sec-memory-extensions), so fluctuations at unequal times are uncorrelated.'''
edit(name,old,new,'Keep a local reminder and link after moving the first white-noise definition to the earlier dependent model.')

name='05-place-fields.md'
old=r'''The model assigns an input $h(x)$ to each position $x$, with nearby values linked so that a cell can have a continuous active region. [A [**Gaussian process**]{.definition-term custom-style="Definition Term"} specifies a distribution of such maps.]{.definition-explanation} Its mean sets the average input, and its spatial covariance describes how inputs at two positions vary together across possible maps. The chosen covariance must also make the maps smooth enough for the derivatives used below. After a map is drawn, moving the animal changes which position is evaluated, not the map itself.'''
new=r'''The model assigns an input $h(x)$ to each position $x$, with nearby values linked so that a cell can have a continuous active region. [A [**Gaussian process**]{.definition-term custom-style="Definition Term"} specifies a distribution of maps such that the values at any finite set of positions form a jointly Gaussian random vector.]{.definition-explanation} [A [**jointly Gaussian vector**]{.definition-term custom-style="Definition Term"} is one for which every linear combination of its entries is Gaussian.]{.definition-explanation} This joint rule constrains how inputs at different positions can vary together, beyond requiring a Gaussian histogram at each position.

The mean sets the average input, and the spatial covariance describes how inputs at two positions vary together across possible maps. These functions determine the joint Gaussian laws. The chosen covariance must also make the maps smooth enough for the derivatives used below. After a map is drawn, moving the animal changes which position is evaluated, not the map itself.'''
edit(name,old,new,'Put the defining joint-Gaussian property on the main reading path before the crossing calculation uses it.')
old=r'''[A Gaussian process is a probability distribution over functions such that the values at any finite set of positions form a jointly Gaussian random vector.]{.definition-explanation} For positions $x_1,\ldots,x_n$, the vector $(h(x_1),\ldots,h(x_n))$ therefore has a multivariate Gaussian distribution. Its mean vector and covariance matrix are obtained by evaluating two functions,'''
new=r'''For chosen positions $x_1,\ldots,x_n$, the input vector is $(h(x_1),\ldots,h(x_n))$. Its mean vector and covariance matrix are obtained by evaluating two functions,'''
edit(name,old,new,'The optional fold now gives notation for the property already explained in visible text.')
old=r'''The expectation runs over possible maps, or over cells assumed to share these statistics. These two functions determine every finite joint distribution. A Gaussian process can thus produce many different curves while keeping a precise rule for their spatial dependence. [A [**jointly Gaussian vector**]{.definition-term custom-style="Definition Term"} is one for which every linear combination of its entries is Gaussian.]{.definition-explanation} For this family, zero covariance between two subvectors implies their independence.'''
new=r'''The expectation runs over possible maps, or over cells assumed to share these statistics. For jointly Gaussian vectors, zero covariance between two subvectors implies their independence.'''
edit(name,old,new,'Remove duplicate definitions after moving them, retaining the special independence property and its limits.')

name='12-simulating-eye-drift.md'
old='::: {.publisher-clarification-note .publisher-fold-always title="Published parameters and public-code settings have different sources"}'
new=r'''Simulating the random events requires a rule for generating repeatable sample sequences. A [[**random seed**]{.definition-term custom-style="Definition Term"} fixes the starting state of a pseudorandom generator so that a specified implementation can repeat its sample sequence.]{.definition-explanation} The seed controls which sequence is drawn; it does not set the intended firing-rate distribution. The code uses a trajectory index to choose that starting state.

'''+old
edit(name,old,new,'Move the seed purpose before its concrete MATLAB setting and later reproduction instructions.')

name='14-simulation-tools.md'
old=r'''NumPy's `Generator` supplies random samples for a Python implementation. A [[**random seed**]{.definition-term custom-style="Definition Term"} fixes the starting state of a pseudorandom generator so that a specified implementation can repeat its sample sequence.]{.definition-explanation} Record the generator, software versions, and order of calls as well as the seed.'''
new=r'''NumPy's `Generator` supplies random samples for a Python implementation. To repeat a sequence using a [random seed](ch-simulating-eye.html#sec-simulating-eye-path), record the generator, software versions, and order of calls as well as the seed.'''
edit(name,old,new,'Retain practical reproducibility cautions and link back to the now-earlier seed explanation.')

# Store exact proposed edits before applying them. Each replacement is one inspected passage.
(TASK/'planned-edits.json').write_text(json.dumps(changes,indent=2),encoding='utf-8')
sources={}
for change in changes:
    relative=change['file']
    text=sources.get(relative,(ROOT/relative).read_text(encoding='utf-8'))
    count=text.count(change['old'])
    assert count==1,(relative,change['old'][:90],count)
    sources[relative]=text.replace(change['old'],change['new'],1)
hashes={}
for relative,text in sources.items():
    path=ROOT/relative
    assert '\t' not in text and '\x08' not in text and '\x0c' not in text
    before=hashlib.sha256(path.read_bytes()).hexdigest()
    path.write_text(text,encoding='utf-8',newline='\n')
    hashes[relative]={'before':before,'after':hashlib.sha256(path.read_bytes()).hexdigest()}
(TASK/'repair-hashes.json').write_text(json.dumps(hashes,indent=2),encoding='utf-8')
state=json.loads((TASK/'STATE.json').read_text(encoding='utf-8'))
state['checkpoint_at_utc']=datetime.now(timezone.utc).isoformat();state['status']='first repair draft complete; independent correctness review next'
state['edits']=len(changes);state['changed_reader_files']=list(sources)
(TASK/'STATE.json').write_text(json.dumps(state,indent=2),encoding='utf-8')
print(f'Applied {len(changes)} exact passage edits in {len(sources)} reader files; optional proofs remain folded.')
