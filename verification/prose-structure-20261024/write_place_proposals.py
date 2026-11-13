from pathlib import Path
import json, hashlib, re
from datetime import datetime

root=Path('C:/dev/clsc/burak-papers/guide')
task=root/'verification/prose-structure-20261024'
names=['05-place-fields.md','05b-place-sizes.md','05c-place-tests.md']
base={n:(task/'baseline/content/chapters'/n).read_text(encoding='utf-8') for n in names}
edits={n:[] for n in names}
def change(n, old, new, kind, why, kept, question=None):
    assert base[n].count(old)==1, (n,old[:100],base[n].count(old))
    pos=base[n].index(old)
    section=re.findall(r'^#{1,3} .+$',base[n][:pos],re.M)[-1]
    edits[n].append(dict(location={'section':section,'baseline_line':base[n][:pos].count('\n')+1,'paragraph_opening':old[:120]},before=old,after=new,kind=kind,rationale=why,preserved_premise_or_limit=kept,source_or_meaning_question=question))
def para(n, start):
    return next(p for p in base[n].split('\n\n') if p.startswith(start))

n=names[0]
old=para(n,'We begin on a track,')
new=old.replace('where a field starts when the input crosses upward through the threshold.','where a field starts at an [**upcrossing**]{.definition-term custom-style="Definition Term"}, a point where the input crosses upward through the threshold.')
change(n,old,new,'definition','Give the crossing object its technical name where its role is first explained.','The threshold crossing starts a field; fixed spatial map interpretation stays in the next paragraph.')
old=para(n,'The expectation runs over')
new=old.replace('A jointly Gaussian vector is one for which','A [**jointly Gaussian vector**]{.definition-term custom-style="Definition Term"} is one for which')
change(n,old,new,'definition','Mark the existing explanation of the Gaussian property needed for height and slope independence.','All finite distributions and the zero covariance implication stay unchanged.')
old=para(n,'Three assumptions have different jobs.')
new=r'''Three assumptions have different jobs:

- [**Stationarity**]{.definition-term custom-style="Definition Term"} means that moving the observation window does not change the map's probability law. Here it gives a constant mean and a covariance $C(x,y)=C(y-x)$ that depends on separation. It does not say that a particular map is flat.
- [**Isotropy**]{.definition-term custom-style="Definition Term"} means that rotating the separation does not change the covariance: in several dimensions, $C(\Delta x)$ depends only on $\|\Delta x\|$. It rules out a preferred direction in the model's statistics. Stationarity alone does not imply isotropy.
- [**Smoothness**]{.definition-term custom-style="Definition Term"} controls whether the map has well defined spatial derivatives. Crossing calculations require differentiable sample functions and nondegenerate joint distributions: the relevant vector of heights and derivatives must have an invertible covariance matrix, rather than obey an exact linear constraint. Peak calculations require second derivatives and enough regularity to control their local approximation.

A Gaussian distribution of values does not guarantee this smoothness. For example, a covariance proportional to $e^{-|x-y|/b}$ has a sharp corner at zero separation and does not supply the differentiable paths assumed below.'''
change(n,old,new,'list','Expose the independent assumptions and keep each with the calculation it supports. Mark the actual smoothness explanation.','Stationarity is distinct from isotropy and smoothness; differentiability, nondegeneracy, second derivative requirements and counterexample remain.')
old=para(n,'Finding every root of a random curve is difficult.')
new='A field starts at an upcrossing, so its expected count can be found by counting upward passages through the threshold. A small interval around each crossing has a width determined by its slope; this lets us count crossings without locating every root.'
change(n,old,new,'transition','Connect the field definition to the counting method and state why the local slope is needed.','The next narrow-band derivation supplies the slope weighting; endpoint correction remains separate.')

