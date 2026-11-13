# Mathematical tools for all three papers

Expanded the existing pre-Part-I chapter, retaining its three memory-tool sections and all eight original displayed equations. Four new sections explain the mathematical tools used by the 2022 eye paper and 2025 place-field paper. The chapter title and opening route now explicitly cover all three papers.

## Added teaching

- **Eye paper:** covariance and correlation; calibrated gains in a shared/private signal model; why a weak single-cell correlation can coexist with mostly shared movement; causal impulse responses and convolution; low-pass filtering; white input versus a diffusing position command; short- and long-lag MSD predictions.
- **Place-field paper:** fixed Gaussian spatial maps and their joint law; covariance, stationarity, isotropy and local correlation length; threshold excursion sets; exact upcrossing counts and the track endpoint correction; high-peak excess statistics, quadratic geometry and the dimension-dependent size laws.
- The visible main text includes both ingredients of the size prediction: the excess-height distribution and the geometric conversion to length, area or volume. Exact crossing results are distinguished from high-threshold approximations.
- Generic covariance/correlation definitions, examples and longer calculations are folded. Physical meanings, key results and conditions remain visible. The page has seven closed notes/examples and 29 blue definitions.

Later first-use locations link back to the new teaching. Definitions were moved rather than marked as new twice, with local explanations retained. The place chapters translate the prelude's input standard deviation and distance-scale symbols to their existing notation. Three glossary entries and relevant source-coverage locations were added. The existing glossary entries, section structure and order are retained.

## Source and teaching review

Two writers drafted disjoint eye and place material from the original sources. A fresh independent reviewer then completed separate correctness, wording and connected-reading calls on the integrated text and its connections. Required repairs defined a motor-neuron count, the impulse and output covariance in the filter example, and the nonsingularity condition for crossings. Size-law forms and their exponential-excess premise were brought into visible text. All required findings were repaired and rechecked.

- [Correctness](stage1-truth.md)
- [Wording](stage2-wording.md) and [repair check](recheck-stage2.md)
- [Connected reading](stage3-flow.md) and [repair check](recheck-stage3.md)
- [Eye source map](eye-source-map.json), [place source map](place-source-map.json)

A separate reviewer assessed 36 first-use relations across six concept groups. Native prerequisite checking found no ordering findings for those relations. Coverage is partial; no whole-guide order acceptance is claimed. [Order review](order-review.md), [current findings](concept-findings.json).

## HTML checks

Native validation and the HTML build pass. Local target checks pass on 30 pages and 2,613 links/assets, with 2,000 math spans and no failures. Five served files match local bytes. All 73 approved visual files are unchanged. Existing outline IDs/order and Chapter 1–21 numbers are preserved; the authorized changes are the prelude title and four new sections.

A representative browser check confirmed seven section headings, 29 dark-blue definitions, 11.9px reading size, no MathJax errors, and seven initially closed disclosures. A new example opened and closed correctly. The opening layout screenshot was visually inspected through the browser tool. The user's prior reading page was restored afterward.

[Final checks](FINAL_CHECKS.json), [outline comparison](structure-comparison.json), [exact changes](CHANGES.json), [build log](build.log).

The release-record audit passes with zero findings after refreshing the structure lock for the authorized additions. The broader semantic ledger and prior full-figure hold remain separate. No full figure review, print output, public deployment, simulation rerun, installation or Git action was performed.

## Time

Task started 2026-11-04 14:18:20 UTC, 16:18:20 Jerusalem. Actual completion and wall duration are recorded in STATE.json. Awake execution time is unverified. Token stats unavailable.

Completed 2026-11-04T14:43:08.253623+00:00. Wall time 24.80minutes. Awake execution unverified. Doctor: matching pins, zero release-record findings; broader semantic ledger remains attention25required.
