# Place-fields chapter writer evidence

Status: draft complete; independent correctness, wording, and reader-understanding reviews pending. This record is not chapter acceptance.

Task: source-grounded teaching chapter for Mainali, Azeredo da Silveira, and Burak (2025), including core derivations and prerequisites. Assigned files only were edited. No further subagents were used. Model inherited from the coordinator: GPT-6.1-sol, high reasoning. Token statistics unavailable.

## Persisted checkpoints

All times are measured local wall-clock timestamps with offset. Awake execution time was not verified from Windows sleep/resume events; no sleep or time-change conclusion is inferred.

| Timestamp | Stage | Wall since writer start | Since prior recorded checkpoint | Estimate remaining then |
|---|---|---|---|---|
| 2026-10-22T19:10:52.5012985+03:00 | plan/source read started | 0 | 0 | 25–35 minutes |
| 2026-10-22T19:13:38.9550497+03:00 | supplement acquired and critical equations inspected | 2m46s | 2m46s | 20–30 minutes |
| 2026-10-22T19:14:36.9660930+03:00 | numeric checks pass | 3m44s | 58s | 15–25 minutes |
| 2026-10-22T19:20:47.2537059+03:00 | complete chapter draft, foundation checked | 9m55s | 6m10s | 8–12 minutes |
| 2026-10-22T19:23:15.1445095+03:00 | final citation corrections, draft frozen | 12m23s | 2m28s | 3–5 minutes for evidence record |

## Files and verified access

Main source: `C:/dev/clsc/burak-papers/papers/mainali-2025-universal-statistics.pdf`, 15 pages, SHA256 `de2ca50a46f5b0d8d14e86269f1beacf6aadde7122bb348568aad92b12fd802e`. Main text and STAR Methods read from local PDF and existing column text. Main Figures 1–5 and STAR equations 8–10 were visually inspected in this task, using a small set of rendered pages. No exhaustive book visual review was performed.

**New supplement acquisition:** `C:/dev/clsc/burak-papers/papers/mainali-2025-supplement.pdf`, 2,840,295 bytes, 16 PDF pages (cover plus printed pp. 1–15), SHA256 `05af1fdf3079906871da12fdafa1f28895380f594a8c6bda3cafc5b503f07c31`.

- Download URL: https://ars.els-cdn.com/content/image/1-s2.0-S0896627325000431-mmc1.pdf
- Publisher's supplement listing: Document S1, Figures S1–S5, Methods S1–S4, supplemental references; Document S2 is article plus supplement.
- On 2026-10-22 at about 19:13+03:00, direct PowerShell `Invoke-WebRequest` HEAD and GET returned HTTP 200, PDF content. The web tool could not access the same route. Prior 403 results are therefore superseded for this local session.
- The mmc2 route also returned HEAD 200, but was not downloaded because S1 supplies the missing material.
- Extracted supplement text: `place-supplement.txt`. Visual checks of printed pp. 12–14 are `place-si-p13.png` through `place-si-p15.png`.

Primary mathematical source: Taylor, J. E. (2006). *A Gaussian kinematic formula*. The Annals of Probability, 34(1), 122–158. DOI https://doi.org/10.1214/009117905000000594. Author preprint https://arxiv.org/pdf/math/0602545 opened successfully and saved as `place-taylor-2006.pdf`, 421,035 bytes, SHA256 `58bd4dafe4a4fc749a16be1372ed850a936b49ffa139fa8d5e7cbdf44e1863ec`; extracted text `place-taylor-2006.txt`. Checked Eq. 1.4, Theorem 4.1, Section 5.1 and Eq. 5.1. These support the general Gaussian EC framework/densities. The piecewise-smooth remark in that paper concerns the target set in value space and is not being used as a separately verified theorem for the spatial box corners. The chapter derives the box face coefficients and checks them against P3 Eqs. 8–10.

Author notes: Mainali, N. (2026, August 6). *Mathematical properties of Gaussian process neural code: Excursion geometry, spectral structure, and coding error*. https://nischmainali.github.io/blog/gp-code-notes/ opened successfully on 2026-10-22. Checked “The Kac-Rice formula,” “Expected crossing count,” “Slope at an upcrossing,” and the high excursion section. Used for supporting the crossing/slope reconstruction, not as an independent verification of all dimensional peak geometry. Its multidimensional extension is explicitly described there as a simplifying approximation. This guide derives the isotropic ball/height route separately.

Canonical article DOI https://doi.org/10.1016/j.neuron.2025.01.017 exists and matches the local published source. Web opening its publisher route gave 403; indexed publisher text confirmed the supplement listing. This is an access limit, not evidence of a broken DOI. No raw data, large code archive, or experimental reproduction was downloaded.

## Source page coverage in original order

