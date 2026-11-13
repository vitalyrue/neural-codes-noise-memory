# Opus 5.5 review: complete findings register

These are the reviewer's original findings on the unchanged guide. They are proposals, not accepted edits. Later qualifications and withdrawn concerns are recorded separately below and in REVIEW.md. Exact provider answers remain in calls/stageN/ANSWER.md.

## Stage 1: Source and mathematics review

Overall the guide is scientifically careful and mostly correct. I re-derived or recomputed the main equations and all numerical examples: Poisson counts; the left-zero-vector projection and the 2D formulas; the Itô/Stratonovich conversion; the Fokker–Planck solution and the π²/3 wrapped limit; the S37 variance expansion; the Cauchy–Schwarz and residual-matrix bounds; the naive and ideal readout (coth); partial access; the two-time-scale left vector; the inverse filter and its static gain; the R² and χ algebra; filtered white versus filtered Brownian MSD; Kac–Rice; the inversion of mean field and gap length; the high-peak size laws; Rayleigh slopes; Euler-characteristic polynomials with box boundary factors; and the random-weight covariance. Each one checks out. Every independent check of a printed source equation that the guide labels is confirmed against the PDFs, and the guide keeps these separate from the official 2017 correction. Burak main Eq. 2 has no numerator square; S40 conflicts with S41 by a factor of 2; S71 has the wrong sign; S85 prints a positive rate-decay block; Eq. 6/S83 have the wrong inequality direction relative to the paper's own model; Mainali S18, S23 and S25 contain the stated errors; the counterexample showing equality does not force an exponential transfer rule holds. One reading needed a second look and is correct: Ben-Shushan Eq. 7 prints τ∓ with ±, so the guide's τ+ (slow) assignment and its phrase 'paired signs in Eq. 7' are right. No confirmed scientific error was found in the guide's own claims. The most important finding is reviewer-derived and concerns a modelling assumption shared by the paper and the guide (F01): the readout model treats observation noise as independent of the state increments. An observer reading the memory network's own spikes sees the same spike surplus that moves the state. Under the paper's linear synaptic model, the cue-state information then decays as e^{-t/τ}, giving asymptotic precision Jτ/2 rather than √(J/2D). The rest are qualifications of hardware descriptions, reasoning wording, citations I could not verify, and optional additions. Coverage limits: the open peer-review file text was not supplied and was not read; the MATLAB and Python code was not opened; several hardware and secondary sources were reached only through search snippets or not at all; no figure pixel audit was done.

### Findings

#### F01

**Kind:** missing_qualification (reviewer-derived calculation; not stated in sources)

**Severity:** medium

**Guide location:** ch:MEMORY-READOUT, sec:MEMORY-READOUT-SETUP; affects sec:MEMORY-IDEAL and sec:MEMORY-FIG3-AND-CAUTION

**File:** guide/03b-memory-readout.md

**Line or section:** L0019–L0032; L0381–L0391

**Short excerpt:** In this approximation, these increments and errors are independent, zero-mean Gaussian variables. ... The derivations below are exact within this local Gaussian readout model.

**Claim or gap:** The observer reads the memory network's own spikes. The same spike surplus that moves θ (η_k = Σ v_i·ΔM_i) also produces the observation error (ε_k ∝ Σ (r_i'/r_i)·ΔM_i/J). At equality v_i = r_i'/(τJr_i), so η_k = (h/τ)ε_k: the two are perfectly correlated, not independent. A two-cell case can be checked exactly. In the linear mutual-inhibition network, r1 − r2 = θ/τ and dθ = dM1 − dM2, so the spike-difference observation is dY = (θ/τ)dt + dθ exactly. More generally, Eq. 7 gives s(t) = e^{−(t−T)/τ}s(T) + Σ_{spikes after T} e^{−(t−t_α)/τ}. Given the observed spikes, only s(T) is unknown, so ∂r_i(t)/∂θ(T) ≈ r_i'·e^{−(t−T)/τ}. The Poisson Fisher information about the cue state is then J∫₀^L e^{−2u/τ}du = (Jτ/2)(1 − e^{−2L/τ}). Its asymptotic variance is 2/(Jτ), not √(2D/J): at equality this is 4Dτ versus 2Dτ, and the approach time is τ/2 rather than 1/√(2DJ). The guide presents the paper's independent-noise model as describing readout of the memory network's spikes without naming the physical reason the approximation may fail.

**Source evidence:**

- source: Burak & Fiete SI; page or section: Sec. VI, p.12–13; equation or figure: S57–S61; what it supports: The observer 'has access to all spikes emitted by neurons in the memory network after the cue'; ξ_i and ζ_i are given as separate independent noises.
- source: Burak & Fiete main; page or section: Materials and Methods p.5; equation or figure: Eq. 7–9; what it supports: s is a linear filter of the neuron's own spikes, which is what makes the e^{−t/τ} decay of cue-state information exact given the observed spikes.
- source: Burak & Fiete main; page or section: p.6 Methods; equation or figure: mutual-inhibition network; what it supports: Linear two-cell model in which r1 − r2 = θ/τ, used for the exact check.

**Strongest retaining reading:** The guide calls this an 'approximation' and says the results are exact only 'within this local Gaussian readout model'. The partial-access section implicitly moves closer to independence as α decreases.

**Why it is still a problem:** The reader's stated interest is the neural versus mathematical assumptions. The text never says the independence is physically violated when the observer receives the spikes that drive the memory. It then uses the model's asymptote √(2D/J) to judge the paper's Eq. 6 and to build the strict-inequality example. Those conclusions are valid inside the model. For full access with known dynamics, the different asymptote 2/(Jτ) gives a total ≤ 2D(T + 2τ), so Eq. 6 is still not universal but for a different reason. Readout 'within τ' remains true, and is even stronger.

**Suggested action:** In sec:MEMORY-READOUT-SETUP, add one sentence: the model treats the state increments as unseen noise independent of the observed spikes, whereas the network's own spikes produce both. In a fold, state the full-access, known-dynamics result (precision Jτ/2 asymptotically) as a guide-derived check needing confirmation. Note that random partial access (small α) brings the observations closer to the independence assumption. Keep the Eq. 6 caution, but scope it to the paper's own readout model.

**Confidence:** medium (the algebra was checked on the exact linear two-cell case; the general case uses linearized rates and an observer that knows W, b, φ and τ)

#### F02

**Kind:** interpretation_risk (reasoning wording)

**Severity:** low

**Guide location:** ch:EYE-CIRCUIT, sec:EYE-SCALING

**File:** guide/04c-eye-circuit.md

**Line or section:** L0146–L0170

**Short excerpt:** If k0 means an absolute slope in Hz/degree, that printed expression has the wrong units for D.

**Claim or gap:** Eq. 1 is printed as a proportionality, which can carry a dimensional constant, so 'wrong units' alone is not decisive. The decisive point is the dependence on λ0 at fixed absolute slope. The derivation also inserts CV² into the 2012 Poisson information–diffusion relation. The 2022 integrator has saturating synapses (each spike adds 1/[τs(λt + λ)]), rectified rates, and a readout E_OI, so the 2012 bound applies only as a heuristic. My own rough check: the λ0-in-numerator conclusion survives for λ ≪ λt but the exponent changes for λ ≫ λt.

**Source evidence:**

- source: Ben-Shushan main; page or section: p.6; equation or figure: Eq. 1; what it supports: Printed D ∝ CV² N⁻¹ λ0⁻¹ k0⁻² τs⁻², cited to Burak–Fiete.
- source: Ben-Shushan main; page or section: p.10–11; equation or figure: Eq. 24–26; what it supports: Saturating synaptic response with λt = 60 Hz.

**Strongest retaining reading:** The guide labels the expression 'a scale', 'not an exact formula', and its own 'dimensional interpretation'.

**Why it is still a problem:** A reader may take 'wrong units' as a proven printing error, and may assume the 2012 Poisson bound applies directly to the saturating sub-Poisson 2022 model.

**Suggested action:** Rephrase: 'If k0 is an absolute slope, the 2012 Poisson relation implies D grows with λ0 at fixed slope; the printed λ0⁻¹ matches a fractional slope.' Add that synaptic saturation and sub-Poisson renewal statistics make this an order-of-magnitude guide.

**Confidence:** medium

#### F03

**Kind:** ambiguous_wording

**Severity:** low

**Guide location:** ch:SIMULATING-EYE, sec:SIMULATING-EYE-DATA

**File:** guide/12-simulating-eye-drift.md

**Line or section:** L0007

**Short excerpt:** ...then use it to reconstruct movement from that cell's spikes. A trial held out of the fit tests prediction on data that did not determine the fitted parameters.

**Claim or gap:** The paper documents leave-one-out only for the firing-rate predictions (Fig. 1). For the inverse-filter eye reconstruction used for R and χ, it does not say whether the fixation segments were held out. The fit used full trials, including the fixation components.

**Source evidence:**

- source: Ben-Shushan main; page or section: p.9 'OMN firing rate estimators'; equation or figure: Eq. 2–3; what it supports: Leave-one-out for 'firing rate prediction'; the fit covers 'the full extent of each trial, including the fixational ... components'.

**Strongest retaining reading:** The sentence can be read as describing the forward fit only. Chapter 7 states the scope correctly.

**Why it is still a problem:** Placed directly after 'reconstruct movement', it suggests the χ analysis used held-out calibration, which the source does not establish.

**Suggested action:** Attach the hold-out statement to the rate prediction. State that the source does not say whether the reconstruction excluded each segment's own trial.

**Confidence:** high

#### F04

**Kind:** interpretation_risk / optional_addition

**Severity:** low

**Guide location:** ch:NEUROMORPHIC-SYSTEMS, sec:NEUROMORPHIC-SYSTEMS-ADVANCES

**File:** guide/09-neuromorphic-systems.md

**Line or section:** L0029

**Short excerpt:** Aitsam and colleagues ran a 768-neuron recurrent sheet on one chip, with signals from a physical event camera.

**Claim or gap:** The chip receives a host-computed, EMA-smoothed centroid injected as a fixed 2×2 cluster; it does not receive raw events. The on-chip network is deterministic integer-weight LIF with a period-two sustained orbit and no stochastic noise source, so 8 s persistence does not exercise noise-driven diffusion. Recurrence reduced jitter by 15% but increased mean error versus the target (5.65 vs 2.02 cells) and added about 115 ms of lag. Positions are also quantized to a 32×24 lattice, which is relevant to pinning (ch. 15).

**Source evidence:**

- source: Aitsam et al. 2026; page or section: §3.2, §2.5, §4.1, §4.3; equation or figure: Eq. 12; Table 3; Fig. 3; what it supports: Host centroid and EMA; period-two orbit; ≤0.50-cell motion; error and lag trade-off.

**Strongest retaining reading:** The guide already says the 8 s is not a lifetime and that noise-controlled tests would be useful.

**Why it is still a problem:** The connection to Burak–Fiete depends on whether noise is present and on what reaches the chip; both are omitted.

**Suggested action:** Add one sentence: the input is a host-smoothed centroid; the deterministic on-chip network shows persistence but not diffusion; recurrence traded positional accuracy for stability.

**Confidence:** high

#### F05

**Kind:** optional_addition (clarification)

**Severity:** low

**Guide location:** ch:NEUROMORPHIC-SYSTEMS, sec:NEUROMORPHIC-SYSTEMS-LIMITS

**File:** guide/09-neuromorphic-systems.md

**Line or section:** L0041–L0049

