# Eye and place chapters: focused physical-meaning gap review

First verified checkpoint: 2026-10-29T10:59:29.7863631+02:00.
Second verified checkpoint: 2026-10-29T11:01:49.3063433+02:00.
Measured wall time between these checkpoints: 2 minutes 19.52 seconds. Awake execution time is unverified; Windows sleep/resume logs were not read. Two earlier messages used guessed times and were corrected to the root agent. No evidence of a clock change was found.

Scope: read-only gap review of 04-eye-drift, 04b-eye-timing, 04c-eye-circuit, 05-place-fields, 05b-place-sizes, 05c-place-tests, and 06-synthesis. Earlier reading checked: 00-reading-guide and the relevant teaching in 01-foundations. Audience: calculus, basic probability, and linear algebra; neuroscience must be taught. Read course-study-guide-builder/SKILL.md and references/pedagogy-language-contract.md. The root owns manuscript changes. This report is neither a full manuscript audit nor the later separate correctness, wording, or reader-flow review.

Actual primary sources inspected: Ben-Shushan 2022 main PDF, Mainali 2025 main PDF, and Mainali 2025 supplement, using local PDF text extraction. Existing footnotes and equations supplied locations, but the source content itself was read for the recommended mechanism explanations. No source figures needed a new visual inspection for these prose findings.

## 1. Give the movement-to-rate coefficients a concrete meaning

Passage: 04-eye-drift.md, section EYE-FORWARD-FIT, lines 61-76, especially "Position alone does not predict a motor neuron's activity during a movement" and the definition of k, r, m through units. The inverse-filter section, lines 102-144, then uses these coefficients to derive two decay times.

Finding: the passage teaches which derivatives are multiplied and checks units, but does not yet explain the different demands on a motor command. The reader can do the algebra without understanding why a cell can need a different rate at the same eye angle, or what changing k, r, or m means. Foundations teaches rate and tuning slope, but not this physical distinction. The pathway names muscles and eye mechanics, which does not supply the missing step.

Suggested short insertion after the coefficient units, before the inverse calculation:

> The position term describes the ongoing command associated with holding the eye at an angle. The velocity term allows a different command while the eye passes through that same angle, and the acceleration term allows a further change while its velocity changes. Thus k measures extra firing per degree of held position, r extra firing per degree per second of velocity, and m extra firing per degree per second squared of acceleration. These are fitted coefficients for the combined neural and mechanical relationship; m is not a direct measurement of the eye's mass.

Then attach one concise consequence to the inverse equation:

> At rest the model gives x=f/k, so doubling k halves the position offset predicted from the same steady rate. During a change, the r and m terms determine how that offset is approached, giving the fast and slow response times below.

Evidence and limits: Ben-Shushan main p. 9, Eqs. 2-7, and p. 11, Eqs. 28-31, explicitly connect the empirical relation and muscle/plant model. The static consequence follows directly from derivatives being zero. The existing units are correct and should remain visible. This repair avoids claiming k is a literal stiffness, r a literal viscosity, or m a literal mass. A more detailed force/torque explanation would require additional physiological evidence and is unnecessary here.

## 2. Explain what the simplified filter's mismatch does to the eye

Passage: 04b-eye-timing.md, EYE-FILTERED-MSD, lines 110-124, especially tau dot(E)+E=B and v=(B-E)/tau. Current text says velocity loses its past value over tau, then derives its covariance.

Finding: the stochastic derivation is strong, but the physical reading of the first equation is left to the reader. It should say what acts on what and what a larger response time changes, before the weighted-noise calculation. The earlier low-pass definition describes frequency suppression, while this is the first explicit command-to-angle equation in the simplified teaching example.

Suggested insertion immediately after the first equation:

> Here B is the changing position command and E is the eye angle that follows it. The difference B-E drives eye velocity: a command to the right of the current eye position makes the eye move right. For the same difference, a larger tau gives a smaller velocity, so the eye takes longer to catch up. It smooths the rapid changes in the command.

After the short- and long-lag formulas, add only if useful:

> At fixed D, increasing tau reduces the short-lag displacement and moves the transition to linear growth to longer lags. It does not remove the long-lag accumulation, whose limiting slope is still 2D.

