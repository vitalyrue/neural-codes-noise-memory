# Memory and foundations: stage 1 truth and reasoning

Local request ID: memory-stage1-20261022T192719+0300. Reviewer: independent agent /root/review_memory_guide. Requested model configuration in PLAN: GPT-6.1-sol/high; exact platform model/version is not exposed to this reviewer. Scope is stage 1 only. No chapter edits, build, historical review, or writer defense was used. The writer numeric script/results were consulted only after the independent open read and mathematical assessment.

Started: 2026-10-22T19:27:19.1583625+03:00. Checkpoints: 19:28:24.1891869, 19:29:00.2935096, 19:29:39.6592549, 19:30:25.4895174, all on 2026-10-22 +03:00. Completion time and source/rule SHA256 values are in memory-stage1.json. Wall-clock elapsed is measured there. Awake execution duration is unverified; sleep/resume logs were not inspected. Token stats unavailable.

## Verdict

Changes required before stage 1 acceptance: one false necessity claim in the central equality discussion, one incorrect source-equation correspondence, and one missing derivation connecting state-dependent random increments with the density equation. The spike-to-diffusion derivation, scalar/matrix information bounds, readout calculations, scaling caveats, and most source inconsistency checks are sufficient as written. This is not acceptance of stages 2 or 3 or of unread chapters.

Audience: undergraduate calculus, basic probability, linear algebra; no assumed neuroscience, stochastic processes, Fisher information, or control theory. I read all four files in order, including every equation and footnote, before applying the targeted checks. There are no reader tables in these files. The foundations figure's text, plotted coordinates, arrow directions, and labels were checked in its SVG source; final caption/alt text are not yet supplied by the empty visual ledger, so root must include those in its asset review.

## Findings

### M1: exponential transfer is sufficient, but the claimed necessity has a counterexample

Location: `03-memory-information.md`, `sec:MEMORY-BOUND`, lines 103–117, especially “Therefore equality requires ... constant over the participating input range” and the stated continuous-range qualification. Related sufficient derivation: lines 80–108. Earlier setup checked: `02-memory-dynamics.md`, lines 173–216 and 277–284. Source checked: SI pp. 10–12, S45–S56, especially the same converse in S50–S51.

The equality condition is pointwise in memory state. The proportionality factor may change with that state. A continuum of input values across different states does not force one common exponential slope.

Counterexample within the guide's own model: set W12=W21=1, W11=W22=0, b0=0, and phi(g)=g/tau for positive inputs. The continuous attracting family is s1=s2=theta>0. Its linear matrix is (-I+W)/tau, with eigenvalues 0 and -2/tau. Thus u=(1,1), v=(1/2,1/2), r1=r2=theta/tau, and r1'=r2'=1/tau. Directly,

- 2D=theta/(2 tau).
- J=2/(tau theta).
- 2DJ=1/tau^2 at every theta>0.

This is a linear transfer function saturating the bound across a continuous input range. Each state has the same input in both cells, so the common ratio phi'/phi=1/theta can change between states. Numerical independent check at tau=.1, theta=100 gave K u=0, v^T K=0, v^T u=1, eigenvalues (-20,0), 2D=500, J=.2, and 2DJ=100=tau^-2.

Repair: keep the exact pointwise condition v_i=c r_i'/r_i and exponential sufficiency. Restrict necessity to a continuous range of participating input values that co-occur in a state, or state an additional overlap condition that forces the proportionality factor to be the same across states. Explain the counterexample, because the source's blanket converse has the same limitation. Do not present a source claim as proof when its extra condition is missing. Priority: high, central false mathematical implication.

### M2: the guide formula does not literally match printed main Eq. 2

Location: `02-memory-dynamics.md`, `sec:MEMORY-SYMMETRIC`, line 216, “This is main Eq. 2”; source footnote line 317. Checked the actual PDF page 2 image and text, not only secondary notes. The supplied six-page Early Edition main PDF prints a numerator with a single power of d g_i/d theta. SI S18, the projected covariance calculation, dimensional consistency, and the guide correctly have the square.

Repair: retain the guide's correct formula. Say it follows from SI S18 and point out that the supplied main Eq. 2 appears to omit the square. This matters because a reader checking the linked source otherwise sees different equations with no explanation, while the reading guide promises to identify apparent printed inconsistencies. Priority: medium, source correspondence and mathematical verification.

### M3: derive why D is inside both density derivatives

