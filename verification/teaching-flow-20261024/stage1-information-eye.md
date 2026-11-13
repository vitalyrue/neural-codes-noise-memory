# Independent Stage 1: Chapters 3 and 4 truth and reasoning

Recorded 2026-10-24T19:05:38.116711+03:00. GPT-6.1-sol/high. Root wall elapsed 11.26 minutes; this stage 1.77 minutes. Awake execution time unverified. Token stats unavailable.

No new mathematical or empirical overclaim was found in the scoped changes. One small moved-proof connection repair remains. No target author ledger, defense or prior verdict was read. No source edits were made, and this is not whole-book acceptance.

## Required repair

**S1-IE-01, priority 3.** `04-eye-drift.md`, line 126, `sec:EYE-INVERSE-FILTER`. The impulse-response fold ends: “Making the response zero before the spike gives”. The expression it promises is now above the fold. The closed path still has the correct formula; the expanded proof ends without its promised object. Change that final sentence to “Making the response zero before the spike gives the impulse response displayed above.” No equation needs changing.

Passage SHA256: `a6a01a1fbe397969ebaa932d712135d84357ed5e36057e80a5ab752575837184`. Source SHA256: `684837131c60b2e21e2b53a89013acf8e54a8472b993c724044fa6c8a4864d47`.

## Checked reasoning

- **Initial open assessment:** Chapter 3 adds a local information measure, a diffusion constraint and a readout cost to the preceding projection model. Chapter 4 needs this only after its separate recording/calibration evidence has established what movement can reveal. Keeping theory before the application gives meaning to the later integrator calculation. An experiment-first order is plausible but would require moving the projection and diffusion prerequisites into the application. No chapter swap is warranted by the connected text.

- **Audience and earlier teaching:** The baseline is undergraduate calculus, probability and linear algebra. Earlier proposed foundations teaches spikes/rates, conditional Poisson noise, covariance, CV, a continuous attractor and Brownian displacement. Proposed Chapter 2 teaches tangent/left projection, 2D=sum(v_i^2 r_i), u=tau r-prime, and both two-cell examples. Chapter 3 teaches likelihood, score and information before using them; Chapter 4 teaches the physiological pathway and filtering before covariance and MSD tests.

- **New title claims:** All 23 chapter/section headings were read with their complete sections and sidecar titles. Chapter 3 titles keep the bound as a lower bound, comparisons conditional on fixed quantities, additive errors conditional on assumptions, and the readout limit distinct from abrupt stopping. Chapter 4 titles use points to, challenges, estimates, and can reproduce, matching inferential rather than unique-cause claims. Its measurement-error heading is qualified visibly to positive lags and errors independent of movement and uncorrelated across sampled times; the filtering heading is qualified visibly to stable decaying kernels and nonzero static gain.

- **Information and equality reasoning:** Cauchy-Schwarz uses the preceding projected diffusion and tangent normalization. Equality is a proportionality condition at the current state. The exponential rule is visibly sufficient, and the linear counterexample does not alter the inequality. The matrix claim requires invertibility and keeps coupled directions distinct from scalar coordinate checks.

- **Readout scope:** Storage time T and observation time L remain separate. Zero cross covariance follows from local unbiasedness and future-noise independence; translation invariance supplies one readout variance. Independent Gaussian observation and transition noises are visibly identified as an approximation. Naive averaging, backward precision, ideal asymptote, full/partial access and the printed inequality caution remain inside that declared model.

- **Eye inference and mechanism:** One-neuron-at-a-time recordings are distinguished from simultaneous neuronal covariance. R squared is a fitted linear explanatory fraction; the common fraction uses calibrated unit gain and approximately uncorrelated contributions. The chapter retains the order-1/N private cross term, two-animal/horizontal/350 ms scope and uncertainty limits. Filtered white input and Brownian position are compared under the same one-pole teaching filter before the fuller model. Upstream localization remains separate from proof that integrator neurons are the unique generator.

- **Figure/caption connections:** All nine guide figure and table sidecar entries were read against their source leads and interpretations. Chapter 3 captions separate readout from storage, preserve the positive-rate range and show that a lower bound can fall while actual diffusion stays fixed. Chapter 4 captions separate the physical pathway from analysis, common from predictor noise, positive-lag measurement offsets from zero lag, and independently normalized model shapes from fitted data. No figure or block is inside a fold. This is a content/caption check, not a pixel inspection.

- **Original paper calculations:** Unchanged full paper calculations and empirical estimates were not rerun. The stage checks the mathematical meaning and conditions of the proposed teaching path and its changes; it does not certify raw-data reproduction or resolve every existing source-paper claim.

## Four fold boundaries

- `03-memory-information.md:129`, **Check: equality can also hold with a linear transfer rule**: The visible proportional-vector condition and the statement that an exponential rule is sufficient rather than necessary preserve the conclusion. The fold supplies a counterexample using Chapter 2 mutual excitation; theta, rates and the 2DJ product match that earlier model.

- `03-memory-information.md:185`, **Check: the residual matrix proves the lower bound**: The matrix inequality, positive-semidefinite meaning, invertible-information condition and U/V identities are visible. The residual Q proof contains no later-needed first definition.

- `04-eye-drift.md:111`, **Derivation: the weights of the two decaying responses**: The h0 formula, distinct positive roots, causality, units, neural lead and convolution are visible. Pulse matching supplies its constants inside the fold. Only the final promised-result connector needs S1-IE-01.

- `04-eye-drift.md:139`, **Check: static gain and coincident decay times**: The visible example already checks kernel area equals 1/k and identifies it as a constructed example. The repeated-root limit and further normalization argument are optional; later covariance and circuit reasoning use calibrated degree units taught visibly.

Optional preferences: none. Exact source hashes and all heading checks are in the accompanying JSON. Wording and reader-flow stages were not performed in this call.
