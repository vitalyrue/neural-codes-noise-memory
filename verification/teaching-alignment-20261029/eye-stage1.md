# Eye and frontmatter truth review

Started: 2026-10-29 12:32:45 +02:00. Completed: 12:43:59 +02:00.

Independent reviewer: `/root/alignment_eye_truth`. Local request: `eye-truth-20261029-01`. This is the first, fresh truth and reasoning call. It does not complete the wording or understanding stages.

All 25 assigned units pass this truth scope. The report accounts for 236 extracted paragraphs and all 220 listed claim rows, plus the actual equations, footnotes, table cells, captions, figure text and sidecar summaries. No confirmed correction remained after testing the full passages with their nearby conditions. No manuscript or ledger was edited.

The most important checks were:

- The 82% result remains an inferred common horizontal displacement-variance fraction over 350 ms, conditional on calibration and noise assumptions. It does not identify the integrator as the unique noise source or describe the fraction of distance traveled.
- The inverse filter retains the required normalization and neural lead. Its example gives a kernel area of 0.25, and an 80 spikes/s input predicts a 20 degree offset when k is 4.
- The independent-predictor bound, calibrated covariance calculation and weighted error match the source and their derivations. The constructed example gives R = 0.1700016 while the common fraction is 0.82.
- Measurement error contributes twice the single-position error variance at positive lags, while exactly zero lag remains zero. The 25% subtraction-uncertainty example is correct.
- The filtered Brownian calculation gives the stated MSD and slopes: 1.718282 at one response time and 1.239490 at five. The text preserves slow correlated peripheral input as a different hypothesis from filtered white noise.
- The circuit is described as an approximate optimized memory system, and its feedback delay is not treated as a hard cutoff for ongoing MSD. The source's 30,000 integrator / 1,000 motor neuron simulation is distinguished from the separate 2,000 motor neuron comparison.
- The absolute versus fractional rate-slope distinction correctly exposes the printed scaling ambiguity. The original PDF equation was reopened. The drift contribution to CV recalculates to 0.0024056.

The added landing review is saved separately under `landing_fields` in the JSON. Its research settings and guide description agree with the sources. Its all-chapter teaching-order promise still needs the other chapter groups and the separate flow stage; this reviewer checked the eye-dependent path. Sidecar purposes and section summaries are separately recorded under `sidecar_reader_fields`.

Source figure meanings, captions and editable SVG text were checked. Extended artwork pixel acceptance and final HTML layout remain deferred. Original animal recordings and complete network simulations were not rerun. The two source page images only support formula/notation checks.

Wall-clock elapsed: 11 minutes 14 seconds. Last persisted calculation checkpoint: 12:35:56; the 12:42:53 update followed 6 minutes 57 seconds later. Awake execution time was not verified from system sleep/resume events. Token stats unavailable.

The structured result is `eye-stage1.json`; `eye-stage1-build-report.py` contains the specific passage judgments used to serialize it.
