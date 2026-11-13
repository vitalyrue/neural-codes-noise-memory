# Stage 3: reader understanding and connected flow

**PASS for current scoped reader understanding and flow.** No new teaching or ordering repair is required. The source-locator typo noted below was corrected and verified in the final narrow check. This is a separate third-stage call, not a re-labeling of the truth/wording calls.

Reviewer `/root/math_table_review`, requested GPT-6.1 Sol high. Backend request ID and exact serving build unavailable. Host start 2026-11-04T18:22:11.055892+02:00, finish 2026-11-04T18:25:05.258648+02:00; wall elapsed 0:02:54.202756. Awake execution time unverified. Since preceding stage2 recheck checkpoint: 0:03:18.478919. No observed clock change. No reader edits/build/visual review.

Scope and audience: physics/CS, calculus, linear algebra and basic probability. Read the opening three-paper route and table shortcut, the connected crossing/peak section including repaired beta paragraph and final finite-threshold warning, all summary-introduction paragraphs, all35 rows and all3 cells per row, and the route into PartI and its opening chapter. Full derivations linked by the table remain available; this optional reference does not have to reteach them in every cell. The source plan puts mathematical tools after the reading guide and before the memory PartI; this is the relevant ordering scope, not a whole-book acceptance claim.

## Connected path and changed paragraphs

MD paragraph locations below refer to the heading/starts in `00-mathematical-tools.md`; exact paragraph hashes follow. Retain all changed paragraphs.

- Opening questions: memory accuracy, shared eye fluctuations and place-field geometry establish concrete questions before tool names. Retain as chapter purpose.
- Audience/routes paragraph and three paper bullets: calculus/probability baseline and paper-specific tools tell the reader what will be explained and where to continue. Retain; they justify the reference table's physical questions.
- Added 'For a compact reference...' shortcut: useful after the routes because the reader knows the three problem families before choosing a formula. Retain as optional navigation, not a mandatory jump past the primers.
- Connected pre-summary crossing/peak section: a field starts at an upcrossing; finite-track endpoints clarify count convention; counts then motivate size distributions; peak excess plus geometry leads to dimensional laws. The beta paragraph's inverse-distance-squared unit check fits this progression. Retain; it supplies the place-size context needed by the summary.
- Final high-threshold warning before the summary: retains the limiting-versus-finite distinction immediately before the general table. Retain; it prevents the prior size laws looking exact for all thresholds.
- Summary paragraph1 ('Which formula...'): gives the table's question, derivation-link role and physical meaning of decoding. Retain because decoding would otherwise suggest only reconstructing values from spikes.
- Summary paragraph2 ('The rows follow...'): gives paper order, result roles, exact/approximate model scope and local-notation warning. Retain; it prepares the reader for model changes and reused symbols without requiring transitions between independent reference rows.
- Summary paragraph3 ('The full derivations...'): explicitly permits continuing to PartI without studying all rows. Retain because the table is a lookup resource before detailed chapters, not a new prerequisite course.
- Responsive wrapper: contains the same table block. It does not change a mathematical premise or prose relation. Presentation was not visually assessed in this review.

The next route is PartI, 'Noise limits memory accuracy in continuous attractor models', then `ch:FOUNDATIONS`. Its opening returns to biological holding of eye position and changing spikes before the network equations. This is a useful return from the reference table to the systematic teaching path. No extra invented transition between independent table rows is needed.

## Row-by-row reading judgments

Each location is `00-mathematical-tools.yaml`, `tbl:MATH-RESULTS.rows[n]`. Hashes cover all three parsed cells, encoded as compact UTF8 JSON. Each judgment below records the point, why it belongs here, and retain/revise decision.

1. **2012 · Spike-driven feedback · model**; row hash `30f8254b04f1afec`. Spike -> activation -> weighted input -> rate defines the circuit cycle before any error formula. N_i, s_i, W_ij and phi have usable roles from the prelude and repaired cell. Retain as the memory group starting model.

2. **2012 · Spike variability · model**; row hash `34677b21dbbd159b`. Counts fluctuate at an effectively fixed value; conditional generation is distinguished from complete recurrent trajectories. Retain after the cycle because it supplies the noise being projected next.

3. **2012 · Lasting displacement · central**; row hash `ec53d3565d4a9086`. K governs disturbances, u follows stored states, and v extracts the surviving shift. The physical meaning of D follows its formula. Retain: this is the general persistence result and gives the v used below.

4. **2012 · Symmetric connections · supporting**; row hash `97501571e094f09c`. Symmetry simplifies the general v calculation into input/tuning slopes. Primes and the correction are locally explained. Retain after the general case so the special condition cannot be mistaken for a requirement of all diffusion.

