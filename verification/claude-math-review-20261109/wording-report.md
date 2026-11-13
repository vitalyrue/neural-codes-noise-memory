# Review of five chapters: necessity, terminology and word choice (stage 2)

## 1. Scope read and limitations

**Read in full:**
- **The five chapters under review:** `00-mathematical-tools.md`, `02-memory-dynamics.md`, `03-memory-information.md`, `05b-place-sizes.md` and `05c-place-tests.md`.
- **Earlier passages, used to check what the reader has already been taught:** `00-reading-guide.md`, `01-foundations.md`, `01b-persistence.md` and `04b-eye-timing.md`.

**Limits:**
- **Unread chapters:** place-fields (Chapter 10), long-delays, readout, eye-drift, the Exam review page and the Glossary were not supplied. Some symbols that look undefined locally may be defined there, for example `Q(q)` and "the 1D case". I say so wherever this applies.
- **Unseen sources:** I did not see the figure and table blocks (`{{block:…}}`) or the papers' PDFs. No citation or figure is verified here.
- **"Once per book" check:** blue-definition marking was checked only against the supplied text.
- **Rendering:** I could not see how `publisher-fold-always` renders, so whether those panels are actually folded is unknown.
- **Stage and edits:** this covers stage 2 only. Meaning questions I came across are listed separately at the end for the truth stage. I made no edits.
- **Arithmetic:** I spot-checked examples and they were correct:
  - mathematical tools (`00-mathematical-tools.md`) lines 53, 122–129 and 219–223;
  - memory information (`03-memory-information.md`) lines 36–40 and 254–268;
  - place sizes (`05b-place-sizes.md`) lines 215 and 219 (3.746 m; 46.0%; 3.73%);
  - place tests (`05c-place-tests.md`) line 129 (−20.06).

## 2. Findings, in priority order

### Problems that span several files

**X1 [High] The tools chapter uses "fixed point" and the attractor family before teaching them.**
- **Where:** `C:\dev\clsc\burak-papers\guide\content\chapters\00-mathematical-tools.md:60`
- **Excerpts:** "The fixed-point family in the memory model has a neutral tangent and locally decaying disturbances…"; then at line 62, "return to the family along a tilted path… incorporates the circuit's return flow."
- **Why it matters:**
  - *State*, *fixed point* and *continuous attractor* are first taught at `C:\dev\clsc\burak-papers\guide\content\chapters\01b-persistence.md:57`–59.
  - The reading guide (`00-reading-guide.md:90`) places that chapter *after* this one.
  - The tools chapter's own plain description only comes later, at line 149: "a continuous range of represented values can persist as stationary activity patterns. Other activity disturbances relax toward those patterns."
- **Fix:**
  - Move those two sentences from line 149 to just before line 60.
  - Add "(fixed points: patterns where ṡ = 0)".
  - Explain "neutral tangent" as "the direction along the family, in which a disturbance neither grows nor decays".
  - Replace the first "return flow" with "the noise-free path back to the family".

**X2 [High] The same example or derivation is taught twice.** Teach each full method once and link back to it.

| Tools chapter | Later chapter | Recommendation |
|---|---|---|
| Lines 64–79, the tilted-decay example (ẋ=ay, ẏ=−by) | `02-memory-dynamics.md:154`–193 (same system, with a figure and the decaying eigenvector) | Keep the Chapter 3 version. In the tools chapter, keep one sentence and a link. |
| Lines 83–90, averaging Poisson counts | `02-memory-dynamics.md:43`–52 | Keep the Chapter 3 version, because it ties into the 1/n weight scaling at line 67. |
| Lines 100–114, the I_h derivation and the definition of J | `03-memory-information.md:47`–62, nearly word for word (and switching from degrees to radians) | Chapter 5 should recap the formula and link to the tools chapter, keeping its *new* background-spike example and the score derivation. |
| Lines 161–175, the θ₁+θ₂ invisible direction | `03-memory-information.md:296` | Keep one. |
| Lines 349–363, the peak/saddle example with diag(−2,−8) and the Hessian marked as a definition | `05b-place-sizes.md:30`–46, the same title, numbers and blue mark | Remove the place-sizes copy and its blue mark. Re-point `05c-place-tests.md:40`, which links to the place-sizes copy. |
| Lines 387–408, the size-law fold | `05b-place-sizes.md:48`–75 and 137–150 | Replace the tools fold with a link. |

