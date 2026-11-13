# Part I current text: Stage 1 truth and reasoning

Request: `final-memory-truth-20261029-01`. Reviewer: `/root/accept_memory`, GPT-6 Astra, high reasoning. Context: fresh. Started: 2026-10-29T13:19:31.0998773+02:00. Completion and measured durations are recorded in the companion JSON.

**Verdict: Stage 1 passes the reviewed text. No confirmed scientific or reasoning defect remains.** This is not completion of Stages 2 or 3, artwork acceptance, format acceptance or release approval. I authored none of this text and read no previous verdicts or repair reasons before reading the current manuscript.

Current input: `3fa06682def9f93bbafd2b39bfe5f3a5641febda3bbd57c2f9caf86c8b465283`. Review contract: `593934f3af51c49175417df3e4263df20a0835575d099bad4f0070163b4a17dc`.

Read all six chapter sources, all six sidecars, the Part opening and relevant earlier reading-guide context. The sources and sidecars match the supplied packet. All 29 units, 331 selected claim rows and 457 extracted paragraph records are represented in the JSON. Of the extracted paragraph records, 82 contain only hidden Vale comments; they remain identified by their original IDs and are not treated as reader prose. Equations, captions, alt text, fold labels, original-paper descriptions and sidecar summaries were read directly. The selected claim inventory contains several HTML wrappers and citation fragments, which receive an explicit non-claim judgment.

Figure labels were read from the current local images and the SVG text. This checks their meaning and mathematical labels only. No current artwork acceptance, crop-fidelity approval or layout/style acceptance is claimed. Claims that an original figure is an exact artwork excerpt remain outside this text verdict's image-fidelity scope. There are no reader code listings to execute.

## 0 ch:FOUNDATIONS
Question: Does the opening confuse persistent activity with an accurate value?
Answer: No. It asks how a useful quantity remains represented in changing activity and separates memory loss, eye-motion source and spatial firing arrangement.
Setup: Neural populations represent an eye angle or a location; the three papers study different properties of those representations.
Mechanism: The opening connects representation to signals, uncertain observations and movement statistics. Its promised distinctions are supplied in the connected chapters.
Limits: This is an overview of the specified studies, not proof of one biological circuit linking all three.
Objection: Persistent firing need not preserve the original value. The opening does not say it does, and the following persistence chapter explicitly separates the two.
Evidence: 2012 main Introduction; 2022 Introduction; 2025 model Introduction; current connected chapters.

## 1 sec:FOUNDATIONS-SPIKES
Question: Are event, rate, tuning and anatomical roles distinguished correctly?
Answer: Yes. Spikes are events, rates are expectations, synapses transmit effects and a population pattern represents a coordinate. CA3 recurrence and input to CA1 are distinguished from CA1 output maps and entorhinal input.
Setup: Presynaptic cells influence receiving cells; an observer interprets their activity pattern rather than a cell's index as physical position.
Mechanism: The local linear tuning rule has rate units spikes/s and slope units spikes/s/degree. A rate map estimates spikes per time spent at a position. Grid fields and irregular place fields are explicitly distinguished.
Limits: Negative predicted rates require modifying the local linear rule. Recorded fields have sampling uncertainty. The 2026 anatomy comparison is identified as later context.
Objection: Inferring where the position estimate is maintained merely from CA1 output maps would be unsupported. The text expressly declines that inference.
Evidence: 2022 Methods Eq. 2 and threshold restriction; 2025 Results model; 2026 CA3/CA1 Introduction and entorhinal-input discussion.

## 2 sec:FOUNDATIONS-POISSON
Question: Does the pooling example use the right uncertainty and independence assumption?
Answer: Yes. A count has mean and variance r times duration. Twenty conditionally independent 20 Hz cells in 50 ms give mean count 20 and relative SD 1/sqrt(20), about 22.4%.
Setup: Cells produce random counts conditional on fixed modeled rates; the observer pools counts and divides by duration and cell count.
Mechanism: Poisson factorial moments give E[K(K-1)]=lambda squared and Var K=lambda. With lambda=1, P(0)=exp(-1)=0.368. Per-cell rate SD is 20 Hz for one cell and 4.472 Hz for twenty.
Limits: Complete recurrent spike trains need not be independent. CV concerns intervals; Fano factor concerns counts and the counting duration.
Objection: Unconditional independence would overstate averaging. The final qualification explicitly restricts independence to elementary noise given the current modeled state.
Evidence: 2012 SI I and S43; 2022 regular OMN firing discussion; direct Poisson moments and scaling.

