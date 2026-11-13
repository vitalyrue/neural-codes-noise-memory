# Eye drift chapter writer evidence

Writer scope: `content/chapters/04-eye-drift.md` and `verification/writers/eye-*` only.
Audience and plan: `PLAN.md`; undergraduate calculus, probability, linear algebra, new to neuroscience. Model: inherited GPT-6.1-sol/high as assigned. No further agents created. Writer completion is not independent acceptance.

## Persisted wall clock checkpoints

| Timestamp with offset | Work state | Wall since writer start | Since preceding checkpoint | Awake execution |
|---|---|---:|---:|---|
| 2026-10-22T19:10:39.2588657+03:00 | Source and instruction reading; first measured start | 0 | 0 | Unverified |
| 2026-10-22T19:14:33.1806442+03:00 | Forward fit, inverse kernel, shared variance bound, and chi draft written | 3m54s | 3m54s | Unverified |
| 2026-10-22T19:18:56.2186425+03:00 | Full first draft, MSD reconstruction and circuit/scaling complete | 8m17s | 4m23s | Unverified |
| 2026-10-22T19:21:57.731613+03:00 | Deterministic numerical checks passed | 11m18s | 3m02s | Unverified |
| 2026-10-22T19:22:32.4898494+03:00 | Heading IDs corrected; definition handoff and source hashes checked | 11m53s | 35s | Unverified |
| 2026-10-22T19:24:55.665132+03:00 | Arithmetic/markup recheck passed; evidence handoff prepared | 14m16s | 2m23s | Unverified |
| 2026-10-22T19:25:48.0674368+03:00 | Nonzero static-gain condition clarified; source hashes rechecked; final draft frozen | 15m09s | 52s | Unverified |

No Windows sleep/resume log audit was performed. No verified clock change occurred in these checkpoints. Durations are wall time from saved timestamps, not estimates of awake work. Final checkpoint and current manuscript hash are recorded in `eye-checks.json` when rerun for handoff. Initial estimate was 25–35 minutes; the draft and direct arithmetic checks progressed faster. Remaining independent review and HTML build belong to the coordinator. Token stats unavailable.

## Source versions and actual access

- P2 main PDF, 13 pages: SHA256 `15f273f99bd8d8e8daa09a9f7809e04c53da514b146750c0ec517812e3478caa`.
- P2SI notes and Extended Data, 14 pages: SHA256 `323335499cb6428f68714fb1c855a9b87d5fe38449d31e26acce76417358a7d6`.
- P2REV peer review, 35 pages: SHA256 `3f3c933f7cd1326d847565363481d7e79e922025ac354ae3872818f5aca3aa7c`.
- The source-register hashes were checked against the actual local PDFs in this turn. Main text read from extracted text, with the original main PDF p. 9 rendered to `eye-main-p09.png` and viewed to resolve Eqs. 6–7, sign pairing, and gain. Existing source renders of pp. 4 and 6 were leads from earlier work, not claimed as newly viewed images.
- Read P2SI notes and figure captions through local extraction. Selected exact peer review pages read directly from the text separated by PDF page breaks: 12–13, 19–21, 23, 34–35, with targeted search of reviewer concerns. No whole-file peer review acceptance claim.
- Supplementary file 5 is an XFA reporting summary whose ordinary extraction is a placeholder. Its form contents remain unreviewed. No claim depends on them.
- Raw data archive, original parameter tables, and computational repository were not downloaded or executed. No full experimental or model reproduction. The guide contains no code listings.
- The main and supplement are supplied sources, not a current literature search. DOI URLs are provided; this writer has not rechecked their network resolution. Coordinator should retain or refresh its link evidence before final citation acceptance.

## Page map in source order

Each explanation location below is a real heading ID in the drafted chapter. A `covered` disposition means the indicated page's needed teaching has a manuscript location, not that a reviewer has accepted that teaching.

