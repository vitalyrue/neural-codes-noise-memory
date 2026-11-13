from pathlib import Path
import re, json, csv, yaml
ROOT=Path(__file__).resolve().parents[2]
p1=ROOT/'content/chapters/01-foundations.md';p3=ROOT/'content/chapters/02-memory-dynamics.md'
a=p1.read_text(encoding='utf-8');b=p3.read_text(encoding='utf-8')
assert 'sec:MEMORY-SPIKES' not in a
section=b.index('## Recurrent spikes renew decaying synaptic activity')
noise=b.index('<!-- vale ai-tells.FormalTransitions = NO -->\nConditioned on the present rates',section)
model=b[section:noise]
syn_start=a.index('[Neurons affect one another through connections')
syn_end=a.index('[A [**tuning curve**]',syn_start)
synapses=a[syn_start:syn_end]
a=a[:syn_start]+a[syn_end:]
old_assumptions='The model assumes fixed connection weights, constant biases, a common synaptic decay time, and independent Poisson spike counts conditional on the present rates. The connections are tuned to a continuous family of steady patterns. The Gaussian description below also assumes weak fluctuations in total input.'
model=model.replace(old_assumptions,synapses.rstrip()+'\n\nBurak and Fiete (2012) use the following equations for interactions inside a neural circuit. These describe synaptic activity; muscle motion is a later part of the pathway. The model assumes fixed connection weights, constant input biases and a common synaptic decay time. Its statistical rule for spike timing is explained in the [spike-count section](#sec-foundations-poisson).')
old_derivation="**Mathematical derivation.** To combine discrete events with continuous decay, a count process records the events and a decay equation records how their effects fade. Here $N_i(t)$ counts neuron $i$'s spikes up to time $t$. The activation $s_i$ tracks the decaying synaptic effect of those outgoing spikes on receiving cells. It rises by one at each spike and otherwise decays:"
new_derivation=r'''**Model dynamics: Burak and Fiete (2012), Equation 7.** [The [**synaptic activation**]{.definition-term custom-style="Definition Term"} $s_i$ tracks the decaying effect of neuron $i$'s outgoing spikes on receiving cells.]{.definition-explanation} The paper writes its dynamics as

$$
\dot s_i+\frac{s_i}{\tau}=\sum_\alpha\delta(t-t_i^\alpha).
$$

The dot means $\dot s_i=ds_i/dt$, and $\tau$ is the decay time in seconds. [The [**Dirac delta**]{.definition-term custom-style="Definition Term"} $\delta(t-t_i^\alpha)$ represents an instantaneous unit pulse at the spike time $t_i^\alpha$; its integral across that time is one.]{.definition-explanation} Between spikes, the right-hand side is zero and activation decays. Integrating through one spike gives a one-unit increase in $s_i$. [Read Eq. 7 as a balance: spikes add activation, while the term $s_i/\tau$ removes it.]{.key-statement} [Original Eq. 7, PDF p. 5](../papers/burak-fiete-2012-persistent-activity.pdf#page=5).

**Equivalent count form.** Let $N_i(t)$ count neuron $i$'s spikes up to time $t$. Integrating the pulse train counts the spikes, so the same dynamics can be written as'''
assert old_derivation in model;model=model.replace(old_derivation,new_derivation)
old_input='The rate $r_i$ has units of spikes per second. The summed input and the firing rule are\n\n$$\ng_i=\\sum_j W_{ij}s_j+b_i,\n\\qquad r_i=\\phi(g_i).\n$$'
new_input=r'''**From activation to new spikes: Equations 8 and 9.** The total input to neuron $i$ combines the activation arriving from other cells with a constant input bias:

$$
g_i=\sum_jW_{ij}s_j+b_i.\qquad\text{(Burak and Fiete, Eq. 8)}
$$

The expected firing rate then follows from that input:

$$
r_i=\phi(g_i).\qquad\text{(Burak and Fiete, Eq. 9)}
$$

Here $r_i$ has units of spikes per second. These equations specify how the input sets the rate; they do not prescribe each spike's time.'''
assert old_input in model;model=model.replace(old_input,new_input)
model += 'Together, Eqs. 7–9 describe one feedback cycle: spikes change synaptic activation, weighted activation changes input, and input changes the rate of new spikes. The next question is how the resulting pattern of rates can represent an eye angle or location.\n\n'
a=a.replace('## Patterns of firing rates represent a value {#sec:FOUNDATIONS-SPIKES}',model+'## Patterns of firing rates represent a value {#sec:FOUNDATIONS-SPIKES}',1)
a=a.replace('The next question is how activity across a group of neurons represents the angle to be held.','So far we have followed the output from motor neurons to muscles. The next step is a model of how neurons act on one another and sustain a signal.',1)
a=a.replace("We then ask how firing rates across a group of neurons represent that angle or an animal's location.","We next establish the equations that connect spikes, synaptic input and firing rate. With that physical meaning in place, we ask how a pattern of rates represents an angle or an animal's location.",1)
a=a.replace('$r_i(\\theta)=b_i+k_i\\theta$','$r_i(\\theta)=r_{i,0}+k_i\\theta$',1).replace('baseline rate $b_i$ in spikes per second','baseline rate $r_{i,0}$ in spikes per second',1)
a=a.replace('The linear expression can describe an active range,','This rate baseline is different from the input bias $b_i$ in Eq. 8. The linear expression can describe an active range,',1)
model_note=re.search(r'^\[\^p1-model\]:.*$',b,re.M).group(0)
a=a.rstrip()+'\n\n'+model_note+'\n'
# Attach a source citation to the model introduction as well as direct equation links.
a=a.replace('Its statistical rule for spike timing is explained in the [spike-count section](#sec-foundations-poisson).','Its statistical rule for spike timing is explained in the [spike-count section](#sec-foundations-poisson).[^p1-model]',1)
new_start=r'''## Many weak inputs allow a continuous approximation to spike noise {#sec:MEMORY-WEAK-NOISE}

**Neural mechanism.** [Chapter 1 established the spike, activation and firing-rate model, Eqs. 7–9](ch-foundations.html#sec-memory-spikes). Here we calculate its fluctuations. The connections are tuned to a continuous family of steady patterns, and the Gaussian approximation assumes small fluctuations in each neuron's total input.

**Mathematical derivation.** We start from $ds_i=-s_i\,dt/\tau+dN_i$. The elementary spike-generation noise is independent across neurons conditional on the present rates.

'''
b=b[:section]+new_start+b[noise:]
b=b.replace('To calculate the loss of accuracy, we first describe how spikes renew synaptic activity as it decays.','Starting from the neural dynamics established in Chapter 1, we first express the random spike input as continuous noise under the paper\'s weak-fluctuation assumptions.',1)
b=b.replace('[connection weights](#sec-memory-spikes)','[connection weights](ch-foundations.html#sec-memory-spikes)',1)
p1.write_text(a,encoding='utf-8');p3.write_text(b,encoding='utf-8')