Location: `02-memory-dynamics.md`, `sec:MEMORY-LONG-TIME`, lines 237–268. Earlier teaching checked: foundations diffusion and covariance, lines 145–194; local projection, dynamics lines 146–179. The density equation is correctly stated, and the later integration-by-parts moment calculation is correct. But the transition from the random increment to partial_t p=partial_theta^2(Dp) is asserted. This is a consequential missing reasoning step for an audience with no stochastic-process background: partial_theta(D partial_theta p) would describe another process when D varies and would alter the mean drift.

Repair: before relying on the PDE, expand a smooth test function over one Itô increment: E[f(theta+dtheta)-f(theta)|theta]=D(theta) f''(theta) dt+o(dt), using zero mean and variance 2D dt. Average over p and integrate by parts twice to obtain the displayed density equation. The same argument with f=theta, theta^2, and D immediately supplies the moments already used. This is a short derivation using the declared calculus/probability baseline, not a demand for a stochastic-calculus course. Priority: medium, missing bridge in a core derivation.

## Passage-based decisions by section

Line ranges refer to the frozen source hashes in JSON. Each row covers every paragraph, display equation, inline mathematical claim, and footnote call within its range. Whole footnote definitions are assessed separately below. Reasons retain sufficient passages rather than inventing defects.

