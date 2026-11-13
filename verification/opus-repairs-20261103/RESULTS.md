# Repairs following the Opus review

The guide's supported review findings have been applied. The overall four-Part, 21-chapter order is retained. This task changes 22 reader Markdown files, their relevant metadata and the Part map; it does not introduce new artwork or replace the source papers.

## What the reader gets

- Chapter 1 now explains what an MSD curve averages, how lag differs from absolute time, what the axes and units mean, and how to interpret ordinary versus logarithmic slopes. It warns that slope alone does not identify a neural cause and distinguishes the represented command from the physical eye angle.
- Chapter 3 distinguishes synaptic state, remembered coordinate and an observer's estimate before the calculation relies on them. A noisy state receives its coordinate through the circuit's noise-free return flow, rather than an assumed perpendicular projection.
- Chapter 5 gives the paper's physical intuition for the information bound before its unchanged algebraic proof. The intuition is labelled as such.
- The two-cell example is connected across persistence, diffusion, information and readout. Its rate and activation coordinates, and their units, remain distinct.
- Fixational drift is distinguished from systematic mean motion. The within-chapter `q` collision is removed, the unrelated uses of `χ` are flagged, and the hardware projection vector is connected to the earlier one.
- The reading guide has a per-paper evidence table: physical system, model, prediction, simulations, recordings and untested links. Place-field readers have a short section-level foundation route.
- Part IV says what its numerical settings, code/data access and reproduction cautions add. Chapter 1 retains the requested explanation of the simulated system and coupled updates.
- Hardware examples identify host preprocessing, deterministic configured dynamics, recent-history storage and the limits of the demonstrated results. The eye scaling argument is explicitly heuristic under its assumptions.
- The glossary has missing lookup terms and a simulation/methods section. References now follow reader use; a fragile numbered paper pointer was replaced by a source link.

The readout chapter now explains what its independent-noise approximation excludes. The unconfirmed alternative readout bound from the earlier review was not added as an established result.

## Review and repairs

Three independent reviewer groups completed separate truth, wording and connected-reading calls. Their records are `stage1-*.json`, `stage2-*.json` and `stage3-*.json`. They cover the actual reader paths, sidecar content and relevant primary sources. The flow records contain 1,153 paragraph, list-item, footnote or lookup-entry judgments across the three scopes, plus chapter and section handoffs. The whole-book arrangement was checked from the actual plan, chapter openings/endings and needed connections; this does not mean every derivation outside a reviewer's assigned group was reread by that reviewer.

The reviews found and resolved additional narrow issues during this task:

1. The eye-feedback sentence must delay only the eye-position input, while retaining the immediate internal-command term.
2. Reference ordering must account for unlinked author-year citations as well as links, and any numbered pointers must follow the new order.
3. The readout derivation's inverse-function step gives precision; a separate reciprocal gives variance.
4. A sidecar retained an obsolete first-definition marker.
5. Two unused specialist phrases were replaced by direct descriptions of the operations.

Original findings and earlier source freezes are retained. Later rechecks record their resolution without rewriting the original reviewer answers. The routes reviewer reported accidental exposure to a few author-rationale search snippets and recorded that limit; the initial brief itself supplied no prior verdicts.

The exact original/replacement passages and reasons are in the `edits-*.json` ledgers. They include planned timestamps before each write. The original Opus review and its later qualifications remain separately preserved under `../opus-review-20261103/`.

## Verification scope

- Native source validation: passed for four Parts.
- Structural diagnostics: discovery passed for all 24 reader files; editorial warnings remain distinct from errors.
- Focused concept check: clear for four reviewed concepts, nine exact teaching/use relations and 32 sections in the six-chapter memory path. Its declared scope is local, not a whole-book concept clearance.
- Preservation: all prior outline IDs remain. One glossary section was added, and the random-wandering chapter title was clarified. The 84 existing asset files, including paper copies and styles, match their recorded hashes.

- HTML build: passed with Publisher0.8.23 and Quarto1.10.18. A second build was necessary after link checks exposed home-page summary links and a missing title anchor. The source-only fixes preserve the explanatory wording; `link-only-review-reuse.json` records this fast path.
- Local links: passed for 29 pages, 2,437 local targets and 1,772 math spans, with zero failures. The initial failed report is retained separately.
- Served bytes: five representative VPN files match the final local outputs, including the home page, reading guide, foundations, long-delay chapter and references.
- Browser: two served pages passed at the normal viewport; the evidence table also passed the 733px width check. The seven-row table renders with math, the MSD teaching is outside closed folds, the base font is11.9px, first-definition color is correct, and an example opens and closes from its default-closed state. Two screenshots were visually inspected; the final screenshots are pixel-identical to those checked before link-only repairs. This is representative HTML verification, not the deferred full figure audit.
- Final doctor: Publisher and skill locks match; release-record audit passes. The broader semantic ledger remains attention, with no claim that this repair task cleared it.

Final BookModel: `6198157910f51426cdb6c6db6a23a0bdf592476163778ee16781360dcaa4818e`. Detailed final numbers: `FINAL_CHECKS.json`.

## Limits

This task does not clear the previously deferred full figure review, reproduce the original experiments, run every original simulation, verify every secondary citation, or produce a DOCX/PDF release. It does not claim that the combined quality gate or Publisher's broader semantic ledger is fully clear. Existing lint warnings were not hidden by weakening the profile.

The original review's optional Part split, larger new artwork and unconfirmed research calculations remain proposals. The inspected printed-paper inconsistencies remain labelled mathematical checks, separate from an author-issued correction.

## Time and model

Start: 2026-11-03 14:30:36 UTC, 16:30:36 Jerusalem. Completed 2026-11-03 15:19:59 UTC; wall-clock elapsed 49.4 minutes. Durations include all wall-clock time; awake execution time is unverified.

The coordinator is GPT-6.1-sol. Editing and independent review agents were configured as GPT-6.1-sol with high reasoning; their own deployment strings were not exposed in their turns. The prior external review used actual Opus 5.5; it was not rerun or represented as reviewing this revised version. Token stats are unavailable for this task.
