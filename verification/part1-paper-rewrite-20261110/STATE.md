# Part I paper-centered rewrite

Started 2026-11-10 16:24:37 +02:00. The user rejected the previous location-note-only pass and requested a rewrite of Part I with explicit in-text marks for paper claims and guide interpretation.

Baseline copies and hashes for the six Part I chapters, sidecars, chapter plan and structural lock are in `baseline/` and `baseline.json`. The plan is to revise chapters in three disjoint groups, preserve useful examples and formulas, review the resulting attributions and reading flow independently, then validate and rebuild local HTML. No full visual audit has been requested.

Labels agreed for this task: `[Paper]` for a linked paper claim or result in paraphrase; `[Interpretation]` for the guide's explanation; `[Guide derivation]` for expanded or rearranged reasoning; `[Example]` with local source indicated; `[Background]` for material outside the 2012 result. Labels do not replace evidence or qualifications. Distinguish the paper's official 2017 correction from independent guide checks.

At 16:26 +02:00, three workers are revising chapters 1–2, 3–4, and 5–6 respectively; the coordinator revised the Part I opening and label key. Independent reviews, preservation checks, HTML build and served-page checks are pending. Token stats and awake execution time unavailable.

At approximately 16:41 +02:00, all six chapter rewrites and three separate focused review stages are complete, with source/label and terminology findings repaired. The S7–S9 derivation now has two added intermediate displayed equations. A final source comparison confirmed that all 123 earlier displayed equations, headings, figure blocks and worked-example titles are retained; `preservation.json` records the current source hashes. The model validates and the structure lock was refreshed after ID/order checks. The full HTML build is running; rendered sample checks and final results are pending. Direct Vale on the six chapters returned 144 error-level alerts, 118 warnings and 533 suggestions, including pre-existing alerts, not all adjudicated.

At 16:42:22 +02:00, the HTML build and asset postprocessing had passed. The served Chapter 3 showed the paper/interpretation/derivation labels and an existing folded example opened correctly. All seven affected pages contained labels and 243 local targets resolved with no failures. Three served pages matched local output. See `RESULTS.md` and `REVIEW.md`. Full quality gate and full-book figure acceptance remain pending. Wall-clock elapsed 17 minutes 45 seconds; awake execution time and token stats unavailable.
