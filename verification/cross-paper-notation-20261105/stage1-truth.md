# Stage1: common notation truth and preservation

- Request cross-paper-notation-stage1-20261105; reviewer /root/exam_review_check; inherited Sol high semantic review; exact backend unavailable.
- Actual host start 2026-11-05T13:00:31.526295+02:00; report checkpoint 2026-11-05T13:01:52.680610+02:00; wall elapsed 81.2s. Awake execution time unavailable because sleep/resume logs were not collected. No clock change observed.
- Scope: changed common key and letter-context list, shortened three paper keys, step3 and connected mathematical-tools route. Compared baseline MD and YAML. No wording/flow/build or repeated source-formula audit.

## Exact unchanged material and allowed reuse

- Entire current YAML byte-identical to baseline YAML: True. Thus all35 formulas, local extra-symbol notes, source/guide locators, proof routes and decoding cells remain exactly unchanged. Existing map and all table metadata also unchanged.
- Reuse actual notation preservation judgments in verification/exam-notation-20261104/stage1-truth.md and earlier actual source judgments only for that unchanged material. This call checks the newly moved definition connections; it does not infer correctness from file hashes alone.

## Required finding

Common indices/counts bullet says i,j label cells where they index neural quantities. E1 instead uses j to label spikes, which are also neural quantities. Add the explicit E1 spike-index exception in this new common scope; its local t_j bullet already identifies time of spike j. No YAML change required.

## Changed group judgments

- Common firing rates: r_i, f/lambda and F are model firing-rate quantities, with spikes/s or Hz preserved. E1 f and E7 lambda are local eye aliases; local E1 r remains a velocity coefficient. This grouping does not identify the calibrated coefficient r with a rate. Retain.
- Common coordinates: memory theta has chosen model units, eye E has degrees and spatial x/y have distance units; explicit non-interchangeability prevents angle/position/state confusion. Initial Theta stays in memory additions; hats follow estimate/prediction rule with matching coordinate units. Retain.
- Common indices/counts: dimensionless N neuronal vs field contexts and N_m motor-neuron count preserved. E7 integrator-vs-motor and P5/P12 field counts remain local. Only E1 j exception needs repair above.
- Common times: seconds apply to intervals and response times, with distinct biological roles deferred locally. P9 spatial t exception explicit. Memory h/T/L meanings and eye lag/u remain local. No unit or response-role loss. Retain.
- Common diffusion: coordinate²/s and constant-D drift-free unbounded 2Dt model preserved. Explicit filtered-eye exception prevents applying Brownian MSD at short eye lags. E6 Brownian command vs filtered output remains local; M5/M11 matrix exceptions visible. Retain.
- Common information: J inverse-coordinate²/s covers memory FI and eye scaling estimate without asserting identical coordinate units or noise model. Gaussian-vs-Poisson exceptions stay local M16/E7. Scalar main vs matrix M5/M11 is explicit. Retain.
- Estimate/array notation: hats mean estimate or prediction, with observation source in row; this preserves theta-hat vs Ehat roles. Bold array and transpose convention supports unchanged equations, without asserting all arrays must use bold type. Retain.
- Letter contexts r/W/h/C: rates vs velocity coefficient, weights vs Brownian process, counting time vs response kernel vs fixed map, shared displacement vs covariance all match local unchanged definitions. Covariance-unit product and angle displacement distinction correct. Retain.
- Letter contexts s/chi/sigma/V: activation vs temporal dummy vs field size; eye fraction vs signed EC; spatial scale vs input standard deviation; variance vs environment measure all preserve previous meanings and units. No single-letter global equality implied. Retain.
- Shortened memory additions: W sender/receiver, initial Theta, h/T/L and source DeltaT, activation normalization/steady bar, rate derivative, input/bias/transfer units, synaptic tau, K/u/v roles and V units remain. Removed duplicate rate/coordinate/count/seconds/D/J meanings are supplied by common key; no missing condition after M13 prior repair. Retain.
- Shortened eye additions: true E/degrees/temporal D/counts/hats now common; Ehat-from-spikes and measured Eobs stay local. MSD/covariance, lag/u/dot, kernel normalization and350ms R remain. Covariance/angle units and exact shared-vs-local scope preserved. Retain.
- Shortened place additions: physical positions and F rate move common; d, input/threshold/std, normalized z/q/excess, gain, covariance/spatial primes, local distance, Gaussian tail/crossings, size and geometric constants remain local. Old x/y scalar/vector and distance meanings preserved globally; no spatial random-variable ensemble changed. Retain.
- Step3 and mathematical-tools route now describe common quantities then paper-specific meanings then row additions. That is an accurate map of the current definition locations; all35 source/guide links remain unchanged. Retain.

## Current source and rule hashes

- `content/chapters/00-exam-review.md` SHA256 `9da40189066df1c017f1c45d5326f4f39b41cbc0267f8a865772be5ae32dc588`
- `content/chapters/00-exam-review.yaml` SHA256 `e46668a7d36da8306487a3e87e6af2ebecdcd699ed1bca03a02d85151a9956e9`
- `content/chapters/00-mathematical-tools.md` SHA256 `4805e574f757ba940c15d4669d47911876ad7daf4e2630212477b803a59d256f`
- `verification/cross-paper-notation-20261105/00-exam-review.md` SHA256 `6dfb25f36518b9b12a94e0d2c7a044e0276302e71f5c972621629f07b0bc0529`
- `verification/cross-paper-notation-20261105/00-exam-review.yaml` SHA256 `e46668a7d36da8306487a3e87e6af2ebecdcd699ed1bca03a02d85151a9956e9`
- `verification/cross-paper-notation-20261105/00-mathematical-tools.md` SHA256 `1b88964307ef836ab154634dda43c747887e5e793b79dacdc1468bfe8491e440`
- `verification/exam-notation-20261104/stage1-truth.md` SHA256 `0bd183e118ca4fd0994feba0d4ef0e9d191b9791dafcbf82ec74673252186012`
- `C:/Users/vital/.codex/skills/course-study-guide-builder/references/math-code-case-contract.md` SHA256 `ce2313f897b63e74ba59a3afe1bbc4046d3aa84584072cda7e76470a7e3cef9a`
- `C:/Users/vital/.codex/skills/course-study-guide-builder/references/pedagogy-language-contract.md` SHA256 `f4c1eb544cf640b708e1970d9572fdc758fcc6aea806675d01a0256658df847a`
- Verdict: one narrow index-scope finding awaiting repair/recheck; all other changed definitions preserve meaning, units and prerequisites. No render, semantic full-book or publication acceptance claimed. No memory used. Token stats unavailable.

## Narrow index repair recheck

- Reread repaired common indices bullet with unchanged local E1 spike-time and P11 dimension definitions. It now scopes cell indices to weight/rate arrays, explicitly marks E1 j as spike index and P11 j as geometric dimension. This removes the overly broad neural-quantity claim. Required finding closed.
- Final stage1 verdict PASS for changed common definitions, shortened keys and preserved connections. No unresolved required truth/preservation finding.
- Final MD SHA256 `9da40189066df1c017f1c45d5326f4f39b41cbc0267f8a865772be5ae32dc588`
- Repaired indices bullet SHA256 `1100acc4a21ec778bf60486bcc98458ab4ac0a52bae9aec877c21875081a70c0`
- Actual host finish 2026-11-05T13:02:04.633528+02:00; wall elapsed 93.1s; since report13:01:52.680610 12.0s. Awake time unavailable.
