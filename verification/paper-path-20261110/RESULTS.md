# Part I article correspondence: result

Started 2026-11-10 16:10:53 +02:00; checks completed 2026-11-10 16:19:30 +02:00. Wall-clock elapsed 8 minutes 37 seconds. Awake execution time was not verified; token statistics unavailable.

Added a seven-item main-article-order route to the Part I introduction, with links to article pages and relevant guide sections. The route distinguishes main-article and supporting-text order, notes that the Methods were brought forward, and gives the article's ideal-before-naive readout path. The earlier supporting-text map remains in place. Added 33 compact source/background notes at section beginnings and important source changes in chapters 1–6; they distinguish the authors' results, other papers and guide reconstructions. Original prose, examples, display equations, headings and chapter order were retained.

Independent source checks and three separate correctness, terminology and reading-order reviews are summarized in `REVIEW.md`. The pre-edit sources and lock are in `baseline/`; `change-check.json` records that the six chapters had no pre-existing nonblank lines removed. After review, the structural-lock hash was refreshed and all earlier IDs and chapter order were verified unchanged.

Publisher validation passed with canonical hash 3671a348a2be. Full HTML build and `verification/publish_assets.py` succeeded. The private served Part I page showed the seven-item article-order list; a link from it opened the linearization section with the S7–S13 note before the explanation. All 33 notes rendered; 219 local targets on the seven affected pages resolved, with zero broken. A separate source check found all 47 linked main/SI PDF page targets within the copied PDFs.

Direct Vale on the six whole chapters reported 137 errors, 112 warnings and 518 suggestions, including prior and newly introduced alerts; these were not all adjudicated. The full quality gate and full-guide semantic and figure acceptance were not run. This is a focused source-correspondence and local HTML check, not full release acceptance.
