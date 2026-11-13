# Review of five chapters: reader understanding and flow (stage 3)

## 1. Scope, limitations, and how the new context was used

**Chapters covered.** I read all five in full for openings, transitions, physical meaning, what each step requires, and whether any fold holds a prerequisite:
- `C:\dev\clsc\burak-papers\guide\content\chapters\00-mathematical-tools.md`
- `C:\dev\clsc\burak-papers\guide\content\chapters\02-memory-dynamics.md`
- `C:\dev\clsc\burak-papers\guide\content\chapters\03-memory-information.md`
- `C:\dev\clsc\burak-papers\guide\content\chapters\05b-place-sizes.md`
- `C:\dev\clsc\burak-papers\guide\content\chapters\05c-place-tests.md`

The reading order comes from `00-reading-guide.md:86`–119. It promises that "the explanations needed for the next section remain in the main text" (line 119), and I used that promise as the test for folded material.

**How the new context changed earlier findings:**
- **`Q(q)`:** it is taught at `05-place-fields.md:189`, before the place-tests chapter. My stage-2 "undefined" finding is withdrawn. A one-line reminder is still useful (see F21).
- **The "x changes by one" sentence:** the caption's values (a/λ = 1/2, y₀ = 2) make the shift exactly 1, so the sentence at `02-memory-dynamics.md:191` is correct. This is now a low-priority request to say so in the text.
- **The 2017 correction:** the handling at `02-memory-dynamics.md:290` is adequate.

**Limitations:**
- I could not read the Chapter 10 place-fields text beyond the fact above, or the long-delays, readout and eye-drift chapters.
- I did not see the figure and table blocks, the captions in the YAML files, or the rendered output.
- I cannot tell from the source whether `publisher-fold-always` renders folded or open. Findings that depend on this are marked.
- This is a review only. Nothing was edited.

**Earlier findings still open.** Stage-2 findings that also hurt understanding are not repeated here in full but remain open:
- symbol reuse: h, τ, b and S/s in the tools chapter; b_i at `03-memory-information.md:179`;
- "weights" used to mean the vector **v**.

The τ clash matters most for the reader. The tools chapter uses τ as the synaptic time in the bound (line 152) and as the muscle response time (line 243) with no warning, while `04b-eye-timing.md:150` makes the distinction explicitly.

## 2. Findings in priority order

### A. Folded or missing material that the visible text depends on (High)

**F1. The tools chapter's visible text describes the difference growing, but the fold shows it staying put.**
- **Where:** `00-mathematical-tools.md:34`. The visible text says "If population 1 becomes more active, it inhibits population 2 more strongly. Population 2 then fires less and inhibits population 1 less strongly… a difference… can persist."
- **The problem:** this chain describes the difference being *amplified*. Why it neither grows nor decays, while the total is pulled back, appears only in the fold at lines 40–53 ("feedback preserves a difference while correcting the total"). Line 60 then relies on the reader knowing about "a neutral tangent".
- **Fix:** add a visible sentence after line 34: "In the tuned model, feedback returns the *total* activity to a set level, while the *difference* is neither restored nor amplified, so it stays where a disturbance left it."

**F2. The tools chapter introduces the left zero vector before the reader has the ideas it depends on.**
- **Where:** `00-mathematical-tools.md:60`–62. Neither "fixed-point family" nor the defining property of **v** (**v**ᵀK = 0, **v**ᵀ**u** = 1) is in the visible text. The property appears only in the fold (line 76), and fixed points are taught later (`01b-persistence.md:57`).
- **The problem:** without the fold, the reader cannot see why "it incorporates the circuit's return flow."
- **Fix (combines with stage-2 X1):**
  - Move the plain description from line 149 ("a continuous range… persist as stationary activity patterns; other disturbances relax toward those patterns") to before line 60.
  - Give K one line of physical meaning: "entry K_ij is how fast a small change in cell j's activation changes cell i's activation."
  - State **v**ᵀK = 0 and **v**ᵀ**u** = 1 in the visible text, with one clause explaining why: "so **v**ᵀδ**s** does not change while the disturbance decays."