**Short excerpt:** m_{k+1} = α m_k + β z_k ... This model illustrates slow storage. It is not the full equations

**Claim or gap:** Sun's slow state is a frozen Legendre-memory (LMU) state-space realization (Ā = e^{AΔt}) that represents a sliding window of length θ, with spectral radius near 1. It is not a scalar leaky average, and it is neither a continuous attractor nor noise-driven.

**Source evidence:**

- source: Sun et al. 2026; page or section: Methods 'Slow memory pathway'; equation or figure: Eq. 4–8; what it supports: LMU A, B matrices; window θ; frozen discretized matrices.

**Strongest retaining reading:** The disclaimer is explicit.

**Why it is still a problem:** The leaky illustration may lead readers to equate this engineered state with the neural memories of Part I.

**Suggested action:** Add a clause naming the LMU sliding-window representation and stating that it stores a recent input history rather than a persistently held cue.

**Confidence:** high

#### F06

**Kind:** unverified_suspicion (citation support)

**Severity:** low

**Guide location:** ch:SYNTHESIS sec:SYNTHESIS-RELATED; ch:FOUNDATIONS sec:FOUNDATIONS-SPIKES

**File:** guide/06-synthesis.md; guide/01-foundations.md

**Line or section:** 06 L0125; 01 L0126–L0131 with footnote f-anatomy

**Short excerpt:** predominantly single fields in CA3 contrast with multiple fields in CA1, while field sizes are similar

**Claim or gap:** A seminar abstract supports single CA3 fields versus multiple CA1 fields in the 200 m tunnel. 'Field sizes are similar' was not found. Footnote f-anatomy also cites this bat place-cell paper for the general grid-cell definition and for CA3/CA1 connectivity facts, which it may not support.

**Source evidence:**

- source: Web search: Maimon et al. 2026 (Nature-index record, seminar abstract); page or section: abstract-level only; equation or figure: —; what it supports: Publication of 27 May 2026; CA3 single versus CA1 multiple fields.

**Strongest retaining reading:** The guide may have read the full Nature text.

**Why it is still a problem:** I could not verify the field-size claim, and the anatomy and grid-cell citations look mismatched to the source type.

**Suggested action:** Check Maimon et al. Figs. 1–2 for the field-size statement. Cite a standard anatomy or grid-cell source for those definitions.

**Confidence:** low

#### F07

**Kind:** unverified_suspicion

**Severity:** low

**Guide location:** ch:HARDWARE-DYNAMICS sec:HARDWARE-DYNAMICS-EVIDENCE; ch:PERSISTENCE sec:PERSISTENCE-EYE-MECHANICS

**File:** guide/08-hardware-dynamics.md; guide/01b-persistence.md

**Line or section:** 08 L0086; 01b L0043

**Short excerpt:** It had 32 bump positions around a circle, a spacing of 11.25°. / ...drifted back with a time constant of about 0.2 s, compared with more than 20 s

**Claim or gap:** Neither number could be checked against the primary text. Search reached only Massoud/Horiuchi posters, which confirm bump persistence but not the count, and only the Cannon & Robinson citation record.

**Source evidence:**

- source: UMD ISR posters (search snippets); page or section: —; equation or figure: —; what it supports: Ring attractor; bump persists after input removal.

**Strongest retaining reading:** The guide cites specific sections (Fig. 21; the abstract).

**Why it is still a problem:** These are specific quantitative claims that the frozen packet does not support.

**Suggested action:** Verify against the IEEE paper Fig. 21 and the J Neurophysiol 57:1383 abstract.

**Confidence:** low

#### F08

**Kind:** optional_addition (scope of EC comparison)

**Severity:** low

**Guide location:** ch:PLACE-TESTS, sec:PLACE-TOPOLOGY / sec:PLACE-DATA

**File:** guide/05c-place-tests.md

**Line or section:** L0119, L0214

**Short excerpt:** These reproduce the paper's Equations 8–10 for interval, square, and cube geometry ... For a rectangular room, replace ...

**Claim or gap:** The room is 5.8 × 4.6 × 2.7 m and the arena shape is not stated. Eq. 10 is printed for a cube with a single L/σ, and Fig. 4A's σ = 4.0 is unit-ambiguous (it fits 10 cm bins). The sources do not say which boundary factors or units produced the Fig. 3G/H theory curves. The guide supplies the rectangle correction but does not tell the reader that this is unknown.

**Source evidence:**

- source: Mainali main; page or section: p.e3; equation or figure: Eq. 9–10; Fig. 3G–H; Fig. 4A; what it supports: Cube and square formulas; non-cubic room; σ = 4.0 in the 3D row.

**Strongest retaining reading:** The σ caution is already present.

**Why it is still a problem:** Readers may assume the plotted EC theory used the correct rectangular boundary terms.

**Suggested action:** State that the geometry factors used for Fig. 3G/H are unspecified, and that the agreement is judged with that uncertainty.

**Confidence:** medium

#### F09

**Kind:** optional_addition (simulation vs theory)

**Severity:** low

**Guide location:** ch:SIMULATING-MEMORY sec:SIMULATING-MEMORY-RING; ch:FOUNDATIONS sec:FOUNDATIONS-SIMULATION

**File:** guide/11-simulating-memory.md

**Line or section:** L0032

**Short excerpt:** That convenient numerical readout differs from the ideal spike-based estimator studied later in the paper.

**Claim or gap:** The argmax-of-rate readout also differs from the theory's coordinate, the flow-projected instantaneous attractor state (Fig. 1A). It includes off-manifold transients and is quantized to 2π/1024. The short-lag agreement therefore tests the theory through a proxy; the 10 ms exclusion partly addresses this.

**Source evidence:**

- source: Burak main; page or section: p.2 and p.6; equation or figure: Fig. 1A; Network Simulations; what it supports: Coordinate defined by flow; simulation uses the argmax angle.

**Strongest retaining reading:** The guide already distinguishes the decoder from ideal estimation.

**Why it is still a problem:** This detail matters for interpreting the agreement between theory and simulation, which is a stated interest of the user.

**Suggested action:** Add one sentence noting the proxy coordinate and its short-lag and quantization effects.

**Confidence:** high

#### F10

**Kind:** optional_addition (source wording)

**Severity:** low

**Guide location:** ch:PLACE-TESTS, sec:PLACE-WIRING

**File:** guide/05c-place-tests.md

**Line or section:** L0297–L0305

**Short excerpt:** The covariance's Gaussian standard deviation is √2 b

**Claim or gap:** Correct, but Methods S2 says the covariance has 'a width equal to twice the width' of the input fields. That is true only if 'width' means variance. A reader cross-checking S2 may be confused.

**Source evidence:**

- source: Mainali supplement; page or section: Methods S2; equation or figure: S5; what it supports: 'twice the width' wording.

**Strongest retaining reading:** The guide fixes its own convention explicitly.

**Why it is still a problem:** There is a minor risk of an apparent contradiction with the source.

**Suggested action:** Add a short note that S2's 'twice' refers to variance.

**Confidence:** high

#### F11

**Kind:** confirmed_error (citation consistency)

**Severity:** low

**Guide location:** ch:SYNTHESIS footnote s-acuity vs ch:REFERENCES entry 22

**File:** guide/06-synthesis.md; guide/references.md

**Line or section:** 06 L0170; references L0075

**Short excerpt:** Nghiem, T. E. ... / Nghiem, T. A. E.

**Claim or gap:** The author initials differ between the footnote and the reference list.

**Strongest retaining reading:** —

**Why it is still a problem:** Inconsistent bibliographic data.

**Suggested action:** Harmonize the initials after checking the PNAS record.

**Confidence:** high

#### F12

**Kind:** unverified_suspicion (rendering)

**Severity:** low

**Guide location:** part:MECHANISMS and part:OBSERVATIONS introductions

**File:** Part intro sources (not in bundle)

**Line or section:** PART sections

**Short excerpt:** Part I and Part II opening paragraphs appear twice in the packet

**Claim or gap:** This may be a packet artifact (purpose line plus body) or a real duplicated paragraph in the reader output. Parts III and IV are not duplicated.

**Strongest retaining reading:** Likely a packet construction artifact.

**Why it is still a problem:** If it is rendered, readers see a repeated paragraph.

**Suggested action:** Check the rendered Part pages.

**Confidence:** low

### Retained strengths

- Independent source checks are kept separate from the 2017 correction and labelled as algebra rather than author corrections; I confirmed each against the PDFs: missing Eq. 2 square, S40/S41, S71, S85, Eq. 6/S83, Mainali S18/S23/S25, and the equality-iff counterexample.
- The left zero vector is explained through the tilted-decay example and Fig. 1A flow projection; this is the key bridge from neural mechanism to diffusion.
- The χ versus R distinction is shown with a constructed numerical example (R = 0.17, χ = 0.82) and its calibration and independence assumptions; this prevents the common misreading of weak single-cell correlations.
- The filtered white versus filtered Brownian MSD derivation (one-pole) explains why an intermediate log slope does not imply superdiffusion inside the circuit.
- Careful separation of storage error from readout error, of naive from ideal readout, and of what Figs. 3/S2 compute (analytic) versus simulate.
- The place-field chapters separate exact stationary results (Kac–Rice means, Rayleigh boundary slopes, EC) from high-threshold limits, quantify the 46% error at q = 1.1, and track fitted versus tested quantities per dataset.
- The unit and convention checks throughout (D units, activation versus rate coordinates rescaled by 1/τ², σ versus filter width √2, MSD offset 2σm²) catch real pitfalls.
- The hardware chapters consistently distinguish weight storage, neural state, and represented value; measured chip versus host versus post-layout simulation; and persistence versus measured lifetime. The reduced models are labelled guide-derived.
- Explicit scope statements: the 2012 results are simulations, not animal data; the integrator is sufficient but not uniquely identified; the random-wiring interpretation is not measured.

### Remaining checks

- F01 needs author or independent confirmation, ideally by a short simulation of the two-cell network comparing full-access ideal readout with 2Dτ coth(L/τ) (not run, per brief).
- Peer-review-file claims in ch. 7–9 (no simultaneous OMNs; noise-subtraction uncertainty example; localization statements; p.23 scaling) are unverified.
- Code-level claims in ch. 19–20 (MATLAB dt, τ_MN, N convention, Eq. 35 regression, missing function; Python RMS normalization, edge handling, README) are unverified.
- Wang 2026 open issues and 'low drift' framing; Massoud '32 positions'; Cannon & Robinson time constants; Maimon field sizes; Koyluoglu characterization: verify against full texts.
- The 2017 correction content was not fetched; reliance is on the guide's citation plus the SI S18 algebra.
- No figure pixel audit; guide-made figures were judged only from captions and alt text.
- Stage 2 (necessity and terminology) and stage 3 (flow and structure: glossary ordering, possible duplicated Part paragraphs, chapter order) are not addressed here.

## Stage 2: Explanations and terminology

