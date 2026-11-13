import json, hashlib, re
from pathlib import Path
import yaml

base=Path(r'C:/dev/clsc/burak-papers/guide')
out=base/'verification/teaching-alignment-20261029'
packet=json.loads((out/'memory-input.json').read_text(encoding='utf8'))
units={}
labels=packet['review_fields']
# Each string below is an independent passage judgment. This script only serializes them.
field_indices=[0,1,2,5,6,7,8,9,10,11,12,15]
def add(suffix, refs, fields, question, claims):
    matches=[k for k in packet['units'] if k.endswith(suffix)]
    assert len(matches)==1,(suffix,matches)
    key=matches[0]; src=packet['units'][key]
    fs=[x.strip() for x in fields.split('||')]
    assert len(fs)==len(field_indices),(suffix,len(fs))
    cs=[x.strip() for x in claims.strip().splitlines() if x.strip()]
    assert len(cs)==len(src['claims']),(suffix,len(cs),len(src['claims']))
    decisions={}
    for row,check in zip(src['claims'],cs):
        verdict='true as written'
        if check.startswith('C:'): verdict='condition stated';check=check[2:].strip()
        if check.startswith('N:'): verdict='not a claim';check=check[2:].strip()
        decisions[row[0]]={'verdict':verdict,'checked':check,'source_line':row[1]}
    units[key]={'status':'pass','findings':[],
        'questions':[{'question':question,'answer':fs[-1],
        'source_refs':[key+'/'+p for p in refs.split()]}],
        'fields':{labels[i]:v for i,v in zip(field_indices,fs)},'claims':decisions}

add('::ch:FOUNDATIONS','p3 p5',
'''p3 asks how changing neural activity can still represent eye angle or location. ||
p5 promises spikes, counts, covariance and mean displacement; the reader is not assumed to know them. ||
Represented value is an ordinary-language description here; formal rate and state definitions follow. ||
Eyes and a navigating animal are biological examples, not the model's measured data. ||
p3 distinguishes the memory, eye-motion and spatial-map problems. ||
Activity patterns represent a value; the text does not identify one cell with one angle. ||
p5 gives the correct sequence from variable spikes to uncertainty in observations. ||
Eye holding and location tracking supply the concrete tasks. ||
These are motivating situations, without an invented numerical result. ||
The three papers concern different parts of the problem; their mechanisms are not asserted identical. ||
Temporal memory loss and spatial rate arrangement are distinguished at the outset. ||
Could this imply that Mainali's fixed random map explains online location tracking? The strongest reading is motivation, followed explicitly by three different problems. The later fixed-map distinction prevents that stronger causal claim.''',
'Does the opening wrongly make the three papers one mechanism?',
'''Main paper introductions support the three separate concerns; p3 says different parts, and p5 only outlines shared background.''')

add('::sec:FOUNDATIONS-SPIKES','p9 p13 p16 p20 p28 p33',
'''p9–20 connect spikes to a value encoded in expected population rates. ||
Spike and rate are introduced at p9; tuning curves and expected-rate mapping precede their use in the model. ||
Rate is expected spikes per time, not regular timing; eye-angle tuning is explicitly a local linear approximation. ||
Oculomotor neurons drive eye muscles; hippocampal/entorhinal cells provide location-related examples. ||
The passage distinguishes recurrent CA3, CA1 outputs and entorhinal input rather than placing all spatial coding in one area. ||
The eye equation maps a physical angle to expected activity; a measured rate map is estimated with finite sampling. ||
Changing the encoded variable changes a pattern of expected rates; an observed spike sample remains variable. ||
20 Hz and a linearly tuned eye neuron make the meaning of rate and slope concrete. ||
The eye example is restricted to a positive-rate working range; the map example separates position from trial noise. ||
The output rate map alone does not identify where or how a location estimate is maintained. ||
Eye angle, place firing and grid firing are alternative examples of population representation, not equivalent circuit models. ||
Could a rate map prove a memory mechanism or conflate CA3 with CA1? p28–33 explicitly separate represented location from maintenance and identify the pathway. Maimon et al. 2026 primary text supports strong CA3 recurrence and CA3-to-CA1 projection; Hafting et al. 2005 supports entorhinal grid organization. No contrary anatomical claim found.''',
'Does the biological setup overstate what a tuning curve establishes?',
'''20 Hz means expected count 20 in one second; rate is not a deterministic interspike interval.
C: Positive working range and local linear tuning are stated; no claim of globally linear neuronal response.
C: Eye-angle slope/intercept and threshold qualification are consistent with oculomotor rate coding and the later eye model.
The text distinguishes the expected function from finite-count estimates of it; this is the proper statistical reading of a rate map.
A rate-position relation does not determine the circuit maintaining the represented position; the limit is stated explicitly.''')

add('::sec:FOUNDATIONS-POISSON','p39 p56 p66 p76 p88 p92 p95',
'''A brief count is unreliable even when the modeled rate is fixed. ||
p39 defines the Poisson count model before its moments are used; the folded derivation supplies the factorial-moment algebra. ||
Mean and variance are both rΔt for the count; relative standard deviation is 1/√(rΔt). ||
K is a random count; r and Δt are fixed conditions, and N independent cells pool counts. ||
Conditional independence is a model of counts given rates, not a claim of independent complete recurrent spike histories. ||
The figure converts counts to K/(NΔt), a rate per cell, so means can be compared at fixed r. ||
E[K(K−1)]=λ² implies Var K=λ; independent sums add both means and variances. ||
At r=20 Hz and Δt=.05 s, one cell has λ=1 and twenty have λ=20. ||
The pooled relative SD is 22.36%; per-cell rate SD falls from 20 to 4.472 Hz, with the same mean. ||
p93–95 distinguish the Poisson assumption from biological regularity and separate interval CV from count Fano factor. ||
Longer windows and more independent cells both improve counting precision only when the conditions being compared stay fixed. ||
Could recurrent coupling invalidate the independent-Poisson calculation? Yes for entire spike trains, but p92–95 explicitly restrict independence to fixed modeled rates and flag non-Poisson alternatives. The displayed distribution and pooling calculation are correct under that restriction; pixels remain pending.''',
'Is the pooling gain claimed for generally correlated recurrent neurons?',
'''C: Poisson PMF with λ=rΔt is correctly normalized for a constant-rate interval.
Shifting k(k−1)λ^k/k! to λ² times the exponential series gives λ².
K²=K(K−1)+K is an identity.
Variance λ²+λ−λ²=λ, checked independently.
C: SD/mean=√λ/λ requires λ>0, the positive example used here.
C: More time or cells improves this count comparison with rates and independence held fixed, as specified.
N: Closing div markup has no scientific assertion.
The stated r=20 Hz, Δt=.05 s are explicitly illustrative, not a biological estimate.
20×.05=1 expected spike.
exp(−1)=.3678794412, so .368 is correct.
Twenty independent Poisson(1) counts sum to Poisson(20), SD √20=4.4721.
√20/20=.2236068, or 22.4% after rounding.
C: Caption distribution moments and stem spacing follow K/(NΔt): spacing20 Hz for N1 and1 Hz for N20. Recomputed; actual drawing/pixel fidelity deferred.
SI S43 is the source Poisson likelihood for counts; locator and intended use agree.
C: SI S1–6 conditions independent increments on the modeled state; text correctly does not assert independent recurrent histories.
Interval CV and count variance/mean are different statistics; equality relations need a process model. Ben-Shushan 2022 reports low motor-neuron interval CV, not automatic Poisson counts.''')

add('::sec:FOUNDATIONS-COVARIANCE','p99 p109 p127 p140 p152 p165',
'''Shared commands, private noise and bias can produce different displacement statistics. ||
Covariance, correlation and MSD are defined before using them to interpret eye motion; probability expectations are explained in the folded definitions. ||
Covariance is centered co-variation, correlation divides by positive SDs, and MSD includes squared mean displacement. ||
The common command and private terms are distinct random inputs; muscle response and measurement noise affect their observed output. ||
The two-eye example assumes stated independence and gains; it does not identify covariance with a unique anatomical source. ||
The same physical displacement has a mean component and a centered random component. ||
Expanding the squared sum gives MSD=Var+mean²; independent private noise drops out of cross covariance. ||
The shared/private decomposition shows why a small correlation can coexist with a sizable common variance contribution. ||
The conclusion is conditional on gains, private noise and the response model, not a direct estimate from correlation alone. ||
Measurement noise contributes two endpoint variances when independent; directional bias must be assessed from means. ||
Covariance, correlation and MSD answer different questions, so none substitutes for the others. ||
Could covariance alone prove a common neural command? No: the passage explicitly retains the pathway and independence assumptions. The algebra is correct, and Ben-Shushan's shared-drive interpretation is a model-supported explanation, not a covariance theorem.''',
'Does the covariance argument claim more biological identification than the assumptions allow?',
'''Ben-Shushan 2022 asks whether common command fluctuations rather than independent motor noise can explain binocular drift statistics; the framing matches.
C: Correlation is shared covariance divided by total SDs; private terms and gains prevent directly equating its size with a common variance fraction.
C: For nonzero finite variances, Cauchy–Schwarz gives −1≤ρ≤1 and units cancel.
C: Mean displacement separates directional bias under the finite-moment decomposition; it does not by itself locate its biological cause.
η=Δx−EΔx is centered by definition.
E[(η+μ)²]=Eη²+μ² since Eη=0, hence MSD=variance+mean².
C: Neural drive, muscle response and measurement error occupy different positions in the observation pathway; the text keeps the modeling conditions explicit.''')

add('::ch:PERSISTENCE','p3 p5',
'''Persistent firing can coexist with a changing stored value. ||
Uses rate patterns from Foundations; state geometry and diffusion are introduced in this chapter. ||
Stability of activity and fidelity of the represented value are distinguished. ||
The circuit sustains activity while a coordinate within its stable family can move. ||
The chapter begins from a two-rate state, then accumulated changes of its encoded angle. ||
Changing cells' activity is interpreted through the represented coordinate, not raw vector size alone. ||
Recovery removes some disturbances but can retain a shift to another fixed point. ||
The eye-angle construction is explicitly a teaching model. ||
It illustrates the two kinds of disturbance before general diffusion formulas. ||
No claim that all persistent networks have a continuous attractor. ||
The later fixed spatial map is kept separate from temporal wandering. ||
Could stable activity imply faithful memory automatically? The opening's explicit distinction is precisely why not; the following equations demonstrate a surviving angle shift.''',
'Does the opening equate persistence with accuracy?',
'''The deterministic stable family permits a persistent coordinate shift; the following two-cell model demonstrates it.
The chapter's geometry/diffusion sequence is present in its actual sections, not an unfulfilled roadmap.
The spatial-map comparison is a difference in the random object, not a claim that all three papers use temporal Brownian motion.''')