**X3 [High] Symbols are reused for unrelated quantities, often in the same chapter.**

In `00-mathematical-tools.md`:
- **`h`:** used for the observation window (line 100), the impulse response h(u) (line 237) and the spatial map h(x) (line 277).
- **`τ`:** used for the synaptic time constant (lines 17 and 152) and the muscle response time (line 243), with no warning. `04b-eye-timing.md:150` does make this distinction explicitly.
- **`b`:** used for the bias (lines 22 and 40), a decay rate (line 68), a gain (line 202), a kernel scale (line 317) and a height (line 391).
- **`u`:** used for a generic eigenvector (line 60) and then for the tangent (line 62).

Elsewhere:
- **`S` and `s` swap roles:**
  - In the tools chapter, `S` is the random variable at line 373 but a threshold value at lines 385 and 401.
  - In `05b-place-sizes.md:156`, `S` is random and `s` is a value; at line 212, `s` is a value.
- **`b` again in place sizes:** `05b-place-sizes.md:212` uses `b` for the Weibull scale, while lines 56–60 use it for height.
- **`b_i` clash in memory information:** `03-memory-information.md:179` defines `b_i = r_i'/√r̄_i`, which collides with the bias `b_i` of the same model (Eq. 8).

**Fix:**
- Use λ in the tools tilted example, as Chapter 3 does.
- Write the muscle time as τ_e and give the impulse response a distinct symbol.
- Fix one convention, with `S` random and `s` a value, across the tools chapter and place sizes.
- Rename the Cauchy–Schwarz vectors to **x** and **y**.

**X4 [High] "Weights" names two different objects.**
- **Excerpt:** `C:\dev\clsc\burak-papers\guide\content\chapters\02-memory-dynamics.md:253` says "The general formula uses the weights **v**… The matrix W contains the connection weights".
- **Other places:** v is also called weights at lines 199 and 239, and at `03-memory-information.md:270` and :351 ("information optimal weights", "projection weights").
- **Why it matters:** **v** is a readout of the circuit's lasting response, not a set of synapses. Calling it "weights" invites the reader to confuse it with W.
- **Fix:** call **v** the "readout vector" (or "projection coefficients") everywhere, and keep "weights" for W.

**X5 [Med] One object goes by several names.**
- **Left vector:**
  - "left zero vector" is marked blue in the tools chapter at line 62;
  - "left zero eigenvector" is marked blue *again* at `02-memory-dynamics.md:127`;
  - "left vector" appears at Chapter 3 lines 143, 152 and 181 and Chapter 5 line 201.
- **The place-field scale:**
  - "correlation length" in the tools chapter (line 308) and place tests (line 214);
  - "local distance scale" in place sizes (line 11);
  - "local spatial scale" in place tests (line 9).

**Fix:** pick one name for each, mark it blue once, and use it consistently.

**X6 [Med] The same caveats are restated many times.**
- **"Matching the mean and variance does not make it Gaussian, and a single neuron's count stays a jump count":** tools chapter lines 81 and 87; Chapter 3 lines 41, 49 and 63.
- **"Differs from a perpendicular projection":** tools chapter lines 62 and 76; Chapter 3 lines 11, 152 and 181.
- **"A negative Euler characteristic is not a negative count":** place tests lines 35, 63 and 129.

**Fix:** state each caveat once, where it is first needed, and cut the rest.

**X7 [Low] Chapter openings announce the plan instead of the problem.**
- **Where:** `02-memory-dynamics.md:5` ("we first… We then…"), `05b-place-sizes.md:9`, `05c-place-tests.md:7` and `00-mathematical-tools.md:5`.
- **Fix:** keep the causal chain but drop the "we first / then / finally" framing, or cut it to one sentence.

