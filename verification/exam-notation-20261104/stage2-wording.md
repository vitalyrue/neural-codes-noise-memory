# Stage2: shared notation wording and necessity

- Separate request exam-notation-stage2-20261104; reviewer /root/exam_review_check; inherited Sol high, exact backend not exposed.
- Actual host start 2026-11-04T20:22:44.091583+02:00; finish 2026-11-04T20:23:39.858233+02:00; wall elapsed 55.8s. Awake time unavailable; no sleep/resume logs collected.
- Scope: changed shared keys, local extra-symbol bullets, changed instruction/route wording. No source/math/flow audit, edits or build.

## Verdict

PASS. No required wording change. Common definitions occur before tables, and local notes identify exceptions/additions rather than repeating every rate/time/diffusion definition. Physics/CS basic probability is respected: mean, variance, standard deviation and density are used without unnecessary tutorials.

## Shared-key and changed-paragraph judgments

- Quick-review step3 says to read shared notation first, then use extra symbols and paper/guide locations. This accurately names the new reading action and does not promise independent row keys. Retain.
- Memory bridge says recurring symbols vs additions/exceptions, while retaining derivative and scalar/matrix cues. Shared-key introduction states that it covers both memory tables. Scope is concrete; retain.
- Memory bullets group neuron/index/direction, coordinate/estimate, time intervals, activation/bar, rates/slopes, input/weight/transfer, synaptic time, diffusion/information, projection and variance. Each group describes object and units, with technical terms tangent/left zero explained by displayed relation and retained-shift role. Retain all10 groups; no empty glossary vocabulary.
- Eye-key introduction explicitly leaves filter normalization and response times local, so h is not given a false universal unit. Its six bullets distinguish times, three angle readings, MSD/covariance, temporal D, causal h and motor correlations. The350ms scope is now present. Retain; angle and time roles are easy to locate.
- Place-key introduction states position rather than time; nine bullets group coordinates, input/threshold, normalization/peak excess, firing gain, covariance/spatial derivative, distance scale, tails/crossing density, size/cutoff and geometric constants. Distinct sigma_0/ell_c and temporal/spatial h/C aliases matter. Retain.
- Extra symbols and notes label honestly includes model conditions as well as symbols. Shared headings and local bullets use stable symbol names, not vague here/above labels. A single shared definition may include several tightly related symbols because its purpose is to make one model object usable.
- Connected old-tools route now says blue keys define shared symbols once per paper and extra symbols appear as bullets beside formulas. This matches current source and user request, so retain.

## Actual row-item judgments by related group