IDs use PDF page numbers; printed locators are supplied separately. `covered` means the topic is explained at the actual indicated heading, not that independent semantic acceptance is complete. Where optional formulas are not taught, that narrower omission is identified.

| Source ID | Printed locator and content | Disposition | Actual explanation location and scope |
|---|---|---|---|
| P3-p01 | graphical cover and highlights | intentional-consolidation | `ch:PLACE-FIELDS` opening introduces variety/statistical question; duplicate summary artwork not inserted |
| P3-p02 | 1110, summary/introduction | covered | `ch:PLACE-FIELDS`; `sec:PLACE-GP`; `sec:PLACE-WIRING`, distinction between maps and dynamic memory |
| P3-p03 | 1111, model and dimensional size law | covered | `sec:PLACE-GP`; `sec:PLACE-KAC-RICE`; `sec:PLACE-SIZE-LAW`; `sec:PLACE-DATA` |
| P3-p04 | 1112, Fig. 1A–F | covered | `sec:PLACE-GP`; `sec:PLACE-WIRING`; `sec:PLACE-DATA`, figure panel reading and histogram versus mean fit |
| P3-p05 | 1113, Fig. 2A–J | covered | `sec:PLACE-SLICES`, lengths/areas/volumes and line/plane restriction |
| P3-p06 | 1114, higher dimensions and shape results | covered | `sec:PLACE-SLICES`; `sec:PLACE-RARE-PEAKS`; `sec:PLACE-SLOPES`; `sec:PLACE-TOPOLOGY` |
| P3-p07 | 1115, Fig. 3 and topology | covered | `sec:PLACE-RARE-PEAKS`; `sec:PLACE-SLOPES`; `sec:PLACE-TOPOLOGY`, all Fig. 3 panel groups interpreted |
| P3-p08 | 1116, Fig. 4, parameter trends and threshold variation | covered | `sec:PLACE-DATA`; `sec:PLACE-RARE-PEAKS`; 3D scale unit ambiguity preserved |
| P3-p09 | 1117, Fig. 5 and discussion | covered | `sec:PLACE-RARE-PEAKS`; `sec:PLACE-DATA`; `sec:PLACE-WIRING`; small sample and high-threshold limits distinguished |
| P3-p10 | 1118, mechanism/discussion/resources | covered | `sec:PLACE-WIRING`; `sec:PLACE-DATA`; resource existence recorded here. Funding, author roles, reagent statement intentionally omitted as nonteaching metadata |
| P3-p11 | 1119, references 1–36 | intentional-consolidation | citations at relevant sections; full source bibliography not reproduced as teaching prose |
| P3-p12 | 1120, references 36–50 | intentional-consolidation | citations at relevant sections; unused cited papers intentionally not summarized without reading |
| P3-p13 | e1, resources, notation, GP and threshold | covered | `sec:PLACE-GP`; notation explicitly translated; code/data links recorded but no reproduction implied |
| P3-p14 | e2, scale, processing, parameter fits, likelihood tests | covered | `sec:PLACE-INFERENCE`; `sec:PLACE-DATA`; Gaussian covariance and exact mean inference taught |
| P3-p15 | e3, moments, 3D/peak/slope/EC methods, Eqs. 6–10 | covered | `sec:PLACE-DATA`; `sec:PLACE-SLOPES`; `sec:PLACE-TOPOLOGY`; all three EC formulas derived after theorem input |
| P3SI-p01 | cover | intentional-omission | metadata duplicates main article citation; retained in source file |
| P3SI-p02 | p. 1, Fig. S1, rat maze comparison/cutoffs | covered | `sec:PLACE-DATA`, simulation cutoff matching, outlier exclusion, log moments; alternative fit coefficient not needed for core derivation |
| P3SI-p03 | p. 2, Fig. S2, spherical null and curvature | covered | `sec:PLACE-SLICES`; `sec:PLACE-DATA`, volume-matched alternative can fail slices/EC; curvature as extra evidence |
| P3SI-p04 | p. 3, surface curvature formulas and finite differences | intentional-consolidation | `sec:PLACE-DATA` teaches principal bending meaning and measurement limits. Exact graph-surface derivative formulas intentionally omitted: they are secondary numerical estimators, not inputs to the GP results; deriving them would require a separate differential-geometry lesson |
| P3SI-p05 | p. 4, Fig. S3, size/count scaling | covered | `sec:PLACE-DATA`, sublinear count scaling and per-unit-size interpretation |
| P3SI-p06 | p. 5, Fig. S4, variable thresholds | covered | `sec:PLACE-DATA`, shared cell threshold creates cross-direction correlation; extra fitted parameters and additional histogram comparisons separated |
| P3SI-p07 | p. 6, Fig. S5 plots | covered | `sec:PLACE-DATA`, higher-moment sensitivity and slope stability |
| P3SI-p08 | p. 7, Fig. S5 caption | intentional-consolidation | `sec:PLACE-DATA`, combined with preceding plots |
| P3SI-p09 | p. 8, Methods S1, Gaussian process introduction | covered | `sec:PLACE-GP`, finite joint normality, means/covariances, threshold interpretation. Full multivariate PDF and IT-cortex comparison intentionally omitted because neither is needed for this chapter's calculations |
| P3SI-p10 | p. 9, Methods S2, homogeneous input sum | covered | `sec:PLACE-WIRING`, CLT conditions, covariance sum and autocorrelation, explicit Gaussian-width convention |
| P3SI-p11 | p. 10, heterogeneous inputs and Methods S3 | covered | `sec:PLACE-WIRING`; `sec:PLACE-KAC-RICE`, heterogeneous shape average and height/slope covariance |
| P3SI-p12 | p. 11, S11–S15, crossings and mean lengths/gaps | covered | `sec:PLACE-KAC-RICE`; `sec:PLACE-INFERENCE`, actual upcross integral and exact stationary means with finite-boundary limits |
| P3SI-p13 | p. 12, S16–S19, higher-d counts, size law, beta | covered | `sec:PLACE-TOPOLOGY`; `sec:PLACE-SIZE-LAW`; linear small-size 1D behavior follows full derived density. Apparent S18 error recorded below |
| P3SI-p14 | p. 13, S20–S23, conditioning/tail heuristic/parabola | intentional-consolidation | `sec:PLACE-RARE-PEAKS`; `sec:PLACE-SIZE-LAW`. Complete local peak/height route replaces the heuristic one-point-tail argument; no claim that one-point exceedance alone gives a full excursion distribution. S23 apparent missing sqrt2 recorded below |
| P3SI-p15 | p. 14, S24–S25, excess height and Rayleigh | covered | `sec:PLACE-RARE-PEAKS`; `sec:PLACE-SIZE-LAW`; `sec:PLACE-SLOPES`, explicit height survival/change of variables and independent slope-scale check |
| P3SI-p16 | p. 15, supplemental references | intentional-consolidation | consequential inputs cited through article/supplement and accessible Taylor source; full Adler/Nosko proofs not independently read |

