from pathlib import Path
from datetime import datetime
import re, json, hashlib, difflib

root=Path(__file__).resolve().parents[2]
out=Path(__file__).resolve().parent
chapters=root/'content/chapters'
names=['02b-memory-long-delays.md','03-memory-information.md']
old={n:(out/'baseline'/n).read_text(encoding='utf-8') for n in names}
new=dict(old)

def replace(n,a,b):
    assert new[n].count(a)==1, (n,a[:90],new[n].count(a))
    new[n]=new[n].replace(a,b)

def take(n,start,end):
    s=new[n]; a=s.index(start); b=s.index(end,a)
    piece=s[a:b]; new[n]=s[:a]+s[b:]
    return piece

n=names[0]
replace(n,'A local diffusion coefficient answers how variance initially grows. It does not by itself say that variance grows at the same rate forever. Boundaries and variation of $D$ can change the long time behavior.',
'**Neural mechanism.** Spike fluctuations keep shifting the stored value after the cue has ended. The local diffusion coefficient describes the variance of those shifts after stable disturbances have relaxed. It does not by itself say that variance grows at the same rate forever: boundaries and variation of $D$ can change the long time behavior. We first keep $D$ constant, so the line and circle differ only in how the memory coordinate is bounded.')
proof=take(n,'::: {.publisher-clarification-note .publisher-fold-always title="Derivation: from random increments to the memory density equation"}', 'When $D$ varies with state,')
proof=proof.replace('it gives the Fokker Planck equation shown above.','it gives the density equation below.')
replace(n,'Let $p(\\theta,t)$ be the density',
'**Mathematical derivation.** A density equation tracks how small random increments redistribute probability. The calculation below first obtains that equation for a general state-dependent $D$; constant $D$ then gives the line and circle solutions.\n\n'+proof+'Let $p(\\theta,t)$ be the density')
replace(n,"The flattening of a ring network's error curve can therefore occur", "**Interpretation.** The flattening of a ring network's error curve can therefore occur")
setup=take(n,'The supplement illustrates this with mutual excitation,', '$$\n2D=\\frac{1}{4}')
setup=setup.rstrip()
assert setup.endswith(', and')
setup=setup[:-5]+'.'
replace(n,'When $D$ varies with state,',
'**Neural mechanism.** The rate of random spreading can change as the stored value changes, because the current firing rates set the spike variability. '+setup.replace('The supplement illustrates this','The supplement illustrates this dependence')+'\n\n**Mathematical derivation.** When $D$ varies with state,')
linear='A state dependent $D$ need not produce a curved variance versus time graph. If $D$ is linear in $\\theta$, then $E[D(\\theta)]=D(E[\\theta])=D(\\Theta)$, so the variance remains linear while the process stays within the model\'s valid domain.[^p1-variable]'
replace(n,'This is [SI Eq. S37, p. 8](../papers/burak-fiete-2012-persistent-activity-si.pdf#page=8&zoom=125,0,602). '+linear,
'This is [SI Eq. S37, p. 8](../papers/burak-fiete-2012-persistent-activity-si.pdf#page=8&zoom=125,0,602).[^p1-variable] The mutual-excitation network gives a concrete case: substituting its two conjugate weights into the spike-noise projection gives')
replace(n,'The implied variance is $\\Theta t/(2\\tau)$,',
'**Interpretation.** '+linear.replace('[^p1-variable]','')+' The implied variance for this network is $\\Theta t/(2\\tau)$,')
replace(n,'Repeated trials can spread apart even if their average stays at the original value.',
'**Neural mechanism.** Repeated trials can spread apart even if their average stays at the original value.')
replace(n,'For state dependent $D$, where the coefficient is evaluated affects the process.',
'**Mathematical derivation.** For state dependent $D$, where the coefficient is evaluated affects the process.')
replace(n,'With $D$ of order $1/N$, random displacement over $dt$ is of order',
'With $D$ of order $1/N$, random displacement over $dt$ is of order') if False else None
replace(n,'The variance calculation captures the leading random term. Small changes to weights or biases might cancel the mean drift;',
'\n\n**Interpretation.** The variance calculation captures the leading random term. Small changes to weights or biases might cancel the mean drift;')
replace(n,'[Figure 1A, p. 2](../papers/burak-fiete-2012-persistent-activity.pdf#page=2&zoom=125,0,439) shows',
'**Neural mechanism in the figures.** [Figure 1A, p. 2](../papers/burak-fiete-2012-persistent-activity.pdf#page=2&zoom=125,0,439) shows')
replace(n,'Panels C and D test different parts of the prediction:',
'**Interpretation of the simulation tests.** Panels C and D test different parts of the prediction:')
setup='Let $p(\\theta,t)$ be the density of the memory coordinate across repeated trials initialized at $\\Theta$. The [**Itô convention**]{.definition-term custom-style="Definition Term"} evaluates a state-dependent noise coefficient at the beginning of each increment.'
replace(n,setup+' In the zero-drift diffusion approximation,','In the zero-drift diffusion approximation,')
replace(n,'**Mathematical derivation.** A density equation tracks how small random increments redistribute probability.',
'**Mathematical derivation.** '+setup+' A density equation tracks how small random increments redistribute probability.')

