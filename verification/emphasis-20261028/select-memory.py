from pathlib import Path
import re, json, hashlib

base=Path('C:/dev/clsc/burak-papers/guide')
names=['01-foundations.md','01b-persistence.md','02-memory-dynamics.md','02b-memory-long-delays.md','03-memory-information.md','03b-memory-readout.md']
files=[]
for name in names:
    p=base/'content/chapters'/name
    raw=p.read_bytes(); text=raw.decode('utf-8'); selections=[]; coverage=[]
    files.append(dict(file=name,sha256=hashlib.sha256(raw).hexdigest(),selections=selections,definitionCoverage=coverage))

def add(i,kind,start,end=None,reason='Central local problem or result'):
    text=(base/'content/chapters'/names[i]).read_bytes().decode('utf-8')
    a=text.index(start)
    b=a+len(start) if end is None else text.index(end,a)+len(end)
    chosen=text[a:b]
    assert text.count(chosen)==1,(names[i],chosen)
    assert '\n\n' not in chosen.replace('\r\n','\n'),chosen
    for s in files[i]['selections']:
        c=text.index(s['text']);d=c+len(s['text'])
        assert b<=c or a>=d,(chosen,s['text'])
    heads=list(re.finditer(r'^#+ .*\{#([^}]+)\}',text[:a],re.M))
    files[i]['selections'].append(dict(kind=kind,text=chosen,section=heads[-1].group(1),reason=reason))
    return chosen

def d(i,terms,start,end=None,limited=False):
    chosen=add(i,'definition',start,end,'Existing first definition, including its meaning' if not limited else 'Definition lead; mathematical definition continues in following display')
    for term in terms.split('|'):
        assert '[**'+term+'**]{.definition-term' in chosen,term
        files[i]['definitionCoverage'].append(dict(term=term,status='term-only' if limited else 'covered',reason='Mathematical meaning continues in following display' if limited else 'Defining clause or sentence selected'))

d(0,'spike','A neuron communicates','Definition Term"}s.')
d(0,'firing rate','A [**firing rate**]','per unit time.')
d(0,'synapse','Neurons affect one another','Definition Term"}s.')
d(0,'excitatory input','An [**excitatory input**]','tendency to fire.')
d(0,'inhibitory input','An [**inhibitory input**]','reduces it.')
d(0,'recurrent connectivity','When neurons send signals back','Definition Term"}.')
d(0,'tuning curve','A [**tuning curve**]','a represented variable.')
d(0,'population code','is a [**population code**]','information about $\\theta$.')
d(0,'decoding','Reading a value from observed spikes','Definition Term"}.')
d(0,'encoding','Establishing a population pattern','Definition Term"}.')
d(0,'rate map','A [**rate map**]','the time spent there.')
d(0,'grid cell','A [**grid cell**]','in a two-dimensional arena.')
d(0,'Poisson process','The 2012 model describes this variability','of length $\\Delta t$ obeys',True)
d(0,'coefficient of variation','The [**coefficient of variation**]','divided by their mean.')
d(0,'Fano factor','The count variance divided','Definition Term"}')
d(0,'covariance','For random variables $X$ and $Y$,','their centered values vary together:')
d(0,'correlation coefficient','The [**correlation coefficient**]','rescales covariance:',True)

d(1,'state',"A circuit's current activities",'Definition Term"}.')
d(1,'fixed point','A [**fixed point**]','rate of change is zero.')
d(1,'continuous attractor','A [**continuous attractor**]','in the ideal deterministic model.')
d(1,'attractor manifold','The family is an [**attractor manifold**]','rather than neurons in the circuit.')
d(1,'Brownian motion','To describe this limit with a continuous path,','for $t\\geq s$.')
d(1,'root mean squared displacement','A [**root mean squared displacement**]','as the represented coordinate.')

d(2,'neural transfer function','The [**neural transfer function**]','into a nonnegative firing rate.')
d(2,'weak fluctuation approximation',"In the paper's [**weak fluctuation approximation**]",'with the same leading mean and covariance:')
d(2,'preferred angle',"For a ring network, a neuron's",'where its tuning curve peaks.')
d(2,'linearization','A [**linearization**]','quadratic or higher in it.')
d(2,'right zero eigenvector','Thus $\\mathbf u$ is a','neither restores nor amplifies.')
d(2,'left zero eigenvector','We also need a [**left zero eigenvector**]','a vector $\\mathbf v$ satisfying',True)
d(2,'diffusion tensor','The [**diffusion tensor**]','per twice the elapsed time.')

d(3,'Itô convention','The [**Itô convention**]','at the beginning of each increment.')
d(3,'Fokker Planck equation','In the zero-drift diffusion approximation,','Definition Term"}:',True)
d(3,'Dirac delta','Here the [**Dirac delta**]','initially all probability is at $\\Theta$.')
d(3,'systematic drift','The paper assumes that the network is tuned to eliminate','a nonzero mean velocity along the attractor.')
d(3,'Stratonovich convention','The [**Stratonovich convention**]','midpoint evaluation in its limiting increments.')
d(3,'activity bump','In Fig. 1B, an [**activity bump**]',"across the neurons' preferred angles.")