| File and section ID | Lines | Strongest substantive check and decision |
|---|---:|---|
| 00, ch:READING-GUIDE opening | 1–3 | Retain: the three papers concern neural representations with different mathematical objects; the reconstructible-calculation aim is appropriate, but acceptance remains pending M3. |
| 00, sec:READING-START | 5–9 | Retain: assumed undergraduate baseline is explicit; place-field route does not depend on memory readout. The glossary is correctly limited to lookup after teaching. |
| 00, sec:READING-PAPERS | 11–19 | Retain bibliographic/layout distinctions: P1 six main pages and 20 SI pages match the local source; no author-confirmed correction is invented. Add M2 at the affected formula. Link behavior is root's output check. |
| 00, sec:READING-SCOPE | 21–27 | Retain: reconstructed examples and numerical checks are not represented as experimental reproduction; D versus d and theta versus q have separate meanings. The general full-derivation claim needs M3 resolved. |
| 01, ch:FOUNDATIONS opening | 1–5 | Retain: coherent activity and correct stored coordinate differ, illustrated by the later two-direction example. Does not claim all representations are persistent attractors. |
| 01, sec:FOUNDATIONS-SPIKES | 7–25 | Retain: rate is expected count per time, vector position is neuron identity, and map estimation divides spikes by occupancy. Negative-rate limitation and CA3/CA1 context avoid false biological implications. Anatomy checked against local 2026 primary text. |
| 01, sec:FOUNDATIONS-POISSON | 27–52 | Retain: factorial moments give mean/variance lambda and relative SD 1/sqrt(lambda). Increasing rate changes absolute as well as relative noise. |
| 01, sec:FOUNDATIONS-COUNT-EXAMPLE | 54–62 | Retain: e^-1=.368, population count SD=sqrt(20), relative SD=.224. Conditional independence is distinguished from independent recurrent spike trains. CV and Fano factor are not equated. |
| 01, sec:FOUNDATIONS-COVARIANCE | 64–99 | Retain: covariance units, sum/difference signs, zero-covariance caveat, and MSD=variance+mean^2 are correct. Correlation is not assigned a causal variance fraction without a model. |
| 01, sec:FOUNDATIONS-ATTRACTOR | 101–105 | Retain: restoring transverse dynamics and neutral tangent distinguish stable activities from retained coordinate. A ring's coordinate is periodic. |
| 01, sec:FOUNDATIONS-ATTRACTOR-EXAMPLE | 107–143 | Retain: x decays, theta is fixed, common perturbation returns to (50,30), tangent perturbation holds 6.5 degrees. Figure solid/dashed arrows represent different actions and match SVG coordinates. |
| 01, sec:FOUNDATIONS-DIFFUSION | 145–167 | Retain: independent zero-mean increments give 2Dt; Brownian approximation and equal-coordinate multidimensional convention are qualified. Does not promise monotone motion on a path. |
| 01, sec:FOUNDATIONS-DIFFUSION-EXAMPLE | 169–194 | Retain: .35 second RMS=7.10 arcminutes, bias crossover=4 seconds. Shared Brownian increments explain min(s,t) covariance. Ring and boundary limits are acknowledged. |
| 01, sec:FOUNDATIONS-RANDOMNESS | 196–200 | Retain: sampled spatial function remains fixed within the model while spike noise remains variable; neither spatial irregularity nor diffusion determines the other's statistics. |
| 02, ch:MEMORY-DYNAMICS opening | 1–5 | Retain: theta versus initial Theta and 2D convention are consistent; constant-coefficient boundary qualification is present. |
| 02, sec:MEMORY-SPIKES | 7–71 | Retain: jump/decay process, compensated increment, Gaussian approximation, and n-replication scaling match SI S1–S10. The approximation concerns summed input, not Gaussian individual spikes. Fixed-point family requires tuning. |
| 02, sec:MEMORY-LINEARIZATION | 73–144 | Retain: K rows carry phi'_i, u=tau r', v^T K=0, and normalization are correct. Tilted two-variable example proves why an orthogonal projection can fail. |
| 02, sec:MEMORY-DIFFUSION | 146–179 | Retain: independent Brownian covariance removes cross terms and yields 2D=sum v_i^2 r_i; tensor factors and coupled coordinates are correct. This is local leading weak noise, not exact finite-network dynamics. |
| 02, sec:MEMORY-SYMMETRIC | 181–231 | Revise source identity M2; retain math: K^T g'=0 follows from symmetric W, normalized v is correct, and two-cell inhibition has 2D=b/tau with activation-difference coordinate. |
| 02, sec:MEMORY-LONG-TIME | 233–284 | Revise missing density bridge M3; retain Gaussian/wrapped solution, pi^2/3, moment identities and D D'' t^2 coefficient. Mutual-excitation D=theta/(4tau) agrees with S41 and exposes S40's factor discrepancy. |
| 02, sec:MEMORY-DRIFT-SCOPE | 286–296 | Retain: noise-induced mean drift is separate from variance, Itô/Stratonovich conversion D'/2 is correct, and correlated innovations require a new likelihood. The paper's wider correlated-model claim remains conjectural. |
| 02, sec:MEMORY-FIGURES | 298–310 | Retain: actual Figs.1–2 confirm flow-based state definition, rate/realized-spike distinction, wrapped-angle saturation, and simulations rather than animal measurements. |
| 03, ch:MEMORY-INFORMATION opening | 1–5 | Retain: T storage and L observation play separate roles, setting up count noise versus motion rather than calling readout time a lifetime. |
| 03, sec:MEMORY-FI | 7–64 | Retain: likelihood, score derivative, expectation, Poisson covariance and units yield Jh. Differentiating unbiasedness and Cauchy Schwarz give the regular local CR bound; finite-sample attainability and priors are qualified. |
| 03, sec:MEMORY-BOUND | 66–156 | Revise necessity M1; retain scalar Cauchy Schwarz proof, exact pointwise equality condition, zero-slope-cell caveat, strict two-cell numerical example, and matrix residual Q^TQ proof with invertibility condition. |
| 03, sec:MEMORY-COMPARISONS | 158–191 | Retain: 1/N, rate, tau and width comparisons identify held quantities. Integral volume w^d and slope w^-2 produce w^(d-2); fixed total rate changes the law. Sensory/internal equality needs matched tuning and does not locate memory in an animal. |
| 03, sec:MEMORY-READOUT-SETUP | 193–217 | Retain: storage/readout variance split is scoped to constant D and local translation invariance. Gaussian approximation is declared; infinitesimal bins are not presented as physically containing many spikes. |
| 03, sec:MEMORY-NAIVE | 219–270 | Retain: double integral of min(s,t)=L^3/3, yielding 2DL/3+1/(JL); differentiation gives sqrt(3/(2DJ)) and minimum factor 2/sqrt(3). |
| 03, sec:MEMORY-IDEAL | 272–346 | Retain: Gaussian convolution adds transition variance, independent measurement adds precision, backward recursion yields P'=J-2DP^2 and coth variance. Small-L and long-L limits and variance/SD ratios agree. |
| 03, sec:MEMORY-PARTIAL | 348–371 | Retain: random thinning gives alpha J while D stays fixed; biased subsets need not carry alpha information. Characteristic times and variance increase by alpha^-1/2, matching arithmetic. |
| 03, sec:MEMORY-EXTENSIONS | 373–419 | Retain: two-block matrix has negative rate decay, left vector b=tau_m a, and tau+tau_m normalization. Constant-q Gaussian model includes q in both likelihood and diffusion, explaining linear equality. |
| 03, sec:MEMORY-FIG3-AND-CAUTION | 421–446 | Retain: actual Fig.3/S2 rescaling matches coth z and z/3+1/z. The printed Eq.6/S83 lower-bound substitution has the wrong direction; guide's inequality chain and strict example are correct within its declared Gaussian model. Leak versus diffusion is correctly distinguished. |

## Footnotes and source scope