## 3 sec:FOUNDATIONS-COVARIANCE
Question: Do covariance and MSD distinguish the stated physical and measurement effects?
Answer: Yes. Shared input contributes covariance, private noise changes individual variance, and MSD combines variance with squared mean. Neither statistic alone locates the responsible circuit.
Setup: A central command acts through motor neurons and muscles. A spike-based prediction is an analysis result, not an extra command sent to the eye.
Mechanism: With independent components, Cov(X,Y)=g_X g_Y Var S. Expanding a centered displacement gives MSD=Var+mean squared. Independent zero-mean position errors add twice their variance to displacement MSD.
Limits: Finite second moments; nonzero variances for correlation; independent private components and measurement errors; fixed input when changing gain. A fitted tuning slope is not a muscle gain.
Objection: A larger MSD could reflect bias or measurement error rather than stronger physical noise. Both alternatives and their conditions are present.
Evidence: 2022 shared-drive Results and Methods; direct covariance, variance and gain calculations.

## 4 ch:PERSISTENCE
Question: Does the chapter opening distinguish activity changes from memory changes?
Answer: Yes. Two disturbances can affect the population differently even when activity persists; the opening promises the two-cell example, accumulation and fixed-map comparison supplied below.
Setup: A population state represents one angle; feedback removes some disturbances.
Mechanism: Stability toward a family of states does not correct neutral displacement within that family.
Limits: This introduces an ideal model family, not the behavior of every recurrent circuit.
Objection: Coherent activity need not mean the correct stored angle. The opening explicitly motivates that distinction.
Evidence: 2012 Introduction and Fig. 1; current persistence sections.

## 5 sec:FOUNDATIONS-ATTRACTOR
Question: Does the two-cell example have the claimed decaying and persistent directions?
Answer: Yes. The common deviation obeys dx/dt=-a x, while theta=(r1-r2)/(2k) has zero derivative.
Setup: Two rate activities encode angle through their difference; the specified feedback removes a common change.
Mechanism: At b=40,k=2,theta=5 the rates are (50,30). The common disturbance (53,33) gives x=3 and theta=5; (53,27) gives x=0 and theta=6.5. The fixed line is r1+r2=80.
Limits: a is positive and rates remain positive. This is a guide construction, not a fitted biological circuit. Changing k in a real network could change its dynamics too.
Objection: Perpendicular projection works in this special geometry but not generally. The passage warns about that limit and points to the later left-vector calculation.
Evidence: Direct addition/subtraction of the guide ODE; 2012 Fig. 1 and SI II.

## 6 sec:FOUNDATIONS-DIFFUSION
Question: Do the variance, bias and shared-history calculations follow from their assumptions?
Answer: Yes. Independent zero-mean increments with variance 2D delta-t sum to variance 2Dt. Brownian motion is introduced as a continuous small-increment approximation.
Setup: Lasting spike disturbances change a represented angle; repeated trials reveal its spread.
Mechanism: At D=.02,t=.35, variance=.014 and RMS=.11832 degrees=7.099 arcmin. With v=.1, MSD=v squared t squared+2Dt; the two contributions equal .16 at t=4. Shared history gives covariance 2D min(s,t).
Limits: Constant variance rate, zero mean for pure diffusion, appropriate limiting scales and no relevant boundary. Ring error and changing D require separate treatment. RMS is not a bound on individual paths.
Objection: A path can return while ensemble spread grows. The text and figure labels distinguish these quantities and separate deterministic bias.
Evidence: 2012 SI III S28-S32; direct variance addition and Brownian increment identities.

