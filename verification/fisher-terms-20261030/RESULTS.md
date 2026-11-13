# Fisher information and terminology repairs

The task was to explain Fisher information properly and find similar unexplained terms throughout the guide. The user clarified that expected value, variance, standard deviation and probability density are known. No elementary lessons on those four were added; the foundations chapter is byte-for-byte unchanged.

## Changes

- Fisher information now begins with the observer receiving variable spike counts. It explains local sensitivity, a background-firing example, sensitivity relative to noise, information per interval versus per second, and what the inverse-information error bound means. The example and two detailed proofs are folded. Definitions are blue and the central relationship is highlighted.
- The whole reader-text terminology audit checked earlier teaching rather than counting unexplained-looking words. Confirmed smaller repairs cover the reported t test and its reference, Spearman ranks, skew and excess kurtosis, thresholding and median filtering, the signs of maxima/saddles/minima in the Euler calculation, and the midpoint origin of the Stratonovich-to-Ito correction. The glossary has matching lookup entries.
- One required review correction added identical distribution to the normal-observation assumptions for the exact Student t reference. Existing figure assets, chapter/section headings, IDs, typography and print styles were preserved.

## Evidence and limits

Initial diagnostic reports: terms-memory.md and terms-observations.md. Their elementary-statistics proposals were explicitly withdrawn after the user clarification.

Independent review proceeded in separate actual calls: fisher-stage1.md, fisher-stage2.md, fisher-stage2-recheck.md, fisher-stage3.md and fisher-final-recheck.md; other-stage1.md, other-stage1-recheck.md, other-stage2.md and other-stage3.md; small-stage1.md, small-stage2.md and small-stage3.md. The root wrote the repairs; independent agents checked them. Reports contain passage evidence, conditions, arithmetic, source hashes and measured times. No unresolved required correction remains in these scoped reviews.

The native Vale 3.24.0 input route checked the six changed Markdown files with the existing project rules. It reports zero blocking errors, 92 warnings and 469 suggestions. Thirteen narrowly bounded exceptions retain meaningful technical wording; decisions are in lint-decisions.json and were independently reviewed. Global rules were unchanged. These diagnostics do not certify meaning; the separate reviews provide that evidence.

The concept packet was refreshed as an audit aid. It is not a new whole-book concept acceptance record. The historical whole-book pedagogy packet and semantic-review ledger were preserved instead of relabeling their old hashes as current. This task establishes focused text repair and HTML checks, not a renewed full-book release. Extended figure acceptance remains deferred, as requested earlier. No PDF/DOCX release, new illustration review, Git initialization, commit or public publication was performed.

The first HTML link check found one new glossary URL pointing to the appendix folder. The source now links to ../chapters/ch-memory-information.html#sec-memory-fi. A requested appendix-only Publisher build is unsupported (Chapter not found); the normal HTML build was repeated for that correction. Final output checks are recorded separately.

The supplementary citation question was checked directly against the saved PDFs: Seung (1996), How the brain keeps the eyes still, is reference 9 in Burak and Fiete (2012) and reference 30 in Ben-Shushan et al. (2022), and is absent from Mainali et al. (2025). Seung and Sompolinsky (1993), Simple models for reading neuronal population codes, is reference 28 in the 2012 paper.

## Timing

First persisted task timestamp: 2026-10-30T10:44:21+00:00. Awake execution time was not verified from system sleep/resume logs. Two early commentary clock estimates were corrected; final durations use saved timestamps. Token statistics are unavailable.

Final output check: 19 HTML pages, 1,429 local targets and all footnote counts pass. Browser checks confirm blue definitions, 11.9px text, no horizontal overflow, and working Fisher example/proof folds. The glossary URL was checked and its destination loaded. See browser-checks.json for the exact action limit.

Completed 2026-10-30T11:03:17.979990+00:00. Wall elapsed 18.95 minutes. Awake execution unverified. Token stats unavailable.

Final metadata reconciliation: the structure lock was identical in every field except BookModel hash, so only that binding was refreshed. Standard release audit passes with zero findings. Publisher doctor remains attention because the preserved historical whole-book semantic ledger requires nine chapters including dependencies to be refreshed before a broader acceptance claim. This does not replace the completed focused reviews above. Final handoff 2026-10-30T11:04:37.467425+00:00, wall 20.27 minutes.
