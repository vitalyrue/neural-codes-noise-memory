# Separate Stage 3: understanding and teaching order

Start only after the coordinator supplies the current packet and hash. Earlier reports remain unchanged. A two-sentence eye-timing deletion is pending; do not begin this stage on the preceding freeze.

Read the connected assigned path, including its openings, visible explanations, folded text, equations, typed tables, figure captions/labels and sidecars. Ask what each paragraph adds, why it belongs here, and whether the reader has the ideas needed to follow it. The reader has undergraduate calculus, basic probability and linear algebra; teach the neuroscience and further tools. Do not fill missing steps from expert knowledge. The glossary and an optional fold do not automatically supply an essential earlier explanation.

Save a separate actual `understanding_flow` call with measured start/end, reviewer identity, context `reviewer_continuation`, current input/rule hashes, unit assessments and supported reader questions. Report a required repair with its meaning and location; do not write replacement prose or edit the manuscript. Keep figure pixel acceptance deferred.

## Evidence to save

For every current paragraph ID, record `purpose`, `connection`, `decision`, and `reason`. Give a specific account of the actual contribution and its neighbor, not one repeated template. Keep the original ID and text/hash. Comment-only records must be explicitly identified as hidden lint controls, with their placement checked, rather than counted as new teaching. Mixed comment-and-reader-text records still need a reader-text judgment. A retained decision is acceptance only after the actual reading.

Complete the ten fields not owned by Stages 1 and 2:

- Reader problem, observable limitation, or engineering decision
- Prerequisites, first use, and first teaching location
- Local relevance and paragraph continuity
- Operating mode and object roles, when relevant
- Representation bridge, when relevant
- Concrete trace or example
- Example setup and conclusion
- Relevant alternatives, common criteria, and selection or scope
- Essential explanation beyond the checklist
- Result that motivates the next section

Use the current packet's exact field names and actual paragraph/line references. For alternatives, include `common problem`, `options`, `relationship`, `criteria`, `selection or scope`, and `verdict: adequate`. A specific `Not applicable: line N; reason: ...` is allowed where it benefits the reader. Essential explanation must include `reader task`, `dependencies checked`, `reasoning chain`, and `unresolved`; it cannot be marked not applicable.

Also answer whether the front matter's promise is true for this group: essential teaching is supplied before its reasoning-dependent use, and optional folds deepen material whose necessary physical meaning and result remain visible. Cite actual examples and any exceptions. The eye reviewer will combine the group findings with the actual book and Part transitions; no reviewer should claim to have read unassigned chapters.

## Prerequisite judgments

The coordinator will supply a current unreviewed concept index. `final-<group>-concept-leads.json` contains neutral old locations and possible current matches, not accepted teaching judgments. Use it only to find passages after the connected reading. Add missing concepts or relationships rather than treating the 57-item candidate catalog as complete. A preview or reference is not automatically teaching.

Save `final-<group>-concept-judgments.json` with reviewed audience assumptions, concepts and aliases, all assigned section IDs, and actual passage-linked teaching/use judgments. Use the exact current concept-index passage ID and a meaningful `[start,end]` text span. Required uses have `need: required`; teaching has `adequacy: adequate` only if it is sufficient. Each relation needs `status: reviewed`, this actual call ID as `review`, and a passage-specific explanation. Teaching sets may combine preceding passages when the explanation is distributed. Preserve the distinction between local formal definitions in folds and the essential visible physical explanation. Sections without a new catalog relation still need a real completeness judgment.

The record schema is defined by the pinned `tools/concept_prerequisites.py`. Older accepted files may illustrate schema but must not supply verdicts for current text. The coordinator will merge the judgments and run the mechanical prerequisite-order check. That check does not prove that the teaching is adequate.

Use actual timestamps for checkpoints every few minutes. Report wall time and time since the previous checkpoint; awake execution is unverified. State token statistics unavailable if not exposed. Keep the work bounded, but report the actual time needed rather than claiming an incomplete review passes.
