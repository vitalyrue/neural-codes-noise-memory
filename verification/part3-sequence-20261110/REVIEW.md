# Part III sequence: focused review

Started 2026-11-10 12:17:09 +02:00. Scope: reorder the five Part III chapters and connect the changed reading path. Baseline copies and SHA-256 values are in `baseline/` and `baseline.json`. The prior structural lock was already stale before this task because the previously authorized architecture chapter had been added without refreshing it.

Initial independent readers inspected the Part III sources and advised the order: physical state, electronic architectures, stability and noise, hardware systems, experiments and readout. They identified an incorrect chapter-number reference and an earlier/later reference that the move would create, and recommended distinguishing one disturbance from ongoing noise and separating mean motion, random spread, output filtering and readout.

Three separate independent reviewer calls checked the current changed path and baseline:

1. **Correctness:** The one-push comparison, MSD decomposition, projected-diffusion assumptions, mismatch and information/readout distinctions are consistent with the local neural and electronic models. This call checked changed passages and source anchors, not the original research papers anew.
2. **Necessity and terminology:** The reviewer requested two repairs: identify an observer rather than a reader of circuit signals, and describe a voltage returning toward the voltage associated with the selected bit. Both were repaired.
3. **Reading order:** The reviewer checked the five chapter openings and endings, Part map and changed cross-references. The reviewer requested folding the detailed drift and readout preview in the newly earlier architecture chapter, while keeping a short visible preview. The original three paragraphs were preserved in the fold.

A separate recheck confirmed the two wording changes and verified the three preview paragraphs remain byte-for-byte present within the fold. `structure-check.json` verifies the existing heading IDs and displayed equations in all five chapters are unchanged, and the intended order is present. The structure comparison against the older lock found no missing IDs and eight additions from the previously authorized architecture chapter. After focused review, the structural lock was regenerated; the older lock remains in the baseline.

The changed-chapter direct Vale diagnostic reported 0/0/9/48 error-level alerts for chapters 07, 08, 10 and 11, respectively, plus warnings and suggestions. These are not all adjudicated. The full quality gate and whole-guide semantic and figure acceptance are outside this focused check. Source and rendered-output checks are recorded separately in `RESULTS.md`.