n=names[1]
replace(n,'Suppose two nearby memory values produce almost identical rates.',
'**Neural mechanism.** Suppose two nearby memory values produce almost identical rates.')
replace(n,'A [**likelihood**]{.definition-term custom-style="Definition Term"} is the probability of observed data as a function of a proposed parameter value. In a short interval $h$, let $n_i$ be neuron $i$\'s count. Treat the state as locally constant and use the conditional independent Poisson approximation. Then',
'In a short interval $h$, let $n_i$ be neuron $i$\'s count. Treat the memory state as locally constant and use the conditionally independent Poisson approximation from the neural model. The calculation below uses positive rates; a vanishing rate needs a suitable limit and regularity of the likelihood.\n\n**Mathematical derivation.** A [**likelihood**]{.definition-term custom-style="Definition Term"} is the probability of observed data as a function of a proposed parameter value. This general tool measures which proposed values make a spike sample more likely. For the neural model,')
cr=take(n,'To understand why inverse information is an error scale,','## Spike information sets a lower bound')
# Keep the derivation in the calculation group, then gather what its result means.
cr_proof,cr_meaning=cr.split('This is the [**Cramér Rao bound**]',1)
cr_meaning='This is the [**Cramér Rao bound**]'+cr_meaning
replace(n,'If the coordinate is an angle in radians,',cr_proof+'**Interpretation.** If the coordinate is an angle in radians,')
replace(n,' We write formulas for positive rates; a vanishing rate requires a suitable limit and regularity of the likelihood.[^p1-fi-source]',
'[^p1-fi-source]\n\n'+cr_meaning.rstrip())
replace(n,'The network has no access to its exact firing rates as noiseless numbers.',
'**Neural mechanism.** The network has no access to its exact firing rates as noiseless numbers.')
replace(n,'From the [projection and diffusion calculation]',
'**Mathematical derivation.** Cauchy Schwarz bounds a dot product by the product of the two vector lengths. Here the normalization of the memory projection fixes that dot product, while the two lengths measure diffusion and information. From the [projection and diffusion calculation]')
replace(n,'This proof uses the general left vector formula,',
'**Interpretation.** This proof uses the general left vector formula,')
replace(n,'Equality requires the two vectors in the proof to be proportional:',
'**Neural mechanism.** Reaching the bound requires the network\'s retained response to each cell\'s spike noise to match that cell\'s information about memory. A cell that adds retained noise without helping distinguish nearby values prevents equality.\n\n**Mathematical derivation.** Equality requires the two vectors in the proof to be proportional:')
replace(n,'gives $\\phi(g)=A e^{kg}$. This exponential family attains equality',
'gives $\\phi(g)=A e^{kg}$.\n\n**Interpretation.** This exponential family attains equality')
replace(n,'For $m$ memory coordinates the information is a matrix,',
'**Neural mechanism.** When a circuit stores several coordinates, a spike can shift more than one of them. Comparing each coordinate separately would miss combinations of shifts. The information and diffusion must therefore describe these shared directions.\n\n**Mathematical derivation.** For $m$ memory coordinates the information is a matrix,')
matrix_proof=take(n,'::: {.publisher-clarification-note .publisher-fold-always title="Check: the residual matrix proves the lower bound"}', '## Improving persistence depends')
matrix_meaning='The matrix inequality applies when every independent small coordinate change can be distinguished through a change in rates, so $J$ is invertible. It also explains why a scalar bound in each coordinate separately would miss coupled directions.[^p1-matrix]'
replace(n,matrix_meaning,matrix_proof+'**Interpretation.** '+matrix_meaning)
replace(n,'The inequality compares diffusion and information for the same network.',
'**Neural mechanism.** The inequality compares diffusion and information for the same network.')
replace(n,'Increasing $N$ while retaining the same distribution of tuning curves',
'**Mathematical derivation.** Increasing $N$ while retaining the same distribution of tuning curves')
replace(n,'These two statements concern different controlled comparisons. A larger cellular time constant',
'\n\n**Interpretation.** These two statements concern different controlled comparisons. A larger cellular time constant')
replace(n,'The paper also links tuning width to memory persistence.',
'**Neural mechanism.** The paper also links tuning width to memory persistence.')
replace(n,'The width $w$ is varied while $a$, $\\rho$, and the shape $f$ are fixed.',
'The width $w$ is varied while $a$, $\\rho$, and the shape $f$ are fixed.\n\n**Mathematical derivation.**')
replace(n,'Each diagonal entry therefore scales as $J_{\\alpha\\alpha}\\propto w^{d-2}$.',
'Each diagonal entry therefore scales as $J_{\\alpha\\alpha}\\propto w^{d-2}$.') if False else None
replace(n,'The resulting comparisons are:',
'\n\n**Interpretation.** The resulting comparisons are:')
replace(n,'The calculation below uses positive rates; a vanishing rate needs a suitable limit and regularity of the likelihood.',
'The calculation below uses positive rates.')
units='**Interpretation.** If the coordinate is an angle in radians, $J$ has units $\\mathrm{rad}^{-2}\\mathrm{s}^{-1}$. The information in a locally stationary interval of duration $h$ is $Jh$, not $J$.[^p1-fi-source]'
meaning=cr_meaning.rstrip()
replace(n,units+'\n\n'+meaning,
'**Interpretation.** '+meaning+'\n\n'+units.removeprefix('**Interpretation.** ')+' A vanishing rate requires a suitable limit and regularity of the likelihood.')
replace(n,'The matrix bound $2D\\succeq\\tau^{-2}J^{-1}$ means',
'The matrix calculation assumes that every independent small coordinate change can be distinguished through a change in rates, so $J$ is invertible. The matrix bound $2D\\succeq\\tau^{-2}J^{-1}$ means')
replace(n,'**Interpretation.** '+matrix_meaning,
'**Interpretation.** The bound controls every combination of stored coordinates, including coupled directions that separate scalar bounds would miss. It applies under the rate-distinguishability condition used above; if $J$ is singular, this ordinary inverse formula cannot be used.[^p1-matrix]')
replace(n,'Otherwise an apparent benefit of a parameter change may come from changing another property at the same time.',
'Otherwise an apparent benefit of a parameter change may come from changing another property at the same time. The comparisons below control how added neurons, altered firing rates, or slower synaptic decay affect the tuning curves and recurrent input.')
new[n]=re.sub(r' +\n','\n',new[n])

