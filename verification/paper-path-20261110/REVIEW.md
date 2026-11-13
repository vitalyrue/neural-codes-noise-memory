# Part I article route and source notes: focused review

Started 2026-11-10 16:10:53 +02:00. Scope: identify where Part I explanations correspond to the 2012 article and supporting text, including guide-created background and examples. Baseline source copies and SHA-256 hashes are in `baseline/` and `baseline.json`. No chapter move was needed; the article-order route permits following the paper while keeping prerequisite teaching before its use.

Initial independent inspection found that the reading guide already contains an appendix map, but no main-article map in publication order. Two source checks independently mapped chapters 1–3 and 4–6 to main and supporting-text sections, pages, equations and figures. Their additions comprise 33 location/background notes across the six chapters. The original paragraphs, display equations and headings were retained, as checked in `change-check.json`. The Part I opening now has a seven-item main-article route and explains the Methods, naive/ideal and generalizations order differences.

Three separate independent review calls assessed the changed map and notes:

1. Correctness: the checked page/equation attributions, article versus supporting-text distinction and the published 2017 correction versus guide checks were supported. A missing Discussion item was added. The two other-paper background labels were present in the completed writers' output.
2. Necessity and terminology: the notes identify source changes at the point needed; one plural-verb error at the S12–S13 note was repaired.
3. Reader flow: the Discussion route and other-paper labels are in place, the naive/ideal and Methods order is explicit, and no remaining critical continuity issue was found. The reviewer compared the six current sources with baseline and checked 79 local links and anchors without missing targets. This is not a full-book review.

Independent checks verified that 47 main/SI PDF page targets in the new notes are within the local PDF page counts. The six chapters retained all pre-existing nonblank lines, heading IDs and display-math delimiters. The earlier structure lock was saved in the baseline; the model hash was refreshed after checking all prior IDs and chapter order remain unchanged.

Direct Vale on the six complete chapters reported 137 errors, 112 warnings and 518 suggestions, including pre-existing and new alerts, not all adjudicated. The full quality gate, full-book semantic review and visual/figure acceptance were not run. Rendered checks and timings are recorded in `RESULTS.md`.