add('::sec:FOUNDATIONS-ATTRACTOR','p9 p21 p35 p41 p51 p58',
'''How can a disturbance decay yet leave a different represented angle? ||
State, fixed point, attracting direction and coordinate count are introduced before the rate construction. ||
Stability is defined in a direction; a continuous attractor has a neutral tangent rather than every disturbance decaying to one point. ||
r1,r2 are rates; x measures common activity displacement and θ the rate difference divided by 2k. ||
The chosen deterministic flow is rdot1=rdot2=−ax with a>0. ||
θ=(r1−r2)/(2k) maps hertz to angle; x=(r1+r2)/2−b has rate units. ||
xdot=−ax and θdot=0 follow by addition/subtraction, so common shifts relax and difference shifts remain. ||
b40,k2 gives rates50,30 at θ5; shifts to53,33 and53,27 separate the two effects. ||
The first shift has x3,θ5; the second has x0,θ6.5 and therefore a lasting error. ||
Positive rates and the illustrative flow are assumed; perpendicular projection is not asserted for general networks. ||
The later tilted-flow example generalizes the projection beyond this symmetric construction. ||
Could the figure's diagonal line make Euclidean perpendicular projection universal? p62–64 explicitly says the return flow determines projection; this special symmetric flow happens to recover perpendicularly. Arithmetic and fixed-point claims check out.''',
'Does this special geometry misstate what general network recovery does?',
'''Fixed point means zero deterministic derivative; directional stability means small disturbances in that direction decay.
Dimension counts independent local coordinates, consistent with the two-rate construction and one-dimensional family.
N: Closing div markup is not a scientific assertion.
C: b40 Hz and k2 Hz/degree are chosen teaching parameters, not fitted data.
r1=b+kθ and r2=b−kθ give the displayed two rates.
Adding the tuning curves gives2b, independent of θ.
C: The stated positive-rate range excludes nonphysical negative rates.
The definitions invert the affine rate coordinates exactly.
C: rdot1=rdot2=−ax is the specified model, not derived as universal physiology.
a has inverse-time units so rdot has rate/time units.
Addition gives xdot=−ax; subtraction gives θdot=0.
The solution x(t)=x(0)e^(−at) has time constant1/a for a>0.
At b40,k2,θ5 the rates are50 and30 Hz.
The common disturbance adds3 Hz to each rate.
For53,33: x=3 Hz and θ=5 degrees.
For53,27: x=0 and θ=6.5 degrees.
The second disturbed state lies on the fixed-point line but represents the wrong initial angle.
C: Caption's disturbance/recovery distinction follows the equations and chosen rates; actual arrow rendering is deferred.
General flow need not be perpendicular to an attractor; SI Fig1 and left-vector projection explicitly support this qualification.''')

add('::sec:FOUNDATIONS-DIFFUSION','p72 p88 p106 p124 p136 p151',
'''Repeated retained changes cause trial-to-trial memory spread. ||
Independent steps are built from the earlier variance addition; Brownian motion and covariance are defined locally. ||
D uses Var increment=2DΔt; RMS displacement is √(2Dt), not2Dt. ||
The random coordinate has independent zero-mean increments; a deterministic velocity v is a separate added term. ||
Equal step variance and duration lead to the continuum Brownian model only on its stated scale. ||
Angles and units remain physical, with degrees converted to arcminutes in the example. ||
Variance adds across independent increments; shared past increments give Cov(Bs,Bt)=min(s,t). ||
D=.02 degrees²/s yields RMS .1183 degrees at .35s and .2 degrees at1s. ||
Adding v=.1 degree/s gives squared bias v²t²; it equals2Dt at4s, both .16 degree². ||
An unbounded coordinate and drift-free increments are assumptions; a circle later has bounded reported angular error. ||
MSD, variance and RMS distinguish biased motion from random spreading. ||
Could linear variance growth imply a square-root bound on each trajectory or infinite error on a circle? p132–138 excludes both interpretations: the envelope is an RMS scale, and the coordinate convention matters. The Brownian covariance proof and crossover arithmetic are correct.''',
'Are Brownian RMS and variance statements correct beyond their stated domain?',
'''Only the retained component survives recovery in the preceding construction.
C: Independent zero-mean equal-variance increments give Var sum=n Var step.
C: Brownian motion is introduced as a continuous-scale model with independent Gaussian increments, not a literal spike sequence.
C: The text states a coarse time-scale and small-displacement regime for the diffusion approximation.
Scaling standard Brownian motion by√(2D) gives variance2Dt.
C: Var[θ(t)−θ(0)]=2Dt holds for constant D on an unbounded coordinate with deterministic initial state.
RMS=√(2Dt); in multiple independent dimensions the squared Euclidean scale sums coordinate variances, as the passage distinguishes.
N: Closing div markup has no scientific assertion.
D=.02 degrees²/s is explicitly a chosen teaching value.
2×.02×.35=.014 degrees²; √.014=.1183216 degrees=7.0993 arcmin.
At1s, √.04=.2 degrees.
v=.1 degree/s is an illustrative bias speed.
MSD=2Dt+(vt)² from the earlier centered-moment identity.
2D/v²=4 seconds is the nonzero crossover time.
At4s, random variance and squared bias are each .16 degree².
Quadratic squared bias eventually exceeds linear variance when v≠0.
Variance removes the mean; MSD alone cannot tell whether a growing mean contributed without checking it.
C: The caption's RMS scale and4s crossing are recomputed; simulated paths are explicitly teaching paths. Image/path fidelity is deferred.
SI S30 uses mean square error2Dt for constant D; the locator and convention agree.
C: Wrapped angular error is bounded and eventually saturates despite continuing local diffusion, as SI S31–32 confirms.''')

add('::sec:FOUNDATIONS-RANDOMNESS','p159 p161 p163 p169',
'''Differentiate temporal memory noise from a spatially random rate function. ||
Uses rate map and temporal diffusion already taught; detailed Gaussian spatial fields come in Part III. ||
A fixed map is a random function drawn once for a cell/environment, then evaluated at visited positions. ||
Position selects an expected rate; trial spikes may still vary independently of that fixed spatial function. ||
The three schematic rows compare different systems rather than one shared generative model. ||
Time and physical position index different random objects. ||
Revisiting a position returns the same expected-rate function in the fixed-map model. ||
The same location is visited twice in the schematic explanation. ||
This comparison isolates expected rates from variable realized counts. ||
It is a modeling distinction, not a claim that biological maps never change. ||
The eye paper proposes changing central commands; the spatial paper analyzes map shape. ||
Could a temporal diffusion law explain place-field arrangements by itself? No: p161–165 says precisely that it cannot. Mainali's thresholded spatial Gaussian-field model supports the fixed function interpretation; the diagram is explicitly a guide schematic.''',
'Does fixed map exclude biological remapping or stochastic spikes?',
'''C: Mainali models a realization of a spatial random field and thresholds it; fixed within the selected model/environment does not assert permanent biological stability.
A diffusion coefficient over time does not determine the shape or spacing of a fixed spatial field.
C: Caption identifies separate paper problems and a proposed eye-command pathway; it does not claim the schematic traces are recorded data. Actual drawing acceptance deferred.''')

add('::ch:MEMORY-DYNAMICS','p3 p5 p7 p9',
'''Calculate how spike noise changes a continuously stored value. ||
Requires rate/state geometry and diffusion from the first two chapters; linearization is developed below. ||
The target is a diffusion coefficient of the represented coordinate, not simply variance of total neural activity. ||
Spikes renew synaptic activation; recurrent weights turn activation into input and rates. ||
A tuned continuous family and weak fluctuations define the calculation. ||
The synaptic state is projected to a memory coordinate through the return flow. ||
The outline follows the causal sequence spikes→activation→rates→retained disturbance. ||
The mutual-inhibition model later evaluates the general formula. ||
It is presented as an analytically chosen network example. ||
The introduction labels the assumptions needed for the derivation. ||
General asymmetric networks are treated before the symmetric simplification. ||
Could this chapter claim that arbitrary recurrent excitation produces a continuous attractor? No: the actual opening says a continuous family is assumed, and the fixed-point section explicitly requires tuning.''',
'Is the model construction mistaken for a generic property of recurrent neurons?',
'''Burak and Fiete main Eqs7–9 and SI S1–6 use decaying activation renewed by spikes and rates set by recurrent input.
C: The weak-noise continuous-attractor setting is stated, consistent with the paper's scope.
The promised derivation and mutual-inhibition specialization are both present in the chapter.''')

add('::sec:MEMORY-SPIKES','p13 p23 p37 p48 p61 p78 p91',
'''How can brief spikes sustain a state and introduce noise into it? ||
Rates and conditional count noise are available; δ impulses, compensated increments and Brownian replacement are explained here. ||
s is activation, g=Ws+b input, r=φ(g) rate; s is not an instantaneous firing rate. ||
Each presynaptic spike adds one activation unit; its downstream effect is weighted by W. ||
The common τ and recurrent feedback define the deterministic field F=−s/τ+φ(Ws+b). ||
Integrating an impulse gives an activation jump; averaging yields τr=s on a fixed point. ||
The centered count fluctuation has variance rdt; √r dB supplies its leading diffusion approximation. ||
The five-spike trace uses50ms decay; the n-copy construction reduces total-input fluctuations as1/√n. ||
Weights1/n keep mean input fixed while independent variances sum to1/n. ||
The Gaussian approximation concerns summed inputs in a large population, not the exact spike train of each cell. ||
General weight matrices precede the symmetric special case, and finite-N equality is not claimed. ||
Could replacing jumps by Brownian noise be invalid for a sparsely firing single neuron? Yes, and p48–70 confines the controlled argument to weak total-input fluctuations from replicated populations. SI S2–6 supports that scope; the chapter does not assert exact finite-size Gaussian spiking.''',
'Is the jump-to-diffusion replacement used beyond its justified regime?',
'''C: Unit jumps followed by exp(−Δt/τ) decay solve the activation equation;50ms and five spike times are illustrative. Actual image rendering deferred.
Main Eqs7–9 use exactly s decay/spike renewal, g=Ws+b, and r=φ(g).
C: dN−rdt has zero conditional mean and variance rdt to leading infinitesimal order under the conditional Poisson law.
C: SI S2–6 controls fluctuations in summed recurrent input, as explicitly stated.
√r has units time^−1/2 and dB units time^1/2, so their product has activation units for unit jumps.
C: Weak-noise diffusion is not exact replacement of every individual point process; the passage says this.
SI S2–5 contains the replication, scaled weights and total-input variance argument used here.
n independent contributions weighted1/n preserve the mean and yield variance n/n²=1/n times the original variance.
C: Increasing ring population at fixed density-normalized weights is a large-population comparison, with profile and input controlled.
C: The displayed stochastic equation is a leading large-population/weak-noise approximation, not an exact finite-N identity.
At deterministic equilibrium0=−s/τ+r, hence s=τr.
C: A continuum of fixed points requires the tuned relation; generic weights need not provide it.''')