Evidence and limits: this is an interpretation of the guide's explicitly marked one-exponential teaching reconstruction, not a new empirical claim. The source main pp. 6-8 and Fig. 5 distinguishes internal position from the smoother eye angle. The formula itself gives velocity in deg/s when B and E are degrees and tau seconds. "Limiting slope" in the last sentence means dM/dell=2D, not the logarithmic slope alpha=1; write "long-lag MSD growth rate" if ambiguity remains. Keep the one-exponential simplification label visible.

## 3. Connect normalized threshold and firing gain to different biological changes

Passage: 05-place-fields.md, PLACE-GP, lines 34-42, especially F=a[z-q]+ and "The original input threshold is q sigma_h." Later passages explain that threshold alters field count, shape, and topology, but its biological meaning remains thin. The later gain conversion in 05c lines 117 does not supply that meaning before use.

Finding: q is algebraically defined but not yet linked to input strength versus the cell's response threshold. a is a separate rate scale, but the reader must infer that changing it does not alter model field boundaries at zero rate cutoff. This distinction is needed to understand what parameter changes could physically mean and what the fitted parameters cannot establish.

Suggested insertion after line 42:

> The threshold summarizes how much combined input is needed before this cell fires in the model. It can reflect the cell's own response properties and inhibitory input. A larger q requires a larger input relative to its spatial variation, so fewer positions are active. At a fixed absolute input threshold, increasing the input's standard deviation lowers q. Changing a instead changes the rate inside an active field while leaving its zero-rate boundaries in the same places.

Optional final limit, if not covered by the nearby evidence sentence:

> Fitting q from a rate map does not tell us which of these biological quantities changed.

Evidence and limits: Mainali supplemental Methods S1, printed p. 8, describes average synaptic input and a threshold-linear transfer arising from input, intrinsic dynamics, and noise. Main main p. 1116 describes intrinsic properties and inhibitory input as possible sources of threshold variation. STAR Eqs. 2-3 define the normalization. For a nonzero input mean m, the effective normalized threshold is (T-m)/sigma_h, because the guide has absorbed m into T. Do not call h a membrane voltage: the source uses an effective input whose absolute units are unspecified here. q and z are dimensionless; a is Hz. The "zero-rate boundaries" condition matters because applying a fixed positive Hz cutoff introduces a-dependent boundaries, as 05c correctly explains.

## 4. Read random summation as a physical input model before its covariance algebra

Passage: 05c-place-tests.md, PLACE-WIRING, lines 202-241. It introduces spatially tuned input neurons, zero-mean random weights, then C(x,y)=v_W sum_i u_i(x)u_i(y), uniform coverage, and the Gaussian-profile example.

Finding: the algebra is correct, but the biological reading of signed/zero-mean quantities and of overlap in the same inputs is not explicit. The chapter currently moves from a possible circuit to a central-limit condition and a covariance sum. A reader can miss why nearby positions yield similar combined input or mistake a signed effective weight for evidence that an identified excitatory neuron supplies inhibition. Foundations distinguishes excitation and inhibition, but does not map that distinction to this sum.

Suggested short insertion before the sum, preserving the current zero-mean-weight assumptions:

> u_i(x) describes how much input cell i contributes when the animal is at x, and W_i sets how strongly that contribution affects the receiving CA1 cell. The signed, zero-mean description is a simplified model of input relative to its background. The source allows the background to be balanced by inhibition or by regulation of excitation and inhibition; it does not mean that an excitatory neuron changes into an inhibitory neuron from one position to another.

Suggested interpretation immediately after the covariance sum:

> If the same input cells are active at x and y, their fixed weights affect h at both positions. The combined inputs therefore tend to vary together across possible weight choices. If little input tuning overlaps between the positions, fewer terms contribute to this covariance. Broad input tuning can consequently produce a broad spatial covariance, as the Gaussian example below shows.