| Source page | Disposition | Guide location and reason |
|---|---|---|
| P2-p01 | intentional-consolidation | Chapter opening and `sec:EYE-LIMITS`: abstract's upstream finding and specific integrator proposal are separated. Author affiliations omitted as nonteaching. |
| P2-p02 | covered | `sec:EYE-PATHWAY`, `sec:EYE-RECORDINGS`, `sec:EYE-FORWARD-FIT`, `sec:EYE-INVERSE-FILTER`: fixation, prior recordings, small rate effects, inverse prediction and mean correlation. Broad debate about drift's visual function omitted because this chapter teaches mechanism and inference. |
| P2-p03 | covered | `sec:EYE-SHARED-VARIANCE`, `sec:EYE-FIGURES`: Fig. 1, R-squared explanatory fraction, independence bound and common-input interpretation. |
| P2-p04 | covered | `sec:EYE-INVERSE-FILTER`, `sec:EYE-CHI`, `sec:EYE-FIGURES`: Fig. 2 kernel constants, displacement correlation, 302 segments, chi and estimation error axes. |
| P2-p05 | covered | `sec:EYE-CHI`, `sec:EYE-FILTERED-MSD`, `sec:EYE-PATHWAY`: gain transfer, common variance result, observed time dependence, and rationale for integrator. |
| P2-p06 | covered | `sec:EYE-MEASUREMENT-NOISE`, `sec:EYE-FILTERED-MSD`, `sec:EYE-SCALING`, `sec:EYE-FIGURES`: Fig. 3, Eq. 1 with normalization caveat, amplitude versus shape constraints. |
| P2-p07 | covered | `sec:EYE-CIRCUIT-MODEL`, `sec:EYE-SHARED-VARIANCE`, `sec:EYE-LIMITS`, `sec:EYE-FIGURES`: feedback's role, intrinsic independence basis, Fig. 4 neutral-direction diffusion and simulation validation logic. |
| P2-p08 | covered | `sec:EYE-CIRCUIT-MODEL`, `sec:EYE-FIGURES`: Fig. 5 stages, smoother physical output, MSD match, simulated analysis controls. |
| P2-p09 | covered | `sec:EYE-RECORDINGS`, `sec:EYE-FORWARD-FIT`, `sec:EYE-INVERSE-FILTER`, `sec:EYE-LIMITS`: Methods, threshold exclusion, timing, fit, leave-one-out, Eq. 2–7, and alternative upstream input sources. Surgical details and animal-care approval text omitted as procedural background. |
| P2-p10 | covered | `sec:EYE-CHI`, `sec:EYE-MEASUREMENT-NOISE`, `sec:EYE-FILTERED-MSD`: Eq. 8 displacement correlation, Eq. 11–17 covariance assumptions and weighting, Eq. 18–22 noise/MSD derivation. Eq. 9 finite-sample covariance-error calculation is described by its role and recorded as the paper's method, not rederived; Eq. 10 rate of uncertainty for R is not used in a new guide result. |
| P2-p11 | covered | `sec:EYE-CIRCUIT-MODEL`, `sec:EYE-SCALING`: Eqs. 23–31 and 34 roles, units and steady state; heterogeneous tuning, threshold and nonoscillation constraints; CV and spike thinning. Exact empirical slope-distribution coefficients of Eqs. 27, 32–33 and empirical CV fit coefficients in Eq. 35 intentionally omitted, since no population simulation is being reproduced. |
| P2-p12 | intentional-consolidation | `sec:EYE-RECORDINGS` covers active-cell/trial exclusions and `sec:EYE-CHI` error interpretation. Data/code availability recorded under source access above. Bibliography consolidated into the guide reference workflow, without copying every cited work. |
| P2-p13 | intentional-omission | Remaining bibliography, acknowledgments, disclosures, license and correspondence add no teaching step. Main source citation and access evidence retained. |
| P2SI-p01 | intentional-consolidation | Inventory used to ensure all ten Extended Data figures and notes were accounted for; guide explanation locations below. SI parameter files are recorded as not downloaded. |
| P2SI-p02 | covered | `sec:EYE-SHARED-VARIANCE`: Eqs. S1–S2 expanded into residual-variance proof. `sec:EYE-SCALING` introduces the question of drift's contribution to measured CV. |
| P2SI-p03 | covered | `sec:EYE-SCALING`: Eqs. S3–S6, covariance integral for within-segment Brownian variance, reciprocal-rate expansion, numerical CV and unit conversion. |
| P2SI-p04 | covered | `sec:EYE-CIRCUIT-MODEL`, `sec:EYE-FIGURES`: distinguish internal spike noise driving diffusion from direct output noise, and explain feedback motivation and role. |
| P2SI-p05 | intentional-consolidation | `sec:EYE-CIRCUIT-MODEL`, footnote p2-feedback: feedback effects combined with final main Eq. 34 and Extended Data Fig. 3. Stale supplement cross references and 15K parameter statement disclosed; final main 30,000 count used. Bibliography consolidated. |
| P2SI-p06 | intentional-omission | Supplemental reference continuation; no separate derivation or result. Sources cited through paper/SI locations and coordinator reference list. |
| P2SI-p07 | covered | `sec:EYE-CHI`, `sec:EYE-FIGURES`: Extended Data Fig. 1, uncertainty and estimates outside the underlying fraction range. Caption's repeated monkey label treated as a source typo, not used for a new claim. |
| P2SI-p08 | covered | `sec:EYE-MEASUREMENT-NOISE`, `sec:EYE-FIGURES`: Extended Data Fig. 2, fixed-coil control, twice-position-variance offset and simulated recovery check. |
| P2SI-p09 | covered | `sec:EYE-CIRCUIT-MODEL`, `sec:EYE-FIGURES`: Extended Data Fig. 3, feedback/no-feedback fit and lag-dependent slope changes. Individual alternate simulation counts intentionally not repeated. |
| P2SI-p10 | covered | `sec:EYE-FIGURES`: Extended Data Fig. 4, no-central-drive control and negative noisy chi estimate; Extended Data Fig. 5, second monkey parameter adjustments and nonunique fit. Exact alternate CV regression coefficients omitted with no reproduction. |
| P2SI-p11 | covered | `sec:EYE-PATHWAY`, `sec:EYE-FIGURES`: Extended Data Fig. 6, motor/internuclear classification by response parameters. No new claim about perfect cell-type certainty. |
| P2SI-p12 | covered | `sec:EYE-RECORDINGS`, `sec:EYE-FIGURES`: Extended Data Figs. 7–8, segment lengths/counts and rank-correlation confirmation. Histogram bins and separate rank-test p-value omitted because neither changes the taught inference. |
| P2SI-p13 | covered | `sec:EYE-CIRCUIT-MODEL`, `sec:EYE-FIGURES`: Extended Data Fig. 9, diverse tuning and motor-response parameters. |
| P2SI-p14 | covered | `sec:EYE-FIGURES`: Extended Data Fig. 10, output spike noise removal preserves internal spike noise and has little effect beyond 50 ms. The finest simulated lag effects are consolidated because the experiment's measurement noise limits that range. |