d(4,'likelihood','A [**likelihood**]','of a proposed parameter value.')
d(4,'score','The [**score**]','when the proposed memory value changes.')
d(4,'Fisher information|internal Fisher information rate','[**Fisher information**]','Definition Term"}:')
d(4,'unbiased',r'To understand why inverse information is an error scale,', 'Definition Term"}.')
d(4,'Cramér Rao bound','This is the [**Cramér Rao bound**]','regular unbiased estimation.')
d(4,'prior distribution','A [**prior distribution**]','before observing the spikes.')

d(5,'translation invariance','In this readout model, [**translation invariance**]','does not change the statistics of the readout error.')
d(5,'precision','The [**precision**]','the reciprocal of its variance.')
d(5,'hyperbolic tangent','The [**hyperbolic tangent**]',r'(e^z+e^{-z})$.')
d(5,'inverse hyperbolic tangent','Its [**inverse hyperbolic tangent**]',r'whose derivative is $1/(1-z^2)$.')
d(5,'hyperbolic cotangent','The [**hyperbolic cotangent**]',r'$\\coth z=1/\\tanh z$.'.replace('\\\\','\\'))

keys=[
(0,'Both abilities require a useful quantity to remain represented in a changing biological system.'),
(0,'The 2012 paper asks how accurately the network can maintain such a pattern using its own noisy activity.'),
(0,'Population averaging helps because the independent count variances add while the mean signal adds directly. If a common varying input makes several cells\' firing rates rise and fall together, that shared variation will not disappear in the same way.'),
(0,'Thus a growing mean squared displacement can contain random spread, a systematic change in the mean, or both.'),
(1,'The geometry of these two changes will explain why a stable-looking circuit can still accumulate memory error.'),
(1,'In the second case, the circuit remains coherent while holding the wrong angle.'),
(1,'The parameter $D$ is the diffusion coefficient. It measures the rate of variance growth; a single trajectory need not move monotonically away from its starting value.'),
(1,'Observing irregular spatial maps does not tell us how fast the maintained position drifts. Conversely, finding diffusion of a stored value does not determine the shapes of individual place fields.'),
(2,'A network can keep firing after a stimulus disappears and still lose the value that the stimulus supplied.'),
(2,'Incoming activations determine new firing rates; the resulting spikes renew those activations. This feedback can support activity after the external stimulus has ended.'),
(2,'To calculate memory loss, we need the one change that survives: the displacement to a different fixed point.'),
(2,"Each cell's random spikes disturb its outgoing synaptic activation; the circuit's return flow determines the lasting shift in memory."),
(2,'When $W_{ij}=W_{ji}$, can we express it through the tuning curves and neural transfer function?'),
(3,'A rate of random spreading measured near one stored value does not yet tell us how memory error behaves after a long wait.'),
(3,"The flattening of a ring network's error curve can therefore occur while its local noise mechanism remains unchanged. It reflects the bounded way angular error is reported."),
(3,'Repeated trials can spread apart even if their average stays at the original value. That random spreading differs from a reproducible movement in one direction.'),
(3,'Small changes to weights or biases might cancel the mean drift; they cannot remove the random increments by subtracting a known average.'),
(4,'Collecting more spikes helps distinguish nearby activity patterns, but during collection the pattern itself keeps moving.'),
(4,'Small internal information forces a large minimum diffusion coefficient. Large information allows small diffusion, but does not guarantee it.'),
(4,'Reaching the bound requires the network\'s retained response to each cell\'s spike noise to match that cell\'s information about memory.'),
(4,'The inequality compares diffusion and information for the same network. To compare different networks, we must say what stays fixed.'),
(4,'These conclusions change under another resource constraint. Fixing the total population spike rate instead of peak rate makes $a\\propto w^{-d}$, giving $J\\propto w^{-2}$ in every dimension.'),
(5,'The question is how much observation helps when the value being read keeps changing.'),
(5,'Waiting longer eventually increases error, even with more spikes available. The problem is their equal weighting for a moving state.'),
(5,'Thus the paper\'s statement about readout within a cellular time constant concerns a characteristic saturation time under full spike access. It does not mean all benefit ends abruptly at $\\tau$.'),
(5,"A downstream area may receive only some of the memory network's spikes. That reduces its information without reducing the fluctuations that already move the full memory network."),
(5,'Diffusion limits the accuracy of the integral and the usefulness of long observation; it does not by itself introduce that restoring pull.'),
]
for i,t in keys:add(i,'key',t)

for i,f in enumerate(files):
    text=(base/'content/chapters'/names[i]).read_bytes().decode('utf-8')
    terms=re.findall(r'\[\*\*(.*?)\*\*\]\{\.definition-term',text)
    assert sorted(terms)==sorted(x['term'] for x in f['definitionCoverage']),(names[i],terms)
    f['selections'].sort(key=lambda x:text.index(x['text']))
out=base/'verification/emphasis-20261028/selections-memory.json'
out.write_text(json.dumps(dict(files=files),ensure_ascii=False,indent=2),encoding='utf-8')
print(out)
for f in files:print(f['file'],len([s for s in f['selections'] if s['kind']=='key']),'key',len([s for s in f['selections'] if s['kind']=='definition']),'definition',len(f['definitionCoverage']),'terms')