## 7 sec:FOUNDATIONS-RANDOMNESS
Question: Is spatial randomness confused with changing spike noise?
Answer: No. A function drawn for a cell and environment remains fixed as the animal visits positions; actual spikes can differ across visits.
Setup: The spatial function determines an expected rate at each location, while temporal memory noise moves a stored coordinate.
Mechanism: Space and time are distinct independent variables. A distribution of place-field shapes does not determine temporal memory diffusion, or conversely.
Limits: The fixed map is a model assumption. The schematic does not establish a single circuit joining the three studies.
Objection: The diagram's same-rate label could be read as identical spike counts. Its axis says expected rate, and adjacent prose explicitly permits visit-to-visit spike variation.
Evidence: 2025 Results Gaussian-process model; 2012 dynamical model; current figure labels.

## 8 ch:MEMORY-DYNAMICS
Question: Are the dynamical target and units consistent with the earlier foundation?
Answer: Yes. Theta is the initial value, theta is its later value, and barred rates denote deterministic steady states.
Setup: Recurrent spikes maintain a tuned family of activity patterns while random events perturb it.
Mechanism: D has coordinate squared/time units and equals half the variance slope when it is constant and boundaries do not matter. The chapter then derives the retained displacement.
Limits: Drift-free diffusion is supplied in the preceding foundation and the later drift check. An arbitrary recurrent network is not assumed to have a continuous family.
Objection: Persistent firing is not proof of memory accuracy; the opening states the distinction rather than equating them.
Evidence: 2012 main Model; SI I-II; preceding persistence chapter.

## 9 sec:MEMORY-SPIKES
Question: Does the spike-to-rate model preserve event size, units and approximation scope?
Answer: Yes. A spike adds one to dimensionless activation s; weights change receiving input, phi converts input to a nonnegative rate and tau sets decay.
Setup: Outgoing counts change activation, weighted activation plus bias determines input, and input sets subsequent spike intensity.
Mechanism: ds=-s/tau dt+dN has conditional drift F and leading covariance r dt. The weak aggregate-input approximation gives sqrt(r)dB. Replicating populations with weights 1/n preserves mean input and reduces its variance as 1/n. Steady s=tau r.
Limits: Conditional elementary independence, weak input fluctuations and leading large-population terms. It does not claim each entire spike train is Gaussian or independent.
Objection: A changing-rate process is not an exact independent Poisson law for arbitrary finite bins. Short dt and conditional intensity are explicit, so that stronger reading is not required.
Evidence: 2012 main Eqs. 7-11; SI I S1-S6.

## 10 sec:MEMORY-LINEARIZATION
Question: Why does the left vector give the lasting coordinate change?
Answer: Differentiating the fixed-point family gives Ku=0. A left null vector normalized by v transpose u=1 removes decaying modes and extracts the lasting tangent displacement.
Setup: K evolves a small activation disturbance; u is the neutral direction and v measures its represented-coordinate change.
Mechanism: K=-I/tau+diag(phi prime)W has inverse-time units. For a nonzero eigenvalue mode, v transpose z=0. In the tilted example integration gives x infinity=x0+(a/lambda)y0, giving shift one for the plotted parameters.
Limits: A smooth family, one neutral direction, all other modes decaying and small disturbances. Symmetric W does not generally make K symmetric.
Objection: A vertical perturbation can change final memory. The worked ODE and left vector capture that shift; perpendicular projection would miss it.
Evidence: 2012 SI S7-S16; direct two-variable ODE solution; current figure parameters.

## 11 sec:MEMORY-DIFFUSION
Question: Does noise projection give the scalar and multidimensional covariance formulas?
Answer: Yes. Left projection removes local deterministic flow; independent Brownian increments leave sum v_i squared r_i as the variance per time, equal to 2D.
Setup: Each cell generates activation noise, and network return flow determines how much remains in the coordinate.
Mechanism: dtheta=sum v_i sqrt(r_i)dB_i. With several coordinates, using v_i alpha gives 2D_alpha_beta=sum v_i alpha r_i v_i beta, including coupled coordinate shifts.
Limits: Leading local weak noise; coefficients evaluated near a fixed point; enough aggregate events but little coefficient change. Systematic drift needs its separate check.
Objection: A high rate alone does not imply worse memory because tuning and projection weights can also change. The interpretation explicitly requires that comparison.
Evidence: 2012 SI S14-S15 and S21-S27; direct covariance projection.