5. **2012 · More than one stored coordinate · supporting**; row hash `9b1a125c696ffe23`. Coordinate covariance and information matrices extend the scalar mechanism; a linear-combination interpretation gives the matrix inequality meaning. Earlier scalar FI prelude and the explicit matrix formula support J before its later scalar table row. Retain as a grouped multidimensional extension.

6. **2012 · Accumulated storage error · supporting**; row hash `342faaabe0f0f7cc`. The local D becomes a delay-dependent distribution, with conditions separating line and wrapped errors. Retain after local projection to explain accumulated storage loss. The limit warning prevents a false inference that a plateau stops neural noise.

7. **2012 · Spike precision · central**; row hash `1fb03caad5f19f11`. Tuning sensitivity relative to count variability gives current-state precision, not bits or original-cue accuracy. Retain before the scalar information bound because J is its second input.

8. **2012 · Information–diffusion bound · central**; row hash `f4b14e116c571d5a`. Normalization plus Cauchy Schwarz joins retained noise to spike precision. The decoding answers why memory must spread and names the held-fixed quantities. Retain as the main connection, rather than leaving D and J as unrelated formulas.

9. **2012 · Attaining the bound · central**; row hash `9a369a96bf77ab98`. Equality tells the reader whether the lower limit can be reached and which response class is sufficient. Retain immediately after the bound; the counterexample qualification prevents an overstrong transfer-rule inference.

10. **2012 · Controlled changes of circuit parameters · supporting**; row hash `758667b5b58d8ca6`. Population/rate/time changes give physical consequences with controlled comparisons and retuning conditions. Retain after equality because the reader can now distinguish a changed lower limit from an actual change in D.

11. **2012 · Tuning width depends on dimension · supporting**; row hash `eb9830739be0fe72`. Tuning width changes the active-cell count and squared slopes differently with dimension. Retain as the next parameter comparison; fixed peak rate/density and equality conditions explain what the powers mean.

12. **2012 · Equal-weight readout · supporting**; row hash `4662d5a0936312d1`. Equal weighting exposes the cost of collecting spikes while the state moves. Constant D/J and separate observation/motion noise appear in the decoding. Retain as the simple readout benchmark before the ideal rule.

13. **2012 · Diffusion-aware readout · central**; row hash `555a7d7b182cb99f`. Backward precision combination uses motion-aware likelihoods and approaches a limit. Precision P and reciprocal variance are tied by V=1/P, with full teaching linked. Retain after the benchmark, with saturation time distinguished from a hard deadline.

14. **2012 · Storage plus partial readout · supporting**; row hash `1d387c4016739e2a`. Storage loss, partial access and total recall are combined after both readout rules. Random thinning, independent storage error and full-access asymptote are distinct. Retain: the full-access phrase prevents alpha being silently dropped from a partial-readout limit.

15. **2012 · A rate response time changes the bound · extension**; row hash `7903fc21cb9da8a2`. A gradual firing response changes the model and resulting time factor. Retain in the extension block after the base readout result; symmetry and the specified two-stage drive prevent an arbitrary-time-sum reading.

16. **2012 · Noise law changes the equality condition · extension**; row hash `31df3b463d0a892e`. A different noise law changes both FI weighting and the equality condition. Retain after the time extension; q_n is locally defined and distinguished from spatial q, so the later paper cannot inherit this noise parameter accidentally.

17. **2022 · From spikes to eye position · method**; row hash `21f28f91277ed2af`. Fitted movement-to-rate inversion turns spikes into a calibrated position prediction. Retain as the eye group entry because the covariance analysis needs both signals in degrees. It distinguishes prediction from one-neuron causal control.

18. **2022 · Independent-noise limit · supporting**; row hash `225552a761186a3a`. Independent predictors have a finite total explained variance. Retain before shared-fraction estimation because it first tests whether independent motor noise alone can explain the data.

19. **2022 · Shared movement fraction · central**; row hash `5d95768316f31442`. Covariance retains the calibrated shared movement contribution. Retain after the independent-source test to estimate how much variance is common, with gain, small private covariance and upstream-source premises visible.

20. **2022 · Measurement offset · method**; row hash `acd4a7ed07acd652`. Two independent reading errors add a positive-lag constant MSD offset. Retain before interpreting lag-dependent motion, because otherwise the shortest-lag data can be mistaken for physical dynamics.

21. **2022 · Filtered white noise · supporting**; row hash `c8ae01698adbe741`. Decaying kernel overlap gives a stationary-noise MSD plateau. Retain as the rival mechanism against which accumulating internal motion is assessed, with the observed-range limit kept.

