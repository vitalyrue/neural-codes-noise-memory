# Figure 2 teaching details added

User-authorized local HTML update, 3 November 2026. The outline and original artwork are unchanged.

## Reader changes

- Chapter 4's Figure 2 walkthrough now explains B's 10-second snapshot separation, 10 ms spike window, approximately 85 Hz peaks and neural-index axis; C's transfer-function inset, simulation markers, theoretical lines and standard errors; D's periodic-variance curve; E's nonperiodic rate-difference memory; F's population-rate units; and G's squared-rate-displacement axes and averaging.
- Chapter 18 now gives the exact rate-difference MSD measurement, defines the finite-simulation average, identifies valid starting times within the 200-second recording, explains overlapping intervals and distinguishes this average from the ring's 100-trial error bars. It explains the factor of one million when squared rates are converted from inverse seconds to inverse milliseconds.
- The new earlier SEM explanation is blue. Its later eye-chapter explanation keeps exactly the same words and loses only duplicate first-definition formatting.

## Focused review

An independent GPT-6.1 Sol high reviewer completed correctness, wording and connected-reading stages in separate calls. The wording stage found that SEM needed meaning at its newly earlier use. That explanation was added and rechecked. No required findings remain in this scope. Original stage reports, repair checks and current file hashes are retained beside this report.

- [Correctness](stage1-truth.md)
- [Wording](stage2-wording.md)
- [SEM repair check](recheck-SEM.md)
- [Connected reading](stage3-flow.md)
- [Later styling check](style-recheck.md)
- [Exact source changes](CHANGES.json)

## Checks and limits

Native source validation and HTML builds passed. The publisher renders the HTML book even for a scoped source request. A first build preceded the SEM review finding; the second included its clarification; the final build included the later duplicate-marking removal. Final build output is in build-final.log. Project asset/style postprocessing ran after the final build.

The affected-page check verifies outgoing links/assets, source scope and unchanged heading lists. Its planted missing-link case is rejected. All three served pages exactly match final local bytes. Figure 2's published image matches the source image. A browser check of Chapters 4 and 18 confirmed visible updated prose, blue SEM styling, 11.9px reading size and the rendered MSD equation without MathJax errors. [Final checks](FINAL_CHECKS.json).

No simulations were rerun. No full-book semantic audit, full figure acceptance, print output, public publication or Git action is claimed. The prior figure hold remains pending. Doctor's final status is recorded in doctor-final.log and CURRENT_STATE.md; the broader semantic ledger is separate from these focused reviews.

Actual timestamps and wall duration are in STATE.json. Awake execution time is unverified. Token stats unavailable.

Final doctor: Publisher/skill pins match; release-record audit passes with zero findings. The structure lock needed its current BookModel hash refreshed; every other field exactly matches its preserved baseline. Broader semantic review remains attention, and no full acceptance is claimed. See structure-comparison.json and doctor-final.log.

Completed 2026-11-03T17:59:02.855907+00:00. Wall duration 10.29 minutes. Awake time unverified; token stats unavailable.