Peer review selected passages and omissions:

- P2REV-p12–13: source versus mechanism distinction and alternative upstream inputs, `sec:EYE-LIMITS`.
- P2REV-p19: absence of simultaneous multiple-OMN recordings, `sec:EYE-RECORDINGS` and `sec:EYE-SHARED-VARIANCE`.
- P2REV-p20–21: why not smooth raw trajectories and how noise-floor uncertainty limits the correction, `sec:EYE-MEASUREMENT-NOISE`.
- P2REV-p23: tuning changes and compensating neuron/time-scale choices, `sec:EYE-SCALING`. It repeats the printed raw-slope/rate scaling ambiguity rather than resolving normalization.
- P2REV-p34: response clarifies that the covariance method uses a single OMN readout versus behavior, not two simultaneous OMN spike trains; supports the recording limitation. This is not a check of the other paper discussed in that response.
- P2REV-p35: final reviewer replies read, no teaching content drawn from their acceptance.
- Remaining peer review pages intentionally omitted from a page-by-page teaching claim: earlier objections/replies, repeated passages, revision figures about extra cell-property comparisons, formatting comments, and revision history are not needed to derive the final paper's methods. Targeted searches found the exact passages listed above. None of the omitted pages is claimed as independently validated.

## Equations and claim checks