n=names[1]
old=para(n,'Near such a peak,')
new=old.replace('Cuts through a map and slopes at field edges provide further checks of its spatial structure. The slope calculation also provides a separate check on the predicted field widths.','Cuts through a map test its spatial structure, and slopes at field edges provide a separate check on the predicted field widths.')
change(n,old,new,'wording','Remove the repeated announcement of a slope check while keeping its purpose.','High threshold size approximation remains separate from the exact boundary-slope derivation.')
old=para(n,'The following is a teaching reconstruction')
new=r'''The following is a teaching reconstruction of the high excursion argument in Methods S4, with algebraic corrections made explicit below. It assumes:

- a sufficiently smooth, stationary, isotropic, unit variance Gaussian field;
- an invertible covariance matrix for the relevant derivative variables;
- the limit $q\to\infty$;
- typical components counted once each, away from environment boundaries.

It is not a proof of the full excursion convergence theorem for every allowed covariance.[^p3-rare-source]'''
change(n,old,new,'list','Make the assumptions and sampling rule separately visible before the peak calculation.','Smoothness, stationarity, isotropy, unit variance, nondegeneracy, asymptotic threshold, component counting and boundary exclusion remain explicit.')
old=para(n,'This supplies two distinct predictions.')
new=r'''This supplies two distinct predictions:

- The length is a scaled square root of an exponential variable, giving a [**Rayleigh distribution**]{.definition-term custom-style="Definition Term"}.
- The peak firing rate is $a\epsilon$, so at fixed high $q$ it is proportional to $s^2$.

The exponent two concerns rate versus linear size. In three dimensions a suitable linear size is $s^{1/3}$ when $s$ denotes volume.'''
change(n,old,new,'list','Separate the two consequences of the same parabola before explaining the linear-size convention.','High q is retained for the peak-rate prediction; the 3D volume distinction remains after the list.')
old=para(n,'Let $v_d=')
new=old.replace('the gamma function,','the [**gamma function**]{.definition-term custom-style="Definition Term"},')
change(n,old,new,'definition','Mark the existing integral definition before the moment formula needs it.','Integral domain t>0 and factorial extension unchanged.')
old=para(n,'**Reading the supplement carefully.**')
new=r'''The printed supplement appears to contain three algebraic errors in this calculation:

- Equation S18 prints multiplication by mean size where the preceding moment formula requires division.
- Equation S23 omits a factor $\sqrt2$ when solving the parabola in S22 for full width.
- In S25 the finite-height quadratic exponent should be negative.

The derivation above retains the main paper's distributional form and obtains the constants from the displayed parabola, the moment integral, and the independent crossing calculation. These corrections concern the printed derivation; they do not establish that the simulation code or empirical fits used the same mistakes.[^p3-corrections]'''
change(n,old,new,'list','Give each printed equation issue its own item and remove the empty reading instruction.','Apparent rather than author-confirmed errors; source equation locators, corrected constants and limit on simulation-code inference retained.')
old=para(n,'Read Figure 2 with these distinctions in mind.')
new=r'''Figure 2 separates the measurements by spatial dimension:

- Panels A–B illustrate 2D thresholding. C measures lengths along slices, D measures original field areas, and E counts fields per observed cell.
- F–G show 3D examples; H, I, and J compare line lengths, planar areas, and full volumes.

The dashed analytical curves change with the dimension of the measurement, even within one recorded map. The alternative spherical-field model in Figure S2 matches empirical volumes and peak rates by construction but fails these slice distributions and the topology test. Matching volumes alone is therefore insufficient.[^p3-slices-source]'''
change(n,old,new,'list','Expose the two panel groups so the measurement dimension can be tracked.','All panel assignments, fitting by construction and failures on slice/topology tests remain.')

