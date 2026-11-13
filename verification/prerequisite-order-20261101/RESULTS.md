# Prerequisite order and Chapter 1 simulation introduction

Completed 2026-11-01T19:42:16.437319+00:00. This record covers the whole-guide prerequisite review and the later request to explain Burak and Fiete (2012) network simulations in Chapter 1.

## Reader result

Chapter 1 now includes section **1.5, Network simulations test whether spike noise moves a stored value**. It follows the spike-count assumptions and precedes the comparison of neural signals with eye motion. It explains the stored synaptic activations, the fixed connection and input parameters, the inhibitory ring and its represented angle, the conditional spike draws and Euler update, the measured displacement, and the comparison with theory. The two-population test is distinguished from the ring implementation. Figure 2 is identified as simulation-versus-theory evidence, with biological motivation and the limits of applying Poisson theory to eye-position recordings explained separately. Paper page links support each part.

In section 1.2, definitions of the dot notation, decay time, spike index, Dirac pulse, weights, input bias and transfer function now precede their equations. The new preferred-angle, activity-bump and Euler definitions are blue. Existing equation content is retained.

The earlier whole-guide pass moved short essential teaching into the main reading path:

- Brownian motion is visible before the optional random-walk derivation in Chapter 2.
- Chapter 3 identifies centered spike counts, Brownian increments, the covariance delta, response matrix, variance matrix and projection weights before the equations depend on them.
- Likelihood is visible before the score calculation in Chapter 5.
- Chapter 6 identifies its observation/noise symbols, presents the finite ideal-readout result and hyperbolic cotangent outside the solution fold, and teaches white noise before its first required use. Chapter 8 links back to that teaching.
- Gaussian-process and jointly-Gaussian meanings are visible before their use in Chapter 10.
- Random seed is taught before the simulation settings in Chapter 19; Chapter 21 refers back to it.

The previous review diagnosed seven main prerequisite gaps. The final reader changes affect nine chapters, including the new Chapter 1 work. All prior outline IDs and the Part/chapter order remain; the only added outline ID is `sec:FOUNDATIONS-SIMULATION`. Details and optional proofs remain folded. Figures, their dimensions, authored screen typography and print rules were not changed. Detailed reproduction settings remain in Chapter 18.

## Review and source evidence

Three independent lanes covered the 21 teaching chapters, reading guide, glossary and references, with root integration of Part/book order. Original truth, wording and connected-reading records are `stage1-*.json`, `stage2-*.json` and `stage3-*.json`; narrow repairs and rechecks remain separate. Reviewers directly inspected display equations, which the paragraph extractor does not include fully.

The Chapter 1 extension has separate source, truth, symbol-move, wording, repair and connected-reading reports under `chapter1-simulation/`. Its independent source check used the local main paper and appendix. Stage 2 found and repaired the missing preferred-angle meaning, the distinction between firing rates and synaptic activation, metaphorical prediction wording, and the actor in the Part map. No further repair remains in the reviewed scope.

The current concept record contains **35 concepts, 88 exact-span relations and 117 reviewed sections**, including chapter openings. `concept-check-current.json` is clear for the reviewed book scope, with no missing chapters or unreviewed sections. The 73 relations from the earlier pass were checked against identical passage text before reuse; the extension adds 15 relations. This establishes the reviewed prerequisite path, not fresh scientific acceptance of every existing sentence or figure.

Structure/source records are in `preservation.json` (before the extension), `chapter1-simulation/integration.json` (the authorized added section), `final-source-changes-current.json`, the source coverage and term-location maps, and the change ledger. The old structure lock and source snapshots are retained. Current BookModel: `2bb5684375d86519c32bf6f6813e9f65aa38034b9667da3e4d8f3486c8c47e5b`.

## Checks actually run

- Native source validation passed.
- Final HTML build with Publisher 0.8.23 and Quarto 1.10.18 passed; the normal asset publisher copied eight paper PDFs with checked hashes.
- The local HTML checker passed for **29 pages, 2,407 local targets and 1,721 math spans**, with zero failures.
- The focused generated-HTML check passed **47 checks** on nine changed chapter pages. Required definitions and the finite readout formula are outside both native details and wrappers that become folds. Optional material follows the default-closed folding contract. In-memory negative fixtures were correctly rejected. This is a markup/runtime-contract check, not a completed browser interaction.
- All nine live pages returned HTTP 200 and exactly matched the local bytes and SHA256 hashes.
- Final doctor confirms matching Publisher/skill locks and a passing release-record audit with zero findings. Doctor remains `attention`: its broader semantic ledger reports 24 current reviews required and zero reusable entries. That ledger was not rewritten to imply full acceptance from this narrower prerequisite review.

## Limits and unresolved acceptance

Native Vale 3.24.0 is **not clear**. Across the eight earlier changed files it reported 45 error-level alerts, 93 warnings and 445 suggestions; three new error-level alerts were independently retained with specific reasons. The current Chapter 1 file reports 41 error-level alerts, 28 warnings and 116 suggestions; compared with its baseline, 12 error-level alerts, 3 warnings and 20 suggestions remain added. The extension's wording review judged those error-level flags in context, repaired the metaphorical wording, and retained valid conditions, mathematical transitions and panel ranges. No rule profile or severity was relaxed. See the Vale reports and independent lint judgments. A prose diagnostic or the record audit is not a full quality-gate pass.

A fresh browser display check could not be completed. The old browser connections were unavailable, and the native-browser attempt was stopped because the computer-use tool could not identify the active URL reliably. No further UI automation was attempted. `browser-limit.json` records this limit. The previously deferred full figure review remains pending. No original simulations were run, no new figure was generated, and no PDF/DOCX/public release or Git action was performed.

## Time

Original start: 2026-11-01T13:32:42+00:00. Extension start: 2026-11-01T19:23:52+00:00. Completed: 2026-11-01T19:42:16.437319+00:00.

Original wall time: 6.16 hours, including the interruption. Extension wall time: 18.4 minutes. No Windows sleep/resume events were returned for the queried interval; awake execution time is unverified. Token stats unavailable.