**X8 [Low] Established names lose their dashes, and hyphenation is inconsistent.**
- **Names:** the text has "Cramér Rao" and "Cauchy Schwarz" (in the tools chapter and Chapter 5); the standard forms are Cramér–Rao and Cauchy–Schwarz.
- **Hyphenation:** "noise free" (Chapter 3, lines 13 and 79) vs "noise-free" (line 143); "high threshold limit" vs "high-threshold limit" (place sizes, lines 154 and 156); "short lag MSD grows" (tools, line 247).

### `00-mathematical-tools.md` (mathematical tools)

- **[High] Line 209:** `χ_Y = b²Var(S)/Var(Y)` appears with no name. It is only described ("shared variance fraction") at line 213.
  - **Fix:** introduce it first: "the fraction of measured-movement variance due to the shared command, χ_Y = …".
- **[Med] Line 62:** the "left zero vector" definition never gives the property behind the name (**v**ᵀK=0, **v**ᵀ**u**=1), which appears only in the fold.
  - **Fix:** add "a left eigenvector of K with eigenvalue zero, normalized so **v**ᵀ**u**=1".
- **[Med] Line 149:** "With zero mean drift and approximately constant coefficients". It is not said which coefficients.
  - **Fix:** "with zero mean drift and D roughly constant over the interval".
- **[Med] Lines 181 and 231:** "If one neuron's spikes predict some eye movement" and "assuming that calibration from larger movements still holds". Neither "prediction" nor "calibration" is explained here.
  - **Fix:** at line 181, add "the displacement calculated from one motor neuron's rate using a rate-to-position relation fitted on larger movements".
- **[Med] Line 245:** "its intensity specifies variability of integrated input, rather than an ordinary finite pointwise variance". This is abstract.
  - **Fix:** "Its strength A is defined through its integral: over a window Δt the integrated input has variance AΔt. A value at a single instant has no finite variance."
- **[Med] Line 315:** "describes local covariance curvature, without fixing distant spatial relationships".
  - **Fix:** "depends only on how C bends at zero separation, so it does not determine correlations between distant positions."
- **[Med] Lines 326–330:** "threshold density" reads as a density *of thresholds*. The key intuition ("A steep crossing occupies less distance… spatial occupancy") also comes after the formula.
  - **Fix:** write "the probability density of the input at the threshold, p_z(q)". Before the formula, give the plain band argument from the fold at line 336.
- **[Med] Line 172:** "For any matrix Q and vector **z**…; this is the nonnegative quantity used in that proof." Q is never introduced in this chapter.
  - **Fix:** delete it under the deletion test; Chapter 5 (lines 304–319) teaches this step.
- **[Low] Line 159:** "small changes in each direction in that space". The "space" is never named.
  - **Fix:** "for each combination of value changes".
- **[Low] Line 7:** "Fisher information measures precision in their spikes".
  - **Fix:** "measures how precisely their spikes indicate the stored value".
- **[Low] Line 183:** "scales that covariance by both signals' standard deviations" does not say whether to multiply or divide.
  - **Fix:** "divides that covariance by the product of the two standard deviations".
- **[Low] Line 237:** "A causal filter calculates present output". Muscles do not calculate.
  - **Fix:** "determines".
- **[Low] Line 140:** "mean agrees with the true value to first order".
  - **Fix:** "its mean equals the true value and changes one-for-one with it near the value studied".
- **[Low] Line 26:** "W_ij has input units per activation unit". Activation is dimensionless, so this is simply input units.
- **[Low] Lines 416–418:** these repeat the pointer at line 11, and "This chapter introduces the mathematical tools" adds nothing.
  - **Fix:** delete line 418.

### `02-memory-dynamics.md` (memory dynamics)

- **[Med] Line 17:** "Here we calculate its fluctuations". It is unclear what "its" refers to.
  - **Fix:** "Here we calculate how random spike timing makes the activations fluctuate."
- **[Med] Line 83:** "all other local modes decay". "Mode" is never defined, yet it is used at lines 107, 123, 143 and later.
  - **Fix:** define it once: "a mode is an eigenvector direction of K together with its own growth or decay rate."
