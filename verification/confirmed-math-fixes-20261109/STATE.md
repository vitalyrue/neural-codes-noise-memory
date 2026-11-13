# Confirmed mathematical-guide fixes

Started 2026-11-09 11:58:45 +02:00. Source of findings: verification/claude-math-review-20261109/REVIEW.md. Repair only confirmed issues in the mathematical-tools, memory-dynamics, memory-information and place-tests chapters. Preserve useful worked examples, blue definitions, fold behavior, citations and reading order. Three separate editors own these files; independent review and local HTML rebuild will follow. Original CLI review input hashes remain in the previous review's request records.

## Checkpoint 2026-11-09 12:09 +02:00

Repairs applied to 00-mathematical-tools.md, 01b-persistence.md, 02-memory-dynamics.md, 03-memory-information.md, 05b-place-sizes.md and 05c-place-tests.md. Independent focused truth, wording, and connected-reading checks completed in separate stages. A reviewer identified missing conditioning on spike-count covariance and a hidden effect of input-profile width on variance; both were corrected and rechecked. Source validation passed; full local HTML build running in session 77567. The structure diagnostic reports three appendix/front-matter link failures and 24 warnings; generated navigation contains the appendix links. A scoped Vale run across six sources reports 142 errors, 130 warnings and 545 suggestions; these are not fully adjudicated. Full guide and figure acceptance remain pending.

## Completed 2026-11-09 12:13:31 +02:00

Source validation, HTML build and focused independent reviews completed. Six live pages matched local copies and 489 local targets checked with zero failures. The tools page rendered 342 MathJax containers with no MathJax error elements; a representative example was collapsed. Structural and Vale limitations are recorded in RESULTS.md. No full guide or figure acceptance. Awake execution time and token stats unavailable.