add('::sec:MEMORY-LINEARIZATION','p95 p104 p124 p139 p158 p170 p180',
'''Find the coordinate shift remaining after all locally stable modes decay. ||
Uses derivatives and matrices from the reader baseline; Jacobian, left/right neutral vectors and their normalization are developed explicitly. ||
u is the tangent to fixed points; v extracts the surviving coordinate and need not be parallel to u. ||
K controls first-order deterministic recovery; R contains the spike-noise amplitudes. ||
One neutral mode and all other local modes stable are assumed; rates and derivatives are evaluated at a fixed point. ||
δs→v·δs is the local bridge from a high-dimensional disturbance to a scalar memory change. ||
Differentiate F(s(θ))=0 to obtain Ku=0; normalize vK=0 and v·u=1. ||
xdot=ay, ydot=−λy gives lasting shift x0+(a/λ)y0. ||
For a/λ=.5, an imposed jump to(0,2) relaxes to(1,0); perpendicular projection would miss it. ||
Small disturbances and decay of other modes are needed; changing one weight does not determine the eigenstructure. ||
The flow-based projection is compared explicitly with the incorrect Euclidean projection. ||
Could nonnormal dynamics or a defective zero eigenvalue invalidate the projection? Nonnormal stable modes are allowed and are the point of the tilted example. A zero Jordan block would violate the assumed one neutral memory direction with relaxation of all remaining modes. Within those assumptions the projection u v and SI S10–13 agree.''',
'Does the left-vector argument silently require orthogonal or symmetric modes?',
'''C: Linearization describes small disturbances near the chosen fixed point, as stated.
Taylor expanding φ at g gives derivative diagφ′ times Wδs.
K=−I/τ+diagφ′W and R=diag√r match SI S7–9.
Every K entry has inverse-time units in the activation coordinates.
Changing an individual recurrent weight can change many eigenvalues/vectors; magnitude alone does not order stability.
Differentiating F(s(θ))=0 gives the chain rule K ds/dθ=0.
Therefore u=ds/dθ=τr′ is a right zero vector.
C: Decay of every other local mode is a required assumed attractor property, not a consequence of Ku=0 alone.
C: vK=0 and v·u=1 specify the local coordinate projection when the neutral mode is simple.
For Kz=λz, left multiplication gives0=λv·z.
For λ≠0 this implies v·z=0.
C: Under the stable-other-modes assumption, only the u component remains after relaxation.
SI S12–13 supplies the left/right zero-vector normalization and projection.
The surviving state perturbation is u(v·δs), with the coordinate shift v·δs.
N: Closing div markup has no scientific assertion.
C: The stated two-variable tilted flow is an illustrative linear system, not a measured network.
Solving y=y0e^(−λt) and integrating xdot=ay gives x∞=x0+(a/λ)y0.
With x0=0,y0=2,a/λ=.5 the endpoint is(1,0).
C: Caption's tilted recovery and crowding of equal time marks follow the exponential solution; artwork fidelity remains pending.''')

add('::sec:MEMORY-DIFFUSION','p184 p193 p207 p215 p220',
'''Calculate variance of the retained coordinate increment. ||
Uses the left vector and conditional spike variances established immediately before. ||
D is half the growth rate of the projected coordinate variance, with the2D convention kept explicit. ||
v determines how each activation fluctuation changes memory; r sets its conditional variance. ||
R is diagonal for independent conditional spike increments, although projected memory coordinates can be correlated. ||
dθ=vᵀδs relates state noise to the stored quantity. ||
vᵀK=0 removes first-order return flow; Var dθ=Σv_i²r_i dt. ||
The multiple-coordinate extension has cross terms Σv_i^a v_i^b r_i. ||
Shared projection of the same independent cell noises can correlate coordinates. ||
The window must be longer than stable relaxation and short enough for coefficients to stay local. ||
Changing rates also changes v in general; the weighted sum is not a fixed-v universal prediction. ||
Could independent cells force diagonal diffusion in multiple memory dimensions? No: each noise source can enter several projections, yielding the stated off-diagonal covariance. This follows directly from VᵀRV and matches SI S21–27.''',
'Are the projected covariance and local time-scale assumptions sufficient?',
'''C: Stable components are removed by local return flow under the earlier spectral assumptions.
vᵀK=0 eliminates the deterministic linear term in the projected stochastic equation.
dθ=Σv_i√r_i dB_i gives the retained noise increment.
SI S14–15 states the same projected diffusion formula2D=Σv_i²r_i.
Changing a firing rate can alter the Jacobian and hence v; no monotone D prediction follows from r alone.
C: The local diffusion window must exceed stable-mode relaxation and remain short enough that coordinate-dependent coefficients barely vary.
C: The chapter states both sides of that window; it does not treat arbitrarily short spike dynamics as already relaxed.
For coordinates a,b,2D_ab=Σv_i^a v_i^b r_i by independent dB covariance.
Independent cell noise need not mean independent coordinate noise because projections share noise sources.''')

add('::sec:MEMORY-SYMMETRIC','p226 p243 p259 p265 p278 p292',
'''Express diffusion through tuning curves when connections are symmetric. ||
Uses K,u,v; the inverse transfer derivative is introduced only where it exists. ||
Symmetric W is reciprocal input weighting, not necessarily identical firing responses. ||
g′ becomes a left zero direction after symmetry; normalization still uses u=τr′. ||
Commonτ, positive interior rates and a stable family remain required. ||
g′=r′/φ′ where invertible bridges the transfer function to the tuning curves. ||
Kᵀg′=0 yields the general squared-gradient numerator and normalized denominator. ||
Two mutually inhibiting cells have s1+s2=b and θ=s1−s2. ||
With b20,τ.1 their rate sum is200/s and D100 activation²/s. ||
The linear interior does not specify boundaries; no translational symmetry is needed for the general symmetric formula. ||
The general left-vector formula covers asymmetric weights; this is an extra simplification, not a necessary network law. ||
Could the printed main Eq2 justify a numerator without the square? No: SI S18 and direct normalization require (g_i′)². The guide explicitly identifies the main equation omission. I reopened the source PDF formula; the guide correction and example are correct.''',
'Is the guide justified in departing from the printed main symmetric-network formula?',
'''For symmetric W, differentiate r=φ(g), g=Wτr+b; this gives Kᵀg′=0 with the stated K.
C: Expressing g′ through inverse φ requires local invertibility, explicitly stated.
Main Eq2 visibly omits the square on dg/dθ; SI S18 and2D=Σv²r contain it. Source PDF page2 inspected.
The symmetric derivation does not assume translationally identical tuning profiles.
N: Closing div markup has no scientific assertion.
C: W off-diagonal−1 and φ(g)=g/τ define the chosen positive linear mutual-inhibition model.
Fixed points obey s1+s2=b and r_i=s_i/τ.
θ=s1−s2 gives s1=(b+θ)/2,s2=(b−θ)/2.
The sum mode has a negative relaxation eigenvalue; the difference is neutral.
u=(1/2,−1/2),v=(1,−1) satisfy Ku=0,vK=0,v·u=1.
2D=r1+r2=b/τ, hence D=b/(2τ).
C: |θ|<b ensures positive rates; boundary behavior is excluded rather than extrapolated from the interior law.
Main Fig2 and SI discuss the mutual-inhibition example with constant activity sum.
b20 andτ.1 imply total rate200/s and D100 activation²/s.
C: Caption values and opposite rate slopes follow the equations; rendered curves/endpoints are deferred.
C: Constant total rate makes local D constant in this chosen model, not in all symmetric networks.''')

add('::ch:MEMORY-LONG-DELAYS','p3 p5 p7',
'''Determine when local spreading predicts errors over long delays. ||
Uses the D formula and geometry already developed; boundaries and coordinate-dependent diffusion are new. ||
Local diffusion is separated from global displacement error and systematic drift. ||
The stored coordinate continues moving even when its reported wrapped error becomes bounded. ||
Line, circle and state-dependent examples are separate controlled models. ||
Angular wrapping changes the error coordinate, not the microscopic presence of random shifts. ||
The opening correctly limits what2Dt alone can predict. ||
The chapter supplies ring and mutual-excitation examples. ||
They illustrate two distinct departures from a naive unlimited constant-slope reading. ||
Long-time behavior needs boundaries and drift information as well as D. ||
Zero-drift and systematic-drift cases are compared without equating their laws. ||
Could local2Dt imply global accuracy for arbitrary time? The opening explicitly rejects that inference and the later wrapped Gaussian calculation provides the counterexample.''',
'Is the long-time scope stated without assuming the result it needs to prove?','')

add('::sec:MEMORY-LONG-TIME','p17 p35 p54 p74 p91 p98 p106',
'''Extend local diffusion to density evolution and finite-range errors. ||
Brownian increments and variance are known; Itô test-function expansion and density equation are derived in the fold. ||
The drift-free density equation is ∂tp=∂θ²(Dp); it differs from D∂θ²p when D varies. ||
p is probability density and D local variance coefficient; periodic angle and unbounded line use different state spaces. ||
Constant D is used for the line/circle comparison; variable D is introduced separately with boundary assumptions. ||
Wrapping an unbounded Gaussian into [−π,π) changes reported error and gives a uniform long-time density. ||
The wrapped sum and uniform second moment yieldπ²/3; the moment generator gives dVar/dt=2E D for zero drift. ||
The excitation example has s=(θ+b0/2,θ−b0/2), v=(1/2,1/2). ||
It yields D=θ/(4τ); since D is linear, the local second-order curvature correction vanishes. ||
The expansion assumes interior smoothness and vanishing boundary terms; the positive-rate domain is retained. ||
The ring plateau and variable-D slope are separate reasons a single local number cannot determine all long-time behavior. ||
Could multiplicative noise produce a hidden mean drift or the SI factor-two D? The chosen Itô zero-drift equation fixes the mean locally; the next section explicitly discusses missing systematic drift. Projection gives θ/(4τ), while SI S40 prints θ/(2τ) and S41 gives variance θt/(2τ). PDF page9 confirms the guide correctly flags this inconsistency.''',
'Are wrapping, variable diffusion, and the excitation normalization mutually consistent?',
'''C: The first comparison holds D constant and changes only line versus periodic coordinate.
C: dθ=√(2D(θ))dB is explicitly an Itô, zero-systematic-drift model.
Taylor expansion E[df]=E[D f″]dt and integration by parts gives ∂tp=∂θ²(Dp) under stated boundary conditions.
Summing Gaussian density over θ+2πk produces the normalized periodic heat kernel.
SI S31 gives the wrapped Gaussian representation used here.
Periodic diffusion with constant positive D tends to uniform1/(2π).
The angular-error plateau comes from bounded reporting; local random increments need not stop.
Error in[−π,π) has bounded square and uniform second momentπ²/3.
D=.5 rad²/s is a declared teaching value.
C: Caption compares analytic line and wrapped curves for the same D, consistent with the heat kernel; image fidelity deferred.
Integrating θ²/(2π) from−π toπ givesπ²/3=3.2898681337.
SI S38–41 gives the mutually excitatory pair and the constant input difference.
The displayed states obey s1−s2=b0 and θ=(s1+s2)/2.
u=(1,1),v=(1/2,1/2) satisfy the neutral normalization.
C: θ>|b0|/2 ensures both linear-model rates are positive.
At fixed v, rate sum2θ/τ increases the projected noise variance with θ.
C: The Itô generator gives dEθ/dt=0 and dVarθ/dt=2E D when boundary terms vanish.
C: Expanding E D around deterministicθ0 gives E D=D0+D0D0″t+O(t²) with smooth local coefficients.
Integration gives Var=2D0t+D0D0″t²+O(t³), matching SI S37.
SI S37 has the displayed curvature term and zero-drift assumptions.
2D=(r1+r2)/4=θ/(2τ), so D=θ/(4τ).
C: Linear D has D″=0 and E D=D(Eθ), giving linear variance while the stated interior/boundary assumptions hold.
SI S41 and FigS1 use the variance slopeθ/(2τ), consistent with the guide's D.
SI S40 visibly printsθ/(2τ) as D while S41 uses it as2D; source PDF page9 inspected.
The summary identifies original FigureS1; its scientific content is the mutual-excitation simulation in SI page10. Exact excerpt fidelity is deferred.
C: Caption describes the plotted excitation trajectory and approximately linear variance; SI FigS1 supports that scientific statement. Exact artwork identity remains pending.''')