- **[Med] Line 199:** "an angle shift δθ… the lasting angular effect". θ is a general coordinate (line 9), and in the two-cell example it is an activation difference (line 310).
  - **Fix:** say "coordinate shift" and "lasting effect on θ".
- **[Med] Line 191:** "As y decays, x changes by one". The plotted values of a, λ and y₀ are never stated.
  - **Fix:** state them, for example a=λ and y₀=1.
- **[Med] Line 248:** the diffusion tensor is defined after D_αβ is used (line 227) and after the unrelated interval conditions. "Per twice the elapsed time" is also awkward.
  - **Fix:** move it to directly after line 227, as "displacement covariances divided by twice the elapsed time".
- **[Low] Lines 19 and 22:** these two sentences make the same statement about conditionally independent spike noise.
  - **Fix:** delete the second sentence of line 19.
- **[Low] Line 67:** "makes this limit concrete" comes before any limit has been named.
  - **Fix:** "makes the many-weak-inputs condition concrete".
- **[Low] Line 9:** "An observer's estimate θ̂…" is never used in this chapter.
  - **Fix:** move it to Chapter 5, line 119.
- **[Low] Line 234:** "dual weights".
  - **Fix:** "readout vectors".
- **[Low] Line 290:** "The guide's checks of other printed formulas remain separate from that correction." This is commentary about how the guide was written.
  - **Fix:** delete it.
- **[Low] Line 319:** the link text "Fig. 2E–G, p. 3" points to a guide page, not to the paper.
- **[Low] Line 333:** "The dashed rate sum in the upper plot" relies on layout to identify the line.
  - **Fix:** name the curve instead.

### `03-memory-information.md` (memory information)

- **[Med] Line 206:** "the network's retained response to each cell's spike noise to match that cell's information about memory".
  - **Fix:** "each cell's lasting effect on the stored value, v_i, must be proportional to r_i′/r̄_i, its rate slope per unit noise."
  - The heading "Neural mechanism." is also a poor fit, because this paragraph states a mathematical condition.
- **[Med] Lines 270 and 280:** "the information optimal weights" is undefined. The sentence "a lower minimum allowed by the inequality is not a reduction in the network's actual diffusion" is convoluted.
  - **Fix:** "no longer satisfy v_i ∝ r_i′/r̄_i" and "J rises, so the bound falls to 750, but the actual D stays 1000."
- **[Med] Line 335:** "The comparisons below control how added neurons… affect the tuning curves". A comparison does not control effects.
  - **Fix:** "Each comparison below states which tuning curves and inputs stay fixed when…".
- **[Med] Line 359:** "A larger cellular time constant… what the experiment keeps fixed". This is a new name for τ, and these are model comparisons, not experiments.
  - **Fix:** "A longer synaptic time constant lowers D in both comparisons; the power of τ depends on what the comparison holds fixed."
- **[Low] Line 341:** "population replication comparison".
  - **Fix:** "replicating each neuron n times (or raising the density of preferred values)".
- **[Low] Line 345:** "held under control". **Line 347:** "their input relation". Both are vague; state the fixed quantity, ḡ_i(θ).
- **[Low] Line 155:** "has a different error problem" and "needs care near boundaries".
  - **Fix:** "is not covered by this bound and can have lower mean squared error", and "the smoothness conditions can fail where rates reach zero or θ reaches the end of its range".
- **[Low] Line 390:** "broader fields recruit more neurons". "Fields" suggests place fields.
  - **Fix:** "broader tuning curves make more neurons respond at each value".
- **[Low] Line 78:** "Both curves change by the same amount with angle".
  - **Fix:** "have the same slope; the upper curve adds a constant background".

### `05b-place-sizes.md` (place sizes)

- **[Med] Line 63:** "Selecting an actual maximum also weights curvatures".
  - **Fix:** "Counting actual maxima weights each point by |det H|, favoring sharper peaks; this does not change the leading shape."
- **[Med] Line 195:** "The dimensional size laws then differ in shape". "Dimensional" could mean "having units" or "per spatial dimension".
  - **Fix:** "The size laws for d = 1, 2, 3 then differ only in shape."
  - Line 203 repeats line 195; merge them.