Stage 2 reviews necessity, terminology and missing explanatory steps on the unchanged frozen guide. Stage 1 findings are carried forward unrepaired. Overall, the main paths are well motivated. Most chapters open with a physical question, name the actors (cells, synapses, motor neurons, muscles, search coil, input cells, chips) and introduce symbols before use, and the folded derivations are placed sensibly. The most important problems are book-level vocabulary problems rather than missing mathematics:
(1) Several words name different objects in different chapters: state, stored value, memory coordinate and represented value; and drift, which means both random fixational motion and systematic mean velocity.
(2) The theory's key object, the instantaneous attractor coordinate, is defined only in Chapter 4, after Chapter 3 already needs it.
(3) The information–diffusion bound is derived only algebraically. The physical intuition that makes it a neurophysics result is absent.
(4) Several symbols are reused for different quantities. Two collisions matter: within Chapter 6, q is both a transition variance and a noise strength; across papers, χ is both the common variance fraction and the Euler characteristic.
(5) Six terms carry a first-definition span twice, against the guide's own rule.
Parts III and IV are useful requested extensions. Part III connects to Part I through the noise-projection formula and a feedback-time-constant model, and its burden is reasonable. Part IV largely retells Figure 2 and the eye model, already told in Chapters 1, 4 and 9. Each Part IV chapter should lead with what it adds: settings, numerical cautions, code and data access. Repeated passages can then be cut to make room for the few essential additions. Proposed essential additions total about 10–15 sentences. Suggested omissions (duplicated figure interpretations, a repeated label paragraph, some main-path derivation detail) more than offset them.

### Findings

#### S2-01

**Kind:** missing_step (book-level terminology)

**Severity:** medium

**Guide location:** ch:MEMORY-DYNAMICS sec:MEMORY-WEAK-NOISE opening and sec:MEMORY-LINEARIZATION first paragraph; definition currently in ch:MEMORY-LONG-DELAYS sec:MEMORY-FIGURES

**File:** guide/02-memory-dynamics.md; guide/02b-memory-long-delays.md

**Line or section:** 02 L0009, L0068; 02b L0162

**Short excerpt:** The memory coordinate is θ ... we need the lasting change: the displacement to a different fixed point.

**Missing or unclear meaning:** The theory tracks θ(t) while noise keeps the network slightly off the attractor. Which θ does a noisy, off-manifold state have? The answer is the flow projection, called the 'instantaneous attractor state' in the paper. It is defined only in ch. 4's reading of Fig. 1A. The book uses five names for this one object: stored value, represented value, memory coordinate, angle, attractor state. It also never separates three objects: the N-dimensional state s, the coordinate θ, and an observer's estimate θ̂.

**Earlier teaching checked:** ch. 2 defines θ = (r1 − r2)/2k, valid for every state of the linear two-cell model; ch. 2 defines state; ch. 3 says 'lasting change … different fixed point'.

**Reader consequence:** The reader cannot say what is diffusing, or why θ is well defined between spikes, until ch. 4. The later readout chapter's distinction between θ(T) and θ̂ rests on an unstated difference.

**Suggested action:** At the start of sec:MEMORY-LINEARIZATION, add two sentences: 'For any nearby state, θ is defined as the fixed point the noise-free dynamics would reach from it (Fig. 1A); this is the paper's instantaneous attractor state. The network state s has N components; θ is one coordinate; an observer's estimate θ̂ is a third, different quantity.' Then say once that stored value, represented value and memory coordinate are synonyms for θ.

**Essential or optional:** essential

**Confidence:** high

#### S2-02

**Kind:** terminology_conflict (book-level)

**Severity:** medium

**Guide location:** reading guide sec:READING-EYE; ch:PERSISTENCE example (systematic drift defined); ch:MEMORY-LONG-DELAYS sec:MEMORY-DRIFT-SCOPE; ch:EYE-DRIFT/EYE-TIMING/EYE-CIRCUIT titles; ch:HARDWARE-DYNAMICS title; ch:HARDWARE-TESTS

**File:** guide/00-reading-guide.md; 01b-persistence.md; 04-eye-drift.md; 08-hardware-dynamics.md; 10-hardware-tests.md

**Line or section:** 00 L0033; 01b L0184; 08 title L0001; 10 L0004/L0029

**Short excerpt:** A theory of random diffusion must account separately for systematic drift, a nonzero mean velocity. / Discrete restoration and continuous drift produce different memory errors

**Missing or unclear meaning:** 'Drift' has three uses. 'Fixational drift' is a conventional name for random, mostly diffusive eye motion. 'Systematic drift' is a nonzero mean velocity. Ch. 15's 'continuous drift' means random wandering, yet ch. 17 uses 'drift' for systematic motion and 'spreading' for random motion. The paper's 'random drift' and Aitsam's 'drift' add further senses.

**Earlier teaching checked:** ch. 1 sec:FOUNDATIONS-COVARIANCE contrasts random wandering with directional bias, but never mentions the word clash.

**Reader consequence:** After ch. 2 and ch. 4, a reader may read 'fixational drift is driven by diffusive dynamics' as contradictory, or read ch. 15's title as being about bias.

**Suggested action:** Where systematic drift is defined (ch. 2), add one sentence: '“Fixational drift” in Chapters 7–9 is the name of the eye's slow motion and is mostly random; in this guide “systematic drift” always means mean velocity.' Repeat a short reminder at the start of ch. 7. Change 'continuous drift' in ch. 15's title and opening to 'continuous wandering' or 'random spreading'.

**Essential or optional:** essential

**Confidence:** high

#### S2-03

**Kind:** symbol_collision (harmful)

**Severity:** medium

**Guide location:** ch:MEMORY-READOUT sec:MEMORY-IDEAL and sec:MEMORY-EXTENSIONS; ch:PLACE-TESTS sec:PLACE-TOPOLOGY vs ch:EYE-DRIFT sec:EYE-CHI

**File:** guide/03b-memory-readout.md; guide/05c-place-tests.md; guide/04-eye-drift.md

**Line or section:** 03b L0136 vs L0318–L0324; 05c L0017 vs 04 L0331

**Short excerpt:** adds transition variance q=2Dh ... / replace Poisson ... with independent additive Gaussian noise of constant strength q>0

**Missing or unclear meaning:** Within one chapter, q is first a per-bin transition variance and then a per-neuron noise strength. Ch. 10–12 then use q as the threshold. χ is the common variance fraction in ch. 7 and the Euler characteristic in ch. 12. η means a readout increment (ch. 6), motor and measurement noise (ch. 7) and readout weights (ch. 9).

**Earlier teaching checked:** The reading-guide symbol list (L0166–L0171) covers only D, d, θ, q and C.

**Reader consequence:** The ch. 6 collision can mislead within a single derivation. The χ collision confuses anyone comparing the two papers in ch. 13 or the glossary.

**Suggested action:** In ch. 6 write 2Dh directly in the recursion, or rename the noise strength to σ_ξ². In ch. 12 add '(unrelated to χ in Chapter 7)'. Add χ and η to the reading-guide symbol list with their per-Part meanings.

**Essential or optional:** essential (ch. 6 q); optional (others)

**Confidence:** high

#### S2-04

**Kind:** symbol_collision (minor) / local reminder

**Severity:** low

**Guide location:** ch:PERSISTENCE mechanics fold; ch:MEMORY-DYNAMICS; ch:MEMORY-READOUT extensions; ch:NEUROMORPHIC-SYSTEMS; ch:HARDWARE-TESTS; ch:EYE-DRIFT/EYE-TIMING

**File:** multiple

**Line or section:** 01b L0015 (τ_m torque, K stiffness, B viscosity); 02 L0078 (K matrix); 03b L0276 (τ_m); 09 L0055 (τ_m memory time); 10 L0043 (ℓ left vector, B noise matrix); 02/02b/03 use E[·] for expectation while 04/04b/04c use E for eye position and 𝔼 for expectation

**Short excerpt:** τ_m(t) the net active muscle torque ... / τ_m\dot r_i = −r_i + φ(g_i)

**Missing or unclear meaning:** These reuses are mostly redefined locally. The ones a reader may carry across chapters: τ_m (torque, then membrane time constant, then memory time); the left zero vector called v in Part I and ℓ in ch. 17 without saying they are the same; and E used both as plain expectation and as eye position.

**Earlier teaching checked:** Local definitions exist at each use.

**Reader consequence:** A small extra decoding cost. The real risk is missing that ch. 17's ℓ is ch. 3's v.

**Suggested action:** Rename the ch. 2 torque (e.g. M_m) or call it 'muscle torque Γ'. In ch. 17 write 'ℓ (the left vector v of Chapter 3)'. Use 𝔼 for expectation in chapters 3–6.

**Essential or optional:** optional (the ℓ = v reminder is the most useful)

**Confidence:** high

#### S2-05

**Kind:** missing_step (physical interpretation)

**Severity:** medium

**Guide location:** ch:MEMORY-INFORMATION sec:MEMORY-BOUND, first 'Neural mechanism' paragraph and interpretation after the boxed bound

**File:** guide/03-memory-information.md

**Line or section:** L0167, L0201–L0204

**Short excerpt:** The lower bound on diffusion follows directly by comparing the state sensitivity of the network with the spike information. ... The units agree: τ²J has units ...

**Missing or unclear meaning:** The reader gets the Cauchy–Schwarz algebra and a units check, but no physical reason why spike information limits stability, or why τ² appears. The paper gives one: the network effectively re-estimates its own state from about τ worth of its spikes. That estimate has variance at least 1/(Jτ), and the resulting wander over τ, 2Dτ, cannot be smaller.

**Earlier teaching checked:** ch. 5 sec:MEMORY-FI (Cramér–Rao); main-paper p.3 interpretation paragraph.

**Reader consequence:** The central result reads as an algebraic coincidence. The reader cannot explain it as a statement about a circuit that is its own noisy observer, which is the neurophysics point.

**Suggested action:** After L0167 add 2–3 sentences: 'Heuristically, the circuit keeps its state by re-reading roughly the last τ of its own spikes. By the Cramér–Rao bound that reading has variance ≥ 1/(Jτ), so the state must wander at least that much per τ: 2Dτ ≥ 1/(Jτ), i.e. D ≥ 1/(2τ²J). The proof below makes this exact without the heuristic.' Label it as the paper's interpretation.

**Essential or optional:** essential

**Confidence:** high

#### S2-06

**Kind:** duplicate first-definition marking (house rule)

**Severity:** low

**Guide location:** multiple

**File:** 00, 01, 01b, 02, 02b, 11

**Line or section:** activity bump: 01 L0272 and 02b L0165; preferred angle: 01 L0272 and 02 L0052; Euler update: 01 L0286 and 11 L0024; Dirac delta: 01 L0048 and 02b L0051; diffusion coefficient: 00 L0164 (span) and 01b L0156 (bold inside definition); MSD: 00 L0164, 01 L0349, 01b L0166

**Short excerpt:** [In Fig. 1B, an [**activity bump**]{.definition-term ...} is a localized peak ...]

**Missing or unclear meaning:** These are not missing meanings: the guide's rule is one blue first definition per book. Re-marking makes 'newly introduced' signals unreliable. The second Dirac-delta passage introduces a genuinely new use (a point-mass initial condition) and should read as a reminder of the extension, not a new term.

**Earlier teaching checked:** First occurrences located as listed.

**Reader consequence:** A reader scanning blue terms finds repeats and may think a second meaning is being introduced.

**Suggested action:** Keep the first span and turn the later ones into plain reminders, e.g. 'The activity bump (Chapter 1) ...'. For D and MSD, the reading guide can define them and ch. 2 can say 'as defined in the reading guide' while giving the derivation.

**Essential or optional:** essential under the guide's own presentation rule; low teaching impact

**Confidence:** high

#### S2-07

**Kind:** definition_placement

**Severity:** low

**Guide location:** ch:MEMORY-READOUT sec:MEMORY-EXTENSIONS (definition); used in ch:EYE-TIMING sec:EYE-FILTERED-MSD

**File:** guide/03b-memory-readout.md; guide/04b-eye-timing.md

**Line or section:** 03b L0278; 04b L0091