**F3. The intuition behind the crossing formula is hidden in a fold.**
- **Where:** the visible sentence at `00-mathematical-tools.md:330` ("A steep crossing occupies less distance near threshold, so its larger slope must compensate when converting spatial occupancy into a crossing count") can only be understood through the band argument in the fold at line 336.
- **Fix:** move the first two sentences of line 336 into the visible text *before* the formula at line 326. Then the formula reads as "density of the input at q × average upward slope there".

**F4. The reader cannot see how the shared variance fraction is obtained from data.**
- **Where:** `00-mathematical-tools.md:209`–213 and :231. χ_Y requires the ratio b/a. Line 213 says only "a calibrated gain", and line 231 mentions "calibration from larger movements" without connecting it to b/a.
- **The problem:** the reader cannot see how the 2022 analysis turns Cov(X,Y)/Var(Y) into a shared-variance fraction. This is the physical point of the section.
- **Fix:** add one sentence explaining that calibration converts each cell's rate into degrees of predicted eye movement, which fixes its gain on the shared command relative to the eye's, and therefore fixes b/a. If calibration makes a = b, then χ_Y = Cov(X,Y)/Var(Y), which is what the example uses with unit gains.
- **Check:** confirm against Eqs. 11–15 of the 2022 paper in the truth stage before writing it.

**F5. The heuristic for the information bound skips its key step.**
- **Where:** `03-memory-information.md:167`. The text says "Comparing this with the variance 2Dτ accumulated over the same time suggests 2Dτ ≥ 1/(Jτ)." It never says why the accumulated variance should be at least the estimation variance.
- **Fix:** insert "Each re-estimate's error is not corrected later; it becomes a lasting displacement. So the variance added in each interval τ cannot be smaller than the best possible estimation variance."

**F6. The equality condition has no physical meaning, and its label is misleading.**
- **Where:** `03-memory-information.md:206`–226. Line 206 is labeled **Neural mechanism.**, but no mechanism follows. The reading guide's skim path (`00-reading-guide.md:146`) tells readers to read exactly these labeled paragraphs.
- **Fix:** give line 206 a physical statement: "Equality requires every cell's lasting effect on the stored value (v_i ∝ g_i′) to be proportional to how informative its spikes are per unit noise (r_i′/r̄_i = (φ′/φ)·g_i′). Exponential φ makes φ′/φ the same for all cells, so no cell adds memory noise out of proportion to the information it carries."

### B. Order and transitions (Medium)

**F7. The tools chapter claims "radius ∝ √ε" before it gives the quadratic shape that produces it.**
- **Where:** `00-mathematical-tools.md:345`. The Hessian paragraph at line 347, which supplies the shape, then interrupts the chain of size → excess → change of variables.
- **Fix:** put line 347 first ("near a peak, z ≈ peak − ½xᵀ|H|x"), then line 345. Keep the peak/saddle meaning, because the place-tests chapter needs it.

**F8. Setup material in the memory-dynamics chapter sits away from where it is used.**
- **Where:** `02-memory-dynamics.md:11` defines the instantaneous attractor state through "deterministic return flow" and "perpendicular geometric projection" four paragraphs before any return flow is computed. The fixed-point equation and its interpretation (lines 70–79) sit at the end of the weak-noise section, although only the linearization section uses them.
- **Fix:** move both to the start of the section at line 81, where the reader first needs them. The opening then goes: problem (line 3), plan (line 5), notation (lines 9 and 13).

**F9. The averaging fold in the memory-dynamics chapter comes before the passage it illustrates.**
- **Where:** `02-memory-dynamics.md:43`–52. The fold ("each spike adds 1/n") previews the supplement's 1/n weight scaling, which line 67 then states again.
- **Fix:** place the fold after line 67 and title it as a worked case of that scaling. The repetition then reads as an example rather than a restatement.