- **[Med] Line 249:** "Converting this same radius into d dimensional size and then cutting it requires both hit probability and cut position." The claim is unclear.
  - **Fix:** "Deriving slice lengths from the field-size law would require the chance that a line hits each field and where it cuts it; the restriction argument avoids that step."
- **[Low] Line 174:** the inversion β(μ_s) is given without its purpose.
  - **Fix:** add "so β can be set from a measured mean size."
- **[Low] Line 17:** repeats the point of line 5.
- **[Low] Lines 20 and 24:** "high excursion argument" and "relevant derivative variables" are vague.
  - **Fix:** "high-threshold argument" and "height, gradient and second derivatives at a point".
- **[Low] Line 48:** "Isotropy and the definition of σ imply…" skips a step.
  - **Fix:** add "differentiating C twice at zero separation".
- **[Low] Line 270:** "the topology test" is taught only in the next chapter.
  - **Fix:** add a forward link.

### `05c-place-tests.md` (place tests)

- **[High] Lines 104 and 141:** "Corners supply Q(q)" and "using Q(q) ≃ φ(q)/q". Q is never defined in the supplied text; the tools chapter writes Pr[z(0)>q]. It may be defined in the unread Chapter 10.
  - **Fix:** at first use, "Q(q) = Pr(z>q), the Gaussian upper-tail probability; VQ(q) is the expected active volume."
  - The abbreviation "EC" (lines 141 and 145) is also never introduced.
- **[Med] Line 9:** "The map is still fixed over space". The map varies over space; it is fixed over *time*. "Normalized activity threshold" is also wrong, because q thresholds the input.
  - **Fix:** "Each map is still fixed in time… q is the normalized input threshold." The same applies to line 14.
- **[Med] Line 254:** "relative to a background that can be balanced through inhibition or regulation of excitation and inhibition" is garbled.
  - **Fix:** "relative to a background level, assuming inhibition, or a balance of excitation and inhibition, cancels its mean."
- **[Med] Lines 297–305:** the √2·b result is never tied back to the model's parameter.
  - **Fix:** add "so the correlation length is σ = √2·b." "Standard deviation" of a covariance shape should read "width parameter".
- **[Med] Line 157:** "It uses different available summaries in different conditions."
  - **Fix:** name the summaries, for example "mean field length and mean gap in 1D".
- **[Med] Lines 44–53:** "The multidimensional Kac–Rice rule counts these zeros with the absolute Hessian determinant". Its intuition ("converts to gradient volume, just as the slope did") arrives only after the formula.
  - **Fix:** move line 53 to before line 48.
- **[Low] Line 37:** "We already derived the 1D case" has no link.
- **[Low] Line 145:** "the nonmonotonic curves" are never described.
  - **Fix:** add "EC rises, then falls and turns negative, as q increases".
- **[Low] Line 25:** "Betti numbers" are never used again. Delete them or keep them only as a pointer.
- **[Low] Line 177:** "held-out forecasts".
  - **Fix:** "tests on data withheld from fitting".
- **[Low] Line 167:** "STAR Methods" is unexplained.
  - **Fix:** "(the article's methods section)".
- **[Low] Line 238:** "draws a positive threshold".
  - **Fix:** "assigns each cell a randomly drawn threshold".
- **[Low] Line 214:** it is unclear which table "the 3D table" means.
- **[Low] Line 280:** "the sum is approximately" should be "the covariance sum ∑_i u_i(x)u_i(y)".
- **[Low] Line 35:** "chi" is written out, while the symbol χ is used elsewhere.

### Blue definitions and folded examples (source only)

- **Marked twice:**
  - "Hessian": tools line 347 and place sizes line 30.
  - The left-vector variants: tools line 62 and Chapter 3 line 127.
- **Stationarity:**
  - Stationarity in time is first taught, unmarked, at tools line 245.
  - Blue marks fall on spatial "stationarity" (tools line 296) and on "stationary process" (`04b-eye-timing.md:93`).
  - Decide whether these are one Glossary entry or two.
