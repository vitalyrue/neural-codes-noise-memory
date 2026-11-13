# Mathematical tools before Part I

Added an unnumbered chapter after the reading guide and before Part I, as requested. Existing Part order, chapter numbers, section IDs and artwork are retained.

## What the reader now gets

- Why connection matrix W is needed: sending and receiving indices, signs, input units, the spike/activation/rate feedback cycle, fixed weights versus changing activity, and a two-unit example that preserves a difference while correcting total activation.
- What Fisher information measures: local distinctions between nearby represented values, sensitivity relative to Poisson count noise, finite-sample information versus information rate, a numerical comparison, and the importance of the information–diffusion bound.
- A blue definition of locally unbiased estimation before the Cramér Rao bound. The memory bound states tuned stationary patterns, relaxation of other disturbances, weak fluctuations, the common time constant and the spike-model assumptions. Current-state precision is distinguished from loss of the original cue.
- Two examples in explicit HTML disclosure boxes, initially closed. Required explanations remain in the main text. Detailed proofs remain in their existing chapters.

Reading-guide previews, first-use links, blue definition locations, the Glossary and source-coverage locations were updated. The simulation chapter's g_i is now correctly called total input, including its bias.

## Independent review

A fresh GPT-6.1 Sol high reviewer completed separate correctness, wording and connected-reading calls. Correctness repairs added the tuned-network condition, clarified the meaning of firing rate, and corrected two new supporting-text page links. Wording repairs explained the conditions on estimation and marked its first definition in blue. All required findings were repaired and rechecked. After the browser check, only example wrapper markup changed; an independent exact comparison adopted the original content reviews for the unchanged prose and mathematics.

- [Correctness](stage1-truth.md), [repair check](recheck-truth.md)
- [Wording](stage2-wording.md), [repair check](recheck-wording.md)
- [Connected reading](stage3-flow.md)
- [Exact content reuse after fold change](review-reuse-folds.md)

A separate first-use reviewer checked 34 selected concept relations. The native prerequisite tool found no ordering findings in those relations. Its coverage is deliberately partial, so this is not a full-guide prerequisite pass. [Current relation check](concept-findings-current-folds.json).

## HTML checks and limits

Native source validation and the HTML build pass. Final local links pass on 30 pages and 2,557 targets. Five served files match final local bytes. All 73 approved visual files from the baseline are unchanged. All existing outline IDs and titles remain in their order; Chapters 1–21 retain their numbers. [Checks](FINAL_CHECKS.json), [outline comparison](structure-comparison.json), [source changes](CHANGES.json).

The browser loaded the new chapter and confirmed 11.9px reading size, nine dark-blue definitions, rendered equations without MathJax errors and two initially closed examples. Automatic callout folding did not close the first draft's examples, so they were replaced with explicit details/summary markup. The browser automation could read the final DOM but input dispatch failed when opening an example; screenshot capture also failed. Open/close interaction and a fresh screenshot are therefore unverified. The final source uses standard HTML disclosure controls.

The structure lock was refreshed for the authorized chapter addition. The release-record audit passes with zero findings. Broader semantic acceptance and the earlier full-figure hold remain separate. No print build, public deployment, simulation rerun, installation or Git action was performed.

## Time

Start 2026-11-04 12:55:42 UTC, 14:55:42 Jerusalem. Actual completion and wall duration are in STATE.json. There was a long gap between the 12:58:30 and 13:25:22 checkpoints. Awake execution time is unverified. Token stats unavailable.

Completed 2026-11-04T13:47:48.171852+00:00. Wall duration 52.10 minutes including the checkpoint gap. Awake execution unverified. Doctor has matching pins and zero release-record findings; its broader semantic ledger remains attention for25units.