**Short excerpt:** The input is idealized as [white noise](ch-memory-readout.html#sec-memory-extensions)

**Missing or unclear meaning:** White noise is a basic idealization behind Brownian increments and the paper's ξ notation. It is defined inside an optional-looking extension about two time scales. The eye chapter must link back into that extension.

**Earlier teaching checked:** ch. 2 Brownian motion; ch. 3 Brownian increments; a ch. 3 footnote mentions the paper's white-noise notation.

**Reader consequence:** A reader following the eye path, or skipping extensions, must open an advanced section to learn a basic term.

**Suggested action:** Move the white-noise definition (two sentences) to ch. 3 sec:MEMORY-WEAK-NOISE, next to dB: 'Its formal derivative is white noise...'. Keep a reminder in ch. 6 and point ch. 8 there.

**Essential or optional:** optional

**Confidence:** high

#### S2-08

**Kind:** unnecessary_repetition (Part IV and Part I overlap)

**Severity:** medium

**Guide location:** ch:FOUNDATIONS sec:FOUNDATIONS-SIMULATION; ch:MEMORY-LONG-DELAYS sec:MEMORY-FIGURES; ch:SIMULATING-MEMORY sec:RING/CONTROLS; ch:EYE-CIRCUIT vs ch:SIMULATING-EYE sec:PATH/CONTROLS

**File:** 01-foundations.md; 02b-memory-long-delays.md; 11-simulating-memory.md; 04c-eye-circuit.md; 12-simulating-eye-drift.md

**Line or section:** 01 L0266–L0292; 02b L0182–L0192; 11 L0028–L0034, L0052–L0054; 12 L0013–L0026, L0040–L0051

**Short excerpt:** Over long intervals, wrapping angle differences into a single turn limits the plotted error. That flattening does not mean the original angle has been recovered.

**Missing or unclear meaning:** Several passages are repeated: the Fig. 2 ring and mutual-inhibition interpretation (three times), the point that flattening does not mean recovery (four times), the four-stage eye pathway and its controls (twice), and the sub-Poisson thinning derivation (twice). Part IV's unique value is hard to find among the retelling.

**Earlier teaching checked:** All listed passages read.

**Reader consequence:** Extra reading burden. It is also unclear what a Part IV chapter adds beyond the earlier teaching.

**Suggested action:** Open each Part IV chapter with one sentence naming what it adds beyond ch. X (settings, numerical rules, data and code access, reproduction cautions). Cut the restated interpretations to links. In ch. 1, keep the algorithm (what is stored, the update cycle, the conditional independence point) and replace the Fig. 2 interpretation with a pointer to ch. 4.

**Essential or optional:** optional (recommended trim to make room for S2-01/02/05)

**Confidence:** high

#### S2-09

**Kind:** dependency_before_teaching (local)

**Severity:** low

**Guide location:** ch:FOUNDATIONS sec:FOUNDATIONS-SIMULATION 'What is measured and compared'

**File:** guide/01-foundations.md

**Line or section:** L0288

**Short excerpt:** They independently calculate the predicted spreading from the same network's steady activity ... without fitting a free diffusion parameter.

**Missing or unclear meaning:** 'Predicted spreading', 'diffusion parameter' and 'theoretical curves' are used before ch. 2 teaches diffusion and before ch. 3 shows how steady activity gives D.

**Earlier teaching checked:** Reading guide L0164 defines D and MSD briefly.

**Reader consequence:** The reader must take 'no free parameter' on trust at this point.

**Suggested action:** Either keep one sentence ('the theory of Chapters 3–4 predicts this spreading from the noise-free tuning curves alone; Chapter 4 reads the comparison') or apply the S2-08 trim.

**Essential or optional:** optional

**Confidence:** medium

#### S2-10

**Kind:** missing_link_to_measurables

**Severity:** low

**Guide location:** ch:MEMORY-DYNAMICS sec:MEMORY-SYMMETRIC interpretation

**File:** guide/02-memory-dynamics.md

**Line or section:** L0255

**Short excerpt:** the diffusion coefficient can be calculated from the tuning curves and transfer function

**Missing or unclear meaning:** The text does not say which ingredients are experimentally measurable and which are model assumptions. Tuning curves r̄_i(θ) can be recorded. ḡ_i requires knowing or assuming φ. Poisson statistics must hold (ch. 1 notes this fails for eye-position neurons). D itself is measured as the slope of the decoded MSD.

**Earlier teaching checked:** ch. 1 L0292 (sub-Poisson eye neurons); ch. 13 sec:SYNTHESIS-EVIDENCE.

**Reader consequence:** The reader cannot say what an experiment would need in order to test the formula until ch. 13.

**Suggested action:** Add one sentence: 'Recorded tuning curves give r̄_i; ḡ_i additionally needs the transfer function; D can be measured as half the slope of the decoded MSD (Ch. 4).'

**Essential or optional:** optional

**Confidence:** high

#### S2-11

**Kind:** repetition (front matter and Parts)

**Severity:** low

**Guide location:** reading guide L0081; each Part intro

**File:** guide/00-reading-guide.md; Part intros

**Line or section:** 00 L0081; Part I–IV 'The contribution labels describe...'

**Short excerpt:** The contribution labels describe the role of each result here. **Central** is ...

**Missing or unclear meaning:** The same four-label explanation appears five times.

**Earlier teaching checked:** —

**Reader consequence:** Minor reading cost.

**Suggested action:** Keep the reading-guide definition. In each Part, use a one-line reminder with a link.

**Essential or optional:** optional

**Confidence:** high

#### S2-12

**Kind:** terminology_inconsistency

**Severity:** low

**Guide location:** reading guide sec:READING-MECHANISM-MATH and chapters 3–6

**File:** guide/00-reading-guide.md; 02*, 03*

**Line or section:** 00 L0123, L0149, L0187; 02 L0007

**Short excerpt:** PNAS appendix ... Supporting Information (SI) ... Supporting Text ... supplement

**Missing or unclear meaning:** One document has four names: appendix, SI, Supporting Text and supplement.

**Earlier teaching checked:** —

**Reader consequence:** A reader may think these are different documents.

**Suggested action:** Name it once ('Burak–Fiete Supporting Information, SI') and use SI throughout.

**Essential or optional:** optional

**Confidence:** high

#### S2-13

**Kind:** local_reminder (state variables)

**Severity:** low

**Guide location:** ch:MEMORY-DYNAMICS opening notation paragraph

**File:** guide/02-memory-dynamics.md

**Line or section:** L0009–L0013

**Short excerpt:** A bar denotes a noise free steady state, so \bar r_i(θ) is neuron i's steady firing rate

**Missing or unclear meaning:** Ch. 2's example uses rates as the dynamical state. Ch. 3's state variables are the activations s_i, with rates computed from them. The mutual-inhibition θ is an activation difference, while the paper's Fig. 2G plots a rate difference.

**Earlier teaching checked:** ch. 1 Eq. 7–9; ch. 3 footnote p1-two.

**Reader consequence:** Possible confusion about what is perturbed and what u and v act on.

**Suggested action:** Add one sentence: 'Here the state is the activation vector s; rates follow from it, and at a fixed point s̄ = τr̄.'

**Essential or optional:** optional (strongly recommended)

**Confidence:** high

#### S2-14

**Kind:** synonym_proliferation

**Severity:** low

**Guide location:** ch:EYE-DRIFT throughout; Part II intro

**File:** guide/04-eye-drift.md

**Line or section:** L0004, L0032, L0039, L0310; 04c L0004

**Short excerpt:** large shared drive upstream ... changing shared command ... common command ... common upstream contribution ... central source

**Missing or unclear meaning:** Several names refer to one quantity, C.

**Earlier teaching checked:** ch. 1 covariance section ('shared command').

**Reader consequence:** The reader may wonder whether 'command', 'drive' and 'source' are distinct objects.

**Suggested action:** Define once: 'the shared upstream drive (the paper's central source), whose contribution to displacement is C'. Then use one term.

**Essential or optional:** optional

**Confidence:** medium

#### S2-15

**Kind:** unexplained_label

**Severity:** low

**Guide location:** ch:EYE-DRIFT sec:EYE-INVERSE-FILTER

**File:** guide/04-eye-drift.md

**Line or section:** L0243

**Short excerpt:** the mean Pearson correlation was ⟨R⟩=0.17±0.02

**Missing or unclear meaning:** 'Pearson' is introduced without explanation, and the symbol changes from ρ (ch. 1) to R.

**Earlier teaching checked:** ch. 1 defines the correlation coefficient as ρ.

**Reader consequence:** A small doubt about whether R is a different statistic.

**Suggested action:** Write 'the ordinary (Pearson) correlation coefficient of Chapter 1, written R here as in the paper'.

**Essential or optional:** optional

**Confidence:** high

#### S2-16

**Kind:** forward_use

**Severity:** low

**Guide location:** ch:PLACE-FIELDS sec:PLACE-KAC-RICE

**File:** guide/05-place-fields.md

**Line or section:** L0187

**Short excerpt:** This identity also gives the paper's exact one dimensional mean Euler characteristic, Equation 8.

**Missing or unclear meaning:** The Euler characteristic is used before its ch. 12 definition.

**Earlier teaching checked:** None earlier.

**Reader consequence:** A minor puzzle.

**Suggested action:** Add '(a topological count defined in Chapter 12; in 1D it is the number of fields)'.

**Essential or optional:** optional

**Confidence:** high

#### S2-17

**Kind:** undefined_term_in_definition

**Severity:** low

**Guide location:** ch:PLACE-SIZES sec:PLACE-SIZE-LAW

**File:** guide/05b-place-sizes.md

**Line or section:** L0185

**Short excerpt:** A Weibull distribution has survival probability exp[−(s/b)^k]

**Missing or unclear meaning:** 'Survival probability' is defined only in a figure caption.

**Earlier teaching checked:** ch. 11 L0069 uses Pr(U>u) without naming it.

**Reader consequence:** A small definitional gap.

**Suggested action:** Write 'survival probability Pr(size > s)'.

**Essential or optional:** optional

**Confidence:** high

#### S2-18

**Kind:** main_path_burden

**Severity:** low

**Guide location:** ch:EYE-CIRCUIT sec:EYE-CIRCUIT-MODEL

**File:** guide/04c-eye-circuit.md

**Line or section:** L0013–L0095

**Short excerpt:** λ_i^R(t)=[ζ_i^R E_OI(t)+λ_i^0+ζ_i^R F(t)]_+ ...

**Missing or unclear meaning:** Nothing is missing. About 15 new symbols appear on the main path before the physical conclusions. The question (can integrator noise give the observed amplitude and timing?) needs the chain, the neutrality condition G'(z) = 1, saturation, averaging over OMNs, and the feedback sign.

**Earlier teaching checked:** ch. 3 attractor tuning; ch. 7 forward model.

**Reader consequence:** High load for the readers most interested in the mechanism.

**Suggested action:** Keep the verbal chain, the G(z) = z condition, the parameter values and the feedback sign on the main path. Fold Eqs. 23–31 with their units. ch. 19 can then point to the fold rather than restating it.

**Essential or optional:** optional

**Confidence:** medium

#### S2-19

**Kind:** main_path_burden

**Severity:** low

**Guide location:** ch:PLACE-TESTS sec:PLACE-TOPOLOGY boundary paragraph

**File:** guide/05c-place-tests.md

**Line or section:** L0104–L0119

**Short excerpt:** Each of its d−j gradient components perpendicular to the face ... factor 2^{−(d−j)}

