# Part I paper-centered rewrite: result

Started 2026-11-10 16:24:37 +02:00; final checks completed 2026-11-10 16:42:22 +02:00. Wall-clock elapsed 17 minutes 45 seconds. Awake execution time and token statistics were unavailable.

Rewrote the Part I opening and six chapters with in-text `[Paper]`, `[Interpretation]`, `[Guide derivation]`, `[Example]`, and `[Background]` labels. The opening explains the distinction. All 56 explicitly labeled paper paragraphs have an article/supporting-text link or footnote in the paragraph. The authors' claims, the guide's explanations and reconstructions, cross-paper context, and separate correction checks are identified. The existing article-order route remains.

Chapter 3 expands the S7–S9 substitution and fixed-point cancellation, with two new intermediate displayed equations and an explicit physical meaning for the entries of K. Across all six chapters, `preservation.json` confirms that 123 earlier displayed equations, all existing heading IDs, figure blocks, example titles and worked-panel counts are retained. The Poisson background now states independent counts for a predetermined rate and flags the recurrent-rate distinction.

Three independent groups completed separate focused source/correctness, terminology and reading-flow reviews of chapters they did not write. Findings and limits are summarized in `REVIEW.md`. The initial sources and earlier structural lock are in `baseline/`; the lock was refreshed after IDs and chapter order were verified unchanged.

Publisher validation passed with canonical hash 6f4ccdb311cd. Full HTML build and `verification/publish_assets.py` succeeded. A browser check of the private served Chapter 3 showed the labels and expanded S7–S9 steps; a formerly folded example opened with its title intact. All seven affected rendered pages contained the new labels; 243 local targets resolved with none broken. The served Part I, Chapter 3 and Chapter 5 responses matched the local HTML bytes/text.

Direct Vale on the six whole chapters returned 144 error-level alerts, 118 warnings and 533 suggestions, including pre-existing alerts; not all were adjudicated. The full quality gate, whole-guide semantic audit, and full figure/visual acceptance were not run. This is focused review and sampled HTML verification, not a claim of complete release acceptance.