22. **2022 · Filtered accumulating command · guide derivation**; row hash `352ac9e6eeb6d3db`. A Brownian command passed through an eye response produces smooth motion with quadratic-to-linear MSD. Retain after the stationary rival as an explicitly marked guide derivation. Distinct eye/synaptic times and incomplete circuit identification are stated.

23. **2022 · Firing variability and sensitivity set a noise scale · supporting estimate**; row hash `b3a80c95b37a2b8d`. Rate, absolute/fractional slope, CV and population count explain the scale estimate. Retain after mechanism/timing because it answers how plausible cellular parameters change magnitude. The normalization ambiguity and full-model limit prevent a false exact source formula.

24. **2025 · Active spatial regions · model**; row hash `9eed756db88c4b93`. Normalized input, threshold, gain and local distance scale define a fixed spatial map. Retain as the place group entry, resetting notation and separating ell_c from input standard deviation.

25. **2025 · Random inputs create spatial covariance · supporting**; row hash `ea81d72da2712dc8`. A weighted sum of input profiles gives covariance across positions. Retain near the map definition as a possible circuit mechanism, while random weights alone are not treated as proof of smoothness or stationarity.

26. **2025 · Crossing density and finite-track count · exact**; row hash `f3b25b0bbd927723`. Crossing slope weighting gives field starts, and the endpoint term defines which finite-track components are counted. Retain before parameter inference because the same density appears in the means.

27. **2025 · Means identify threshold and scale · exact**; row hash `ac8726a701890183`. Active/inactive fractions divided by crossing density give two complete-object means and parameter inversion. Retain after counts: the explicit active-fraction ratio and clipping/selection qualifications tell the reader how the means may be used.

28. **2025 · Rare field locations and gaps · limiting approximation**; row hash `1ee4c3455b581661`. Rare independent locations supply whole count/gap distributions beyond means, and the zero-field conditioning changes observed counts. Retain after inference; spatial decay and finite-track exclusions keep the approximation scope visible.

29. **2025 · Universal size laws · central approximation**; row hash `0936cef692486838`. High-peak excess and geometry turn the map into dimension-specific size laws. Retain as the main place-size prediction; isotropy, equal field weighting and high threshold are all visible.

30. **2025 · Peak firing and field size · supporting approximation**; row hash `d3eeec9977af9ec9`. The same parabola gives peak rate versus size. Retain directly after size geometry because epsilon, radius, gain and dimension are already established, and finite-threshold exponents are explicitly separated.

31. **2025 · Size moments and shape · supporting approximation**; row hash `052bd34f31bb0a49`. Changing variables in the size law supplies moments and a shape test after the mean is set. Retain after the size/rate results as a derived way to compare full histogram shapes.

32. **2025 · Slices retain Gaussian structure · central test**; row hash `9ed6c19909a5a178`. Gaussian restriction gives line/plane excursion laws in higher-dimensional maps. Retain as a separate test after whole-field sizes: slice components and their weighting are expressly different from whole fields or central cuts.

33. **2025 · Boundary slopes · exact**; row hash `1799605e176827f0`. Upcrossing selection weights a Gaussian slope by v, giving an exact boundary law independent of q. Retain after the approximate size laws because it supplies a distinct local test and prevents confusing exact slope and asymptotic width results.

34. **2025 · Components and holes · exact**; row hash `0fc1c452e14919cf`. Signed critical-point contributions and boundary geometry give Euler characteristic, decoded into components and holes/tunnels/cavities. Retain before any EC-to-count approximation so the topological statistic is not mistaken for ordinary field count.

35. **2025 · Rare-field count in higher dimensions · supporting approximation**; row hash `f5c97b282c4c3116`. High isolated components let the leading EC volume term approximate their count. Retain last: it explicitly uses the preceding topological formula and names omitted holes/boundaries, closing the place group with the approximation limits.

## End-of-reading judgment

Reading the connected text as an open-ended explanation, I can distinguish current-state spike precision from drift of the stored value, an independent-noise test from estimation of shared movement variance, a stationary-noise plateau from a filtered accumulating command, and exact crossings/topology from high-threshold field laws. Parameter and sampling changes have stated conditions, and each group's formula can be followed to its physical implication and detailed teaching location. The table does not force me to infer that a one-cell predictor controls the eye, that every transfer function reaches the memory bound, that a Gaussian map is automatically smooth, or that a slice samples whole fields uniformly. No missing premise or broken conceptual jump requiring a new paragraph was found in this scoped reading. This is reviewer judgment for the stated audience, not evidence from an actual user comprehension study.