## 12 sec:MEMORY-SYMMETRIC
Question: Is the symmetric formula and mutual-inhibition example correct?
Answer: Yes. Symmetry makes g prime a left null vector; normalization gives v_i=g_i prime/[tau sum r_j prime g_j prime], whose square belongs in the noise variance.
Setup: Equal reciprocal connection weights can still produce unequal firing responses through the transfer function.
Mechanism: r prime=phi prime g prime and g prime=tau W r prime imply K transpose g prime=0. Mutual inhibition has a decaying sum and neutral difference, so 2D=b/tau. At b=20,tau=.1 the rate sum is 200 and D=100.
Limits: Stable continuous family, positive-rate interior, noise assumptions and invertibility only where phi inverse is used. Translation symmetry is unnecessary.
Objection: Main Eq. 2 appears to lack a numerator square. Direct projection and SI S18 require it, and the guide correctly labels this as an independent source inconsistency.
Evidence: 2012 main Eq. 2 and Fig. 2E-G; SI S16-S18; direct projection.

## 13 ch:MEMORY-LONG-DELAYS
Question: Is local diffusion kept distinct from long-delay error?
Answer: Yes. The opening lists wrapping, boundaries, state-dependent spreading and systematic mean motion as reasons a local slope alone is insufficient.
Setup: Repeated trials begin from one stored value and evolve without anchoring input.
Mechanism: The introduction restricts 2Dt to constant D before boundaries matter and without systematic drift, then motivates evolving the full density.
Limits: A model prediction and simulation interpretation, not a claim of indefinitely increasing bounded angular error.
Objection: Saturation does not disprove positive local diffusion. The chapter explicitly proposes the bounded-reporting explanation.
Evidence: 2012 SI III and current connected long-time section.

## 14 sec:MEMORY-LONG-TIME
Question: Do the density equation and excitation example follow from the stated stochastic model?
Answer: Yes. A zero-drift Ito increment has generator D F double-prime; the density equation differentiates Dp twice. Constant D gives Gaussian and wrapped-Gaussian solutions, with wrapped error tending to pi squared/3.
Setup: The density records the distribution of the stored coordinate across trials initialized at Theta.
Mechanism: Integration by parts gives the density and moment equations. dVar/dt=2E D and dE D/dt=E[D D double-prime] yield the stated t squared term. Excitation has v=(1/2,1/2), rate sum 2theta/tau, so D=theta/(4tau).
Limits: Zero Ito drift, valid boundary terms, constant D for the line/ring comparison and the positive-rate excitation domain theta>|b0|/2. Interior formulas do not determine boundary behavior.
Objection: Printed S40 disagrees by a factor of two with projection and S41. The guide states this accurately and preserves the source rather than claiming an author correction.
Evidence: 2012 SI S28-S41 and Fig. S1; direct generator and moment checks.

## 15 sec:MEMORY-DRIFT-SCOPE
Question: Does the variance calculation incorrectly settle systematic drift?
Answer: No. Deterministic mistuning and possible noise-induced mean motion are separate from random spread. The convention comparison estimates a possible scale rather than the exact circuit drift.
Setup: Weights, biases and state-dependent noise affect movement along the attractor.
Mechanism: With b=sqrt(2D), the Stratonovich-to-Ito correction b b prime/2 is D prime/2. D of order 1/N gives random size sqrt(dt/N) and mean displacement dt/N. Correlated noise changes projection to v transpose Q v.
Limits: Exact drift needs the microscopic model. Conditional elementary independence is weaker than whole-train independence; the correlated-model extension is not proved by the paper.
Objection: Subtracting a known mean cannot remove random increments. The text limits possible tuning corrections to mean motion and keeps decoder conditions visible.
Evidence: 2012 SI Systematic drift pp. 4-5; main Discussion on correlated models.