add('::sec:MEMORY-DRIFT-SCOPE','p111 p113 p115 p117 p119 p121',
'''Explain what the diffusion calculation leaves unknown about systematic movement. ||
Uses the distinction between mean and variance; Itô/Stratonovich are introduced as two representations needing matched drift. ||
Noise-induced mean drift is distinct from random spreading and from an arbitrarily chosen stochastic convention. ||
Microscopic spikes and nonlinear return flow determine the actual drift. ||
The leading weak-noise diffusion approximation alone does not fully determine mean motion. ||
For b=√(2D), conversion addsbb′/2=D′/2 between the two equation conventions. ||
Curved state space or return flow can shift the mean after perturbations even without a designed drive. ||
The text calculates the conversion scale D′/2 rather than presenting it as a universal physical drift. ||
This illustrates the size of a possible term, not its unique biological value. ||
Tuning away mean drift does not remove the variance of future random increments; correlations need extra analysis. ||
The microscopic jump process resolves physical drift; choosing a calculus notation alone does not. ||
Could D′/2 be mistakenly treated as the exact spike-induced drift? p115–119 explicitly denies that. SI Systematic drift pp4–5 calls it an estimate of plausible scale and says the microscopic description is needed. The guide preserves that limit.''',
'Does the passage confuse stochastic-convention conversion with a physical prediction?',
'''Nonlinear return flow can cause a nonzero mean retained displacement from symmetric local perturbations, consistent with SI Systematic drift.
SI says exact systematic drift requires a microscopic/master-equation treatment rather than the simplified diffusion limit alone.
Converting σdB with σ=√(2D) changes drift byσσ′/2=D′/2.
Differentiating b²=2D givesbb′=D′.
C: The text presents D′/2 as a possible scale, not the universal exact drift of the spike network.
C: Under the paper's large-N scaling, D and plausible noise-induced drift are order1/N.
Compensating a deterministic mean term does not cancel independent centered noise variance.
C: Correlated noise and other departures are described as extensions needing changed calculations, consistent with the paper's discussion rather than a proved universal bound.''')

add('::sec:MEMORY-FIGURES','p125 p129 p134 p140 p147 p158',
'''Read the source figures as tests of coordinate movement and estimation uncertainty. ||
Uses flow projection, diffusion and angular wrapping already derived; readout is previewed, not assumed solved. ||
Instantaneous attractor state is the endpoint of noise-free return flow from the current state. ||
Source Fig1 distinguishes internal state movement from an external reader's uncertainty. ||
Fig2 uses ring and mutual-inhibition simulations under the theoretical assumptions. ||
The caption translates visual arrows and rate bumps into memory-coordinate and measurement quantities. ||
Two successive return-flow endpoints define retained change; displacement statistics test the D prediction. ||
Ring saturation atπ²/3 and mutual inhibition's constant-D regime are the specific comparisons. ||
They are network simulations rather than animal observations. ||
The figures support their tested models; they do not establish every biological continuous attractor. ||
State diffusion and finite-sample readout error remain distinct objects. ||
Could the simulation figures be used as direct proof about measured eyes or as proof that noise stops at the ring plateau? p147–152 says simulations, and the preceding density calculation explains saturation through wrapping. Source main Fig1–2 text agrees. Exact embedded artwork/pixel acceptance is separately pending.''',
'Do the figure explanations overstate the kind of evidence shown?',
'''Main Fig1A defines the memory coordinate by noiseless flow to an attractor endpoint, not Euclidean closest point.
Main Fig1B separates movement of the bump/state from uncertainty in estimating its current coordinate.
The link to Fisher information and readout is a correct preview of main Eqs3–5, not a new result claimed from the picture.
The summary identifies original Fig1 on main PDF page2; exact embedded excerpt fidelity deferred.
C: Caption correctly distinguishes return-flow coordinate and readout uncertainty; source Fig1 supports those claims. Artwork identity pending.
Main Fig2 contains ring-attractor and mutual-inhibition network simulations.
The ring angular-error plateauπ²/3 follows SI S31–32 and the figure's wrapped convention.
The curves are model simulations, not recordings from animals, as the passage states.
The summary identifies original Fig2 on main PDF page3; exact embedded excerpt fidelity deferred.
C: Caption's simulation/theory comparison matches main Fig2; seven-panel artwork matching remains a deferred figure task.''')

add('::ch:MEMORY-INFORMATION','p3 p5 p7',
'''Determine what the information in spikes can demand of memory stability. ||
Uses projected D from the preceding chapters; Fisher information is taught next. ||
A lower bound is a restriction on the minimum possible D, not a prediction of equality. ||
The network and an observer both receive noisy spikes rather than noiseless rates. ||
The same network supplies the D and J compared in the bound. ||
Local tuning sensitivity connects the represented coordinate with count distinguishability. ||
The later Cauchy–Schwarz argument relates that sensitivity to projected noise. ||
The two-cell counterexample later shows higher J with unchanged D. ||
It concretely tests the opening's warning about bounds. ||
The notation and weak-noise Poisson scope are stated. ||
An actual network's diffusion and a best permitted lower limit are different quantities. ||
Could a larger J guarantee a more stable memory? p3–5 expressly says no; the subsequent mutual-inhibition example keeps D fixed while J rises. The opening is correctly one-sided.''',
'Does the information claim confuse a bound with an achieved performance?',
'''The chapter derives a lower bound D≥1/(2τ²J) under the stated network/noise assumptions.
Higher J reduces the lower bound but does not require the actual D to fall.
The passage explicitly defines its variance notation and local interpretation before applying it.
The previous chapter's projection result2D=Σv²r is the actual premise used below.''')

add('::sec:MEMORY-FI','p11 p34 p48 p64 p70 p76',
'''Quantify whether a short spike observation can distinguish nearby memory values. ||
Uses conditional Poisson counts and rate derivatives; score and local unbiasedness are derived here. ||
J=Σ(r′)²/r is information per unit time, while Jh is the information in duration h. ||
θ changes rates; K is observed; the score is the derivative of log likelihood with respect to θ. ||
Rates are positive, differentiable and effectively fixed during the short local observation. ||
The squared rate slope is normalized by count noise to measure nearby-state distinguishability. ||
Differentiate the log likelihood, use independent Poisson variance and Cauchy–Schwarz to get Var estimator≥1/(Jh). ||
Two Gaussian-shaped tuning curves differ only by a20 Hz baseline. ||
Their slopes match; increasing the denominator lowers information away from the peak, where both slopes vanish. ||
The local unbiased regularity and positive-rate assumptions matter; priors or other loss functions change the question. ||
Internal memory-coordinate information is separated from sensory information about an external stimulus. ||
Could Cramér–Rao guarantee an achievable exact finite-window error for any estimator? p64–70 explicitly restricts it to a local bound and notes priors and boundaries. It does not claim attainment. The score variance and the higher-baseline example are algebraically correct.''',
'Are Fisher information rate and finite-observation error being equated without the needed assumptions?',
'''Nearby coordinates with near-identical expected rates have small local statistical distinguishability under the same noise law.
The likelihood derivative scales with rate sensitivity, while Poisson noise contributes the rate denominator.
C: Differentiating Eθ[θhat]=θ gives E[(θhat−θ)S]=1 under the stated regularity/unbiasedness assumptions.
The score has zero mean because differentiating the normalized likelihood gives zero.
C: Cramér–Rao is a local lower bound, not a promise of finite-sample equality; passage explicitly says so.
Adding a prior or accepting bias changes the estimation problem and can change the applicable risk bound.
J has units coordinate^−2 time^−1, since(r′)²/r has these units.
C: The positive-rate formula gives window information Jh; rate-zero boundaries need a separate limiting argument, as stated.
Internal information concerns the currently represented state; it need not equal information about a sensory stimulus that originally generated it.
C: Holding slope fixed while adding baseline raises Poisson variance and lowers(r′)²/r; the text controls exactly that comparison.
C: For rA=5+35exp(−θ²/(2w²)),rB=rA+20,w=.6, both derivatives vanish at0 and the higher denominator lowers information elsewhere. Caption math checked; drawing deferred.
Main Eq3 and SI S42–44 give the Poisson information-rate formula and interpretation.''')

add('::sec:MEMORY-BOUND','p82 p107 p127 p139 p169 p185 p201',
'''Find the unavoidable diffusion associated with internally available spike information. ||
Uses v,u and Fisher rate; the scalar Cauchy–Schwarz and matrix positive-semidefinite arguments are supplied. ||
The scalar bound is2DJ≥τ^−2; equality means alignment of the noise-weighted projection and tuning derivative. ||
v maps noise to memory and r′ maps memory to rate changes; u=τr′ fixes their normalization. ||
Commonτ, positive rates, conditional Poisson increments and a smooth stable continuous family define the scope. ||
Vectors v_i√r_i and r_i′/√r_i connect dynamical and statistical descriptions. ||
Their dot product is1/τ, so Cauchy–Schwarz yields the bound; the residual matrix proves the multidimensional order. ||
The equal-input linear excitation model saturates without an exponential transfer; inhibition shows a strict gap away fromθ0. ||
b200,τ.1 gives D1000 at bothθ0 and100 while J rises .05→1/15 and the lower bound falls1000→750. ||
Positive rates, nonzero information and invertible multidimensional J are required; singular J is not inverted. ||
Exponential transfer is sufficient under source conditions but is not necessary for every fixed input and family. ||
Does rejecting the SI exponential-only converse overlook its quantifier? SI S51 requires a constant ratio across a span of input values. The guide's b0=0 excitation family has a common input at each θ, ratio1/θ shared by both cells but varying across states, and2DJ=τ^−2. This is a valid counterexample to an unrestricted necessity claim; the guide states the weaker source interpretation rather than declaring all of S51 false.''',
'Is the exponential-equality qualification a real mathematical distinction, and is the matrix extension justified?',
'''The derivation starts from2D=Σv²r,u=τr′ andv·u=1, exactly the prior projection setup.
Squared vector lengths are2D and J by construction.
Cauchy–Schwarz gives(1/τ)²≤(2D)J, hence D≥1/(2τ²J).
The guide labels the compact proof as a reconstruction of the paper's result rather than a verbatim derivation.
C: Commonτ, positive rates, local weak noise and conditional Poisson structure are retained assumptions.
Small J forces a larger minimum D by the inequality, for fixedτ.
Large J alone need not reduce actual D; the inequality is one-sided.
Equality in Cauchy–Schwarz requires alignment of the two weighted vectors.
Normalization givesv_i=c r_i′/r_i withc=1/(τJ).
If r_i′=0 andr_i>0, alignment requiresv_i=0 for that cell; this is included in the condition.
C: Exponential φ gives a sufficient alignment structure; necessity needs the source's stronger range-of-input condition, as the text explains.
C: Equal-input linear mutual excitation b0=0 is a valid positive-interior model within the stated tuned family.
For s=(θ,θ),u=(1,1),v=(1/2,1/2) is correctly normalized.
r1=r2=θ/τ andr1′=r2′=1/τ give J=2/(τθ),D=θ/(4τ).
The common ratio r′/r=1/θ varies between states yet equality holds at each positive θ; numerically checked atθ100,τ.1.
N: Closing div markup has no scientific assertion.
b200 activation units andτ.1s are illustrative fixed parameters.
r1,2=(b±θ)/(2τ), with opposite constant slopes±1/(2τ).
Atθ0 rates1000 each,J=.05,D1000; independently recomputed.
1/(2×.1²×.05)=1000, so the bound is attained there.
Atθ100 rates1500 and500/s.
J=25/1500+25/500=1/15, giving lower bound750.
Rate sum stays2000/s andv=(1,−1), so D stays1000.
C: J=2000/(40000−θ²) follows the two rates and slopes; caption domain excludes zero-rate endpoints. Actual plot deferred.
The gap250 atθ100 is an actual strict inequality despite increased J.
Main Eq4 states the scalar relation2DJ≥τ^−2.
Several coordinates require matrix-valued J and D, as SI S21–27 describes.
C: The displayed inverse needs positive-definite J; the assumption is explicit.
The matrix inequality is2D−τ^−2 J^−1 positive semidefinite.
Positive semidefinite means every real directional quadratic form is nonnegative.
UᵀV=I/τ under the defined noise-weighted tangent and projection matrices.
Q=V−U J^−1/τ is the residual after the stated projection, with UᵀU=J.
Expanding QᵀQ givesVᵀV−J^−1/τ²=2D−J^−1/τ².
Nonnegative QᵀQ proves the constraint for every linear combination of coordinates, not just diagonal entries.
C: A singular J has no ordinary inverse; the passage correctly stops rather than applying the formula there.''')