def hash_text(s): return hashlib.sha256(s.encode('utf-8')).hexdigest()
def blocks(s): return [p for p in re.split(r'\n\s*\n',s) if p.strip()]
def clean(s):
    return re.sub(r'\*\*(?:Neural mechanism(?: in the figures)?|Mathematical derivation|Interpretation(?: of the simulation tests)?)\.\*\*\s*','',s)

record={'created':datetime.now().astimezone().isoformat(),'status':'planned, saved before chapter writes','files':[]}
for n in names:
    ob,nb=blocks(old[n]),blocks(new[n]); items=[]
    for i,p in enumerate(ob):
        exact=[j for j,q in enumerate(nb) if clean(q)==p]
        contained=[j for j,q in enumerate(nb) if p in clean(q)]
        if exact:
            j=min(exact,key=lambda j:abs(j-i)); status='retained' if j==i else 'moved'
        elif contained:
            j=contained[0]; status='rewritten'
        else:
            j=max(range(len(nb)),key=lambda j:difflib.SequenceMatcher(None,p,clean(nb[j])).ratio());status='rewritten'
        items.append({'old_item':i+1,'status':status,'old':p,'new_item':j+1,'new':nb[j],
                      'reason':'Role labels, connected teaching order, or paragraph split; exact complete before/after text retained below.' if status=='rewritten' else 'Content preserved verbatim; destination reflects the paired teaching order.'})
    assert re.findall(r'^#{1,2} .+$',old[n],re.M)==re.findall(r'^#{1,2} .+$',new[n],re.M)
    assert re.findall(r'\$\$.*?\$\$',old[n],re.S)==re.findall(r'\$\$.*?\$\$',new[n],re.S) or sorted(re.findall(r'\$\$.*?\$\$',old[n],re.S))==sorted(re.findall(r'\$\$.*?\$\$',new[n],re.S))
    record['files'].append({'file':str(chapters/n),'old_sha256':hash_text(old[n]),'new_sha256':hash_text(new[n]),'old':old[n],'new':new[n],'items':items})

(out/'edits-information.json').write_text(json.dumps(record,ensure_ascii=False,indent=2),encoding='utf-8')
for n in names:
    (chapters/n).write_text(new[n],encoding='utf-8',newline='\n')
print(json.dumps({'at':datetime.now().astimezone().isoformat(),'files':[{'file':f['file'],'old_sha256':f['old_sha256'],'new_sha256':f['new_sha256'],'old_items':len(f['items'])} for f in record['files']]},indent=2))