**Missing or unclear meaning:** The face-counting derivation is visible on the main path, while the reader mainly needs the result: boundary terms depend on the environment's geometry and matter for small rooms.

**Earlier teaching checked:** The Gaussian determinant fold is already folded.

**Reader consequence:** Extra density before the data comparison.

**Suggested action:** Fold the face-factor argument. Keep Eqs. 8–10, the rectangle rule and the limiting checks visible.

**Essential or optional:** optional

**Confidence:** medium

#### S2-20

**Kind:** glossary_gaps_and_organization

**Severity:** low

**Guide location:** ch:GLOSSARY

**File:** guide/glossary.md

**Line or section:** L0001–L0162

**Short excerpt:** - [[**Euler update:**]...] ... (after the hardware list, no heading)

**Missing or unclear meaning:** There are no entries for 'line attractor' (used in ch. 2), 'lag', or 'instantaneous attractor state' (if S2-01 is adopted). Part IV terms are appended under the hardware heading. Capitalization is inconsistent (Isotropy, Smoothness). The two 'translation' entries do not say how they differ.

**Earlier teaching checked:** —

**Reader consequence:** Lookup friction.

**Suggested action:** Add the three entries and a 'Simulation and methods' heading. Add 'contrast: translation symmetry concerns the network; translation invariance concerns readout statistics'.

**Essential or optional:** optional

**Confidence:** high

### Useful additions

#### A1

**Topic:** Physical intuition for the information–diffusion bound

**Placement:** ch:MEMORY-INFORMATION sec:MEMORY-BOUND, before the Cauchy–Schwarz proof

**Reader question:** Why should information in spikes limit how stable a memory can be, and why τ²?

**Why it helps:** It turns the central result into a statement about a circuit that observes itself.

**Minimum sufficient treatment:** 2–3 sentences, as in S2-05.

**Source support needed:** Burak & Fiete main p.3 interpretation paragraph

**Priority:** high

#### A2

**Topic:** Three objects: network state s, memory coordinate θ (flow projection), estimate θ̂

**Placement:** ch:MEMORY-DYNAMICS start of sec:MEMORY-LINEARIZATION; echoed briefly in ch. 14 roles

**Reader question:** What exactly diffuses when the network never sits exactly on the attractor?

**Why it helps:** It removes ambiguity across chapters 3–6, 9 and 14–17.

**Minimum sufficient treatment:** 2 sentences, as in S2-01.

**Source support needed:** Burak main p.2 and Fig. 1A

**Priority:** high

#### A3

**Topic:** Reconciling 'fixational drift' with 'systematic drift'

**Placement:** ch:PERSISTENCE at the systematic-drift definition; reminder at ch:EYE-DRIFT opening

**Reader question:** Is fixational drift a bias or random wandering?

**Why it helps:** It prevents a direct contradiction with the 2022 paper's title.

**Minimum sufficient treatment:** 1 sentence each place, plus a ch. 15 title change.

**Source support needed:** Ben-Shushan abstract (diffusive statistics)

**Priority:** high

#### A4

**Topic:** What must be measured to apply D and J to a real circuit

**Placement:** ch:MEMORY-DYNAMICS symmetric interpretation, or end of ch:MEMORY-INFORMATION

**Reader question:** Could I compute D from recordings?

**Why it helps:** It connects the formulas to observable quantities before the synthesis chapter.

**Minimum sufficient treatment:** 1 sentence, as in S2-10.

**Source support needed:** Burak main p.2 (Eq. 2 applicable to data), p.5 (sub-Poisson caveat)

**Priority:** medium

#### A5

**Topic:** Where noise comes from in hardware versus spike-count noise

**Placement:** ch:HARDWARE-DYNAMICS errors section or ch:HARDWARE-TESTS parameters

**Reader question:** What plays the role of Poisson spike noise on a chip?

**Why it helps:** It makes the D = ½ℓᵀBBᵀℓ transfer concrete: digital chips have no intrinsic noise unless it is injected (pseudo-random), while analog chips have device and thermal fluctuations and fixed mismatch acting as bias.

**Minimum sufficient treatment:** 2 sentences.

**Source support needed:** General electronics; ch. 16 already notes injected noise. A cited device-noise source would be needed for specifics.

**Priority:** medium

#### A6

**Topic:** Placing the filtered-Brownian transition on the data axis

**Placement:** ch:EYE-TIMING after the α(ℓ) values

**Reader question:** At what lag should the slope cross from about 2 toward 1 for real muscles?

