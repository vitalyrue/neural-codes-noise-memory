# Current text review record plan

Started 2026-10-29T12:57:41.1710728+02:00. Checkpoint 2026-10-29T12:59:57.7022415+02:00. Model: Sol high as assigned; exact platform build not independently exposed. Wall elapsed at checkpoint: 2m 17s; awake execution unverified. Token stats unavailable.

Read-only investigation of Publisher 0.8.23 review scripts, installed acceptance/work-efficiency/teaching contracts, and current stage artifacts. No manuscript, skill, rule or ledger edits. This file records a plan, not acceptance.

## Decision

Freeze all accepted wording edits and native Vale comments together, then prepare one new packet directory. Preserve the existing baseline and all initial call reports unchanged. A raw unit with a new comment is changed under this validator even if the comment never reaches the reader. Do not retag an old call with the new source hash. Old call reports remain useful evidence of diagnosis and prior calculation; they do not become current acceptance merely because the visible text mostly matches.

Use three NEW independent reviewer contexts for the three disjoint groups. Each first receives neutral rules, audience, current text, exact changed sentences/diff, original sources and needed preceding teaching. Omit earlier verdicts, intended findings and writer defenses from the first input. Have each begin with an open read. Earlier mathematical computation artifacts may be supplied after that read as calculation evidence; verify exact relevant inputs and inspect the calculation rather than rerunning unchanged arithmetic without a reason. Review all current statements in the assigned units, with changed wording and its connections first. New reviewers should identify failures without writing exact replacement prose if they will later accept the fixes.

Keep the three stages as separate sequential calls per group: truth_reasoning, necessity_language, understanding_flow. The flow stage is the first full paragraph-purpose/connection review of this round, so every current paragraph needs an actual decision. It must also review the whole reading path and include the final connected read. Assign one reviewer the cross-group book/Part path, including adjacent actual passages, rather than adding another compulsory whole-book pass.

## Minimum real calls

- With the coordinator's three parallel groups: nine stage calls, followed by one current independent recheck call covering every repaired unit and affected connection. Total ten. Three group recheck calls are an easier parallel alternative, total twelve. The shared recheck may be done by one of the new reviewers only if that reviewer wrote none of the text it accepts; it must read the other groups' affected text too.
- Absolute call-count minimum with one capable new reviewer covering the entire scope: three stage calls plus one later repair recheck, total four. This saves calls but removes the three-group parallelism and is not necessarily faster or cheaper.
- The fourth call is a separate `recheck` run because the validator requires declared repairs to have a later call on the final hash, after the three stages for each assessed unit. A stage3 call cannot also have stage `recheck`.
- If these reviews find a required correction, record it, apply only an authorized fix, freeze again and return to the earliest affected question. Repeat later dependent checks on that connected scope. Do not restart unrelated whole-book reading.

Rotating existing reviewers is semantically permitted for units they did not write, using truthful unit-level writer records. However it does not provide an honest cheap route for this particular current workflow: a reviewer's first included run must be `fresh`; a continuation requires an earlier included run from that reviewer. The old fresh runs have old hashes and can enter the current workflow only through genuine unchanged-unit reuse. All place units are expected to change. Do not relabel an old agent's current continuation as fresh. A fresh new context avoids both this problem and the memory reviewer's global-first-call gap.

## Preserve historical evidence

Keep global-order-stage1.md, all original stage JSON/Markdown, request/result evidence and baseline bytes untouched. Preserve actual IDs, times, hashes, limits and unresolved findings. The global report is a narrow global purpose/order diagnosis, not three completed stages. The memory truth report is correctly a continuation of that fresh global context; do not silently change it to `fresh` during assembly.

Original stage JSON uses `call` plus `units`, not a complete validator workflow artifact. It can be assembled into a new explicitly described wrapper containing the actual run and its actual unit answers, without changing the original artifact or pretending a new review occurred. A reuse binding requires the original artifact to contain that exact run under `workflow.runs` or root `runs`, plus top-level original input_hash and review_contract_hash. Existing `call`/`units` files cannot be cited directly as that wrapper. Avoid this extra assembly when the raw unit is changed anyway.

Only truly unchanged complete units qualify for the built-in reuse path. It compares raw unit text, complete relevant metadata, paragraph hashes/order and local figure bytes. A Part opening comparison serializes the entire corresponding Part record, not merely its opening prose. A change elsewhere in that Part record can therefore invalidate opening reuse. Missing snapshot assets or sidecars also keep reuse pending. Reuse of a few Part openings is optional and likely costs more record work than the brief fresh assessment saves here.