## 16 sec:MEMORY-FIGURES
Question: Do the figure explanations accurately distinguish simulation and readout claims?
Answer: Yes. Figure 1 defines the coordinate through noise-free return and separates displacement from readout uncertainty. Figure 2 tests diffusion in ring and mutual-inhibition networks, not animals.
Setup: A simulated network evolves; an observer has a finite spike sample with which to estimate its state.
Mechanism: Panel C compares predicted diffusion and the sigmoid information bound; panel D wraps angular error and tends to pi squared/3. The inhibition example tests a design without rotation symmetry.
Limits: Source simulations and schematics. Original Fig. 1 uses an inverse-information label schematically; the next chapter explicitly distinguishes rate J from finite-duration information Jh.
Objection: The dashed sigmoid bound is not a fitted trajectory, and saturation does not mean noise stops. The current prose explicitly makes both distinctions.
Evidence: 2012 main Figs. 1-2 and captions; SI S31-S32; current source-figure labels.

## 17 ch:MEMORY-INFORMATION
Question: Does high information guarantee low diffusion in the opening?
Answer: No. It describes a lower bound for one network and explicitly says high information permits, but does not ensure, better stability.
Setup: The same spikes are observed externally and feed back within the memory circuit.
Mechanism: Local distinguishability is connected to the previously derived retained noise; the following proof supplies the quantitative relation.
Limits: Applicable model assumptions and controlled comparisons, not a theorem about every noisy memory system.
Objection: Confusing a lower allowed value with actual circuit performance is blocked by the opening's explicit qualification.
Evidence: 2012 main Eqs. 3-4; SI IV-V; current inequality and examples.

## 18 sec:MEMORY-FI
Question: Is the information and inverse-error calculation valid for the stated observer?
Answer: Yes. Conditional Poisson counts give score sum (r prime/r)(n-rh), whose expected square is h sum r prime squared/r. Regular local unbiasedness and Cauchy Schwarz give variance at least 1/(Jh).
Setup: An observer uses short population counts to distinguish nearby internal states.
Mechanism: The score has zero mean, cross terms vanish by conditional independence and differentiation of mean estimator=theta gives covariance with the score equal to one. J has inverse-coordinate-squared/time units.
Limits: Positive regular rates, locally constant state and unbiased regular estimation. Finite-sample attainability, informative priors and global ambiguities are not assumed away silently.
Objection: Peak rate alone is not local information. The two illustrative curves have equal slopes and different baselines; at the peak slope is zero, and extra baseline lowers information elsewhere.
Evidence: 2012 SI S42-S44 and main Cramer-Rao discussion; direct score and unit checks.

## 19 sec:MEMORY-BOUND
Question: Does the inequality and equality discussion survive the stated counterexample?
Answer: Yes. Cauchy Schwarz gives 2DJ at least tau^-2. Equality requires cellwise matching of retained-noise and information weights. An exponential transfer is sufficient for symmetric weights, but is not generally necessary.
Setup: Return-flow weights determine retained spike noise; rate slopes and count variability determine information.
Mechanism: The normalized dot product is 1/tau. In zero-bias linear excitation, 2D=theta/(2tau) and J=2/(tau theta), attaining equality. In inhibition, J=.05,D=1000 at zero and J=1/15 with lower bound 750 at theta=100. Expanding Q transpose Q proves the matrix bound.
Limits: Positive rates, applicable weak-noise family, and invertible J for the ordinary inverse. A common ratio at one state need not be the same ratio across different states.
Objection: The source's converse is too strong without additional restrictions linking participating inputs. The guide's linear family has the correct fixed states, decaying transverse mode and equality algebra, so its qualification is justified.
Evidence: 2012 SI S45-S56; independent linear-family and residual-matrix checks.

## 20 sec:MEMORY-COMPARISONS
Question: Are the parameter and width comparisons sufficiently controlled?
Answer: Yes. The text says what is held fixed and explicitly adds radial tuning and uniform centers before treating inverse matrix entries as reciprocal diagonal information.
Setup: Network choices determine tuning, spike variability and projection; an observer reads the resulting rates.
Mechanism: Replication gives J proportional N and D inverse N. Matched rate scaling gives J proportional a and D inverse a. Fixed rate/input curves give inverse tau squared, while fixed activation curves give inverse tau. The width substitution gives J proportional w^(d-2).
Limits: Fixed peak, shape and center density; interior continuum approximation; radial tuning and bound attainment for D proportional w^(2-d). Fixing total spike budget instead gives J proportional w^-2.
Objection: General coupled information matrices cannot be inverted entry by entry. The explicit radial-symmetry condition makes off-diagonal entries zero before the scalar comparison, so that objection is resolved.
Evidence: 2012 main scaling and tuning-width discussion; direct change of variables, resource comparison and matrix check.