## Locator note and prior-stage reuse

Following row6's long-time link exposed one visible locator typo: 'SI Section II' should be 'SI Section III' for the density/long-delay result. The linked chapter target itself is correct. No formula or derivation change is needed. Coordinator was told to repair this label. This report does not waive the correction.

The responsive-wrapper change preserves prior semantic judgments. Its markup has no new reader-facing mathematical text. Prior truth and wording judgments apply to identical prose/formulas, except that the locator correction is recorded separately. Final exact content/hash verification is appended when the locator repair is present.

## Review boundaries

No full-book order decision, browser behavior, responsive layout, export, raw data or simulation-code check is claimed. Actual per-row understanding judgments above, not hashes alone, support the scoped pass. The primary-source math and rule basis were checked in their respective separate stages. No further optional expansion is requested. Token stats unavailable.

## Current reader, context and rule hashes

- `content\chapters\00-mathematical-tools.md`: SHA256 `0F663C5307F43FEE752A5E1EF3643CAED46DE10E3C85D78262F31E6AA4096FF5`
- `content\chapters\00-mathematical-tools.yaml`: SHA256 `7AD0589604D1F4209D9909789C525E354420F732DFF9B08C369B584E5D034E8E`
- `plan\chapter-plan.yaml`: SHA256 `3DD8B7972AEBACE997AF85D029932A303290547B033A4D1EF8C2192840D9BD71`
- `content\chapters\01-foundations.md`: SHA256 `54569CC3A6A93BB9EA9A67BE0F81A4BFC1B498D17BC533845167B8DA4165539D`
- `C:\Users\vital\.codex\skills\course-study-guide-builder\references\pedagogy-language-contract.md`: SHA256 `F4C1EB544CF640B708E1970D9572FDC758FCC6AEA806675D01A0256658DF847A`
- `C:\Users\vital\.codex\skills\course-study-guide-builder\references\math-code-case-contract.md`: SHA256 `CE2313F897B63E74BA59A3AFE1BBC4046D3AA84584072CDA7E76470A7E3CEF9A`

## Changed paragraph hashes

- `For a compact reference while reading, use the [major-results tab...`: SHA256 `53de47c7e26102dc091b0d5a90c9ffb466f6861a62e397ab39cb1b84a2ae2c52`
- `The result is three different limiting size laws. [The 1D length ...`: SHA256 `9f35413c9f493fc68b9dc0ac1821e0cff1990bd89eb1cb4205d4dc63e237788e`
- `Which formula answers the question you are asking? Use this table...`: SHA256 `a1434be72ac0e1bede07347dcccc645f9d06eecdd3451dafaeb9112e55c053dd`
- `The rows follow Burak and Fiete (2012), Ben-Shushan et al. (2022)...`: SHA256 `697446232afde8b9f648a344d5ae0276a2b0df4dae74935735467367665bb7f4`
- `The full derivations remain in their chapters. You can continue t...`: SHA256 `5a0962813e6d4e103d59f92ff0f1885f5646fbd7686e6825726ced207a18c975`

## Final narrow locator and content verification

At 2026-11-04T18:25:29.659465+02:00, verified row6 now says `Chapter 4; SI Section III`, matching the primary long-delay section. Its linked target remains unchanged. This resolves the sole locator note. New row6 all-three-cell hash: `342faaabe0f0f7cc`. The other34 row hashes above remain current.

Exact prior-stage reuse was verified by removing only the responsive wrapper in memory and obtaining the prior Markdown SHA256 `BECA4E530159D77B49C58495FC126530C6671AF8994E4310EF1F95BF9BC0DA02`, then reversing only the SectionII-to-III label in memory and obtaining prior YAML SHA256 `ADE8100D6E7F9271C0BBD3DDBD9A708BDF252B60AACE126D9FF708BF00F48BF6`. Windows CRLF and the existing YAML serialization settings were retained for these comparisons. Thus all mathematical prose and formulas reviewed in stage1/stage2 remain exactly unchanged, and only the checked locator plus non-semantic wrapper differ. No further truth or wording review is needed for these two changes. No new interpretation is inferred from the hash comparison.

Final source SHA256:

- `content\chapters\00-mathematical-tools.md`: `0F663C5307F43FEE752A5E1EF3643CAED46DE10E3C85D78262F31E6AA4096FF5`
- `content\chapters\00-mathematical-tools.yaml`: `7AD0589604D1F4209D9909789C525E354420F732DFF9B08C369B584E5D034E8E`

Final wall elapsed from stage3 start: 0:03:18.603573. Awake time unverified. No required finding remains in this scoped review.