| Guide calculation or result | Source and actual check |
|---|---|
| Movement-to-rate model, threshold and neural lead | Main Eq. 2–3, p. 9. Read extracted text and original rendered page. Units checked term by term. Fit uses full trials; fixation correlation uses fixation only. |
| Delayed double exponential inverse | Main Eq. 4–7, p. 9. Original image checked. Quadratic roots, partial fractions, normalization and zero-frequency gain derived. `eye-checks.py` verifies time constants, prefactor, area and inverse gain at 0, 1, 10, 100 rad/s with positive delay. |
| R-squared explained fraction and independent-source sum bound | SI Eq. S1–S2, p. 2. Expanded best-linear-gain and standardized residual-variance proofs; 0.17 squared checked. Representative-population and private independence conditions retained. |
| Covariance chi formula and its weak self-noise correlation | Main Eq. 11–16, p. 10. All four covariance terms written before the approximation, with gain-transfer and pairwise uncorrelated assumptions. Order 1/Nm is attributed to source's model. |
| R=.17 and chi=.82 coexist | Constructed independent components; exact formula check gives R=0.1700015928, chi=0.8200000000, R²=0.02890054156. No experimental cell parameters asserted. |
| Weighted mean and estimation error | Main Eq. 17, p. 10. Minimization of sum a_i² sigma_i² with unit-sum weights explained. The reported .07 is distinguished from animal variation and calibration/model uncertainty. |
| Measurement-noise correction | Main Eq. 18–19 and SI Fig. 2. Derived 2 sigma_m² for positive lag, exact zero-lag distinction, and colored-noise modification. Constructed subtraction and 25% uncertainty arithmetic checked. |
| White-noise MSD saturation | Main Eq. 20–22. Kernel-overlap covariance derived, then stationary squared-difference identity. Normalized one-pole example checked by numerical quadrature. |
| Filtered Brownian MSD | Guide reconstruction: velocity stochastic equation, exponential covariance, double integral, M=2D[l-tau(1-exp(-l/tau))], both limits and local slope. Numerical quadrature agrees with formula at l/tau=.001,.1,1,5,100; short/long limits and alpha bounds checked. No claim this is the actual double-pole full model. |
| Network, motor, plant, feedback | Main Eq. 23–31 and 34, p. 11. Roles, all variables/units, spike jumps, nonlinear synaptic mean, steady-state gain and feedback sign explained. No fitting, stability proof of full recurrent network, or new simulation claimed. |
| D scaling and slope-normalization caveat | Main Eq. 1 p. 6 and previous chapter information relation. Dimensional check: absolute slope requires rate numerator, fractional slope gives printed inverse-rate dependence. Conditions fixed geometry, local response and noise preserved. |
| CV regularization and count scaling | Main “Sub-Poisson spike trains,” p. 11. Sum of M independent exponential intervals gives CV=1/sqrt(M); long window renewal count variance expanded from interval-time uncertainty. |
| Drift contribution to CV | SI Eq. S3–S6 pp. 2–3. Brownian covariance integration yields DT/3 within-window variance. Checked CV=.0024056261 and D=.0138888889 deg²/s; labeled an order-of-magnitude illustration. |
| Figures 1–5 and ten Extended Data figures | Main and SI captions read as evidence; guide table links each figure to a different inference step. No new drawing or visual was created for the chapter. |