y1=ROOT/'content/chapters/01-foundations.yaml';y3=ROOT/'content/chapters/02-memory-dynamics.yaml'
d1=yaml.safe_load(y1.read_text(encoding='utf-8'));d3=yaml.safe_load(y3.read_text(encoding='utf-8'))
old=d3['section_list'].pop(0);old['summary']='Burak and Fiete (2012), Eqs. 7–9, define how spikes renew a decaying activation, weighted activations set neural input, and input sets the rate of new spikes. This model precedes coding, noise and stability calculations.';d1['section_list'].insert(1,old)
d3['section_list'].insert(0,{'id':'sec:MEMORY-WEAK-NOISE','title':'Many weak inputs allow a continuous approximation to spike noise','summary':'Starting from the model taught in Chapter 1, conditional Poisson counts yield a mean input and a fluctuation. Small input fluctuations permit a continuous Gaussian approximation and define the deterministic steady states.','level':2})
trace=next(x for x in d3['blocks'] if x['id']=='fig:MEMORY-SPIKE-TRACE');d3['blocks'].remove(trace);d1['blocks'].insert(0,trace)
trace['caption']=trace['caption'].replace('the chapter equation','Burak and Fiete (2012), Eq. 7')
d1['purpose']='Start from eye muscles and neural spikes, establish the dynamical model in Burak and Fiete (2012), Eqs. 7–9, then explain coding and variable spike counts. These foundations precede the stability and diffusion arguments.'
d1['section_list'][2]['summary']='Tuning curves relate expected firing rates to an eye angle or location. A population code represents the value across neurons; the rate baseline is distinguished from the model input bias.'
d3['purpose']='Starting from the neural model in Chapter 1, derive the weak-fluctuation approximation and follow small disturbances through the circuit to calculate diffusion of a stored value.'
d3['pedagogical_prerequisites']=['ch:FOUNDATIONS','ch:PERSISTENCE']
d3['section_list'][-1]['summary']='The connection matrix W contains the weights from neuron j to neuron i. Equal weights in opposite directions allow the projection vector to be expressed through tuning curves under the stated assumptions.'
y1.write_text(yaml.safe_dump(d1,allow_unicode=True,sort_keys=False,width=100),encoding='utf-8');y3.write_text(yaml.safe_dump(d3,allow_unicode=True,sort_keys=False,width=100),encoding='utf-8')

changed_links=[]
for p in (ROOT/'content/chapters').glob('*.md'):
 text=p.read_text(encoding='utf-8')
 if 'ch-memory-dynamics.html#sec-memory-spikes' in text:
  backup=ROOT/'verification/foundation-dynamics-20261101/baseline'/p.relative_to(ROOT);backup.parent.mkdir(parents=True,exist_ok=True)
  if not backup.exists():backup.write_text(text,encoding='utf-8')
  p.write_text(text.replace('ch-memory-dynamics.html#sec-memory-spikes','ch-foundations.html#sec-memory-spikes'),encoding='utf-8');changed_links.append(p.name)
p=ROOT/'source-maps/chapter-redirects.json';routes=json.loads(p.read_text());routes['ch-memory-dynamics.html'].update({'sec-memory-spikes':'ch-foundations.html','fig-memory-spike-trace':'ch-foundations.html'});p.write_text(json.dumps(routes,indent=2)+'\n',encoding='utf-8')
p=ROOT/'content/chapters/glossary.md';text=p.read_text(encoding='utf-8')
terms={'Dirac delta':'An ideal unit impulse. Its integral over an interval containing the event time is one; in Eq. 7 it represents a spike that adds one activation unit.','synaptic activation':'In the 2012 model, the decaying trace of a neuron\'s outgoing spikes. Each spike adds one unit; connection weights convert this trace into input to other cells.'}
for term,meaning in terms.items():
 if re.search(r'\*\*'+re.escape(term)+r':\*\*',text,re.I):continue
 entry=f'- [[**{term}:**]{{.definition-term custom-style="Definition Term"}} {meaning}]{{.definition-explanation}}\n'
 matches=list(re.finditer(r'^- \[\[\*\*([^:]+):\*\*',text,re.M));position=next((m.start() for m in matches if m[1].lower()>term.lower()),len(text));text=text[:position]+entry+text[position:]
p.write_text(text,encoding='utf-8')
print('Moved Eqs7–9 and the existing trace figure. Updated links:',changed_links)