**F10. The diffusion section breaks off for the multi-coordinate case before finishing the scalar story.**
- **Where:** `02-memory-dynamics.md:224`–248. The scalar result (line 221) is followed by the multi-coordinate case (224–237). Only then come the scalar interpretation (239) and the time-interval conditions (241–246), and the diffusion tensor is defined last (248).
- **Fix:** use the order 221 → 239 → 241–246 → 224–237 → 248.

**F11. Figure 3 is cited at place sizes line 118 but appears only at line 314.**
- **Where:** `05b-place-sizes.md:118` cites Figure 3C–D, while the figure's fold is at line 314.
- **Fix:** add "(shown in the boundary-slope section)", or move the fold.

**F12. The place-tests chapter tests log length before saying why.**
- **Where:** `05c-place-tests.md:173`. The skew and kurtosis of log length are defined before the lognormal alternative that motivates taking the log.
- **Fix:** open the paragraph with "A competing lognormal description makes log length Gaussian; the skew and kurtosis of log length test that."

**F13. The place-tests chapter gives the determinant intuition after the formula it explains.**
- **Where:** `05c-place-tests.md:44`–53. The intuition ("converts to gradient volume, just as the slope did") comes after the formula at line 48.
- **Fix:** move it to before the formula.

**F14. The boundary-sign condition is not explained.**
- **Where:** `05c-place-tests.md:104`. "must have the appropriate sign to contribute" does not say which sign or why.
- **Fix:** state the sign condition and its geometric meaning: which way the input must change across the face for a face point to count as an extremum of the box. Refer this to the truth stage to confirm the direction.

### C. Gaps in physical meaning and in what an example requires (Medium)

**F15. The memory-dynamics two-cell example never uses the formula its section derives.**
- **Where:** `02-memory-dynamics.md:301`–313. The example computes 2D from the general **v** formula, not from the tuning-curve formula boxed at lines 282–286.
- **Fix:** add one line applying the boxed formula. With g′ = ±1/2, r′ = ±1/(2τ) and Σr′g′ = 1/(2τ), it gives 2D = r̄₁ + r̄₂. This confirms the formula on a case the reader can follow.

**F16. The reader is never told what physically produces a "tilted" return.**
- **Where:** `02-memory-dynamics.md:152`–193. The only neural example (the two-cell model) has **v** ∥ **u**, because φ′ is equal across cells, so no tilt occurs. Line 152 gives the cause (unequal φ′ across rows) only in abstract terms.
- **Fix:** add one sentence. Tilt appears when cells sit at different slopes of the transfer function, for example cells on the flanks of a ring bump versus its peak. In the two-cell example equal slopes make **v** ∥ **u**, so the perpendicular projection happens to be correct there.

**F17. The memory-information numerical example points to the wrong chapter and asks the reader to recompute a slope.**
- **Where:** `03-memory-information.md:254`.
  - "the preceding chapter's plot" is wrong: the plot is in Chapter 3 (memory dynamics), while the preceding chapter is Chapter 4 (long delays).
  - The value "slopes are ±5" requires the reader to rederive r = (b ± θ)/(2τ).
- **Fix:** write "Chapter 3's plot" and add "since r̄_{1,2} = (b ± θ)/(2τ), the slopes are ±1/(2τ) = ±5."

**F18. The matrix bound in memory information depends on an unlinked definition.**
- **Where:** `03-memory-information.md:298`–301. The bound needs the multi-coordinate tangent and readout vectors **u**^α and **v**^α from `02-memory-dynamics.md:224`, but no link is given. "2D" also silently becomes a matrix here.
- **Fix:** link to that section and say "the diffusion matrix D".

**F19. The equality check in memory information cannot be verified without an unseen chapter.**
- **Where:** `03-memory-information.md:228`–238. The fold relies on the mutual-excitation example in the long-delays chapter, which I could not read.
- **Fix:** restate its weights in one line, apparently W₁₂ = W₂₁ = 1 with zero self-weights for s̄₁ = s̄₂ = θ. This needs checking against the long-delays chapter.

