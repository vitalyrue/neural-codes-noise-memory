# Vale diagnosis and honest teaching-review records

Started: 2026-10-29T10:26:32Z. Diagnostic checkpoint: 2026-10-29T10:29:22Z. Completed: 2026-10-29T10:30:56Z. Wall-clock elapsed: 4m 24s; time since previous checkpoint: 1m 34s; awake execution time is unverified. No manuscript, rule, profile, auditor, or generated packet was changed by this investigation. Token stats unavailable.

## What makes the Vale gate fail

`verification/vale-report-guide.json` contains 2,211 native Vale alerts from 16 source files: 660 errors, 209 warnings, and 1,342 suggestions. `audit_vale_prose.py:237` passes only when error count is zero. The category counters are not additional failure conditions. The separate 1,828 built-in advisory findings do not cause this failure.

The saved report records Vale 3.24.0 with native footnote handling. Its source hash (`fd656539524b93006d1c5c10f5c637e20cc4ee88ee407ba3aa4159fbc34592e9`) and configuration hash (`364960c862b5d6b3ec302245455a460a68def92596c8da9935ea860d83e389b0`) matched the actual current source/configuration during this diagnosis. The installed auditor, packet orchestrator, and workflow validator are byte-identical to their Publisher 0.8.23 copies.

The largest error groups are EmDashUsage 201, SemicolonUsage 119, FormalTransitions 105, VerbTricolon 28, AnthropomorphicCognition 27, CataphoricForecasting 23, ContrastiveFormulas 17, and FillerIntensifier 13. These sum to 533; the remaining rules produce 127 errors. No rule change is needed to explain the failure.

## Counts describe contexts, not 2,211 proven writing defects

Counts below use the native alert's start line and column and identify fenced code, display math, inline code/math, link targets, and bibliography footnotes from the source. They do not decide semantic suitability.

| Source context of alert start | Total | Error | Warning | Suggestion |
| --- | ---: | ---: | ---: | ---: |
| Ordinary prose, headings, table prose | 1,619 | 462 | 203 | 954 |
| Bibliographic footnote lines | 590 | 198 | 6 | 386 |
| Display math | 2 | 0 | 0 | 2 |
| Fenced code, inline code/math, link targets, attribute starts | 0 | 0 | 0 | 0 |
| Total | 2,211 | 660 | 209 | 1,342 |

The 590 alerts occur on 98 footnote lines. Several footnotes mix reference details, source locators, and explanatory claims; they cannot all be dismissed as bibliography false positives. Reference lists outside footnotes are included in the ordinary-text row. The two math alerts are the same semicolon argument separator, reported by Google.Semicolons and Microsoft.Semicolon in `04-eye-drift.md:84`: `f_a(t_j;k,r,m,...)`. It is mathematical notation, not sentence punctuation.

There are 1,671 distinct `(file, line, span, match)` locations when the rule ID is excluded. This is useful for grouping simultaneous rules, not a claim that each grouped location has only one issue. Examples of duplicate rule families are Google/Microsoft semicolons (252 each), passive voice (203 each), and first-person plural (52 each).

39 error matches contain exposed Pandoc attributes or math placeholder characters: 35 SemicolonUsage, 2 VerbTricolon, 1 EmptyPaddingStacked, and 1 NounString. These overlap the table above and are not a separate additive bucket. For most, the semicolon is real even though the reported clause includes markup. Their output must be checked against source and reader-visible text. At least the EmptyPaddingStacked and NounString examples below are parsing/POS artifacts. There is no honest exact count of genuine prose defects without actual passage review.

## Representative high-severity alerts