n=names[2]
old=para(n,'The [**Euler characteristic**]')
new=r'''The [**Euler characteristic**]{.definition-term custom-style="Definition Term"}, written $\chi$, combines these counts differently in each dimension:

- In 1D it equals the number of connected active intervals.
- In 2D it is the number of connected components minus the number of independent holes. Three disjoint disks have $\chi=3$; one connected ring has $\chi=1-1=0$.
- In 3D it is components minus independent tunnels plus enclosed cavities. A solid ball has $\chi=1$, a solid ring has $\chi=0$, and a hollow spherical shell has $\chi=2$.

These counts are the first three [**Betti numbers**]{.definition-term custom-style="Definition Term"}: numbers of independent components, loops, and cavities, respectively.[^p3-ec-source]'''
change(n,old,new,'list','Make the dimension-specific rules easy to compare without separating them from their examples.','Signed count, dimensional distinctions, examples, Betti explanation and citation retained exactly.')
old=para(n,'The expected Euler characteristic has')
new=old.replace('whose critical points have zero gradient','whose [**critical point**]{.definition-term custom-style="Definition Term"}s have zero gradient').replace('conclusion of Morse theory.','conclusion of [**Morse theory**]{.definition-term custom-style="Definition Term"}.')
change(n,old,new,'definition','Mark the existing critical-point explanation and the theorem family where its needed result is explained.','Compact domain, smoothness, invertible Hessians, signed counts, boundary contributions and unproved-theorem limit remain unchanged.')
old=para(n,'The limiting checks are informative.')
new=r'''The formulas have two limiting checks:

- As $q\to-\infty$, the whole box becomes active and all three expectations tend to one.
- As $q\to+\infty$, they tend to zero.

At intermediate thresholds the higher dimensional signed densities can be negative because tunnels or holes outnumber components. For example a cube with $L/\sigma=10$ has expected $\chi=-20.06$ at $q=0$. A negative expected Euler characteristic is meaningful; a negative expected field count would not be.'''
change(n,old,new,'list','Separate the two limits and retain the intermediate-threshold interpretation in prose.','All limit directions, numerical example and distinction from field count remain.')
old=para(n,'The processing choices affect')
new=r'''The processing choices affect the quantities being compared:

- Bat maps were rectified at about 0.5 Hz for denoising.
- The 3D maps, sampled in 10 cm bins, also received a median filter.
- Fields larger than three standard deviations above mean 3D volume were removed as possible merges, including from slice analyses.
- Peak counting excluded incomplete boundary fields and used a range of smoothing widths.
- The 1D rate versus width comparison used an additional 1 Hz cutoff.

These decisions can remove small components, alter peaks, and change tails. They belong to the definition of the analyzed fields.[^p3-processing]'''
change(n,old,new,'list','Reveal five independent processing choices before interpreting their effects on the comparison.','Every measurement condition, cutoff, boundary exclusion, possible-merge qualification and processing consequence is preserved.')
old=para(n,'Figure 1C distinguishes')
new=old.replace('then skew is','then [**skew**]{.definition-term custom-style="Definition Term"} is').replace('and excess kurtosis is','and [**excess kurtosis**]{.definition-term custom-style="Definition Term"} is').replace('A lognormal size distribution makes','A [**lognormal distribution**]{.definition-term custom-style="Definition Term"} of sizes makes')
change(n,old,new,'definition','Mark the moment definitions and the distribution characterized by Gaussian log sizes where those meanings are explained.','All moment formulas, zero population quantities and finite sample fluctuation limits remain unchanged.')
old=para(n,'The supplement adds useful checks.')
new=old.replace('Locally, mean curvature averages','Locally, [**mean curvature**]{.definition-term custom-style="Definition Term"} averages').replace('and Gaussian curvature multiplies','and [**Gaussian curvature**]{.definition-term custom-style="Definition Term"} multiplies')
change(n,old,new,'definition','Mark the two existing curvature explanations at first teaching use.','Principal-direction meanings, sphere and saddle comparison and surface/finite-difference limitations unchanged.')
old=para(n,'Uniform coverage supplies')
new=r'''The assumptions supply different parts of the model:

- Uniform coverage supplies stationarity away from boundaries.
- Smooth input tuning supplies smoothness.
- Random weights supply the Gaussian limit under their independence and size conditions.

For heterogeneous shapes, average the last integral over the distribution of input shapes, as in Methods S2, Equation S8.'''
change(n,old,new,'list','Separate which assumption supplies which statistical property.','Boundary qualification, random-weight independence/size conditions and heterogeneous-shape extension retained.')
old=para(n,"The covariance's Gaussian standard deviation")
new=r"The covariance's Gaussian standard deviation is $\sqrt2 b$, fixing the width convention used in the comparison."
change(n,old,new,'wording','Remove commentary about an ambiguity the explicit width calculation already resolves.','The precise Gaussian standard deviation and width convention stay explicit.')