- **Dirac delta:** its blue mark sits inside an optional fold (tools line 253). A reader who skips folds first meets it at `01-foundations.md:48`, unmarked.
- **Missing definition-explanation wrapper:** tools line 279 ("Gaussian process"), Chapter 3 line 297 ("translation symmetry") and place tests line 182 ("median filter"). This matters only if the project convention requires the wrapper.
- **Spelling of marked terms:** "Skew" (place tests line 173) is marked with a capital letter. Check it against the paper's term and the Glossary spelling; "skewness" is the standard name.
- **Folding:**
  - The tools chapter folds all optional examples with `<details>`.
  - Chapter 3 mixes `<details>` (line 43) with `publisher-fold-always` divs (lines 154 and 299).
  - Long optional derivations are also in `fold-always` blocks: Chapter 5 lines 82, 133 and 304, and place tests line 65.
  - If `fold-always` renders open, these do not meet the "optional deeper material folded" preference. This needs a render check.
- **Other markup:**
  - At place sizes line 203, "to U" is not set as math.
  - At tools line 414, the anchor `tbl-math-results` has no table.

## 3. Material that is adequately taught

- **Mathematical tools:**
  - Lines 15–32: spike, firing rate, synaptic activation and the connection matrix, with the feedback cycle traced step by step.
  - Lines 94–98: the Fisher information question stated as a physical comparison between 30° and 31°.
  - Line 177: the distinction between the current value and the initial value.
  - Lines 199–226: the shared/private model and the weak-correlation example, once χ_Y is named.
  - Line 243: τĖ = U − E, explained as "mismatch drives velocity".
  - Lines 279–292: jointly Gaussian variables, with the X²−1 counterexample.
  - Lines 367–383: change of variables, explained through equivalent events.
- **Memory dynamics:**
  - Line 32: dM_i as a "surplus or deficit".
  - Line 85: linearization.
  - Line 105: the physical meaning of each term in K.
  - Line 123: the right zero eigenvector.
  - Line 143: why **v**ᵀδ**s** stays constant without assuming diagonalizability.
  - Line 290: how the erratum is handled.
  - Line 310: explicit unit conversion between the two two-cell examples.
- **Memory information:**
  - Lines 33–43: the background-spike example, which teaches something new.
  - Lines 80–117: likelihood and score.
  - Line 119: estimator and unbiased estimate.
  - Line 143: Cauchy–Schwarz explained in words.
  - Line 167: the heuristic argument labeled as a heuristic.
  - Line 169: how the two vectors map onto diffusion and information.
  - Line 351: the τ mechanism.
  - Line 404: the alternative resource constraint.
- **Place sizes:**
  - Line 56: Gaussian conditioning via Y = Cov·Z + ε.
  - Lines 78–92: the distribution of excess height.
  - Lines 99–118: rate ∝ s², with honest treatment of the finite-threshold exponents.
  - Line 212: the Weibull definition and the 3D divergence.
  - Lines 215–219: worked numbers.
  - Lines 240–249: slicing.
  - Lines 284–306: slope selection and its independent check.
- **Place tests:**
  - Lines 17–23: the Euler characteristic, with examples.
  - Line 40: what the critical-point signs mean.
  - Lines 119–129: boundary terms and limit checks.
  - Line 173: skew, kurtosis and the lognormal distribution.
  - Line 177: a likelihood gloss, which is needed on the place-field-only reading path.
  - Lines 181–188: the processing choices.
  - Lines 263 and 277: the CLT conditions and the covariance mechanism.
  - Line 308: the limits of what can be inferred about the circuit.

## Meaning questions for the truth stage

- **Memory dynamics, lines 41, 57 and 63:** the text says the approximation concerns *summed input*, but the equation adds Gaussian noise to each neuron's own s_i. The reader needs to be told what the equation literally does.
- **Mathematical tools, line 53:** "with the paper's tuned parameters" sits uneasily with footnote line 420, which calls the calculation a teaching reconstruction.
- **Place tests, line 182:** "a neighborhood two bins wide on each axis" describes an even-width median filter. Check this against the paper.