**F20. The place-tests wiring example stops before reaching the model's parameter.**
- **Where:** `05c-place-tests.md:297`–305. The example ends at "standard deviation √2·b" without connecting to σ, so the physical consequence (input width sets field scale) is left implicit.
- **Fix:** add "so the correlation length is σ = √2·b: twice-as-wide input profiles give twice-as-wide fields." The garbled background sentence at line 254 (stage 2) also blocks understanding of what h(x) is measured against.

### D. Lower-priority items

**F21. Small reminders and pointers:**
- **`Q(q)` reminder:** at `05c-place-tests.md:104`, add "Q(q) = Pr(z > q) (Chapter 10)", linking to `05-place-fields.md:189`, because the place-sizes chapter in between does not use it. At line 37, link "We already derived the 1D case".
- **The "changes by one" sentence:** `02-memory-dynamics.md:191` is consistent with the caption values (a/λ = 1/2, y₀ = 2). Write "(here (a/λ)·y₀ = 1)" so the sentence does not depend on the caption.
- **σ_X:** `00-mathematical-tools.md:213` uses σ_X, but it is defined only in the fold at line 194. Write "the standard deviation of X".
- **Tools folds that lean on later chapters:**
  - The step "conditioning on height b gives mean second derivative −b/ℓ_c²" in the fold at `00-mathematical-tools.md:391` relies on the conditioning rule taught at `05b-place-sizes.md:56`. Add a link.
  - "Stationarity gives Cov(z, z′) = 0" in the fold at line 338 needs the clause "because Var z(x) is constant, its derivative 2Cov(z, z′) is zero."
- **Shift to the place-field paper:** `00-mathematical-tools.md:273`→277 changes papers without a bridge. One sentence would help: "The third paper's randomness is over space, not time." `01b-persistence.md:227` already does this.
- **Order inside the place-sizes opening:** in `05b-place-sizes.md`, the motivation at line 17 should come before the link and notation paragraph at line 15. Name the Weibull distribution at line 172 ("This is the paper's Equation 1"), not after the table at line 212.
- **Errata placement:** the errata paragraph at `05c-place-tests.md:167` interrupts the table → Figure 1 discussion. Make it a table note. Line 170 needs a link to where Figure 1 is shown.
- **Labels:** `03-memory-information.md:47` says "Mathematical result" and line 119 says "Interpretation: …". Use the labels promised at `00-reading-guide.md:128`–133.
- **Covariance symbols:** `01-foundations.md:344` re-teaches the gain model with g_X and ε_X right after the tools chapter used a, b and η. Align the symbols so the second pass reads as a recap.

### E. Repetitions reassessed for teaching value

This table revises my stage-2 X2 and X6 recommendations, taking account of the preference for foldable examples.

| Repetition | Does it help the reader? | Revised recommendation |
|---|---|---|
| Tilted-decay example: tools fold at `00-mathematical-tools.md:64`–79; memory dynamics `02-memory-dynamics.md:154`–193 | **Yes.** The tools fold carries the prerequisite for the left-vector definition at tools line 62 (F2). The memory-dynamics version adds the decaying eigenvector and a figure. | Keep both. In memory dynamics, open with "the same system as the tools example, now with its decaying direction plotted". In the tools fold, point forward to it. |
| Averaging Poisson counts: tools fold at line 83; memory dynamics fold at line 43 | Partly. Memory dynamics adds the 1/n weights. | Keep both as folds; reposition the memory-dynamics one (F9). |
| Poisson Fisher-information derivation: tools lines 100–114; memory information `03-memory-information.md:47`–62 | **Yes, as a recap.** Memory information is the teaching location and links it to the likelihood. | Keep it. Mark it as a recap ("as in the tools chapter") and keep the angle units the same, or say why they switch. |
| Two-coordinate invisible direction: tools fold at line 165; memory information line 296 | Yes. The memory-information version is one sentence at the point of use. | Keep both. |
| Peak/saddle example: tools lines 349–363; place sizes `05b-place-sizes.md:39`–46 | **No.** Same numbers, same conclusion. | Replace the place-sizes fold with something new: the elliptical active region at height ε above q, with radii √(2ε/\|λ_i\|), which ties curvature to field size. Keep a single blue mark for Hessian. |
| Size-law fold: tools lines 387–408 | It is an optional preview of place sizes. | Keep it folded and add a link to `05b-place-sizes.md:131`. |
| Gaussian-approximation caveat: memory dynamics lines 41, 49 and 63 | Line 63 repeats line 41 two paragraphs later. | Cut line 63's restatement and keep the units sentence. |
| Perpendicular projection: memory dynamics lines 11, 152 and 181 | Lines 152 and 181 frame the example (general point → instance). | Keep 152 and 181. Line 11's clause can go if F8 moves the definition. |
| Negative Euler characteristic: place tests `05c-place-tests.md:35`, 63 and 129 | Each attaches to a different object: the figure, the densities, the box. | Keep them. Cut only the second sentence at line 129. |
| Repeated sentence at `02-memory-dynamics.md:19` and 22 | No: consecutive sentences say the same thing. | Delete the second sentence at line 19. |