add('::sec:MEMORY-COMPARISONS','p214 p220 p228 p237 p249 p258 p264',
'''Judge how neuron number, firing scale, decay time and tuning width change stability under controlled comparisons. ||
Uses J,D and the replicated-population construction; the radial-width change of variables is shown. ||
Scaling claims are conditional families of models, not free biological design prescriptions. ||
Weights1/N preserve recurrent mean input while independent noise averages; τ also changes the activation-to-rate relation. ||
The section names what is fixed for each comparison, including peak rate versus total rate. ||
A width-scaled tuning function r=a f((x−c)/w) changes slopes and occupied volume together. ||
At fixed peak and center density J scales asw^(d−2); an attained bound gives D∝w^(2−d). ||
The table contrasts dimensions1,2,3 and the alternate fixed-total-rate comparison. ||
Fixed total firing makes a∝w^−d and J∝w^−2, changing the dimension conclusion. ||
Isotropy and continuum center coverage are required for the simple diagonal scaling; the bound need not be attained. ||
The section explicitly compares fixed-rate and fixed-activation changes inτ, which yield different powers. ||
Could the table prescribe wider tuning as universally better in3D? No: it states fixed peak rate and center density, assumes the bound is attained, and immediately derives the different fixed-total-rate result. The dimension powers follow one derivative factorw^−2 and integration volumew^d; no unconditional biological optimum is claimed.''',
'Are the parameter comparisons actually controlled well enough to support their conclusions?',
'''The inequality compares D and J for one network; comparisons across networks require additional fixed quantities.
C: Replication with weights1/N preserves mean recurrent input under the stated independent-copy construction.
C: That construction gives D∝1/N andJ∝N at fixed per-cell tuning, consistent with SI S2–6.
C: Firing-rate scaling changes both noise and sensitivity; the text qualifies how tuning and weights are controlled.
C: At fixed rate tuning and appropriately adjusted recurrent dynamics, v∝1/τ andD∝τ^−2.
u=τr′ andv·u=1 produce the inverseτ normalization when the projection direction is held fixed.
Squaring v inΣv²r givesτ^−2 with rates fixed.
C: At fixed activation tuning, rates scale1/τ and the matching projection leads to the differentτ^−1 diffusion scaling.
C: Width conclusions are labeled a scaling reconstruction under a particular family, not a universal theorem for all networks.
Changing variables x=c+wz supplies volumew^d; squared rate derivatives contributew^−2.
Each coordinate derivative of f((x−c)/w) introduces1/w.
Thus J∝a w^(d−2) for fixed center density and profile.
C: A common radially symmetric profile is the explicit family used in the dimension comparison.
C: Symmetric coverage/isotropy removes cross-direction terms and equalizes diagonal information components.
C: D∝w^(2−d) follows only when the information bound is attained and the other conditions hold.
The exponents give narrower benefit in1D, no leading width power in2D, and broader benefit in3D under that fixed-peak comparison.
C: Holding integrated rate fixed gives a w^d constant, hence a∝w^−d andJ∝w^−2.
The fixed-total-rate result differs because it changes the resource constraint, not because of an algebraic contradiction.
C: Equality of internal and sensory information is a special identification; the section does not assert it for biological networks generally.
The concluding comparison keeps model parameter scaling separate from a demonstrated biological optimization.''')

add('::ch:MEMORY-READOUT','p3 p5 p7',
'''Estimate a cue-time memory from later spikes while that memory continues moving. ||
Uses information rate and Brownian accumulation; finite-time inference is developed here. ||
Readout error is uncertainty about the state at the cue, distinct from storage displacement before it. ||
An observer sees future spikes; the original value and cue state are separate targets. ||
The observation interval begins only after recall is requested. ||
The noisy internal rate code becomes a time series of observations of a moving state. ||
Later samples add information but are separated from the target by new diffusion. ||
Equal weighting and ideal backward information accumulation are the compared readers. ||
Partial access changes available information rather than the full network's noise. ||
The opening does not claim a known neural implementation of the ideal reader. ||
Storage fidelity and readout quality are separated before comparing decoders. ||
Could future observations reconstruct the exact earlier random path? Under this future-only Markov model, they depend on the past through the cue state and cannot identify its particular previous increments. The opening's statement is qualified by that setup, not a claim about every possible observer with external records.''',
'Does the future-only readout limitation exclude information the model actually provides?',
'''C: Future spikes are conditioned on the cue-time state in the stated model; they cannot uniquely recover particular earlier Brownian increments without extra information.
The chapter separately treats finite observation, ideal readout and partial spike access, matching its stated purpose.''')

add('::sec:MEMORY-READOUT-SETUP','p11 p25 p35 p43 p46 p50 p56',
'''Separate storage error from inference error about the cue state. ||
Uses Brownian independent increments and local information; Gaussian observations are introduced as an approximation. ||
Θ is encoded value, x=θ(T) cue state, and xhat is inferred from future data. ||
The observer seeksΘ but its future observations directly constrainx. ||
Discrete model process noise variance2Dh and observation variance1/(Jh) are independent as specified. ||
The local spike likelihood is replaced by a Gaussian observation with matched local information. ||
Total error=(x−Θ)+(xhat−x); conditional unbiasedness and future independence make the cross covariance zero. ||
The timeline separates encoding, cue and observation endpoint. ||
Its estimate concerns the cue state, not the endpoint of the illustrated path. ||
Storage variance2DT adds to an x-independent readout variance only with the stated unbiasedness, independence and translation assumptions. ||
Biased/prior-informed estimators or state-dependent coefficients require a changed decomposition. ||
Could storage and readout error be correlated because the observation starts from x? The text conditions onx and uses E[xhat−x|x]=0; the tower property then kills the cross term. Merely assuming independent future process noise would not suffice, but the guide states the additional condition. The exactness claim is confined to this Gaussian model.''',
'Does the variance decomposition have all the conditions needed to remove its cross term?',
'''C: Future-only observations at recall timeT and the original targetΘ are explicitly specified.
C: Conditional onx, future data do not encode the particular past increments; extra records or priors would change the problem.
C: The Gaussian state-observation equations are a local approximation to spike evidence, not an exact Poisson identity.
Independent increments have process variance2Dh; the matched local observation variance is1/(Jh).
C: The recursion is exact for the stated Gaussian model; the guide distinguishes that from exact neural spiking.
Expanding Var[(x−Θ)+(xhat−x)] gives the two variances plus twice their covariance.
C: Future independence and conditional unbiasedness are explicitly required before dropping covariance.
The tower calculation E[(x−Θ)E[xhat−x|x]]=0 is valid under those conditions.
C: Translation-invariant constant-coefficient readout makes the conditional error variance independent ofx.
C: Constant-D zero-drift storage from deterministicΘ gives Var(x−Θ)=2DT.
With zero covariance, total variance=2DT+readout variance.
C: The passage explicitly limits the formula for bias, priors, boundaries or state-dependent parameters.
C: Caption and alt correctly target the cue state and list assumptions for additive variance; illustration fidelity deferred.''')

add('::sec:MEMORY-NAIVE','p60 p74 p88 p102 p109',
'''Show why equal-weight averaging eventually confuses later diffusion with better observation. ||
Uses Brownian covariance already taught and variance of independent averages. ||
Naive means a stationary-state equal-weight reader, not an undefined claim of poor reasoning. ||
Each sample contains shared accumulated process noise and independent observation noise. ||
Continuous observation limit has fixed information rateJ and state diffusionD. ||
An average of changing states is compared with the fixed cue-time targetx. ||
The double integral ofmin(s,t) gives process error2DL/3, while observation error is1/(JL). ||
Differentiating their sum gives Lnaive=√(3/(2DJ)). ||
The minimum variance is(2/√3)√(2D/J); longer equal weighting worsens it. ||
This conclusion concerns equal weights and a moving state; it does not say extra data must harm an optimal estimator. ||
The ideal reader can downweight distant observations rather than average them equally. ||
Could the process term be DL rather than2DL/3 because samples are independent? They are not: they share Brownian history. Cov=2Dmin(s,t) integrates to2DL/3. I recomputed the double integral numerically and analytically; the stated optimum follows.''',
'Is the time-averaged Brownian noise term calculated with the correct correlations?',
'''Brownian increments shared before min(s,t) give Cov[θ(s),θ(t)]=2Dmin(s,t).
For independent local observation noise at information rateJ, averaging overL yields variance1/(JL).
The symmetric double integral ofmin(s,t) on[0,L]² isL³/3; dividing byL² gives the process term2DL/3.
Setting derivative2D/3−1/(JL²)=0 givesL=√(3/(2DJ)); substitution gives(2/√3)√(2D/J).
C: Late samples worsen equal-weight estimation after that optimum; this is not a claim that optimal use of extra observations increases error.''')