| Source | Rule and match | Assessment for routing |
| --- | --- | --- |
| `00-reading-guide.md:15` and many reference locators | EmDashUsage: `–` | All 201 matches are U+2013 en dashes, zero em dashes. Rule YAML explicitly bans both. 154 occur on footnote lines; remaining 47 are outside footnotes. Range punctuation, rather than sentence asides, explains the samples. Judge each range use; do not call the rule broken merely because its message says em dash. |
| `02-memory-dynamics.md:132` | NegatedObject: `left zero eigenvector` | Exact mathematical term; automatic replacement changes meaning. The same phrase is flagged at `glossary.md:52`. |
| `01-foundations.md:127` | NegatedObject: `gives zero covariance` | A quantitative result, not a stilted grammatical absence. Verify the surrounding condition, retain exact meaning. |
| `02b-memory-long-delays.md:74`, `glossary.md:68` | FigurativeFires: `both firing`, `that fires` | Actual neuronal firing. The software-metaphor rule does not understand this domain. |
| `02b-memory-long-delays.md:127`, `04-eye-drift.md:89`, `05c-place-tests.md:269` | Google.Units: `1B`, `1d`, `1B` | Figure panel labels, not numerical quantities missing unit spacing. |
| `06-synthesis.md:128,130`, `references.md:23,31` | Vale.Repetition: `O. O`, `M. M` | Author initials in reference entries; check exact names rather than delete an initial. |
| `00-reading-guide.md:27` | EmptyPaddingStacked: `particular locations.]{.definition-explanation} [` | Parser/POS artifact extends through Pandoc attribute syntax. Read the actual sentence before deciding whether “particular” matters. |
| `01b-persistence.md:114` | NounString: `angular diffusion coefficient ******** degrees` | Source is `angular diffusion coefficient $D=0.02$ degrees squared per second`. Math masking joins unrelated noun fragments. |
| `00-reading-guide.md:3` | VerbTricolon: `...memory, eye control, and navigation` | Match calls three noun phrases “parallel verbs.” Three real research topics are not automatically a defect. |
| `00-reading-guide.md:7` | SemicolonUsage: `; a moving animal must keep track...` | A real prose semicolon. Existing stricter error rule remains enforceable; a reviewer should decide an accurate sentence repair. |
| `06-synthesis.md:54` | HeadingColons: `: o` | A genuine style question about text after a heading colon; inspect the heading. |

## Supported narrow exception mechanism

The current auditor has **no** flag, ledger loader, or disposition field that accepts a reviewed native alert. `--from-report` checks exact hashes and reuses raw alerts unchanged; editing/deleting saved alerts would falsify the lint record. The pedagogy packet's expert-objection `disposition` concerns the teaching review and does not suppress Vale.

Vale itself supports rule-specific comment regions. This was tested against installed Vale 3.24.0 through stdin using the actual guide configuration and a synthetic sample; no source file was written:

```markdown
<!-- vale ai-tells.NegatedObject = NO -->

A left zero eigenvector identifies the direction.

<!-- vale ai-tells.NegatedObject = YES -->

Therefore, the result follows.

A left zero eigenvector identifies the direction.
```