assessments={
names[0]:{'retained_structure':'The chapter moves from the need for spatial dependence to Gaussian maps, local scale, slope-weighted crossings, endpoint correction and parameter inference. The crossing and length calculations remain connected prose because each step explains the next. The sample-selection calculation and limits of Poisson independence remain intact.','rejected_edits':[{'candidate':'Number every line of the Kac–Rice calculation or parameter inversion.','reason':'These are causal derivations, not independent actions; the equations already show the algebra.'},{'candidate':'Convert the long-track and selection qualifications to short labels.','reason':'Those limits determine what the fitted means and counts mean and must remain full explanations.'}]},
names[1]:{'retained_structure':'Peak conditioning leads to a radius and excess-height law, then to dimension-specific size densities. Slices and boundary slopes test additional structure. Three folds, exact math, printed-source corrections and approximation errors remain.','rejected_edits':[{'candidate':'Turn Gaussian conditioning and high-excursion derivation into numbered steps.','reason':'A numbered procedure would hide why each relation follows from the preceding one.'},{'candidate':'Delete finite-threshold rate exponents or mean-error example.','reason':'They prevent interpreting limiting size laws as exact finite-threshold predictions.'}]},
names[2]:{'retained_structure':'The chapter distinguishes topology from field count, derives signed densities and boundary terms, then separates fit choices, empirical tests and a possible random-wiring origin. Mathematical reasoning stays prose; independent dimension rules, limits and processing assumptions become lists.','rejected_edits':[{'candidate':'List the entire signed critical-point and face-factor derivation.','reason':'The determinant, gradient density, integral and boundary multiplicities depend causally on one another.'},{'candidate':'Shorten the wiring conclusion to random weights explain the data.','reason':'That would discard alternatives, measurement limits and stationarity limits.'},{'candidate':'Define median filtering, skew, kurtosis and curvature at length.','reason':'This is a structure pass; those terms require targeted source/teaching review rather than unverified new claims. Existing formulas and curvature explanations remain.'}]}}
glossary=[{'term':t,'chapter':n} for n,terms in [(names[0],['upcrossing','jointly Gaussian vector','smoothness']),(names[1],['Rayleigh distribution','gamma function']),(names[2],['critical point','Morse theory','skew','excess kurtosis','lognormal distribution','mean curvature','Gaussian curvature'])] for t in terms]
ledger={'created_at':datetime.now().astimezone().isoformat(),'writer':'GPT-6.1-sol/high','scope':names,'rules':'Publisher 0.8.23 course-study-guide-builder and references/pedagogy-language-contract.md','earlier_context_read':['00-reading-guide.md','01-foundations.md','01b-persistence.md','plan/chapter-plan.yaml'],'files':[],'new_glossary_terms_for_root':glossary,'limits':'Draft proposals only. No canonical edits, build or source-paper audit. Independent correctness, wording and flow reviews remain with root. Token stats unavailable.'}
for n in names:
    ledger['files'].append({'source_path':str(root/'content/chapters'/n),'baseline_path':str(task/'baseline/content/chapters'/n),'baseline_sha256':hashlib.sha256((task/'baseline/content/chapters'/n).read_bytes()).hexdigest(),'edits':edits[n],**assessments[n]})
# Persist the exact ledger before applying any proposal.
(task/'changes-place.json').write_text(json.dumps(ledger,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
out=task/'proposed/content/chapters'
out.mkdir(parents=True,exist_ok=True)
for n in names:
    text=base[n]
    for e in edits[n]:
        assert text.count(e['before'])==1
        text=text.replace(e['before'],e['after'],1)
    (out/n).write_text(text,encoding='utf-8')
    # Independent checks cover structural elements; the human change records cover meaning.
    for pat in [r'^#{1,6} .+$',r'\{\{block:[^}]+\}\}',r'^\[\^[^\]]+\]:.*$',r'^:::.*$',r'\$\$\n.*?\n\$\$']:
        assert re.findall(pat,base[n],re.M|re.S if '.*?' in pat else re.M)==re.findall(pat,text,re.M|re.S if '.*?' in pat else re.M),(n,pat)
print(json.dumps({'files':len(names),'edits':sum(map(len,edits.values())),'counts':{n:len(edits[n]) for n in names},'ledger':str(task/'changes-place.json')},indent=2))