All 01 footnotes, lines 202–210: source names/DOIs and claimed source roles checked against local P1, P2, P3, and the local 2026 CA3/CA1 primary text. Teaching constructions are identified; anatomy is not attributed to P3. No independent external anatomy literature survey was necessary for this narrow review.

All 02 footnotes, lines 312–325: source ranges, equation/figure roles, and construction qualifiers checked against all six P1 pages and SI pp.1–10,17–20. Retain except p1-symmetric needs the M2 qualification. S40/S41 discrepancy checked directly; neither guide nor review asserts an author correction.

All 03 footnotes, lines 448–467: checked FI S42–S44, information bound S45–S56, Gaussian readout S57–S83, two-times S84–S92, and Gaussian S93–S95. p1-equality needs M1's stronger condition. Retain the other checks: S71 has a plus sign incompatible with the displayed cosh solution; S85 rate-decay block prints the wrong sign relative to S84; Fig.3 equation pointers are stale; S94/S95 omit normalizations that the guide keeps in q/tau. These are independent mathematical observations, not author-confirmed corrections.

The SI p.20 references and P1 acknowledgments/bibliography supply citation context rather than new teaching. Full source-page disposition is root's separate integration task. This review does not certify other chapters, captions still being assembled, output rendering, external linked PDF behavior, or empirical reproduction.

## Added glossary scope, requested at 19:32

Read every entry in `glossary.md`, lines 1–68, as truth/meaning only. Source hash is included in JSON. This extends the current stage 1 request; it does not establish the teaching of eye/place concepts in chapters outside this review.

### M4: clarify the Poisson process lookup entry

Location: glossary line 47; earlier teaching checked: foundations lines 29–62 and dynamics lines 32–60. “A counting process with conditionally independent increments and a specified event rate” does not specify what is conditioned on. For a usual Poisson process with deterministic intensity, counts in disjoint intervals are independent and Poisson. For the recurrent model, conditional intensity depends on evolving history: instantaneous spike innovations can be conditionally independent, while full interval counts and spike trains are not independent. The next clause about a deterministic-rate interval has the right limitation but does not repair the first clause's ambiguous definition. Repair the ordinary Poisson definition and add the recurrent conditional-intensity qualification explicitly, consistent with the main teaching. Priority: medium, lookup consistency.

### M5: spatial tuning alone does not define a place cell

Locations: glossary line 45 and foundations line 23, checked against the following place-field and grid-cell explanations at foundations lines 23–25. “A neuron whose expected firing rate varies with the animal's position” literally includes grid cells and other spatially tuned neurons, although the guide correctly distinguishes those cells next. Describe place cells through localized regions of elevated firing, with multiple fields permitted; do not make all position-dependent firing sufficient. This is a small repair to a first-use definition and its lookup entry, not a change to the spatial mathematical model. Priority: medium, definition too broad.

| Glossary term set and lines | Truth/meaning verdict |
|---|---|
| Neural anatomy and encoding: 5–6, 12, 17, 23, 25–26, 29, 40–46, 48, 50–51, 56–57, 62–64 | Retain except M5: motor-neuron axons and muscle roles are distinct; a state and its lower-dimensional persistent coordinates are distinguished; tuning and rate-map meanings match earlier teaching. Lookup definitions do not supply missing experimental teaching. |
| Probability and estimation: 8, 10–11, 14–16, 22, 24, 32, 35–37, 47, 49, 52–55, 60, 65–66, 68 | Retain except M4: CR includes regular unbiased scope, R-squared explicitly uses an intercept and optimal linear fit, left/right vectors have different equations, and precision is scalar Gaussian variance inverse. Renewal requires identical independent intervals; sub-Poisson depends on a specified measure. White noise is described by a generalized covariance rather than finite instantaneous variance. |
| Dynamics and filtering: 9, 13, 18–19, 27, 31, 38–39, 54, 58, 61, 63 | Retain: causal filtering uses present/past input; the convolution entry describes the guide's causal-filter use rather than a claim about every possible mathematical convolution. Local diffusion/tensor factors agree with 2Dt; stationarity concerns a probability law and superdiffusion only the specified lag range. FP remains subject to M3 in its teaching passage. |
| Spatial geometry and distributions: 7, 20–21, 28, 30, 33–34, 59, 67 | Retain as lookup meanings: Betti counts, alternating Euler sum, excursion threshold, finite-dimensional Gaussian law, Hessian and rotation/translation invariance are correctly distinct. Kac–Rice is qualified by regularity; Weibull survival includes positive scale/shape. Main chapter derivation sufficiency remains assigned to its independent reviewer. |