add('::sec:MEMORY-IDEAL','p113 p129 p142 p154 p173 p187 p199',
'''Use future measurements optimally to infer the cue state while accounting for intervening motion. ||
Gaussian precision addition and a backward recursion are explained before the differential equation; hyperbolic functions are defined in the fold. ||
P is precision of future evidence about the current state, not state variance or a firing rate. ||
Moving backward adds transition variance before combining independent local evidence. ||
The linear Gaussian, constant-D,J model permits a scalar sufficient Gaussian likelihood. ||
Precision converts the covariance of a moving hidden state into accumulated information about the fixed cue state. ||
P/(1+2DhP)+Jh gives P′=J−2DP² and P(0)=0, hence V=√(2D/J)coth(L√(2DJ)). ||
At durations1,2,3 timesL*, variance ratios are1.3130,1.0373,1.0050. ||
Ideal error decreases to√(2D/J); the naive minimum is15.47% larger in variance,7.46% in SD. ||
The model is a benchmark observer, not a demonstrated circuit; small-h continuum limit and positiveD,J are retained. ||
An ideal reader discounts the process uncertainty separating later evidence from the cue, unlike equal weights. ||
Could the backward precision formula have the wrong Riccati sign or conflate filtering with cue smoothing? Adding transition variance weakens precision, giving the negative2DP² term. The guide targets the state at the beginning of future observation. Independent finite-bin covariance inversion converged toward its coth formula; SI S75 agrees. The SI S71 plus sign is inconsistent with S73 and is correctly flagged.''',
'Does the ideal-readout derivation solve the correct target with the correct sign?',
'''Independent Gaussian likelihood precisions add because quadratic log likelihood exponents add.
C: Future evidence has a Gaussian likelihood summarized by one mean and precision in the specified linear Gaussian model.
Marginalizing a Gaussian backward transition adds process varianceq=2Dh to likelihood variance1/P.
The resulting precision is1/(1/P+q)=P/(1+qP).
Adding the local observation givesP(L+h)=Jh+P(L)/(1+2DhP(L)).
Expansion of1/(1+2DhP) to first order givesP+h(J−2DP²)+O(h²).
Dividing the increment byh yields the stated differential equation.
P′=J−2DP² withP0=0 has a nonnegative saturating solution, consistent with information accumulating.
The definitions of sinh,cosh,tanh in exponentials and tanh derivative are correct.
Separation of variables givesartanh(P√(2D/J))=L√(2DJ), henceP=√(J/(2D))tanh(...).
Reciprocal precision gives the coth variance; SI S75 agrees. The SI S71 sign inconsistency is visible in the reopened PDF page14.
L*=1/√(2DJ) sets the transition between observation-limited and diffusion-limited readout.
coth z=1/z+z/3+O(z³), giving1/(JL)+2DL/3 at shortL.
For positivez,coth decreases to1, so ideal variance decreases to√(2D/J).
coth1=1.3130353, confirming the first quoted ratio.
coth2=1.0373147 andcoth3=1.0049698, confirming the later quoted ratios.
From2DJ≥τ^−2, L*=1/√(2DJ)≤τ; inequality direction checked.
The best naive variance divided by ideal limiting variance is2/√3=1.1547005.
The corresponding standard deviation ratio is√(2/√3)=1.0745699, not1.1547.
C: The conclusion concerns this constant-coefficient Gaussian observer; no neural implementation is claimed.''')

add('::sec:MEMORY-PARTIAL','p203 p211 p220 p224 p228 p230',
'''Calculate how limited observation changes time and error scales while the full network keeps diffusing. ||
Uses ideal/naive formulas and Poisson thinning; an information fraction is distinguished from a neuron fraction. ||
α is retained spike fraction in independent thinning or an explicitly known information fraction. ||
Observer information becomesJo; the hidden network'sD stays fixed. ||
Thinned rates and derivatives both scale byα, so Poisson Jo=αJ. ||
Partial spike availability maps into an effective information rate, not reduced internal noise. ||
SubstituteαJ intoL* andV∞ to getα^−1/2 scaling of both. ||
D=.005,J10000,α.1 compares full and partial readout over2s storage. ||
L* grows .1→.3162s, readout variance .001→.003162; total .021→.023162. ||
An arbitrary10% subset of heterogeneous neurons need not contain10% ofJ. ||
Random thinning, equal-information sampling and arbitrary cell selection are distinguished. ||
Could the paper's α fraction silently mean any subset of neurons? The guide explicitly rejects that generalization and derivesαJ only for independent thinning or a known information fraction. This resolves the main counterexample of selecting cells with zero tuning slope.''',
'Is proportional information loss justified for the kind of partial access being discussed?',
'''A downstream observer may access fewer spikes while the entire recurrent network continues generating its original fluctuations.
C: Independent Poisson thinning mapsr→αr andr′→αr′, giving each information contributionα(r′)²/r.
ReplacingJ byαJ multipliesL* and limiting readout variance byα^−1/2.
C: The text explicitly warns that an arbitrary neuron fraction is not generally the same information fraction.
N: Closing div markup has no scientific assertion.
D=.005,J10000,τ.1 are declared illustrative values;2DJ100 saturatesτ^−2.
FullL*=.1s andV∞=.001 coordinate², recomputed.
FullLnaive=√3×.1=.173205s.
Atα.1,Jo=1000 under the stated thinning/information assumption.
PartialL*=.3162278s andV∞=.003162278 coordinate².
PartialLnaive=.5477226s.
AtT2,storage variance2DT=.02; totals.021 and.023162278 are correct.
C: More future spikes improve inference of the cue state, not the particular storage trajectory already lost under the future-only model.''')

add('::sec:MEMORY-EXTENSIONS','p234 p244 p255 p270 p278 p282',
'''Determine how an added rate time constant and a changed local noise law modify the bound. ||
Uses left-vector normalization and information weighting; the two-block dynamic system is displayed. ||
τm is a rate-relaxation time in this specific model, andq is a matched local variance factor. ||
Activation and firing rate are distinct state blocks; stochastic forcing enters the activation block. ||
Symmetric weights, two first-order stages and the specified noise placement support theτ+τm result. ||
The normalized left projection maps activation noise through both time scales into coordinate displacement. ||
The left-block equations give b=τm a; normalization yields an effectiveτ+τm. Constantq scalesD byq andJ by1/q. ||
The text contrasts constantq with state-dependent/noise-weighted equality conditions. ||
It explains why the product bound can persist while the equality criterion changes. ||
An arbitrary sum of biological time constants is not claimed; matched noise/information approximations are required. ||
Poisson, constant sub-Poisson factor and more general variance laws are separate cases. ||
Could τ+τm be a universal neural integration time, or could q be added to one side only? No: p244–282 restricts the two-stage dynamics and carriesq into both diffusion and local information. SI S84's negative rate relaxation supports the guide's correction of S85's printed positive bottom-right sign; PDF page17 inspected.''',
'Are the time-scale and noise-law extensions consistent with the actual state equations?',
'''The left zero equations of the displayed two-block Jacobian implyb=τm a for the stated block conventions.
C: Stochastic forcing enters only the activation block in this model, as in SI S84–92.
Normalizing the left vector against the tangent gives the squared(τ+τm) denominator; SI S92 agrees.
C: The guide explicitly says this is not a general rule to add arbitrary biological time constants.
C: A constant matched noise factorq is assumed for the stated simple scaling, not inferred from one empirical CV number.
At fixed response and projection, variance scaling givesDq=qD; matched local Gaussian information givesJq=J/q.
The q factors cancel in2DqJq, preserving the Cauchy–Schwarz product constraint in that matched model.
C: For state-dependent variance the equality criterion uses the pointwise variance weights, not the unmodified Poisson criterion.
Changing noise weighting alters which dynamical sensitivity aligns with information; the text does not treat every non-Poisson process as identical.''')

add('::sec:MEMORY-FIG3-AND-CAUTION','p286 p292 p303 p312 p320 p330 p341',
'''Interpret readout curves and check the direction of a printed total-error bound. ||
Uses the ideal and naive formulas, partial access and the network inequality already derived. ||
Normalized error excludes storage; z=L√(2DJ) and variance unit√(2D/J) are specified. ||
The observer's finite readout error is compared with a printed claim about total memory error. ||
The sameD,J,τ must satisfy the internal inequality for the claimed substitution. ||
Converting the information bound to a bound on√(2D/J) reverses the tempting but wrong inference. ||
2DJ≥τ^−2 implies√(2D/J)≤2Dτ, so substituting2Dτ cannot establish a universal lower bound. ||
D=.005,J40000,τ.1 gives2DJ400>100 and ideal total .0205 atT2, below the printed .021. ||
The numerical strict case refutes the printed universal lower-bound form while preserving equality-case examples. ||
The guide calls it an apparent source inconsistency, not an author-issued correction; its scope is the stated model. ||
Ideal, equal-weight and partial-access curves are distinguished from storage error and from deterministic leak. ||
Could an unattainable arbitraryD,J pair make the counterexample irrelevant? The algebra already proves the claimed lower bound does not follow, and the preceding mutual-inhibition family supplies strict2DJ>τ^−2 cases. Thus the example illustrates a valid strict regime rather than creating the logical objection. The printed main Eq6 and SI S83 were checked; the guide's qualified correction is warranted.''',
'Does the proposed source-bound caution survive the strongest reasonable interpretation of the original result?',
'''Main Fig3 rescales readout variance by√(2D/J) and duration byL*; storage2DT is not in those curves.
Under that scaling ideal=cothz andnaive=z/3+1/z.
Both diverge as1/z at shortz; the next term reflects diffusion.
The naive minimum is atz=√3 with value2/√3, by differentiation.
C: SI FigS2 usesα=.1 with the paper's proportional-information assumption; useful time and error scales increaseα^−1/2.
The summary identifies original Fig3, main PDF page4; embedded artwork matching is deferred.
C: Caption's ideal saturation and equal-weight upturn agree with Fig3 and derived formulas; exact excerpt fidelity pending.
The summary identifies original FigS2, SI PDF page16; embedded artwork matching is deferred.
C: Caption's partial-access scale shift agrees with S82 and FigS2 under the stated access assumption; artwork fidelity pending.
C: Constructed-curve caption correctly givesminimum(√3,2/√3),limit1 and excludes storage; these are analytic formulas, not digitized data. Pixel acceptance deferred.
FromJ≥1/(2Dτ²), reciprocal-square-root algebra gives√(2D/J)≤2Dτ, not≥.
An upper bound on the optimal readout term cannot be substituted as its universal lower bound.
C: With proportional partial information the corresponding readout scale is bounded above by2Dτ/√α, subject to the same conditions.
The guide labels the issue an apparent inconsistency and does not claim an author-issued correction.
C: D=.005,J40000,τ.1 are an illustrative strict-inequality choice; this is not a measured biological parameter estimate.
2DJ=400 whileτ^−2=100, so the internal constraint is satisfied strictly.
√(2D/J)=.0005 while2Dτ=.001.
AtT2 the ideal total is.0205, below the printed lower-bound expression.021; numerical recomputation agrees.
Diffusion alone does not add deterministic restoring leak; SI Integration time discussion distinguishes finite memory precision from deterministic decay.''')

add('part:MECHANISMS::part-opening','',
'''The Part asks how a continuing activity pattern can lose the value it stores. ||
Chapters1–2 supply spikes, representation, variability and attractor geometry before the circuit calculation. ||
Memory accuracy is separated from activity persistence in the title and purpose. ||
Many cells jointly represent an angle; random spikes perturb the represented value. ||
The Part is explicitly about continuous-attractor memory models, with biological motivation. ||
The purpose maps a population activity pattern to an angle rather than equating one spike with a value. ||
The chapter sequence runs from variable spikes through projected diffusion to information and readout constraints. ||
The eye-angle example supplies a common concrete coordinate through the opening chapters. ||
Its role is introductory, without claiming the models are fitted to eye data. ||
The title retains the model scope and avoids a universal claim about all memory systems. ||
The later Parts address eye-drift inference and spatial-map statistics as different scientific problems. ||
Could the Part promise that persistence alone protects accuracy? Its wording says random spikes can change the angle while activity persists. All six chapter purposes support that distinction; no contrary promise found.''',
'Does the Part opening correctly describe the models and the progression that follows?','')

# Align check records with the exact packet rows and the manuscript's notation.
def unit(suffix):
    return units[next(k for k in units if k.endswith(suffix))]
def check(suffix,c,text,verdict=None):
    obj=unit(suffix)['claims'][c];obj['checked']=text
    if verdict: obj['verdict']=verdict