## 21 ch:MEMORY-READOUT
Question: Does the opening separate the original value, cue state and later state?
Answer: Yes. Later spikes estimate the cue value and do not reveal the particular random displacements before it. T and L separately denote storage and observation.
Setup: An observer starts receiving spikes after the recall cue while the network continues moving.
Mechanism: The opening motivates storage versus readout uncertainty, then equal weighting, ideal inference and partial access.
Limits: The following calculation supplies a local drift-free, constant-D model without relevant boundaries or an informative prior.
Objection: Future observations cannot reconstruct every past random increment. The opening explicitly limits recovery and the next section states the independence assumptions.
Evidence: 2012 SI VI opening and S57-S63; current setup.

## 22 sec:MEMORY-READOUT-SETUP
Question: Why may storage and readout variances be added?
Answer: Zero conditional readout bias at every cue state and future noise independent of storage imply E[s e]=0. Translation invariance makes readout variance the same at each cue value.
Setup: The observer estimates x=theta(T); storage error is s=x-Theta and readout error is e=xhat-x.
Mechanism: Var(s+e)=Var s+Var e+2Cov(s,e). Conditional expectation removes the covariance and Var s=2DT supplies the storage term. Discrete transition and observation variances are 2Dh and 1/(Jh).
Limits: Independent Gaussian errors in the stated local approximation, constant D, unbiasedness, no relevant drift/boundary/prior and translation invariance. Infinitesimal bins are not asserted to contain physically many spikes.
Objection: Independent process and observation noise are modeling assumptions, not established for every neural circuit. The text explicitly scopes its exact derivations to that Gaussian model.
Evidence: 2012 SI S57-S63; direct total-variance and conditional-expectation calculation; current timeline labels.

## 23 sec:MEMORY-NAIVE
Question: Does equal weighting give the stated variance and optimum?
Answer: Yes. Later state observations share earlier Brownian increments, so motion contributes a double covariance integral, not independent-state variances.
Setup: A stationary-state decoder averages later noisy observations of a moving state.
Mechanism: The integral of min(s,t) over the L square equals L cubed/3. Thus V=2DL/3+1/(JL); differentiation gives L optimal=sqrt(3/(2DJ)) and minimum=(2/sqrt3)sqrt(2D/J).
Limits: Constant-D local Gaussian readout with independent observation errors and correlated state history.
Objection: Ignoring shared history would lose the motion term. The explicit triangle integral accounts for it.
Evidence: 2012 SI S76-S81; direct covariance integration and differentiation.

## 24 sec:MEMORY-IDEAL
Question: Does backward precision accumulation produce the stated result and time interpretation?
Answer: Yes. Transporting a later likelihood backward adds transition variance; the new independent observation adds precision. The recursion gives P prime=J-2DP squared and P(0)=0.
Setup: An ideal observer estimates the cue state from later evidence; no implementing neural circuit is claimed.
Mechanism: The solution is P=sqrt(J/(2D)) tanh(sqrt(2DJ)L), whose reciprocal gives the stated coth variance. Coth at 1,2,3 gives 1.313,1.037,1.005. L star is at most tau, while the naive optimum is at most sqrt3 tau.
Limits: No informative prior, local constant coefficients and the stated Gaussian continuum approximation. Saturation is gradual, not a hard cutoff at tau.
Objection: Printed S71 has a sign inconsistent with S73. The guide's independent recursion produces S75 and flags that issue. It correctly separates variance ratio 1.155 from SD ratio 1.075.
Evidence: 2012 SI S58-S75 and S80-S81; direct recursion, expansion and ratio checks.