`eye-checks.py` runs without optional scientific packages. Output is in `eye-checks.json`. These arithmetic and markup checks do not establish semantic acceptance. A few rounding and prerequisite improvements were applied after the initial run; rerun at handoff updates the manuscript hash.

Frozen chapter SHA256: `d5078b02cde50521c2a0d6b16a88d7937cc729f8a334b1217b40820dc7daa968`. A readback of the filtered-MSD section prompted the explicit nonzero static-gain condition for accumulation of filtered Brownian input, avoiding an overclaim about filters with zero DC gain. Source files and numerical/markup checks were then rerun successfully. The outer workspace `C:\dev\clsc` is not a Git checkout, so its `git status` cannot identify this file set; no Git mutation was attempted.

## Terms introduced for glossary integration

| First-marked text | Meaning | Section |
|---|---|---|
| microsaccades | Brief rapid eye movements separating drift intervals | Chapter opening |
| fixational drift | Small smooth irregular eye movement during fixation between microsaccades | Chapter opening |
| oculomotor integrator | Circuit maintaining a continuous eye-position command | EYE-PATHWAY |
| ocular motoneurons (OMNs) | Neurons whose spikes activate the eye muscles | EYE-PATHWAY |
| abducens nucleus | Brainstem group containing lateral rectus OMNs and other projecting neurons | EYE-PATHWAY |
| ocular plant | Eye muscles and eye mechanics that convert commands into movement | EYE-PATHWAY |
| causal filter | Filter using present and past input | EYE-INVERSE-FILTER |
| impulse response | Output produced by one instantaneous unit input | EYE-INVERSE-FILTER |
| convolution | Integral adding time-shifted responses to input | EYE-INVERSE-FILTER |
| coefficient of determination | Fraction of variance explained by a best linear prediction | EYE-SHARED-VARIANCE |
| superdiffusion | MSD growth faster than linear over the range considered | EYE-FILTERED-MSD |
| low pass filter | Filter suppressing rapid variations relative to slow ones | EYE-FILTERED-MSD |
| White noise | Ideal input uncorrelated between different times, specified by intensity in continuous time | EYE-FILTERED-MSD |
| stationary process | Here, a process with constant mean and covariance depending only on lag | EYE-FILTERED-MSD |
| sub-Poisson spiking | Here, renewal spiking with lower long window count variability than Poisson at same rate | EYE-SCALING |
| renewal process | Process with independent identically distributed successive intervals | EYE-SCALING |

CV markup was removed because `01-foundations.md` already defines coefficient of variation. Brownian motion, diffusion, covariance, recurrent connectivity and tuning are also inherited from foundations. Coordinator should resolve any first-definition overlap with the final memory chapters; those chapters were still being written during this handoff.

## Prerequisite and review handoff

- Earlier Chapter 1: rates/spikes, variance/covariance/correlation, tuning, fixed points/neutral direction, Brownian covariance and MSD=2Dt, CV and Poisson variability.
- Earlier Chapter 2: synaptic jump/decay, projection of independent spike fluctuations onto the memory coordinate, Brownian increment notation. This chapter briefly reuses rather than reteaches that full projection.
- Earlier Chapter 3: Fisher information J=sum(lambda-prime²/lambda), information-diffusion scale. This chapter supplies the needed local comparison to avoid dependence on memorizing a formula.
- The chapter itself teaches the motor pathway, experimental protocol, causal filtering, independent-source variance argument, covariance estimator, measurement correction, stationary versus accumulating input, renewal regularity, and observation-model distinction.
- Still pending: three separate independent reviewer stages, book-level first-definition and cross-chapter checks, rendered equations and footnotes, representative desktop/narrow visual check, DOI/link refresh if not retained from coordinator evidence. Writer has not accepted its own text or claimed any of those checks passed.