check('::ch:PERSISTENCE','c3','The following section derives variance2Dt and fixed-bias MSD2Dt+v²t², fulfilling the promised comparison.')
check('::ch:MEMORY-DYNAMICS','c1','The main model and SI S7–13 assume a smooth continuous set of fixed activity patterns with stable transverse modes.')
check('::ch:MEMORY-DYNAMICS','c2','The following left-vector calculation identifies the coordinate displacement retained after stable disturbances decay.','condition stated')
check('::ch:MEMORY-DYNAMICS','c3','D has memory-coordinate-squared/time units since Var displacement=2DΔt, matching SI S15.')
check('::sec:MEMORY-SPIKES','c9','Preferred angle is where the tuning curve peaks. Increasing the number of evenly sampled preferred angles with normalized weights supplies the stated large-population ring comparison.','condition stated')
check('::sec:MEMORY-LINEARIZATION','c3','K=−I/τ+diag(φ′)W and R=diag(r), so R^(1/2)=diag(√r), matching SI S7–9. The manuscript uses R for covariance strength, not amplitude.')
unit('::sec:MEMORY-LINEARIZATION')['fields'][labels[5]]='K controls first-order deterministic recovery; R is the diagonal conditional variance per time and R^(1/2) supplies its amplitudes.'
check('::sec:MEMORY-LINEARIZATION','c17','At y=0, both xdot=ay and ydot=−λy vanish for every x, giving the fixed-point line.')
check('::sec:MEMORY-LINEARIZATION','c18','Solving y=y0 exp(−λt) and integrating xdot=ay gives x∞=x0+(a/λ)y0. The chosen(0,2),a/λ=.5 endpoint is(1,0).')
check('::sec:MEMORY-DIFFUSION','c7','Many individually weak spike contributions are needed for the total-input Gaussian approximation; SI S2–6 provides the large-population basis.','condition stated')
check('::sec:MEMORY-DIFFUSION','c8','The coefficients are evaluated near one memory state, so the interval must be short enough that movement does not appreciably change them.','condition stated')
check('::sec:MEMORY-BOUND','c31','With U_iα=u_iα/√r_i and V_iα=v_iα√r_i, normalization gives UᵀV=I; u=τr′ gives UᵀU=τ²J; projection gives VᵀV=2D.')
check('::sec:MEMORY-BOUND','c32','Q=V−U(UᵀU)^−1 is the component orthogonal to U because UᵀV=I. Expanding its squared norm yields the stated bound.')
check('::sec:MEMORY-COMPARISONS','c16','For d=1, D∝w, so narrower curves reduce D in the stated fixed-peak, attained-bound comparison.','condition stated')
check('::sec:MEMORY-COMPARISONS','c17','For d=2, D∝w^0, so width has no leading power under the same stated comparison.','condition stated')
check('::sec:MEMORY-COMPARISONS','c18','For d=3, D∝w^−1, so broader curves reduce D under the same stated comparison.','condition stated')
check('::sec:MEMORY-COMPARISONS','c19','Fixed total rate implies a w^d constant, hence a∝w^−d and J∝w^−2. The passage names finite coverage, boundaries and altered noise as limits of this integral scaling.','condition stated')
check('::sec:MEMORY-COMPARISONS','c20','Mathematical compatibility does not identify a biological storage location. Equating sensory and internal tuning curves is an additional empirical premise, explicitly stated.','condition stated')
check('::sec:MEMORY-IDEAL','c9','The displayed tanh=(e^z−e^−z)/(e^z+e^−z) and artanh=.5log((1+z)/(1−z)) on(−1,1) are inverse functions; differentiating artanh gives1/(1−z²).')
check('::sec:MEMORY-IDEAL','c16','coth(2)=1.0373147207, confirming the quoted second ratio.')
check('::sec:MEMORY-IDEAL','c17','coth(3)=1.0049698233, confirming the quoted third ratio.')
check('::sec:MEMORY-IDEAL','c18','2DJ≥τ^−2 implies L*=1/√(2DJ)≤τ. The direction is correct.')
check('::sec:MEMORY-IDEAL','c19','coth continues decreasing beyondτ, so benefit does not abruptly stop. Best naive variance divided by the ideal limiting variance is2/√3=1.154700538.')
check('::sec:MEMORY-IDEAL','c20','Taking the square root of the variance ratio gives SD ratio√(2/√3)=1.074569932, hence1.075.','true as written')
check('::sec:MEMORY-PARTIAL','c3','Both the naive optimal duration√(3/(2DJ)) and its minimum(2/√3)√(2D/J) acquire the same factorα^−1/2 when J→αJ.')
check('::sec:MEMORY-PARTIAL','c8','Lnaive=.17320508s and its minimum variance=.00115470054 rad², confirming both rounded values.')
check('::sec:MEMORY-EXTENSIONS','c5','Here q is a common additive Gaussian activation-noise variance per time, independent of the cell rate. It is not a Fano-factor multiplier of Poisson variance.','condition stated')
check('::sec:MEMORY-EXTENSIONS','c6','A mean-rate observation over h has variance q/h and mean r(θ), giving information hΣ(r′)²/q; projection gives2D=qΣv². These factors use the same additive noise model.')
check('::sec:MEMORY-EXTENSIONS','c7','Cauchy–Schwarz applied to √q v_i and r_i′/√q has dot product1/τ, squared norms2D andJ, and yields2DJ≥τ^−2.')
check('::sec:MEMORY-EXTENSIONS','c8','Equality is pointwise alignment v_i∝r_i′ for constant additive q. For symmetric weights v∝g′, a constant φ′ supplies it; the previous linear-family exception keeps exponential sufficiency from becoming a universal necessity.','condition stated')
ext=unit('::sec:MEMORY-EXTENSIONS')['fields']
ext[labels[2]]='τm is a rate-relaxation time in this model; q is a common additive Gaussian activation-noise variance per time, not a rate-proportional Fano factor.'
ext[labels[8]]='The left equations give b=τm a and normalization givesτ+τm. In the separate additive-noise model,2D=qΣv² andJ=Σ(r′)²/q; Cauchy–Schwarz yields the same product bound.'
ext[labels[9]]='The explicit q example changes the Poisson rate-dependent noise weights to a constant shared strength and derives the changed equality condition.'
ext[labels[12]]='Poisson noise and constant additive Gaussian noise are distinct controlled models; the latter makes linear transfer a sufficient equality class.'
ext[labels[15]]='Could τ+τm apply to arbitrary biological time constants, or could the Gaussian noise change be treated as multiplying every Poisson variance by q? No. The passage restricts the two-stage dynamics, then explicitly sets ds=Fdt+√q dB and observes mean rates with variance q/h. Its new J and D use that same additive law. SI S84 and S92 support the time-scale result; PDF page17 confirms the printed S85 sign issue.'
unit('::sec:MEMORY-EXTENSIONS')['questions'][0]['answer']=ext[labels[15]]
unit('part:MECHANISMS::part-opening')['questions'][0]['source_refs']=['part:MECHANISMS::part-opening']

# Record reader-facing material outside extracted paragraph records without inventing unit IDs.
chapter_notes={
 '01-foundations':'Purpose and navigation correctly teach rate representations, conditional count noise, covariance and MSD before their later use. Biological setting was checked against the three primary papers and CA3/CA1 primary anatomy text.',
 '01b-persistence':'Purpose and navigation distinguish persistent activity from retained angle, introduce independent-step diffusion, and distinguish a fixed spatial map from temporal motion. The exact examples and assumptions are checked in the corresponding units.',
 '02-memory-dynamics':'Purpose and navigation trace spikes through synaptic activation and recurrent rates into a retained coordinate shift. They retain weak noise, a tuned family, and stable transverse modes; symmetry is an added specialization.',
 '02b-memory-long-delays':'Purpose and navigation correctly separate local diffusion, boundary/wrapping effects and systematic drift. Source figure summaries describe model simulations and the return-flow coordinate, not animal evidence.',
 '03-memory-information':'Purpose and navigation correctly frame a lower bound, not a guarantee of achieved stability. Fisher information measures local distinguishability and parameter comparisons specify fixed quantities.',
 '03b-memory-readout':'Purpose and navigation correctly separate the original value from the cue state, state the future-only observation problem, and compare equal weights, ideal inference and limited access. Exactness is confined to the Gaussian readout model.'}
figure_notes={
 'fig:FOUNDATIONS-POISSON-POPULATION':'Analytic Poisson count masses and K/(NΔt) moments match the example:20 Hz mean, SD20 and4.472 Hz, spacings20 and1 Hz, p0=.367879 for one cell. Truncation at100 Hz is a display statement pending pixels.',
 'fig:FOUNDATIONS-ATTRACTOR':'Rates50,30 encode5 degrees;53,33 retains5 with relaxing common component;53,27 encodes6.5. The deterministic recovery/imposed disturbance distinction is correct.',
 'fig:FOUNDATIONS-PAPER-MAP':'Three separate temporal/spatial problems and a proposed central-command eye pathway are scientifically accurate. The traces are explicitly illustrative.',
 'fig:FOUNDATIONS-DIFFUSION-BIAS':'D=.02,v=.1 imply RMS/bias crossing .4 degrees at4s, with squared contributions .16 each. RMS is not a path boundary. Number and placement of drawn paths are deferred.',
 'fig:MEMORY-TILTED-DECAY':'a/λ=.5 and(0,2) give endpoint(1,0); equal-time marks crowd exponentially, and v measuresδx+.5δy. It is a guide construction rather than a paper-network simulation.',
 'fig:MEMORY-SPIKE-TRACE':'Unit spike jumps and50ms exponential decay follow the activation equation; close spikes sum remaining activation. Exact trace/spike alignment is deferred.',
 'fig:MEMORY-INHIBITION-RATES':'b20,τ.1 give rate sum200/s,D100; positive interior |θ|<20 excludes the endpoints. These are formula curves rather than measured data.',
 'fig:MEMORY-LINE-RING':'The same D=.5 produces line MSE2Dt and wrapped error tendingπ²/3; the uniform density is1/(2π). Analytic teaching construction is correctly distinguished from simulations.',
 'fig:PAPER-MEMORY-1':'Main Fig1 supports return-flow state definition and the distinction between state motion and readout uncertainty. Exact excerpt identity is deferred.',
 'fig:PAPER-MEMORY-2':'Main Fig2 tests ring and mutual-inhibition simulations against diffusion predictions. Seven-panel/embedded-artwork fidelity is deferred.',
 'fig:PAPER-MEMORY-S1':'SI FigS1 page10 depicts mutual-excitation state motion and near-linear variance growth; the guide correctly discusses its factor-two convention issue. Exact excerpt identity is deferred.',
 'fig:MEMORY-TUNING-INFORMATION':'For the two declared positive tuning curves, slopes match, are zero at the peak, and squaring/dividing by the larger baseline rate gives lower Poisson information on each flank.',
 'fig:MEMORY-BOUND-STRICTNESS':'For b200,τ.1, J=2000/(40000−θ²),D1000; the bound is1000 at0 and750 at100. The caption specifies positive interior rates.',
 'fig:MEMORY-READOUT-TIMELINE':'The orange estimate targets cue statex, not the final moving state; the displayed variance decomposition needs the listed independence, conditional unbiasedness and translation conditions.',
 'fig:MEMORY-READOUT-CURVES':'Normalized ideal cothz tends1; equal weights z/3+1/z minimize at(√3,2/√3); storage variance is absent. These are analytic formulas, not digitized data.',
 'fig:PAPER-MEMORY-3':'Main Fig3 page4 supports ideal saturation and equal-weight upturn. Exact embedded artwork and line-style matching are deferred.',
 'fig:PAPER-MEMORY-S2':'SI FigS2 page16 supports the upward/rightward shift forα=.1 under proportional information access. Exact artwork and dotted-line fidelity are deferred.'}