**Why it helps:** It links the one-pole model to measured scales (fitted τ about 5 and 120 ms; the paper's muscle response about 180 ms) and to the observed slope of 1–2 over 0.01–1 s.

**Minimum sufficient treatment:** 1 sentence, with a caveat that the real plant has two time constants plus feedback.

**Source support needed:** Ben-Shushan Fig. 2b; main p.5 (~180 ms)

**Priority:** low

#### A7

**Topic:** Part IV chapter leads stating what is new

**Placement:** First paragraph of ch. 18–20

**Reader question:** Why read this after ch. 4/9/12?

**Why it helps:** It reduces apparent repetition and guides selective reading.

**Minimum sufficient treatment:** 1 sentence per chapter.

**Source support needed:** none

**Priority:** medium

#### A8

**Topic:** Expanded symbol list with cross-paper reuse

**Placement:** reading guide sec:READING-SCOPE

**Reader question:** Does χ (or q, η, τ_m) mean the same thing everywhere?

**Why it helps:** It flags the few dangerous collisions without renaming the papers' notation.

**Minimum sufficient treatment:** Add χ, η, τ_m, α and K lines, each with per-Part meanings.

**Source support needed:** none

**Priority:** low

### Retained choices

- The mechanism / derivation / interpretation triplet in ch. 3–5 makes neural versus mathematical assumptions visible; keep it.
- The ch. 1 eye-mechanics opening (elasticity holds, viscosity damps, inertia does not hold) gives a physical reason for persistent commands before any memory theory.
- The ch. 2 two-cell example and the ch. 3 tilted-decay example teach the projection geometry in two dimensions before the network formula; both are necessary.
- Fisher information is taught from a numerical example (background spikes lower information) before the formula, and the units note ('not bits') prevents a common misreading.
- The ch. 7 constructed χ = 0.82 versus R = 0.17 example is essential and correctly placed on the main path.
- The ch. 8 warning that the filter τ is not the synaptic τ, and ch. 10's statement that the spatial coordinate is not time, are precise disambiguations that should stay.
- Ch. 13's explicit list of what 'position' means in each paper is the model for the proposed state and drift reconciliations.
- Part III teaches electronics terms (current, voltage, capacitor, conductance, SRAM, PCM) just in time and keeps weight, state and value distinct. The burden is proportionate and the ch. 17 projection formula is a genuine bridge to Part I.
- Folds for the Poisson limit, Fokker–Planck, Stratonovich, Cramér–Rao, the coth solution, the impulse-response weights and the Gaussian determinant hold optional proof detail while the main text keeps the results usable.
- The ch. 20 width-convention fold (σ = √2·b) and the ch. 21 step-size example are concise practical teaching that only Part IV supplies.

### Remaining checks

- Paragraph-by-paragraph acceptance was not performed. Findings cover the main paths, terms and symbols checked above.
- Not every one of the roughly 250 first-definition spans was compared with the glossary for exact spelling.
- Figure labels, alt text and rendered fold visibility were not checked for terminology consistency.
- Chapter order, Part transitions and global flow are deferred to Stage 3, apart from the repetition notes in S2-08/09.

## Stage 3: Structure and learning path

The book's structure fits the reader's neurophysics interest. It moves from a physical problem (holding the eye still, keeping a value) through a spiking model and its derivations (diffusion, information bound, readout), then to empirical tests (eye drift), a separate spatial-coding model (place fields), a synthesis, and two requested extensions (hardware, simulation methods). The order mostly respects prerequisites. Chapters 1–2 supply the shared foundation, chapters 3–6 depend on them, the eye chapters reuse the attractor and diffusion results, and the place-field chapters need only chapters 1–2, as the reading guide says.

The main structural weaknesses are about progression, not missing chapters:
(1) No running neural example connects the attractor, diffusion, information and readout chapters to the eye data. The guide uses several unrelated two-variable toys. One small change (state that the ch. 2 toy is the rate form of the paper's mutual-inhibition network), plus one recurring eye example with paper-sourced numbers, would tie the path together.
(2) The chain from mechanism to model to derivation to test to what remains untested exists, but is scattered across chapters 1, 4, 13, 18 and 19. No visible map shows it per paper.
(3) Part IV and the early simulation section of Chapter 1 retell the same figures. Part IV works better as a methods companion linked from each paper's chapters, while staying a Part.
(4) Part II joins two very different kinds of study: eye drift tests Part I's dynamics in behaviour, while place fields are a static spatial-statistics model. Renaming or splitting it would make the route clearer, but this is optional.

The Stage 2 vocabulary findings remain the top content actions: what θ means off the attractor (S2-01), the meanings of 'drift' (S2-02), physical intuition for the bound (S2-05), and symbol collisions (S2-03).

Stage 1 F01 is narrowed after the coordinator's independent check. It is a supported optional qualification and research note, not a confirmed error, and my timing comparison is withdrawn. F06 (field-size part) is withdrawn after I verified the PubMed abstract myself. F07 is withdrawn on coordinator primary-source evidence; the Cannon & Robinson abstract could not be re-fetched in this session. F12 is withdrawn. F11 is confirmed.

One new source item arose and needs a correctness check before any running example uses it: Ben-Shushan main p.6 says the model's 350 ms MSD is 'in the order of 0.1 deg²', which appears inconsistent with Fig. 3a and the SI diffusion value (~0.01 deg²). No structural change can repair an equation; none of the equation findings depends on reordering.

### Part and chapter path

#### ch:READING-GUIDE

**Current purpose:** Orientation to the three papers, their results and limits; reading routes; mechanism/derivation/interpretation split; symbols; source copies.

**What reader should be able to explain:** What each paper claims and how strongly; which chapters serve which route; that guide checks of printed equations are not author corrections.

**Prerequisite locations:** none

**Retain or change:** retain with small changes

**Reason:** Accurate and well scoped. Add an evidence-chain map (C3), widen the symbol list (S2-03), list the ch. 1 sections place-field readers need (SR3), add Part IV cross-routes (SR2), and define the contribution labels only here (S2-11).

#### part:MECHANISMS

**Current purpose:** Burak–Fiete theory: background (ch. 1–2), central diffusion and information results (3, 5), supporting long-delay and readout results (4, 6).

**What reader should be able to explain:** How spike noise moves a stored value along an attractor, how fast, why spike information sets a minimum, and why readout saturates.

**Prerequisite locations:** reading guide

**Retain or change:** retain

**Reason:** Correct dependency order. The chapter map states the role of each result.

#### ch:FOUNDATIONS

**Current purpose:** Eye muscles and the need for tonic drive; Eq. 7–9; tuning and population code; Poisson variability; the 2012 simulation algorithm; covariance and MSD for eye motion.

**What reader should be able to explain:** What s, g, r, W, b and τ are physically; why one cell's count is noisy and a population less so; what the simulation updates; how bias and spread contribute to MSD.

**Prerequisite locations:** reading guide definitions

**Retain or change:** change (trim and route)

**Reason:** Essential shared foundation, but it carries the Fig. 2 interpretation before diffusion is taught (S2-08/09). Keep the algorithm and the conditional-independence point; point to ch. 4 for the comparison. The eye-specific 'what changes the movement' bullets could move to ch. 7–8 (optional).

#### ch:PERSISTENCE

**Current purpose:** Mechanical holding versus neural integrator; attractor geometry (two-cell); independent increments and Brownian diffusion; time-varying versus spatial randomness.

**What reader should be able to explain:** Why a stable pattern can hold a wrong value; why variance grows as 2Dt; why diffusion differs from bias; why place-field randomness is not memory noise.

**Prerequisite locations:** ch. 1 eye action and tuning

**Retain or change:** retain with one bridge

**Reason:** Add that the two-cell rate toy is the rate form of the paper's mutual-inhibition network, with a = 2/τ (SR1). Reconcile 'systematic' versus 'fixational' drift here (S2-02).

#### ch:MEMORY-DYNAMICS

**Current purpose:** Weak-noise approximation, linearization, left and right vectors, D formula, symmetric form, two-cell check.

**What reader should be able to explain:** Which part of a spike-induced disturbance survives, why the left vector rather than perpendicular projection, and how D depends on rates, slopes and τ.

**Prerequisite locations:** ch. 1 Eq. 7–9, ch. 2 attractor/diffusion, linear algebra

**Retain or change:** retain, add the coordinate definition

**Reason:** Move the Fig. 1A flow-projection definition here and state the state/θ/θ̂ distinction (S2-01, S2-13). Add the measurable-ingredients sentence (S2-10).

#### ch:MEMORY-LONG-DELAYS

**Current purpose:** Density evolution, line versus ring, state-dependent D, systematic drift scope, reading Figs. 1, 2 and S1.

**What reader should be able to explain:** Why ring error flattens without recovery; when variance stays linear despite state-dependent D; why the paper assumes no mean drift; what the simulations test.

**Prerequisite locations:** ch. 3

**Retain or change:** retain

**Reason:** Supporting role is clear. The S40 note could become a footnote. After S2-01, Fig. 1A becomes a recap here.

#### ch:MEMORY-INFORMATION

**Current purpose:** Fisher information, Cramér–Rao, information–diffusion bound, equality, matrix bound, controlled comparisons.

**What reader should be able to explain:** Why internal information limits stability; what equality requires; how N, rates, τ and tuning width change the bound and what each comparison holds fixed.

**Prerequisite locations:** ch. 3 D formula; ch. 1 Poisson

**Retain or change:** retain, add intuition

**Reason:** Central result; add the heuristic 'circuit reads its own spikes over τ' (S2-05).

#### ch:MEMORY-READOUT

**Current purpose:** Storage plus readout, naive versus ideal readout, saturation within τ, partial access, extensions, Eq. 6 caution.

**What reader should be able to explain:** Why longer observation helps less and less, the role of τ, and why the Eq. 6 inequality needs qualification within the paper's model.

**Prerequisite locations:** ch. 2 Brownian covariance, ch. 5 J

**Retain or change:** retain; mark extensions optional

**Reason:** Add the F01 optional note on shared spike noise. Move the white-noise definition out of the extension (S2-07). Fix the q collision (S2-03). Label the two-time-scale and Gaussian-noise extensions as optional so the eye route can skip them.

#### part:OBSERVATIONS

**Current purpose:** Eye study (7–9), place-field study (10–12), synthesis (13).

**What reader should be able to explain:** How one neuron's spikes can reveal a shared upstream drive; how a wandering command becomes smooth superdiffusive eye motion; how thresholded random inputs explain field statistics.

**Prerequisite locations:** Part I

**Retain or change:** optional change

**Reason:** The two halves have different dependencies and logic (SR4). Renaming or splitting would make the place route clearer.

#### ch:EYE-DRIFT

**Current purpose:** Pathway, recordings, forward fit, inverse filter, independent-noise bound, χ.

**What reader should be able to explain:** Why a correlation of 0.17 can coexist with an 82% shared fraction, and which assumptions (gain transfer, independence) carry the inference.

**Prerequisite locations:** ch. 1 covariance/CV; ch. 2 integrator

**Retain or change:** retain

**Reason:** Strong chapter. Unify the names for the shared drive (S2-14); add the drift-terminology reminder.

#### ch:EYE-TIMING

**Current purpose:** Measurement-noise offset; filtered white versus filtered Brownian MSD.

**What reader should be able to explain:** Why private motor noise saturates and why diffusion filtered by muscles gives a slope between 1 and 2.

**Prerequisite locations:** ch. 1 MSD, ch. 2 diffusion, white noise (currently ch. 6 extension)

**Retain or change:** retain, add scale link

**Reason:** Point to the moved white-noise definition. Add one sentence placing the transition lag on the measured axis (Stage 2 A6).

#### ch:EYE-CIRCUIT

**Current purpose:** Integrator model through motor neurons and plant, feedback, scaling, figure roles, limits.

**What reader should be able to explain:** How integrator noise produces the eye-drift amplitude and timing, what is constrained versus tuned, and what is not identified.

**Prerequisite locations:** ch. 2–3 attractor/diffusion, ch. 5 J, ch. 7 forward model

**Retain or change:** retain; optionally fold the equations

**Reason:** The main path is heavy (S2-18). The figure-reading table is excellent. It closes the theory-to-behaviour bridge.

#### ch:PLACE-FIELDS

**Current purpose:** Recordings; Gaussian-process input and threshold; Kac–Rice counts; inference of q and σ from mean field length and gap.

**What reader should be able to explain:** How one smooth random input yields several fields, and why mean length plus mean gap fix q and σ.

**Prerequisite locations:** ch. 1 rate map/place cell; ch. 2 map versus wandering value

**Retain or change:** retain

**Reason:** Self-contained. Note the Euler-characteristic forward reference (S2-16).

#### ch:PLACE-SIZES

**Current purpose:** High-peak parabola, size laws per dimension, slices, boundary slopes.

**What reader should be able to explain:** Why size distributions differ in 1D, 2D and 3D, and which predictions are limiting versus exact.

**Prerequisite locations:** ch. 10

**Retain or change:** retain

**Reason:** Clear separation of limiting and exact results.

#### ch:PLACE-TESTS

**Current purpose:** Euler characteristic, what was fitted versus tested, processing effects, random-wiring interpretation.

**What reader should be able to explain:** Why topology is an independent test, which agreements are fitted, and what the wiring interpretation does not establish.

**Prerequisite locations:** ch. 10–11

**Retain or change:** retain; fold face factors

**Reason:** Optional folding (S2-19); disambiguate χ.

#### ch:SYNTHESIS

**Current purpose:** Separate map, dynamics and movement; shared-position covariance; matched tests; related work; joint experiment.

**What reader should be able to explain:** Why no paper alone establishes one circuit, and what joint measurement would.

**Prerequisite locations:** ch. 3–12

**Retain or change:** retain; host the evidence-chain table

**Reason:** This is the natural place to collect the per-paper chain (C3) if it is not put in the reading guide.

#### part:HARDWARE

**Current purpose:** Requested extension: physical storage versus neural state versus remembered value; feedback; selected chips; a proposed test protocol.

**What reader should be able to explain:** Where a chip's memory physically lives and which error sources (decay, bias/pinning, noise projection, readout) limit a remembered angle.

**Prerequisite locations:** Part I ch. 2–3, 5; ch. 8 measurement offset

**Retain or change:** retain

**Reason:** Proportionate burden. Ch. 17 links back to the Part I projection and the eye-measurement lessons.

#### ch:HARDWARE-MEMORY

**Current purpose:** Weights versus states versus value; storage media; update paths.

**What reader should be able to explain:** Why correct weights do not guarantee a retained cue.

**Prerequisite locations:** ch. 1 Eq. 8, ch. 2 attractor

**Retain or change:** retain

**Reason:** Mirrors the state/θ/θ̂ distinction; cross-reference S2-01 once it is added.

#### ch:HARDWARE-DYNAMICS

**Current purpose:** Feedback-extended time constant; restoring versus neutral; silicon examples.

**What reader should be able to explain:** How tuning feedback gain sets persistence and why a continuous memory accumulates error while a bit does not.

**Prerequisite locations:** ch. 2 diffusion, ch. 4 drift

**Retain or change:** retain; retitle 'drift'

**Reason:** S2-02. A5 (noise source) belongs here, worded within the modelled update rule (C7).

#### ch:NEUROMORPHIC-SYSTEMS

**Current purpose:** Architectures and 2025–26 results classified by memory type.

**What reader should be able to explain:** Which result concerns temporal state, weight adaptation, or material stability, and what each does not show.

**Prerequisite locations:** ch. 14

**Retain or change:** retain with qualifications

**Reason:** Apply F04 and F05.

#### ch:HARDWARE-TESTS

**Current purpose:** Proposed protocol separating drift, diffusion and readout error; parameter actions; matched comparisons.

**What reader should be able to explain:** How to measure b(θ), D(θ) and readout noise on a chip, and convert time scales.

**Prerequisite locations:** ch. 3 projection, ch. 8 offset

**Retain or change:** retain

**Reason:** Say that ℓ is the v of ch. 3 (S2-04).

#### part:SIMULATIONS

**Current purpose:** Requested extension: methods, settings, code and data, reproduction.

**What reader should be able to explain:** What each simulation adds as evidence and what must match to reproduce it.

**Prerequisite locations:** matching paper chapters

**Retain or change:** retain as a Part; change the routing

**Reason:** Use it as a methods companion with links from ch. 4, 9 and 12; trim the retelling (SR2, S2-08).

#### ch:SIMULATING-MEMORY

**Current purpose:** State update, ring and mutual-inhibition settings, analytic versus simulated curves, code status.

**What reader should be able to explain:** Exactly what was simulated and what numerical choices (step size, one-spike versus count rule, units) a reproduction must fix.

**Prerequisite locations:** ch. 1, 3–4

**Retain or change:** trim

**Reason:** Lead with its unique content; link instead of re-reading Fig. 2. F09 belongs here.

#### ch:SIMULATING-EYE

**Current purpose:** Data versus model, pathway stages, controls, MATLAB code and data.

**What reader should be able to explain:** Which reproduction task each artifact supports.

**Prerequisite locations:** ch. 7–9

**Retain or change:** trim

**Reason:** The stage and control narrative repeats ch. 9; keep the code/data sections. Apply F03.

#### ch:SIMULATING-PLACE

**Current purpose:** Map generation, fitted versus tested, detection and preprocessing, tools.

**What reader should be able to explain:** How to generate and measure maps compatibly with the data, including the width convention.

**Prerequisite locations:** ch. 10–12

**Retain or change:** retain

**Reason:** The least repetitive Part IV chapter.

#### ch:SIMULATION-TOOLS

**Current purpose:** Cross-paper reproduction practice.

**What reader should be able to explain:** How to check convergence and record the choices that determine a conclusion.

**Prerequisite locations:** ch. 18–20

**Retain or change:** retain

**Reason:** Short and practical.

#### ch:GLOSSARY

**Current purpose:** Lookup.

**What reader should be able to explain:** —

**Prerequisite locations:** —

**Retain or change:** small change

**Reason:** S2-20.

#### ch:REFERENCES

**Current purpose:** Bibliography.

**What reader should be able to explain:** —

**Prerequisite locations:** —

**Retain or change:** small change

**Reason:** F11 (Nghiem initials); optionally add a grid-cell definition source (F06 remainder).

### Structural recommendations

#### SR1

**Priority:** high

**Current location:** ch. 2 sec:FOUNDATIONS-ATTRACTOR example; ch. 3 sec:MEMORY-SYMMETRIC example; ch. 5 bound-strictness example; ch. 6 examples; ch. 9 scaling

**Proposal:** Make one running neural example visible. (a) State that the ch. 2 two-cell rate toy is the rate form of the paper's mutual-inhibition network: the common mode decays at rate a = 2/τ and the difference is neutral. Then carry that network through D (ch. 3), J and equality (ch. 5) and readout (ch. 6), as the guide already partly does. (b) Thread one eye example, 'holding gaze after a saccade', using paper-sourced numbers: D ≈ 0.014 deg²/s from Ben-Shushan SI, the 350 ms window, filtered slope ~1.7. Use it from ch. 2 to ch. 9 and in ch. 17 as the hardware target.

**Teaching benefit:** The reader can follow one physical system from mechanism to formula to measurement instead of re-orienting to a new toy in each chapter.

**Prerequisite evidence:** ch. 2 L0083–L0092 (ṙ = −a·x); ch. 3 L0268–L0278 (common mode relaxes, difference neutral); ch. 2 L0173 uses an illustrative D = 0.02 deg²/s; ch. 9 L0199 gives D = 0.0139 deg²/s from SI.

**Cost or risk:** Small text edits; possibly re-parameterizing the ch. 2 figure. Do not use the main-text '0.1 deg² at 350 ms' value until it is checked (scientific follow-up SF1).

**Affected chapters:**

- ch:PERSISTENCE
- ch:MEMORY-DYNAMICS
- ch:MEMORY-INFORMATION
- ch:MEMORY-READOUT
- ch:EYE-TIMING
- ch:EYE-CIRCUIT
- ch:HARDWARE-TESTS

#### SR2

**Priority:** medium

**Current location:** Part IV; ch. 1 sec:FOUNDATIONS-SIMULATION; ch. 4 sec:MEMORY-FIGURES; ch. 9

**Proposal:** Keep Part IV, but route it as each paper's methods companion. At the end of ch. 4, 9 and 12 add 'Methods and reproduction: ch. 18/19/20'. Open each Part IV chapter with what it adds. Reduce ch. 1's simulation section to the update algorithm, and remove the duplicated figure interpretations (S2-08).

**Teaching benefit:** Readers interested in a paper see its test methods when they need them; total reading load drops; the requested coverage stays.

**Prerequisite evidence:** Repeated passages listed in S2-08: 01 L0288, 02b L0189, 11 L0034; 12 L0013–L0051 versus 04c.

**Cost or risk:** Low. Do not cut ch. 18's unique numerical cautions (one-spike versus count rule, D_r = D_s/τ²).

**Affected chapters:**

- ch:FOUNDATIONS
- ch:MEMORY-LONG-DELAYS
- ch:EYE-CIRCUIT
- ch:PLACE-TESTS
- ch:SIMULATING-MEMORY
- ch:SIMULATING-EYE
- ch:SIMULATING-PLACE

#### SR3

**Priority:** medium

**Current location:** reading guide sec:READING-START; ch. 1

**Proposal:** Define a short shared foundation route instead of swapping chapters. Place-field readers need ch. 1 sec:FOUNDATIONS-SPIKES and sec:FOUNDATIONS-POISSON plus ch. 2 sec:FOUNDATIONS-RANDOMNESS, not eye mechanics, Eq. 7–9 or simulation. List these sections in the reading paths.

**Teaching benefit:** The place-field route becomes genuinely short. The current 'read the two foundations chapters' sends readers through about 20 pages of eye and memory material.

**Prerequisite evidence:** ch. 10–12 use only rate map, place cell, tuning and the spatial-versus-time distinction; no use of Eq. 7–9, D or J was found.

**Cost or risk:** Very low; a text change in the reading guide only.

**Affected chapters:**

- ch:READING-GUIDE

#### SR4

**Priority:** low

**Current location:** part:OBSERVATIONS

**Proposal:** Either rename Part II to state its two halves (e.g. 'Testing memory dynamics in eye drift; a spatial model of place fields'), or split it into Part IIa (ch. 7–9) and Part IIb (ch. 10–12), keeping ch. 13 as the closing synthesis.

**Teaching benefit:** Signals that eye drift tests Part I's dynamics while place fields are an independent static-map model. This prevents readers from expecting a dynamical link that ch. 13 says is untested.

**Prerequisite evidence:** Part II intro; ch. 2 L0223–L0226; ch. 13 L0029.

**Cost or risk:** Navigation and ID changes need author approval under the structure lock.

**Affected chapters:**

- ch:EYE-DRIFT…ch:SYNTHESIS

#### SR5

**Priority:** low

**Current location:** ch. 6 sec:MEMORY-EXTENSIONS; ch. 12 boundary derivation; ch. 9 Eqs. 23–31

**Proposal:** Mark ch. 6 extensions as optional for the eye route (after moving the white-noise definition). Fold the face-factor derivation and Eqs. 23–31, keeping the results and roles visible.

**Teaching benefit:** Lowers the main-path load without losing content.

**Prerequisite evidence:** S2-07, S2-18, S2-19.

**Cost or risk:** Make sure ch. 8 and ch. 19 links still land on visible text.

**Affected chapters:**

- ch:MEMORY-READOUT
- ch:EYE-CIRCUIT
- ch:PLACE-TESTS

### Clarifications and additions

#### C1

**Priority:** high

**Placement:** ch. 3 start of sec:MEMORY-LINEARIZATION

**Proposal:** Define θ for off-attractor states (flow projection, the paper's instantaneous attractor state). Distinguish s, θ and θ̂, state that the state variables are the activations, and give one name for the stored value (S2-01, S2-13).

**Reason:** Every later diffusion, readout and hardware statement depends on what θ means.

**Source requirement:** Burak main p.2, Fig. 1A (already in packet)

#### C2

**Priority:** high

**Placement:** ch. 2 systematic-drift definition; ch. 7 opening; ch. 15 title

**Proposal:** Reconcile 'fixational drift' (random eye motion) with 'systematic drift' (mean velocity). Retitle ch. 15's 'continuous drift' (S2-02).

**Reason:** Otherwise the 2022 title reads as contradicting ch. 2 and ch. 4.

**Source requirement:** Ben-Shushan abstract

#### C3

**Priority:** high

**Placement:** reading guide (or ch. 13 table)

**Proposal:** A conceptual evidence-chain map per paper: physical system → modelled actors and equations → derived prediction → simulation test → empirical test → untested link. Example for Burak–Fiete: spikes/activations → Eq. 7–11 → D, J, bound → Fig. 2 simulations → no animal test in the paper; the eye study provides a related but non-equivalent test. Recommended as a table or diagram; not created here.

**Reason:** This makes the mechanism–model–test bridge visible, which is the reader's stated priority. It currently has to be pieced together from ch. 1, 4, 13, 18 and 19.

**Source requirement:** existing packet sources

#### C4

**Priority:** high

**Placement:** ch. 5 sec:MEMORY-BOUND

**Proposal:** Heuristic: the circuit re-reads about τ of its own spikes, so 2Dτ ≥ 1/(Jτ). Label it as the paper's interpretation (S2-05).

**Reason:** Gives a physical reason for the central inequality.

**Source requirement:** Burak main p.3

#### C5

**Priority:** medium

**Placement:** ch. 6 sec:MEMORY-READOUT-SETUP (one sentence) plus an optional fold

**Proposal:** State that the independence of ε_k and η_k means process increments are treated as separate from the observed count noise, whereas the network's own spikes generally produce both. Readout from the actual spike stream needs a joint model. An optional research note may give the two-cell same-spike result with its conditions: frozen local Gaussian noise, known initial transverse state, and a limit 2/(Jτ) that is a Cramér–Rao bound for Poisson spikes.

**Reason:** This is F01 as narrowed by the independent check.

**Source requirement:** Burak SI S57–S62; the reviewer-derived calculation must stay labelled guide-derived and unconfirmed

#### C6

**Priority:** medium

**Placement:** ch. 6 (q), ch. 12 (χ), reading-guide symbol list, ch. 17 (ℓ = v)

**Proposal:** Remove the within-chapter q collision; disambiguate χ; say that ℓ is v (S2-03, S2-04).

**Reason:** These prevent misreading inside a derivation and across papers.

**Source requirement:** none

#### C7

**Priority:** low

**Placement:** ch. 15 or ch. 17

**Proposal:** A5 reworded: in a deterministic configured update rule (digital or integer LIF, e.g. Aitsam), there is no stochastic neural-noise term unless one is added. Analog circuits have device fluctuations and fixed mismatch, which act as noise and bias. Do not claim that physical digital chips are free of timing variation or hardware errors.

**Reason:** This maps the B term of D = ½ℓᵀBBᵀℓ onto the modelled implementation without overstating.

**Source requirement:** Aitsam §2 (deterministic LIF); a cited analog-noise source if specifics are added

#### C8

**Priority:** low

**Placement:** ch. 3 sec:MEMORY-SYMMETRIC interpretation

**Proposal:** List the measurable ingredients of D (S2-10).

**Reason:** Connects the formula to experiments before ch. 13.

**Source requirement:** Burak main p.2, p.5

#### C9

**Priority:** low

**Placement:** ch. 8 after α(ℓ) values

**Proposal:** Place the filter transition on the data's lag axis (Stage 2 A6).

**Reason:** Links the one-pole teaching model to Fig. 3.

**Source requirement:** Ben-Shushan Fig. 2b; main p.5

#### C10

**Priority:** low

**Placement:** ch. 16 Aitsam paragraph; ch. 16 Sun model

**Proposal:** Apply F04 (host-smoothed centroid input, deterministic network, accuracy/lag trade-off) and F05 (LMU sliding-window state).

**Reason:** Accurate classification of what each hardware result shows.

**Source requirement:** Aitsam §3–4; Sun Methods (in packet)

#### C11

**Priority:** low

**Placement:** book-wide

**Proposal:** One first-definition mark per term; one name for the Burak SI; glossary additions (line attractor, lag, instantaneous attractor state) and a 'Simulation' heading; Nghiem initials; optionally a dedicated grid-cell definition source (S2-06, S2-12, S2-20, F11, F06 remainder).

**Reason:** Consistency and lookup.

**Source requirement:** Nghiem PMC11831129 (coordinator-verified); a grid-cell review if added

### Reconsidered findings

#### F01

**Disposition:** narrowed: retained as an optional qualification and research note, not a guide error; severity lowered to low–medium

**Evidence:** Guide 03b L0019 ('In this approximation, these increments and errors are independent') and L0032 already scope the model. The independent check confirms the same-spike cross-covariance (correlation 1/(τ√(2DJ)), equal to 1 at equality) and the two-cell factor of two in the limit (b·[coth(L/τ)+1] versus b·coth(L/τ)).

**Reason:** Three of my statements were imprecise and are withdrawn. (1) 'Cue-state information decays as e^{−t/τ}': it is the intensity sensitivity that decays as e^{−t/τ}; the information rate decays as e^{−2t/τ}. (2) The contrast 'approach time τ/2 versus 1/√(2DJ)' compared unlike definitions; at equality both residual variances decay as e^{−2L/τ}. (3) For Poisson spikes, 2/(Jτ) is only a Cramér–Rao bound, and my total-error claim 'total ≤ 2D(T+2τ)' assumed attainability and a known initial transverse state. The general concern stands: the paper's readout model is not the joint observation model for an observer who receives the memory network's own spikes.

#### F02

**Disposition:** retained

**Evidence:** 04c L0170 versus Eq. 1 (main p.6); saturating synapses at Eq. 26.

**Reason:** No new evidence.

#### F03

**Disposition:** retained

**Evidence:** 12 L0007; Ben-Shushan p.9 leave-one-out stated only for rate prediction.

**Reason:** No new evidence.

#### F04

**Disposition:** retained

**Evidence:** 09 L0029; Aitsam §3.2, §4.3.

**Reason:** Wording should follow C7 for the noise statement.

#### F05

**Disposition:** retained (optional)

**Evidence:** 09 L0049 disclaimer; Sun Methods Eq. 4–8.

**Reason:** No new evidence.

#### F06

**Disposition:** field-size suspicion withdrawn; citation-source suggestion retained as optional

**Evidence:** PubMed 42203876 abstract (fetched this session): 'the sizes of place fields were very similar between the two subregions, across 5 different environment sizes … 6 m to 200 m'.

**Reason:** The guide's ch. 13 L0125 claim is supported. Citing a bat CA3/CA1 paper for the general grid-cell definition (ch. 1 footnote f-anatomy) is still better served by a dedicated source.

#### F07

**Disposition:** withdrawn

**Evidence:** Coordinator primary-source check: Massoud & Horiuchi author manuscript (32 positions, Eq. 3, Figs. 13, 15); Cannon & Robinson abstract (>20 s intact, ~200 ms minimum after injections, in darkness after saccades). My own re-fetch of the Cannon abstract returned 403.

**Reason:** Both numbers are supported. My independent confirmation of Cannon & Robinson is limited to the coordinator's evidence.

#### F08

**Disposition:** retained

**Evidence:** 05c L0119, L0214; Mainali Fig. 4A (room 72.0 m³, σ = 4.0).

**Reason:** No new evidence.

#### F09

**Disposition:** retained (optional)

**Evidence:** 11 L0032; Burak p.6.

**Reason:** —

#### F10

**Disposition:** retained (optional)

**Evidence:** 05c L0305; Mainali Methods S2.

**Reason:** —

#### F11

**Disposition:** confirmed

**Evidence:** Coordinator: PMC11831129 gives Trang-Anh E. Nghiem.

**Reason:** Use T. A. E. or T.-A. E. consistently.

#### F12

**Disposition:** withdrawn

**Evidence:** Coordinator HTML check: no duplicated paragraphs in the four Part pages.

**Reason:** It was a packet artifact.

#### S2-01…S2-20

**Disposition:** retained; S2-09 merged into S2-08/SR2

**Evidence:** Re-checked against nearby qualifications: ch. 3 L0068 says 'displacement to a different fixed point' but does not define θ for a noisy state (S2-01 stands); ch. 2 L0184 defines systematic drift with no fixational-drift reconciliation (S2-02 stands).

**Reason:** —

#### Stage2 A5

**Disposition:** reworded as C7

**Evidence:** Coordinator note; Aitsam's network is deterministic integer LIF.

**Reason:** Restrict the statement to the modelled or configured update rule; do not claim physical chips are noise-free.

### Top actions in order

#### 1

**Kind:** clarification (essential)

**Finding ids:**

- S2-01
- S2-13
- C1

**Action:** Define the off-attractor memory coordinate and the s/θ/θ̂ distinction at the start of ch. 3.

**Why first:** Every later chapter's 'what diffuses, what is read, what the chip stores' depends on it, and it costs about 3 sentences.

#### 2

**Kind:** clarification (essential)

**Finding ids:**

- S2-02
- C2

**Action:** Reconcile 'fixational' versus 'systematic' drift; retitle ch. 15.

**Why first:** It removes an apparent contradiction right at the Part I to Part II bridge.

#### 3

**Kind:** addition (essential)

**Finding ids:**

- S2-05
- C4

**Action:** Add the physical intuition for the information–diffusion bound.

**Why first:** It is the central result, and the neurophysics reader currently has algebra only.

#### 4

**Kind:** structure

**Finding ids:**

- SR1

**Action:** Make the mutual-inhibition network and the gaze-holding eye example explicit running examples, with paper-sourced numbers after SF1 is checked.

**Why first:** Gives the mechanism → formula → measurement continuity the user asked about.

#### 5

**Kind:** addition

**Finding ids:**

- C3

**Action:** Add the per-paper evidence-chain map.

**Why first:** It lets readers see what was derived, simulated, measured and left untested.

#### 6

**Kind:** clarification

**Finding ids:**

- S2-03
- S2-04
- C6

**Action:** Fix the ch. 6 q collision; disambiguate χ; note ℓ = v.

**Why first:** Prevents misreading inside derivations.

#### 7

**Kind:** qualification

**Finding ids:**

- F01
- C5

**Action:** Add the one-sentence shared-spike-noise note in the ch. 6 setup, with an optional labelled research fold.

**Why first:** Makes a hidden modelling assumption visible; not urgent because the guide already scopes it.

#### 8

**Kind:** structure

**Finding ids:**

- SR2
- SR3
- S2-08

**Action:** Route Part IV as a methods companion, trim the duplicate retelling, and list the place-route sections.

**Why first:** Recovers the space needed for actions 1–5 and shortens the routes.

#### 9

**Kind:** qualification

**Finding ids:**

- F02
- F03
- F04
- F05
- F08
- F09
- C7

**Action:** Apply the local scientific-wording qualifications.

**Why first:** Small edits, each local.

#### 10

**Kind:** presentation

**Finding ids:**

- S2-06
- S2-12
- S2-20
- F11
- SR4
- SR5
- S2-07

**Action:** Single definition marks, glossary, citations, optional Part rename, folds, white-noise placement.

**Why first:** Consistency work best done last, after content changes.

### What to keep

- The overall order: Part I theory before Part II tests, and place fields after the shared foundation. No whole-chapter swaps are needed.
- The mechanism / derivation / interpretation triplets in ch. 3–5, and the folds for proofs.
- The explicit, labelled checks of printed source equations, kept separate from the 2017 correction. All were confirmed in Stage 1.
- Ch. 1's physical opening (eye mechanics, Eq. 7–9 as a feedback cycle) and ch. 2's map-versus-wandering distinction.
- Ch. 7's χ versus R example, ch. 8's filtered white versus filtered Brownian derivation, and ch. 9's figure-reading table and limits section.
- Ch. 10–12's separation of exact, limiting and fitted results, and the fitted-versus-tested table.
- Ch. 13's per-paper 'position' disambiguation and its proposed joint experiment.
- Part III's weight/state/value framing and ch. 17's projection-based test protocol. Both are requested coverage and real bridges to Part I.
- Part IV's unique practical content: settings, one-spike versus count rule, unit conversions, code and data access, width convention, convergence and reproduction records.

### Coverage and limits

- covered: Reading guide, all four Part introductions, all 21 chapters, glossary and references, each given a path entry. Stage 1 and Stage 2 findings were re-checked against nearby text, the coordinator evidence and one new fetch (Maimon PubMed abstract).
- scientific_followups: ["SF1 (new, needs a check before use in a running example): Ben-Shushan main p.6 says the model's '350 ms … MSD … in the order of 0.1 deg²', but Fig. 3a shows measured MSD of about 0.01–0.02 deg² at 0.35–0.6 s, and SI S6 gives 2D ≈ 0.028 deg²/s (≈0.01 deg² at 0.35 s). Check against the Fig. 4d/5d axes in the PDF before quoting any value. The guide does not currently quote 0.1 deg².", 'F01 as narrowed: any full-recall calculation that includes unknown transverse initial state and Poisson attainability remains open research; it is not for the main text.']
- limits: ['No figure pixels inspected and no image sweep proposed.', 'No edits, simulations or code runs.', 'Cannon & Robinson and Massoud are accepted on coordinator evidence; my Cannon re-fetch failed (403).', 'The peer-review file and author code remain unread.', 'This is an expert structural review, not a formal release acceptance.']

## Coordinator checks after the original replies

These distinguish supported improvements, unresolved questions and objections resolved by checking the sources. No manuscript changes were made.

### F12

Not a duplicated paragraph in the generated reader HTML. Repeated purpose in packet is not a reader defect. Local HTML text checked, no pixel audit.

### F11

Confirmed bibliography inconsistency. Primary article gives Trang-Anh E. Nghiem, initials TAE; use T. A. E. or T.-A. E. consistently. No guide edit made.

Primary url: https://pmc.ncbi.nlm.nih.gov/articles/PMC11831129/

### F03

Valid clarification. Source explicitly assigns leave-one-out to firing-rate prediction. Current simulation paragraph puts the held-out sentence after reconstructed movement and can imply wider validation. No evidence supplied that reconstruction uses or does not use held-out fits; narrow wording to documented claim.

Source: inputs/paper-text/ben-shushan-2022-fixational-drift.txt:907-931

### F04

Useful supported qualification. Actual Aitsam text confirms host-smoothed centroid, deterministic period-two finite-grid dynamics, 5.65 vs 2.02 cell mean error and 115 ms added lag. The current guide already limits the persistence interval and robot/power claims. Additions would explain performance trade-off, not reverse its existing persistence statement.

Source: inputs/additional-sources/aitsam-2026.txt:1116-1150

### F05

Optional useful addition. Actual Sun Methods identify LMU-like slow state encoding a sliding input window. Guide labels scalar toy model as not full architecture, so no demonstrated factual error.

Source: inputs/additional-sources/sun-review.txt:878-885

### F02

Supported wording concern. A proportionality may hide a dimensional factor. The absolute-versus-fractional-slope distinction is useful; avoid presenting units alone as a proven source error or treating heuristic scale as full saturating model derivation.

### F09

Useful optional measurement clarification. Argmax coordinate on finite lattice need not equal noise-free flow projection; existing text already distinguishes it from ideal spike readout. Quantization and transient effects belong beside the simulation comparison.

### F06

Withdraw field-size suspicion. The original Maimon abstract explicitly supports similar CA1/CA3 field sizes across five environment sizes (6 to 200 m). Nature body fetch failed, but indexed original PDF abstract and PubMed original abstract agree. A separate grid-cell-definition source is still a reasonable citation addition.

Primary url: https://www.nature.com/articles/s41586-026-10537-0.pdf

Abstract url: https://pubmed.ncbi.nlm.nih.gov/42203876/

### F07

Withdraw numeric suspicion. Massoud/Horiuchi author manuscript text confirms 32 possible bump positions, Eq.3 and Figs.13,15. Cannon/Robinson original abstract confirms intact time constant >20 s and minimum about200ms after injections, measured after saccades in darkness.

- https://www.researchgate.net/publication/260666649_A_Neuromorphic_VLSI_Head_Direction_Cell_System
- https://journals.physiology.org/doi/abs/10.1152/jn.1987.57.5.1383

Limits: Massoud source was author manuscript text on ResearchGate; Cannon original abstract, not full article.

### F01

Supported optional qualification/research question; not a confirmed guide error. Existing guide already scopes independence. Root requested independent gpt-6.1-sol high check; see readout-independent-check.md. Local Gaussian two-cell factor-of-two asymptote checked; general Poisson inverse FI is only CR bound. Initial transverse state matters. The alleged faster residual-variance relaxation is not supported; both tails decay exp(-2L/tau) at equality.

Supporting check: readout-independent-check.md

### SF1

No confirmed contradiction. Main Fig4d is internal E_OI; Fig5d is filtered actual eye E. The SI value 2D about100arcmin²/s is an illustrative assumption for a CV calculation, not a fitted value of those curves. A future D about0.014 example must be labelled constructed. Distinguish within-segment variance2DT/6 from endpointMSD2DT. No current guide error.

Supporting check: SF1-source-check.md