## Derivations, numerical checks, and claims

`place-checks.py` ran successfully under Python 3.14.4. Output saved in `place-numeric-checks.json` at 2026-10-22T19:14:36.862364+03:00. This is a mathematical check of the teaching examples, not an experimental replication.

- Kac–Rice: derive narrow-band crossing compensation, integral over positive derivative, independence from joint Gaussianity, and exact density `exp(-q^2/2)/(2*pi*sigma)`.
- Mean inference: occupancy/intensity identities, explicit inversion. Numeric round trip recovers q=1.1,2.4,5 and sigma=2.4 with tolerance 1e-8. q=1.1 gives occupancy 0.13566606, density 0.03621269/m, mean length 3.74636845m, gap 23.86826429m, finite 200m count 7.37820309.
- Count selection: zero-truncated Poisson derived; lambda1 gives mean1.5819767068693265 and excluded fraction0.36787944117144233.
- Rare geometry: Gaussian conditional Hessian, relative curvature concentration, excess-height scaling, ball volume, full 1D width. Assumptions and theorem/proof limit are visible.
- Size density: change variable u=beta*s^(2/d), normalization, general moments, units, Rayleigh/exponential/Weibull distinctions. Numerical midpoint integration in u over[0,30], 200000 points, checks normalization within1e-7 and mean within1e-6 for d=1,2,3. At sigma1m,q5, means0.50132565m,0.25132741m2,0.12599688m3. Geometric mean matches occupancy/high-count asymptote algebraically.
- High-threshold approximation is not finite-threshold exactness: q1.1 rare 1D mean overestimates exact crossing mean by45.98%; q5 error3.73%.
- Slopes: derivative-weighted sampling at crossings gives exact Rayleigh slope law; high-q second-root width gives beta=q²/(8sigma²), independently matching peak geometry.
- EC: theorem input stated explicitly; conditional Hessian determinant expectations for d1/2/3, cancellation of fourth-covariance parameter, three Gaussian integrals, face/corner terms, cube and general rectangle convention, low/high limits. Numerical q=-12/+12 limits approach1/0; cube L/sigma10,q0 expectedEC=-20.05565 for d3.
- Empirical numerical exponents1.42/1.46 in1D and1.75/1.71 in3D verified directly from main Fig.3 raster. Asymptotic exponent2 is not called measured.
- Fit/processing/sample boundaries checked against STAR and SI. No new raw-map measurements claimed. Included-cell counts not supplied uniformly in inspected source, recorded visibly.
- Wiring: finite-vector CLT, suitable normalization/no dominant input, covariance/autocorrelation sum; Gaussian input shape integral evaluated explicitly. Sufficiency is separated from unique identification of connections.