fold_notes={
 'Derivation: why a Poisson count has variance equal to its mean':'The enclosed factorial-moment calculation gives VarK=λ.',
 'Mathematical definitions: covariance, variance and correlation':'The enclosed centered-moment definitions and finite-positive-SD normalization match this title.',
 'Derivation: separating spread from mean displacement':'The enclosed identity MSD=Var+mean² proves the title.',
 'Mathematical model: independent steps and Brownian motion':'The enclosed equal independent increments and Brownian limit are explicitly model assumptions.',
 'Mathematical detail: why two times share accumulated noise':'The enclosed shared-increment argument gives Brownian covariance2Dmin(s,t).',
 'Derivation: from random increments to the memory density equation':'The Itô test-function calculation and integration by parts produce∂tp=∂θ²(Dp).',
 'Check: equality can also hold with a linear transfer rule':'The equal-input excitation family gives2DJ=τ^−2 at every positiveθ with linearφ.',
 'Check: the residual matrix proves the lower bound':'QᵀQ=2D−τ^−2J^−1 is positive semidefinite under invertibleJ.',
 'Mathematical solution: hyperbolic functions and finite-time readout error':'The enclosed Riccati solution gives the positive coth variance and defines tanh/artanh/coth.',
 'Original paper figure: Burak and Fiete (2012), Figure S1':'Source SI FigureS1 is on page10; source identity label is correct; exact excerpt fidelity pending.',
 'Original paper figure: Burak and Fiete (2012), Figure 1':'Source main Figure1 is on page2; source identity label is correct; exact excerpt fidelity pending.',
 'Original paper figure: Burak and Fiete (2012), Figure 2':'Source main Figure2 is on page3; source identity label is correct; exact excerpt fidelity pending.',
 'Original paper figure: Burak and Fiete (2012), Figure 3':'Source main Figure3 is on page4; source identity label is correct; exact excerpt fidelity pending.',
 'Original paper figure: Burak and Fiete (2012), Figure S2':'Source SI FigureS2 is on page16; source identity label is correct; exact excerpt fidelity pending.'}
extras=[]
for stem,note in chapter_notes.items():
    rel='content/chapters/'+stem+'.yaml'; data=yaml.safe_load((base/rel).read_text(encoding='utf8'))
    extras.append({'source':rel,'location':'title; purpose; pedagogical_prerequisites; navigation_dependencies',
        'text':{k:data.get(k) for k in ['title','purpose','pedagogical_prerequisites','navigation_dependencies']},
        'verdict':'true as written','checked':note})
    for sec in data['section_list']:
        key=next(k for k in units if k.endswith('::'+sec['id']))
        extras.append({'source':rel,'location':'section_list[id='+sec['id']+'].title/summary',
          'text':{'title':sec['title'],'summary':sec['summary']},'verdict':'true as written',
          'checked':units[key]['fields'][labels[0]]+' '+units[key]['fields'][labels[11]],'unit_ref':key})
    for fig in data.get('blocks',[]):
        if fig.get('kind')!='figure':continue
        extras.append({'source':rel,'location':'blocks[id='+fig['id']+'].caption/alt',
          'text':{'caption':fig.get('caption'),'alt':fig.get('alt')},
          'verdict':'scientific text checked; figure acceptance deferred', 'checked':figure_notes[fig['id']]})
    md=base/'content/chapters'/f'{stem}.md'
    for n,line in enumerate(md.read_text(encoding='utf8').splitlines(),1):
        found=re.search(r'title="([^"]+)"',line) if 'publisher-' in line else None
        sm=re.search(r'<summary>(.*?)</summary>',line)
        title=found.group(1) if found else sm.group(1) if sm else None
        if title:
            assert title in fold_notes,title
            extras.append({'source':str(md.relative_to(base)).replace('\\','/'),'line':n,
              'location':'visible title attribute' if found else 'summary label', 'text':title,
              'verdict':'true as written','checked':fold_notes[title]})

assert set(units)==set(packet['units'])
assert sum(len(v['claims']) for v in units.values())==329
for key,item in units.items():
    allowed={p['id'] for p in packet['units'][key]['paragraphs']}
    for q in item['questions']:
        for ref in q['source_refs']:
            if ref==key:continue
            assert ref.rsplit('/',1)[1] in allowed,(key,ref)

source_paths=[base/'guide-project.yaml',base/'plan/chapter-plan.yaml',base/'content/index.md',base/'content/chapters/00-reading-guide.md',base/'content/chapters/00-reading-guide.yaml']
source_paths += [base/'content/chapters'/f'{stem}.{ext}' for stem in chapter_notes for ext in ['md','yaml']]
source_paths += [base/'assets/papers'/f'burak-fiete-2012-persistent-activity{suffix}.pdf' for suffix in ['', '-si']]
source_paths += [base.parent/'research'/f'burak-fiete-2012-{suffix}.txt' for suffix in ['main','si']]
source_paths += [base.parent/'research'/x for x in ['ben-shushan-2022-main-text.txt','mainali-2025-text-columns.txt','related-2026-ca3-ca1-body.txt']]
skill=Path(r'C:/Users/vital/.codex/skills/course-study-guide-builder')
source_paths += [skill/'SKILL.md',skill/'references/pedagogy-language-contract.md',skill/'references/math-code-case-contract.md',skill/'references/concept-prerequisites.md']
hashes={str(p).replace('\\','/'):hashlib.sha256(p.read_bytes()).hexdigest() for p in source_paths}

def write_result(completed):
    result={'call':{'run_id':'memory-truth-20261029-01','reviewer_id':'/root/alignment_global','stage':'truth_reasoning',
      'context':'reviewer_continuation','started_at':'2026-10-29T12:32:27.0845644+02:00','completed_at':completed,
      'input_hash':packet['input_hash'],'review_contract_hash':packet['review_contract_hash']},
      'scope':'All six Part I chapter bodies, equations, tables, footnotes, headings, sidecar purposes/navigation/captions/alt, visible fold labels, and Part I opening. This is text truth/reasoning only, not stage2/stage3 or full book acceptance.',
      'status_semantics':'Unit pass means no confirmed text truth/reasoning defect under the full reasonable passage and explicit model assumptions. It does not accept exact embedded artwork, graphical marks, rendering, links or publication.',
      'units':units,'extra_reader_text_inventory':extras,
      'source_hashes':hashes,
      'source_reopening':{'purpose':'Focused checks of ambiguous source formulas, not a book visual sweep.',
       'main_pdf_pages':[2,4],'si_pdf_pages':[9,11,14,17,19],
       'outputs':'source-formula-checks/'},
      'independent_recomputations':'memory-stage1-recomputations.json',
      'deferred':['All figure pixel/layout acceptance, including exact artwork excerpt identity, drawn line styles, counts of simulated paths and visible label placement.',
                  'Stage2 terminology/prerequisite judgments and stage3 plain-language/flow review require separate calls.'],
      'timing':{'clock':'Get-Date local offset timestamps','awake_execution':'unverified','token_stats':'unavailable',
                'verified_checkpoints':['2026-10-29T12:32:27.0845644+02:00','2026-10-29T12:38:24.1107482+02:00','2026-10-29T12:43:52.4199539+02:00','2026-10-29T12:47:39.2023558+02:00','2026-10-29T12:48:15.3394303+02:00']}}
    (out/'memory-stage1.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
    from datetime import datetime
    elapsed=(datetime.fromisoformat(completed)-datetime.fromisoformat(result['call']['started_at'])).total_seconds()
    report=f'''# Part I: truth and reasoning review

Call: `memory-truth-20261029-01`. Independent reviewer: `/root/alignment_global`. Requested configuration: Astra, high reasoning. Runtime model label and token counts are not independently exposed in this report.

Started: {result['call']['started_at']}  
Completed: {completed}  
Wall time: {elapsed:.2f} seconds, including any pauses. Awake execution time is unverified. Verified wall-clock checkpoints are stored in the JSON. No clock change was established. Earlier informal checkpoint labels are not used to compute duration.

## Result

No confirmed text truth or reasoning defect found in this call. All 29 assigned units have individual passage judgments and all 329 extracted claim rows have individual checks. I read the full assigned Markdown, including displayed mathematics and footnotes, rather than treating those rows as the complete inventory. The Part opening and {len(extras)} extra reader-text records cover chapter purposes/navigation text, sidecar captions and alt descriptions, and visible fold titles. This is a Part I truth review, not a full book acceptance or a terminology/flow pass.

The important checks were:

- `sec:MEMORY-SYMMETRIC`, paragraphs p243–p259: the squared derivative in the symmetric diffusion numerator is required by projection and SI S18. The guide correctly flags the missing square in main Eq. 2.
- `sec:MEMORY-LONG-TIME`, p84–p98: the excitation pair gives D=θ/(4τ). The source prints a factor-two inconsistency between S40 and S41; the guide keeps its own diffusion convention consistent.
- `sec:MEMORY-BOUND`, p127–p151: the linear equal-input excitation family is a valid equality case. The unrestricted exponential-only converse would be too strong; the guide's pointwise condition and qualification survive the source's strongest reasonable reading.
- `sec:MEMORY-BOUND`, p193–p210: the residual proof uses UᵀV=I and UᵀU=τ²J, giving QᵀQ=2D−τ⁻²J⁻¹. No hidden orthogonality assumption is needed for the original neural dynamics.
- `sec:MEMORY-READOUT-SETUP`, p35–p50: conditional unbiasedness and independent future noise justify zero storage/readout covariance. The passage states these assumptions instead of treating independence of increments alone as enough.
- `sec:MEMORY-IDEAL`, p129–p199: the backward precision recursion gives the negative Riccati term and the coth result. A separate finite-bin covariance inversion converges to it. The stated variance and standard-deviation ratios differ correctly.
- `sec:MEMORY-EXTENSIONS`, p244–p282: the two time constants belong to the specified two-stage model. The later constant additive Gaussian q model uses matching information and diffusion weights; it is not a rate-proportional Fano-factor substitution.
- `sec:MEMORY-FIG3-AND-CAUTION`, p320–p341: 2DJ≥τ⁻² gives √(2D/J)≤2Dτ. It cannot justify the printed universal lower bound by substitution. The guide calls this an apparent inconsistency rather than an author-issued correction.

I recomputed the Poisson example, two-cell coordinates, Brownian scales and bias crossing, ring limit, inhibition/equality cases, ideal/naive/partial readout numbers and strict-bound example. Details are in `memory-stage1-recomputations.json`. Focused source-PDF formula checks covered main pages 2 and 4 and SI pages 9, 11, 14, 17 and 19.

## Limits and next call

Caption and alt scientific statements were checked against their equations or primary source descriptions. Exact artwork excerpt identity, curve/arrow rendering, path counts, visible labels and all figure pixel acceptance remain deferred by the user's scope. A text-unit pass does not accept those items. No manuscript, packet or review ledger was changed.

The separate Stage 2 terminology/prerequisite and Stage 3 language/flow calls remain pending. In response to the root's handoff, the gain explanations are confirmed at Foundations lines 129 and 167; their first-teaching marker placement is reserved for Stage 2.

The JSON contains all source hashes, exact unit and paragraph references, claim decisions, and the extra reader-text inventory. Token stats unavailable.
'''
    (out/'memory-stage1.md').write_text(report,encoding='utf8')
    return result

if __name__=='__main__':
    import sys
    if len(sys.argv)>1:write_result(sys.argv[1])