- M1,M3,M7,M8: M1 local counts use counts/new spikes verbs; M3 local disturbance says retained shift; M7 adds short-observation information and fixed-state restriction. M8 needs no extra-symbol box because every formula symbol is shared. These short local entries fit their remaining job.
- M9,M13: M9 keeps only rate scale, input sensitivity and symmetry, with units and positivity. M13 labels cue-state variance, characteristic time, precision, coth and constant D/J. None is the general D/J/time definition repeated; keep all.
- M2,M4,M5,M6: M2 distinguishes count K_i from matrix K and expected count. M4 says steady input, derivative and symmetry. M5 groups coordinate indices, right/left vectors, slopes/delta, matrices/units/invertibility and PSD sign, avoiding an unexplained matrix exception. M6 groups density/constant-D, averaged D and wrapped-angle limit. Each bullet removes a specific alias or scope uncertainty.
- M10,M11,M12: M10 retains c multiplier and controlled comparison. M11 retains dimension/positions/width/gain/shape/density, referring to matrix units already in M5. M12 labels equal weighting, time-s alias and separate-noise/constant coefficients. The shared key removes repeated basic D/J/time prose while these conditions remain needed.
- M14,M15,M16: M14 local bullets distinguish access fraction, observed J, characteristic times and original-vs-cue error; M15 distinguishes response time from synaptic time and target rate; M16 states new noise intensity, Gaussian-information exception and threshold alias. These are changes of meaning, so a shared general definition cannot replace them.
- E1,E3: E1 items group offset/rate, fitted coefficients, delay/frequency, response times and impulse units; this is one calibration model rather than an overfull list of unrelated definitions. E3 items group displacement pair, shared/private errors, shared fraction and estimation uncertainty; shared R/time/angle definitions need not be repeated.
- E5,E6: E5 local normalization, stationary condition and A alias are essential because kernel units depend on input. E6 local command/filter time/Brownian process/velocity covariance distinguish input and observed motion. The word Brownian is an exact known model term; replacing it would hide mechanism.
- E2,E4,E7: E2 local population-vs-sample and standardization notes support bound use. E4 two local bullets give reading-error and measured-MSD quantities. E7 explicitly says integrator N differs from motor N_m, then rate, absolute/fractional slope, information, CV/time and source-sensitivity ambiguity. All address necessary distinctions; no statistics tutorial added.
- P1,P3,P4,P6: P1 positive-part operator and covariance derivative remain local; P3 track count/clipping and slope explain result-specific objects; P4 per-field/gap means and inverse tail distinguish samples; P6 excess/radius/counting weight give high-peak additions. Shared q/scale/size/gain definitions avoid repetition.
- P2,P5,P7,P8: P2 groups profiles/weights/covariance ensemble and Gaussian condition. P5 groups distances/counts/conditioning scope. P7 only peak rate/radius/linear-size measure remains. P8 only moment order/mean/Gamma transformation remains. Each retained item has a specific formula or derivation use.
- P9,P10,P11,P12: P9 states spatial t exception and restricted quantities. P10 distinguishes selected and ordinary slope densities and firing slope. P11 distinguishes signed topology from positive count and states boundary geometry. P12 distinguishes count N/environment V and high-threshold EC limit. These local exceptions should not be made global.

## Deletion test and list form

- Keeping shared units once per paper reduces repeated definitions while preserving the exact same coordinate/time meaning. Local repeated words such as dimensionless or degrees are retained when a new quantity has its own units or alias. Removing them would make the new symbol ambiguous.
- Matrix and stochastic-process terms are exact names used by formulas, so no synonym loop is warranted. Local examples are unnecessary for these reference keys because linked chapters already teach them and the page is explicitly a return point.
- All multi-item local definitions use one role=list span with separate role=listitem spans, visible bullet entities and breaks; shared keys use Markdown list items. Source has discrete bullet items. Actual rendered list spacing/color remains an output check rather than a wording verdict.

## Reuse and exact binding

- Parsed comparison confirms all70 old/current source/derivation/decoding cells exactly unchanged: True. Adopt earlier actual wording judgments only for those unchanged cells from verification/exam-review-20261104/stage2-wording.md; current shared/local definitions judged above. Formula display prefixes are unchanged as recorded in current stage1.
- `content/chapters/00-exam-review.md` SHA256 `6dfb25f36518b9b12a94e0d2c7a044e0276302e71f5c972621629f07b0bc0529`
- `content/chapters/00-exam-review.yaml` SHA256 `e46668a7d36da8306487a3e87e6af2ebecdcd699ed1bca03a02d85151a9956e9`
- `content/chapters/00-mathematical-tools.md` SHA256 `1b88964307ef836ab154634dda43c747887e5e793b79dacdc1468bfe8491e440`
- `verification/exam-review-20261104/stage2-wording.md` SHA256 `57b57dfc7f3c6fec7eedade88e95a4b8a03e8ca176da91ee96b21771e6c61a79`
- `C:/Users/vital/.codex/skills/course-study-guide-builder/references/pedagogy-language-contract.md` SHA256 `f4c1eb544cf640b708e1970d9572fdc758fcc6aea806675d01a0256658df847a`
- `C:/Users/vital/.codex/skills/course-study-guide-builder/references/math-code-case-contract.md` SHA256 `ce2313f897b63e74ba59a3afe1bbc4046d3aa84584072cda7e76470a7e3cef9a`
- No open required finding. Separate flow call remains. No memory used. Token stats unavailable.