## Apparent source discrepancies requiring independent review

The following are suspected printed errors, not accepted author corrections. The chapter presents the independently calculated expressions and keeps the note concise. The coordinator is to obtain independent mathematical review before accepting them.

1. **S18 (printed p12, PDF13):** preceding line says mean(s)=Gamma(d/2+1)*beta^(-d/2), but S18 visibly prints beta=[Gamma(d/2+1)*mean(s)]^(2/d). Solving gives beta=[Gamma(d/2+1)/mean(s)]^(2/d). The printed expression has units length² rather than inverse length². Screenshot `place-si-p13.png`.
2. **S23 (printed p13, PDF14):** S22 says z(x)≈z(0)+z(0)R''(0)x²/2. With R''(0)=-1/sigma², z(0)=q+epsilon, threshold roots are ±sigma*sqrt(2epsilon/(q+epsilon)). Full width is approximately2sigma*sqrt(2epsilon/q); S23 visibly prints2sigma*sqrt(epsilon/q). The next page inherits beta=q²/(4sigma²), whereas exact Kac–Rice mean's high-q limit and independent upcross slope calculation give beta=q²/(8sigma²). Screenshot `place-si-p14.png` plus `place-si-p15.png`. Shared sigma definition checked against main Eq4.
3. **S25 (printed p14, PDF15):** Gaussian tail ratio exp(-(q+epsilon)²/2)/exp(-q²/2) equals exp(-q*epsilon-epsilon²/2), whereas intermediate displayed terms use a positive epsilon²/2. After epsilon=u/q, either sign tends to exp(-u), so the final limiting law survives. Screenshot `place-si-p15.png`.
4. **S21:** its local one-point conditional-tail exponent also appears to have a factor-two issue: (q²/2)*(1-R)/(1+R) with R≈1-x²/(2sigma²) leads q²x²/(8sigma²), not q²x²/(4sigma²). It also conditions on a point at the level rather than selecting an upcrossing, so it should not be treated as a direct derivation of the field-length tail. The guide uses the complete peak and crossing routes, not this heuristic.
5. Main STAR contains several displaced figure references and one virtual-track species inconsistency (rats in method sentence versus mice in main Figure1F/results). Chapter follows the actual figure/caption and calls out the labeling issue briefly. Main Figure4 3D sigma4.0 unit interpretation remains unresolved and is not used numerically.

These observations do not establish that code, numerical fits, or empirical conclusions inherited the printed mistakes. No code audit performed.

## First-use terms and dependencies

Chapter introduces: Gaussian process; stationarity; isotropy; excursion set; Kac–Rice formula; Hessian; Weibull distribution; Euler characteristic; Betti numbers. It also defines gamma function and conditional Gaussian projection where needed. Root glossary may use those exact spellings. Existing foundation terms used without duplicate emphasis: firing rate, place cell, place field, rate map, covariance, Poisson process, synapse, recurrent connectivity. Foundation `sec:FOUNDATIONS-SPIKES`, `sec:FOUNDATIONS-POISSON`, `sec:FOUNDATIONS-COVARIANCE`, and `sec:FOUNDATIONS-RANDOMNESS` were read before freeze.

Audience assumptions: undergraduate calculus, basic probability, linear algebra. Assumed operators: covariance differentiation under stated smoothness, Gaussian integrals, determinants, Taylor expansion, change of variables. The first new GP section teaches the joint-Gaussian meaning and independence property. Local Hessian conditioning is derived through an independent Gaussian residual. Topological Morse theorem and general multidimensional Kac–Rice are explicitly theorem inputs, not falsely labeled proved.

No chapter reader exercises or code listings were added, so there are no unrun reader snippets or missing answer keys. Numerical verification code is separate from the manuscript.

## Handoff

Final chapter frozen hash at 2026-10-22T19:23:15.1445095+03:00: `5c054f8eb13f9b6995d845046a96692f1ae73b42a1b0446b039d8bd900053dc9`.

Root owns integration, sidecars, global ledgers, full reference list, separate three-stage independent review, HTML math/footnote checks, and representative visual checks. No local book build or claim of release acceptance is made here.

Completion checkpoint: 2026-10-22T19:25:59.0011644+03:00. Wall-clock elapsed since writer start: 15m06.500s. Time since the frozen-draft checkpoint: 2m43.857s. Awake execution time remains unverified. No system time change was established. Final structural rerun passed at the frozen hash: 6,576 whitespace-separated words including citations, 22 matched footnotes, 38 display math blocks, 10 valid section IDs. Page map contains 15 main and 16 supplemental unique IDs, and every recorded chapter heading target exists. Independent review remains pending.