## 25 sec:MEMORY-PARTIAL
Question: When does a fraction of spikes equal the same fraction of information?
Answer: Independent thinning with fixed probability alpha scales both rates and slopes by alpha, so observed J=alpha J while the full network D stays fixed.
Setup: A downstream observer receives fewer spikes from an unchanged memory network.
Mechanism: Substituting alpha J scales useful duration and limiting variance by alpha^-1/2. At tau=.1,J=10000,D=.005 the full values are .1 s and .001; at alpha=.1 they are .3162 s and .003162. T=2 adds .020 in both cases.
Limits: Positive alpha, unbiased independent thinning and the same local readout approximation. A selected neuron subset must carry the stated information fraction; a count fraction alone is insufficient.
Objection: Neurons with different slopes contribute different information. The current selected-subset warning prevents equating neuron fraction with information fraction automatically.
Evidence: 2012 SI S82 and Fig. S2; Poisson thinning and substitution.

## 26 sec:MEMORY-EXTENSIONS
Question: Do the two-time-constant and Gaussian-noise extensions preserve their assumptions?
Answer: Yes. Rate relaxation adds a second state block, while modeled spike noise enters only the synaptic block. Normalization gives tau+tau_m. Constant noise changes information weighting and makes a linear transfer sufficient for equality.
Setup: Synaptic activation and firing rate adjust in two stages; the alternative model has independent additive Gaussian noise of common strength q.
Mechanism: The block matrix has negative rate decay. Left-null equations give b=tau_m a and normalization gives the displayed a_i. For constant q, J=sum r prime squared/q and 2D=q sum v squared, retaining the Cauchy Schwarz bound.
Limits: Symmetric weights for the shown extension, its noise placement and stable family. Arbitrary biological time constants cannot simply be added. Both transfer-function classes are sufficient, not universal necessities.
Objection: A general rule that linearity is best would be unsupported. The text links each sufficient condition to its particular noise weighting and preserves the earlier pointwise criterion.
Evidence: 2012 SI S84-S95; direct block-matrix and Gaussian-score calculation.

## 27 sec:MEMORY-FIG3-AND-CAUTION
Question: Is the printed total-error lower bound correctly qualified?
Answer: Yes. From 2DJ at least tau^-2 follows sqrt(2D/J) at most 2D tau. Substituting this upper bound cannot establish the printed universal lower bound on total error.
Setup: The ideal observer estimates the cue state and adds storage uncertainty. A neural integrator can keep the mean accumulated signal while uncertainty grows.
Mechanism: Rescaled readout curves are coth z and z/3+1/z. At D=.005,J=40000,tau=.1, readout variance tends to .0005 while 2D tau=.001. At T=2 the totals are .0205 and .021, exposing the inequality-direction issue.
Limits: The guide's defensible lower limit is 2DT+sqrt(2D/J) within the local Gaussian model. This is an independent formula check, not an author-issued correction or an original-network reproduction. Plotted readout curves exclude storage variance.
Objection: A saturation special case cannot justify a universal lower bound. The strict example checks that error directly. The concluding paragraph also correctly distinguishes diffusion from a deterministic restoring leak.
Evidence: 2012 main Eqs. 4-6 and Fig. 3; SI S75,S79-S83 and Integration time constant p. 17.

## 28 part:MECHANISMS::part-opening
Question: Does the Part opening fit the six chapters without overgeneralizing?
Answer: Yes. It scopes the result to a model circuit, distinguishes sustained activity from a changing angle and accurately maps the chapters to signals, diffusion, information and readout.
Setup: A model population represents an angle through firing patterns and continues to generate random spikes.
Mechanism: The reading sequence supplies neural definitions and accumulation, projected diffusion and long-time limits, then the information bound and moving-state readout.
Limits: The title explicitly names continuous-attractor models; no universal biological memory theorem is asserted.
Objection: Noise need not make activity stop. The purpose instead states that the represented value can change while activity persists, which matches the models.
Evidence: Actual chapter-plan opening and the six connected chapter sources.

Token stats unavailable. Awake execution time unverified. No system-clock change was observed during the call.

Completed: 2026-10-29T13:32:27.9929590+02:00. Stage 1 wall time: 776.9 seconds. Since preceding persisted checkpoint: 281.4 seconds. Wall time since preparation began: 1663.9 seconds, including the wait for Stage 1 authorization. Awake execution time unverified.