If reuse is used, preserve the exact old run in workflow.runs, and add workflow.reuse with run_id, original_call_path, original_call_sha256, snapshot_root, unit_map, recheck_run_ids. Add unchanged prerequisite units to the map when original answers cite them. A current independent recheck must answer reuse_sources, reuse_rules and reuse_connections for every adopted unit, cite that current unit, and identify original_run_ids. Source equality alone does not establish that the snapshot belonged to the original call or that its teaching answer remains sound. Do not import old open assessments as passing answers.

## Final assembly requirements

Prepare current packets once after the integration freeze using the pinned 0.8.23 script and a new output directory. Its generated inventory is the authority for IDs, counts, full quotations, locations, neighbors, claims and code occurrences. Preserve the current whole-book index and schema_version 2 paragraph record. Do not hand-edit identities or counts to match old reports.

workflow needs writer_ids, exact ordered unit_ids, runs and repairs. Include the coordinator and anyone whose exact proposed prose was adopted among actual writers. If some existing reviewers assess other authors' units, unit_writer_ids must map EVERY current unit to a nonempty subset of declared actual writer IDs, with every declared writer used at least once. Without that map, every reviewer is excluded if present anywhere in writer_ids. New reviewers who write no manuscript avoid this conflict.

Each run needs a distinct actual platform ID or clearly labelled local request ID, reviewer_id, stage, truthful context, timezone-aware started_at/completed_at, current input_hash/review_contract_hash, and nonempty assessments. Each assessment needs unit_id, status pass, unresolved [], and passage-based questions/answers with current source_refs. Stages must finish before the next begins for each unit, and cover every unit EXACTLY ONCE per stage. Historical non-reused calls should remain archived outside the current workflow rather than being inserted as stale or duplicate coverage.

Use IDs from the prepared record. In particular, the existing reviewer shorthand `unit/p3` is not a generated paragraph ID. The generated form is `unit::p3`. An assembler may resolve a genuine shorthand reference to its confirmed generated passage; it must not invent a passage or silently drop a reference.

Every current paragraph must keep its generated text, source location, hash, neighbors and order, plus an actual purpose, connection, decision and reason. The only accepting final decision is retain. A report with revise/move/remove is still an open finding until the resulting source has been reviewed. Copying a previous field mechanically is not a new paragraph judgment.

Current Markdown packet records must also retain all generated unit markers, full paragraph quotations, claim text/line/changed flags, code test occurrence records and content kinds. Complete every required evidence field in the prepared form, including concrete wording and continuity, source-supported claim decisions, structured system/method/essential-explanation checks and the strongest expert objection. A unit with equations, tables, code or figures needs a correctness objection and reasoned disposition. Every claim needs its actual verdict and how checked; code needs an existing test path or reason not run. Each final unit verdict must be Pass only when semantically resolved.

Repairs need affected unit_ids, before_input_hash, current after_input_hash, applied_at, reason, and later recheck_run_ids. The recheck must cover affected connections as well as the changed sentences. Preserve original/repaired phrase and reason in the existing integration record. Record actual source freeze time, not an inferred or future time.

Run the pinned orchestrate_pedagogy_reviews.py with --output-dir <current-packet-dir> --validate-review --json after assembly. It checks current coverage, exact generated records, stage order, declared independence, structured evidence, hashes and repair rechecks. It cannot prove reviewers actually ran, decide whether source claims are true, determine adequate prerequisite teaching, or establish figure meaning. A malformed record failure needs record repair; it is not automatically a request for another semantic book review.

Figure pixel/layout acceptance remains explicitly deferred. Current text acceptance may cover caption/alt claims and figure-dependent explanations while retaining this limit. A clean teaching-record validator cannot clear the figure hold or establish full guide/release acceptance. Do not give the combined quality gate a general whole-guide pass while its figure checks remain pending.

## Sources inspected

- Pinned scripts: C:/dev/NBIS/publisher-releases/0.8.23/skills/course-quality-gate/scripts/orchestrate_pedagogy_reviews.py and pedagogy_review_workflow.py. Installed and pinned workflow-script SHA256 matched at 2026-10-29T12:59:57.7022415+02:00.
- Installed course-quality-gate/SKILL.md and references/prose-and-style-contract.md.
- Installed course-study-guide-builder references/acceptance-contract.md, work-efficiency.md and pedagogy-language-contract.md, especially the review rounds and historical reuse rules.
- This task's PLAN.md, global-order-stage1.md, memory-stage1.json, eye-stage1.json, eye-stage2.json and initial generated paragraph inventory.

No memory lookup was needed for this bounded record investigation. No external web research was needed.

Completed checkpoint: 2026-10-29T13:01:04.3279394+02:00. Measured wall elapsed 3m 23s; time since previous measured checkpoint 1m 07s. Awake execution remains unverified. No system-clock change was observed in the sampled timestamps. Token stats unavailable.