The first NegatedObject alert disappeared; the later identical phrase still fired, and FormalTransitions still flagged “Therefore.” This establishes a working bounded mechanism. It does not approve any real exception. Keep a region as small as the parser permits, suppress only the specific rule, and restore it immediately. Do not use blanket `vale off` or disable a category, file, citation collection, or shared profile to make the report pass. Confirm an exception does not disturb Markdown/Pandoc rendering, particularly a single-line footnote. [Vale markup/scopes documentation](https://docs.vale.sh/topics/scopes) describes native parsing and rule scopes; the local executable test is the direct evidence for this installed version's comment behavior.

For each independently judged exception, keep a small JSON record outside the manuscript containing: alert identity `(source path, line, span, Check, Match)`, source-file SHA256, report/config hashes, exact source quotation, reader-visible phrase if syntax caused the match, decision (`repair`, `retain_scientific_term`, `retain_citation_convention`, `parser_false_positive`, `pending`), plain reason, actual reviewer/call ID, and time. After approval and insertion, record the exact comment region and new report hash. A ledger alone cannot clear the current gate. Building an auditor feature to consume such a ledger is a separate tooling change requiring design and tests, not a hidden local workaround.

## Practical route through 2,211 flags

1. Keep the original native report unchanged. Group alerts by exact source location and show all applicable rules together. Review genuine prose by paragraph, not one synonym per alert. Start with the 660 blocking errors, especially the few high-volume families.
2. Route scientific terms, citation conventions, and math/markup artifacts to independent judgments. Preserve mathematical symbols, author names, quotation text, and technical meanings. Accepted exceptions can use the bounded native mechanism above; pending cases remain visible.
3. Review actual semicolon clauses and word choice in their surrounding explanation. Where a repair helps, recast the passage while preserving the actor, condition, consequence, and limitation. Do not alter every “therefore,” passive, or three-part list simply because a style package dislikes it.
4. Review suggestions/warnings while completing the full paragraph review. They are signals rather than 1,551 additional blocking errors. Check unflagged wording and missing explanations too.
5. Record repairs, regenerate the current packets after source changes, perform actual independent stage/recheck calls, and rerun native Vale once the integrated source is stable. Do not repeatedly rerun all checks after each small wording repair. Keep semantic acceptance separate from the lint outcome.

## Minimal honest teaching-review records

Current target: `verification/teaching-alignment-20261029/pedagogy-initial`. It has 968 paragraphs, 76 units, 3 packets, zero workflow runs, and no recorded review. Source/review hash is `81f7e2f3f75c1d85db5116fb870c668bdebcfc94c180926ad1673e33b6f06e76` / `593934f3af51c49175417df3e4263df20a0835575d099bad4f0070163b4a17dc`. These hashes intentionally differ from the Vale hash scheme.

Keep these three connected forms of evidence:

1. **Paragraph decisions:** retain generated ID, source text/hash and neighbors. Fill `review.purpose`, `connection`, `decision` (`retain`, `revise`, `move`, `remove`), and `reason` from actual reading. Assess every paragraph, including list/callout prose; read intervening equations/tables/figures. A revise/move/remove proposal stays unresolved until changed source is reviewed. Do not stamp the same generic reason onto 968 records.
2. **Packet unit evidence:** preserve generated unit markers, claims, code checks, quotations, and all required fields. Cite exact line/paragraph and give the reader-based explanation. Structured fields require their actual components: system setup; alternatives/common problem/criteria; essential dependency chain; expert objection with kind/target/disposition/reason. Units with code, table, equation, or figure require a correctness objection. Claim verdicts are `true as written`, `condition stated`, `fixed`, or `not a claim`, plus how checked. Every code listing needs an actual executable test path or an honest non-run reason. Concrete wording requires phrase, plain paraphrase, actor, object, action, condition/consequence, verdict, replacement or retention reason. A generic “clear/pass” is insufficient.
3. **Actual calls:** populate `workflow.writer_ids` with real writers, including explicit unknown legacy writer where necessary. Save the actual reviewer result before assembly. Each `workflow.runs` entry needs distinct real platform/local request ID, independent reviewer identity, stage, fresh/continuation context, timezone-aware start/end, current source/rule hashes, and per-unit questions, supported answers, current unit/paragraph refs, verdict, and unresolved questions. Record `pass` only when resolved. A reviewer who wrote a unit cannot review that unit; `unit_writer_ids` can declare exact actual authorship when needed.

Stages must be separate calls in order for each unit: `truth_reasoning`, `necessity_language`, `understanding_flow`. A fresh independent reviewer can continue into later calls; changing the writer's role label is insufficient. Each stage must cover every current unit exactly once in the assembled record. Parallel reviewers can own disjoint units, preserving per-unit stage order. Save actual call IDs/times while each call happens, rather than constructing them after the fact.

A source repair record needs affected current units and connections, before/after input hashes, actual applied time, reason, and later current-source `recheck_run_ids`. Avoid editing until the initial diagnosis is saved. On regeneration, map unchanged paragraphs by exact source and review actual changed connections; never retag an old run with a new hash.

Historical `teaching-compliance-20261025` evidence was inspected only for structure: `actual-review-calls.json` links call IDs and timestamps; original and final review JSONs preserve real results; `assemble_workflow.py` assembles reviewer artifacts; the old paragraph report contains 824 paragraphs and 15 runs. These are not current acceptance. Historical reuse additionally requires original call artifact/hash, original source snapshot/sidecars/visual bytes, unchanged-unit mapping, and actual current `reuse_sources`, `reuse_rules`, and `reuse_connections` recheck answers. Starting current calls is simpler if exact original evidence is missing. Do not copy prior verdicts or invent adoption answers.

## Pinned commands and code pointers

Use `C:/dev/NBIS/publisher-releases/0.8.23/skills/course-quality-gate/scripts/` for the following scripts. Commands are advice; this investigation did not regenerate packets or rerun the whole guide:

```powershell
python <scripts>/audit_vale_prose.py C:/dev/clsc/burak-papers/guide --help
python <scripts>/audit_vale_prose.py C:/dev/clsc/burak-papers/guide
python <scripts>/orchestrate_pedagogy_reviews.py C:/dev/clsc/burak-papers/guide --output-dir <new-current-packet-dir>
python <scripts>/orchestrate_pedagogy_reviews.py C:/dev/clsc/burak-papers/guide --output-dir <completed-current-packet-dir> --validate-review
```

Relevant implementation: `audit_vale_prose.py:96` freshness, `:153` native execution, `:188` counts, `:237` gate condition; `orchestrate_pedagogy_reviews.py:632` packet evidence instructions, `:841` evidence checks, `:1267` paragraph validation, `:1306` full packet validation, `:1519` preparation; `pedagogy_review_workflow.py:42` calls/authorship/stage/repair validation. Validator success checks record coverage and freshness, not truth or whether the declared agent actually ran.

Read contracts: `C:/Users/vital/.codex/skills/course-quality-gate/SKILL.md` and `references/prose-and-style-contract.md`. Their instruction to protect code/math/links/quotes and avoid automatic synonyms governs triage. Existing configured error severities remain unchanged.
