# Independent review: focused repairs, stage 1 truth and reasoning

Request ID: other-stage1-terms-memory. Reviewer: terms_memory subagent. Started 2026-10-30T10:52:11.4572705Z. Audience: undergraduate math and ordinary statistics are known. This call covers truth/reasoning only; necessity, wording and reader-flow judgments are pending separate stages. I did not author these repairs and did not read terms-observations.md or a writer defense. Only this report was written.

Scope: current changed passages and their connected sections in 04-eye-drift.md (forward fit), 04c-eye-circuit.md (figure discussion), and 05c-place-tests.md (topology and data tests), compared against verification/fisher-terms-20261030/baseline/content/chapters. Relevant earlier support checked in 01-foundations.md, 05-place-fields.md and 05b-place-sizes.md. Associated sidecar captions/alt text read as claims, without opening figure pixels. No builds or general quality gate.

## Result

One narrow mathematical condition should be added before this stage can clear: the exact Student t reference at 04-eye-drift.md:120 needs identically distributed normal observations, including a common variance. The other changed claims pass this focused truth/source review with the limits below. This does not approve unrelated unchanged book content.

## Required correction

**S1-T1, medium: incomplete condition for the exact Student t law.**

Location: 04-eye-drift.md:120. The text calls Student t56 the distribution of the displayed ratio for independent, normally distributed observations with true mean zero. Independence and individual normality do not ensure this law if cell observations have different variances. A strongly unequal variance example violates the required independence between the normalized mean and pooled variance and does not produce the t56 law.

Repair: say independent, identically distributed normal observations with true mean zero, or explicitly add a common variance. The next sentence already correctly calls the cell-level use a sampling approximation. The final sentence correctly distinguishes 57 cells from 57 independent animals. That warning and the sampling-assumption caveat at :116 should stay. This finding is about the exact mathematical reference, not a claim that the authors' reported p value is numerically wrong.

## Passage judgments and source evidence

### T test, p value and the sample unit

04-eye-drift.md:77-133 read in context with recordings at :44-65. The fitted activity predicted from eye position is compared with measured firing-rate fluctuations, and the changed explanation keeps the population observation unit as one correlation per cell. Ben-Shushan et al. main PDF page 3, Figure 1d caption, explicitly states 57 cells in two monkeys, one-sided t test, p=3 x 10^-9. It does not provide enough raw per-cell correlations to recompute that p value here. The new standard one-sample statistic is the appropriate mathematical explanation of that test, subject to S1-T1.

At :116 the p value is the upper-tail reference probability under a zero population mean and sampling assumptions, which is correct for the positive alternative stated at :114. It is not described as the probability that a null or neural mechanism is true. This avoids reversing the conditional probability. Small within-cell correlation is kept separate from the later common-variance estimate. The nearby sidecar 04-eye-drift.yaml:87-91 describes weak positive fluctuations and the rate/correlation panels consistently. No figure pixels were checked.

### Spearman correlation

04c-eye-circuit.md:202-265 read with the figure-guide table. The changed :214 describes correlation computed after replacing paired measurements with ranks. This is the Spearman rank-correlation definition and it tests ordered, potentially nonlinear association rather than requiring a linear displacement relationship. A curved monotonically increasing relation is a useful counterexample to the need for linearity; a U-shaped relation would not in general be captured by this statistic, and the text does not claim it would be.

Source check: Ben-Shushan main PDF page 10 states that the rank correlation was computed between the two sets of eye differences, recorded delta E and predicted delta E. Supplement 1 PDF page 12, Extended Data Figure 8 caption, describes their distribution with positive mean 0.16. Thus the new words predicted and recorded displacements identify the correct measurements. The main page rounds/reports the significance as 2.5 x 10^-12 and the supplement caption as 3 x 10^-12; the added explanation gives neither numerical p value, so it does not introduce a conflict. Sidecar 04c-eye-circuit.yaml:139-142 also correctly describes the true/shuffled Spearman histograms. No correction needed for the changed claim.

### Critical points, Morse signs and determinant

05c-place-tests.md:11-144 read, with the earlier Hessian teaching at 05b-place-sizes.md:28-45 and crossing-count construction at 05-place-fields.md:120-143. At :37 the gradient-zero definition and nondegenerate critical-point condition are correct. Suitable boundary conditions and boundary contributions are explicitly retained rather than treating an open region or periodic box as an ordinary closed box.

At :39 the threshold moves downwards through interior critical points in 2D. A maximum creates a component (+1), a saddle either merges two components or creates a hole (-1), and a minimum fills a hole (+1). The Hessian signs are respectively (--), (-+) and (++), so det(-H) has signs +,-,+. This agrees with the signed Kac-Rice formula directly following at :42-58. Boundary changes need additional terms, as stated. The topology caption at 05c-place-tests.yaml:64-65 instead moves the threshold upwards and consistently says the active sets shrink; it does not reverse the new downward-threshold signs. No correction needed.

The source's STAR Methods, main Mainali PDF page 15, gives the EC as the alternating Betti-number sum and its dimension 1-3 formulas. The added local Morse explanation is a mathematical teaching derivation, not described as an empirical observation or a proof of the theorem. Its determinant signs can be independently verified as above. I did not re-prove the general Morse theorem.

### Log lengths, skew and excess kurtosis