Evidence and limits: Mainali supplement Methods S2, printed pp. 9-10, explicitly says u_i can stand for rate deviations from the mean and discusses lateral inhibition or homeostatic balancing; its weights are independently drawn with zero mean. The current guide permits nonzero profile means because it averages over zero-mean weights, which is algebraically valid. Keep that exact distinction. An even safer short wording is "The signed sum describes effective input relative to its background" without assigning positive/negative W_i directly to actual synapse types. For positive Gaussian profiles, overlap is positive and decreases with separation. For general centered profiles, covariance can be negative; do not say overlap always creates positive covariance. The Gaussian example gives sigma=sqrt(2)b, so widening b at fixed normalized threshold stretches the map. Increasing rho or v_W at fixed profile changes covariance amplitude, not its normalized spatial scale; if an absolute firing threshold is fixed, it can also change q through sigma_h.

## Formal-math fold candidates, with the meaning kept outside

These are optional presentation moves, not additional defects and not authorization to fold the whole mathematical treatment.

- 05-place-fields lines 17-24: the detailed mean/covariance definition and joint-Gaussian characterization can sit in a clarification fold after the main text has said that a Gaussian process draws a fixed smooth spatial input map and that covariance controls how similar inputs are at nearby positions. Keep the actual input-map meaning, fixed-over-space condition, and later Gaussian independence requirement visible or stated before they are used. The user's covariance/rho request is principally owned by the root's foundations edit.
- 04-eye-drift lines 203-229: the residual-variance proof of the independent-neuron bound can be folded while retaining its assumptions, numerical comparison, and meaning in the main text. The causal shared/private variance interpretation at lines 237-275 should remain visible.
- 04b-eye-timing lines 124-152: the weighted Brownian-increment and covariance integration steps are a reasonable fold candidate, retaining the physical command-to-angle equation, both limiting MSD laws, what tau and D change, and the stationarity assumptions in the main text. This is optional, since the user's specific fold request concerned definitions rather than all derivations.

## Sufficient connected passages retained

- 04-eye-drift lines 237-275 already explains which physical contribution occurs in both records, why calibration matters, and why private prediction noise can reduce correlation without reducing the shared movement fraction. No new generic covariance tutorial is needed there.
- 04c-eye-circuit lines 18-53 already maps spikes to lingering synaptic output to represented angle to rates, explains saturation and spike jump size, and distinguishes approximate persistence from exact neutrality. Lines 85-94 explain feedback sign and delay. The scaling section distinguishes fixed absolute from fixed fractional slope. These do not need another mechanism template.
- 05b-place-sizes already explains height above threshold, curvature, radius, and dimensional size in causal order, then separates finite-threshold evidence from high-threshold limits. No extra broad biology belongs inside that local geometric derivation.
- 05c topology states how changing threshold shrinks, splits, or removes active regions, and distinguishes signed Euler characteristic from field count. No new physical mechanism is required to understand the mathematical topology result.
- 06-synthesis identifies its common moving coordinate, fixed rate maps, local slopes, resulting opposite or same-direction rate changes, and distinguishes shared position change from inhibitory connectivity. No new gap found within this focused question.

No manuscript changes, builds, full semantic audits, or CURRENT_STATE edits performed. Findings are proposed repairs for coordinator judgment and later separate review of the actual revised text. Token stats unavailable.

Report saved at: 2026-10-29T11:03:52.3233329+02:00
SHA256 04-eye-drift.md D40D1FCC6ED1047BDD47445CB02A78C3FD5D145F22309F6E090D85B4FDD733F7
SHA256 04b-eye-timing.md FCEB2DAB984B5A8A2D22A7849882319FC5DC31056736C794E4D9417799521893
SHA256 04c-eye-circuit.md D78C954750E1AB16BD1A7B8CBD9743382F6333E98C121AFD48EF2FAB3063F5FD
SHA256 05-place-fields.md 9D3CC8E71D66C0C005A99707EB1417694FEAEA32874DCB871BD35BFCA28F78DA
SHA256 05b-place-sizes.md 0B85730BECD9E26563FC9F7A78801AA11D27508A66E3B7326402BDA6B231135D
SHA256 05c-place-tests.md 6C9F70E32576F9A52B3DEDA8D6FDEBC5B2F9603AAD5DBB6AC19EF917D872B5F7
SHA256 06-synthesis.md 54F589C1D9CE1C8E0D65B9849BB8FD7E29A3E9A8DB6B7963A02B20FD5EE6A76F
