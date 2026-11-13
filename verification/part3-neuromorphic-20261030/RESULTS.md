# Part III: neural memory in electronic hardware

Scope: the new Part III, Chapters 14–17, and its reading-path, reference, glossary and source-map additions. Existing Parts I and II retain their order and structure. The research snapshot is October 30, 2026.

The Part opens with a 23-word quotation from von Neumann, checked against printed page 66 (PDF page 78). Its four chapters separate stored weights, changing neuron states and decoded working memory; compare restoring feedback with neutral drift; explain selected current neuromorphic implementations; and develop experiments connecting device parameters to memory error. Current evidence includes 2025–2026 work on Loihi 2, SpiNNaker2, phase-change memory and a proposed dual-memory architecture. Fabricated devices, host-assisted experiments and post-layout simulations are identified separately.

## Independent teaching review

Three reviewers completed separate calls for truth/reasoning, terminology/necessity, and reader understanding/flow. The records are `review-memory-stage1/2/3.json`, `review-systems-stage1/2/3.json`, and `review-tests-stage1/2/3.json`. Each final Stage 3 verdict passes its assigned new-text scope. Findings and repairs remain in the records rather than being erased.

Repairs included current/voltage/capacitor meanings, the PCM input-duration and stored-conductance mapping, source-location corrections, hardware and learning terms, unwrapping, the precise open endurance question in the Wang paper, and a visible measurement-noise condition before the optional calculation. Mathematical models and illustrative numbers are distinguished from measured hardware results.

The reviewed concept check covers 23 selected concepts, 16 sections and 74 teaching/use relations. `concept-check.json` is clear for this local scope. It does not certify all concepts in the older book. Tables, equations and footnotes were also read directly; the passage extractor alone does not cover all of them.

## Formatting and checks

The final native Vale 3.24.0 report has zero blocking errors. Warnings and suggestions remain advisory; see `vale-native-current.json`. Forty-eight individual alerts received narrow, independently justified exceptions for exact quotations and source titles, ranges, mathematical wording or necessary distinctions. No shared style rule was disabled globally.

HTML checks found and repaired two rendering defects. Blank lines now separate footnote blocks containing lint comments. The three new raw pipe tables were moved into the publisher's native table blocks. All table headers and cells were retained exactly. `footnote-spacing-reuse.json`, `table-format-reuse.json` and `rebind-locators.json` document why the text reviews remain applicable after those format changes. The final concept packet binds to current source files. Its 46 referenced passage texts are unchanged after the table conversion.

The complete HTML link/footnote check passes: 24 pages, 1,858 local targets, 1,528 math spans and no failures. The three new tables pass row/column checks; the same check rejects a literal-pipe negative control. Live private-HTTPS browser checks verified the quotation and chapter navigation, the hardware table, blue definitions, 11.9px reading text, no page-width overflow, and opening a collapsed worked example with rendered mathematics. Screenshots are saved in this folder. This was a representative check, not an extended figure review.

The four new chapters have current direct semantic acceptance records. The final doctor reuses three of them automatically; it continues to flag Chapter 17 because its prerequisite, the earlier Fisher-information chapter, has an inherited whole-chapter review hold. The new Chapter 17 text and its needed connections were reviewed, but the earlier whole-chapter acceptance was not manufactured or expanded. The doctor reports 8 reusable and 12 required chapters across the complete guide. Fourteen selected source groups have reviewed coverage; this is not whole-paper coverage for every added reference. Previous source-map rows and the structure of the original two Parts are unchanged. No Git repository, commit, public deployment, PDF or DOCX output was created.

## Remaining boundaries

The older guide's full figure acceptance remains deferred at the user's request. Prior whole-guide semantic-review holds are retained. New-Part text acceptance and representative HTML checks do not claim complete whole-book or all-format release acceptance. The standard release-record check is recorded separately in `release-audit.json`; it is not an override of these holds.

Timing, final model hash, browser observations and handoff status are recorded in `STATE.json`, `scoped-acceptance.json` and `browser-checks.json`. Awake execution time was not verified from Windows sleep/resume events. Token statistics are unavailable.