05c-place-tests.md:147-187 read with its data-comparison table and source figure references. At :168-170 Y is explicitly log length, with central moments m_k. The skew and excess-kurtosis formulas are correct and refer to log lengths, not raw lengths. Cubed centered departures have signs and fourth powers weight large departures of either sign. A Gaussian of any mean with the same positive variance has fourth centered moment 3 m_2^2, so the reference subtraction and interpretation of positive excess are correct.

The claim nonzero population moments exclude a lognormal length distribution is correct, while the qualification zero alone does not prove lognormality is essential and correct. Counterexample: a symmetric log-length variable with probability 1/6 at each of -sqrt(3), +sqrt(3), and probability 2/3 at zero has variance 1, skew 0 and fourth moment 3, but is not Gaussian. Exponentiating it gives non-lognormal positive lengths with zero log-skew and log-excess-kurtosis. Finite-sample deviations from zero are not declared decisive population evidence in the repair.

Source check: Mainali PDF page 4, Figure 1E caption, compares simulated log-field-size skew/kurtosis with the empirical values and best-fit lognormal. STAR Methods PDF pages 14-15 gives the formulas and identifies log field sizes. At :173 likelihoods are correctly described as probabilities or densities assigned to observations by a model. The STAR page 14 reports a better log-likelihood and better AIC/BIC for the Gaussian excursion model, supporting the unchanged result statement. The fit is not represented as a held-out forecast.

### Rectification and median filtering

05c-place-tests.md:177-184 is supported by Mainali STAR Methods PDF page 14: bat 1D/3D maps rectified at approximately 0.5 Hz, 3D rate-map resolution 10 cm on each axis, scipy.ndimage median filter with kernel size 2. Therefore two bins on each axis is the correct interpretation of the scalar size-2 neighborhood. The new explanation uses a middle-ranked rate; it does not incorrectly claim that an even-sized kernel averages its two central values. The caution that filtering can change small features is mathematically sound: an isolated one-bin high value can disappear among low neighbors.

The rectification sentence correctly says below-cutoff rates are set to zero. The paper's short processing description does not specify in that sentence whether above-threshold amplitudes are shifted by subtracting the cutoff. The guide does not claim they are unchanged, so its stated below-cutoff effect is supported; do not expand that into an exact amplitude-transformation claim without additional evidence.

Source PDF page 15 also supports removing exceptionally large 3D fields and excluding them from slice analysis, Gaussian smoothing for peak identification, boundary exclusion, and the extra 1 Hz rectification for the rate/width comparison. Supplemental PDF page 8 (printed supplement page 7), Figure S5, confirms sensitivity to small denoising thresholds and stabilization above 1 Hz. The associated sidecar correctly states that thresholds change log-size moments. No new discrepancy was introduced by the focused repairs.

## Evidence and limits

A first PDF extraction failed because the Windows output encoding could not print a Unicode character. Repeating with UTF-8 succeeded; no scientific content was inferred from that failed call. Ordinary statistical definitions were treated as known and no basic-statistics primer is requested. No external web sources were needed because the supplied primary PDFs were read directly. Source-specific claims were checked from PDF text, not figure appearance. The t-test p value and empirical moments were not independently re-estimated from raw animal recordings.

Source hashes at the reviewed version, SHA256:
- content/chapters/04-eye-drift.md: 8E58C899BA46968D83B7A137E75CA70B46F5157BD08A50C7E0930BEC91B36933
- content/chapters/04-eye-drift.yaml: B987975477E369AF4EA4DF616B05BEC2DCC73AC2C0E04B701B5CD80D9077E41F
- content/chapters/04c-eye-circuit.md: 54E9715273CB0DEF9E045E02F6F1B71841DCDF1A1FDFAA9C6AA46606E9236007
- content/chapters/04c-eye-circuit.yaml: EAF05BC6D089A80FDF8ECCD7DEA973938456A8F8A3ACF390E767CF267536E41A
- content/chapters/05c-place-tests.md: B119F91382ACCAA6D0581AF2D2008B2DBE13A01448C3C38147F8439B62A49D75
- content/chapters/05c-place-tests.yaml: 210C382FF32BD22F1A9DFEEF2544BAD6F670467E3F622B1CF78126A7778392DA
- assets/papers/ben-shushan-2022-fixational-drift.pdf: 15F273F99BD8D8E8DAA09A9F7809E04C53DA514B146750C0EC517812E3478CAA
- assets/papers/ben-shushan-2022-supplement-1.pdf: 323335499CB6428F68714FB1C855A9B87D5FE38449D31E26ACCE76417358A7D6
- assets/papers/mainali-2025-universal-statistics.pdf: DE2CA50A46F5B0D8D14E86269F1BEACF6AADDE7122BB348568AAD92B12FD802E
- assets/papers/mainali-2025-supplement.pdf: 05AF1FDF3079906871DA12FDAFA1F28895380F594A8C6BDA3CAFC5B503F07C31

Finished 2026-10-30T10:53:58.5596686+00:00. Wall-clock elapsed: 107.1 seconds. Awake execution time unavailable because Windows sleep/resume logs were not queried. Measured checkpoint was 2026-10-30T10:53:01.1275718Z, 49.7 seconds after start; an earlier message used an estimated clock label 22 seconds ahead, so this measured record replaces that label. No observed system clock change. Stage 1 remains pending S1-T1. Token stats unavailable.