## 3. Openings, transitions, and material that is adequately taught

**Mathematical tools (`00-mathematical-tools.md`)**
- **Opening (lines 3–9):** sound. It starts from three questions and maps each tool to a paper.
- **Transitions:** the handoffs at lines 138 (information → bound) and 177 (bound → eye paper) are meaningful.
- **Adequately taught:**
  - lines 15–32: the feedback cycle;
  - lines 94–116: the Fisher-information question and the numerator/denominator meaning;
  - line 243: "mismatch drives velocity";
  - line 247: "filtering smooths without stopping accumulation";
  - line 294: the map is fixed in time;
  - lines 367–383: change of variables explained through equivalent events.

**Memory dynamics (`02-memory-dynamics.md`)**
- **Opening (line 3):** states the problem well.
- **Skim path:** the mechanism → derivation → interpretation sequence works in every section (17/19/79, 83/85/152, 197/199/239, 253/256/290).
- **Adequately taught:**
  - line 32: the physical meaning of dM_i;
  - line 105: the meaning of each term in K;
  - line 143: why **v**ᵀδ**s** stays constant;
  - line 310: the unit conversion that reconciles the two two-cell examples.
- **No closing paragraph is needed.** The forward link at line 246 is enough.

**Memory information (`03-memory-information.md`)**
- **Opening (line 5):** joins readout and memory noise in physical terms.
- **Examples placed before formulas:** the background-spike example (lines 33–43) comes before the formula and teaches something new. The heuristic is placed before the proof and labeled as a heuristic (line 167).
- **Adequately taught:**
  - line 169: what the Cauchy–Schwarz vectors stand for;
  - line 335: framing of the comparisons;
  - line 351: the τ mechanism;
  - line 404: the alternative firing budget.

**Place sizes (`05b-place-sizes.md`)**
- **Opening (line 5):** asks a concrete track/arena/room question.
- **Adequately taught:**
  - line 56: Gaussian conditioning;
  - lines 78–92: the excess-height distribution;
  - lines 99–118: rate ∝ s², with honest treatment of finite-threshold exponents;
  - line 237: motivation for slicing;
  - line 284: the boundary-selection effect;
  - the fold at lines 298–306: an independent check.

**Place tests (`05c-place-tests.md`)**
- **Opening (line 4):** poses the topology question and is answered by the closing at line 312.
- **Transitions:** the section handoffs at lines 152 and 252 are meaningful.
- **Adequately taught:**
  - line 40: the geometric meaning of the critical-point signs;
  - lines 122–133: the limit checks;
  - line 177: an inline likelihood gloss, which the place-field-only reading path needs;
  - lines 277–294: what each assumption supplies.

**Not yet passed.** The open findings above, and the stage-2 findings on symbols and the "weights" term, keep the affected passages from passing. They need a recheck once repairs are authorized.