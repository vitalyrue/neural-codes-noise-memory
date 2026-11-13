# Part IV simulations and Part contribution labels

Completed 2026-10-30T17:25:16.355210+00:00. Task started 2026-10-30T16:43:18+00:00. Wall-clock duration 2518 seconds. Awake execution time is unverified; no Windows sleep/resume events were inspected. Token statistics are unavailable.

## Delivered scope

Added Part IV, **Simulations connect model assumptions to measurable outcomes**, with four short chapters:

- Chapter 18: Burak and Fiete (2012), stochastic neural networks, spike updates, diffusion measurement, alternative network designs and the distinction between numerical trajectories and evaluated formulas.
- Chapter 19: Ben-Shushan et al. (2022), recorded-data analysis, noisy integrator, motor pathway, muscle filtering, feedback, controls, MATLAB code and deposited recordings.
- Chapter 20: Mainali et al. (2025), Gaussian spatial maps, smoothing and normalization, fitted summaries, field measurement, topology, Python code and data limits.
- Chapter 21: source code versus an independent implementation, numerical tools, time and spatial resolution, repeatability, uncertainty and a record for reproducing one figure.

All four Part openings identify chapter contributions by author/year and distinguish central findings, supporting results, background and guide-derived explanations or tests. Original chapter IDs, titles and order are preserved. Part III remains the neuromorphic-computing part.

The only changed scientific claim in an older chapter is the narrow attribution of the corrected 2012 Eq. 2 to the authors' official 2017 correction. The equation was already correct. Other source-equation checks remain separate.

## Evidence and independent review

Sources and actual code settings were inspected, not executed as full-paper reproductions. See memory-sources.md, eye-sources.md, place-sources.md and tool-sources.md. Original program defaults are not silently combined with the publications' different parameter sets. Optional tools are distinguished from the packages actually used by each paper.

Separate independent truth, wording and reader-flow calls passed for the changed scope. The records are review-memory-stage1/2/3.json, review-eye-stage1/2/3.json and review-place-stage1/2/3.json, with separate repair rechecks. Initial findings are retained. Wording-repairs.json, wording-repairs-round2.json and flow-repairs.json record the edits. The final flow repairs teach the Gaussian filter operation, avoid using random seed before its explanation, and describe Part II's actual chapter order.

The local prerequisite check is clear. concept-judgments-merged.json and concept-index-final.json preserve the independently reviewed concept locations and assumptions. This does not newly approve the earlier chapters used as prerequisites.

Native Vale 3.24.0 checked the four new chapters and extracted changed Part/reading/reference/glossary passages. Its final raw counts are 68 error-level pattern matches, 28 warnings and 253 suggestions. These raw outputs have not been rewritten as zero. The independent wording records contain passage-specific repair or retain decisions, including exact source titles, numeric ranges, necessary contrasts and real causal statements. No global rule or severity was changed. Reader-flow review is separate from lint.

## HTML verification

- Canonical validation and full HTML build completed using Publisher 0.8.23 and the pinned teaching skills.
- 29 HTML pages, 2351 local targets and 1594 math spans checked; no local link, footnote-count or math failures.
- Eight existing local paper PDF assets were republished with matching hashes.
- Representative live browser checks passed for the new Part opening, the six-row native software table, blue definitions and the expanded numerical example. Base reading size remains 11.9px, without horizontal overflow or math-rendering errors. Screenshots are saved beside this report.
- Standard release-record audit and final doctor results are in release-audit.json and doctor-final.json. Current model: fa214ab2fbb3611db857ac47d83b3011bda2a178be917c6974bdab1dd431055d.

## Remaining scope limits

Whole-guide doctor status remains attention. Existing semantic/prerequisite and figure holds are not cleared by this extension. The full visual review of the earlier figures remains deferred. No full source simulation, raw-recording reanalysis, new raster artwork, DOCX/PDF release, public deployment or Git action was performed.

Open: https://vrdell15.tail8b993e.ts.net/burak/parts/part-simulations.html
