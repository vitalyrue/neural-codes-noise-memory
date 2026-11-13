# Current task and neutral review brief

Started 2026-10-24T18:54:22.5524387+03:00, Asia/Jerusalem. User: most titles describe topics rather than what the section adds to knowledge; deeper explanations skippable on a first pass may be folded; paragraph order matters; use the Publisher teaching skill. User authorizes these local guide revisions. No new art, source-paper change, public release, or whole-book pixel sweep.

Project C:/dev/clsc/burak-papers/guide. Current BookModel a853f7a996cf5c54f254d458c93442377608dec60fe17e9aaba1fecf28925957. Publisher 0.8.23. Use C:/dev/NBIS/publisher-releases/0.8.23/skills/course-study-guide-builder/SKILL.md and its pedagogy-language-contract.md, structural-preservation-contract.md, concept-prerequisites.md; relevant math/visual/publication contracts where needed. Do not use previous findings or verdicts to anchor the initial assessment.

Audience: actual reading-guide baseline, undergraduate calculus, basic probability, linear algebra; teach neuroscience, stochastic processes, information, filters and random fields as needed. Read the actual 00-reading-guide.md, plan/chapter-plan.yaml, relevant prior teaching and assigned whole chapters. Start with an open-ended read and book/Part/chapter purpose and order; compare a plausible alternative with benefit/cost. Then read section and paragraph order.

Target: headings state what the reader learns or what a model/result/experiment establishes, with necessary limits. A background section need not claim a new scientific discovery. Keep IDs stable. Review each heading separately; no blanket rewriting. Preserve sufficient existing wording. Original mathematics, supporting explanations, source links, typed blocks and all22 images remain available. Do not invent paper findings, amplify inference into causation, or make an asymptotic result exact.

First-pass path: keep motivation, first-use meanings, core mechanisms, assumptions, key equations/results, shortest useful examples, figures and implications visible. Fold only a deeper derivation, alternative check or extension after its result/conditions are taught visibly. Every fold needs a clear title and a dependency argument showing the closed path still works. Do not fold by length alone or hide the needed explanation while leaving an unexplained result. Preserve full step-by-step depth behind folds. No nested folds, no headings inside folds, no image/typed-block references inside folds. Main section IDs and existing figures remain in place unless a specific move earns a reason and is reviewed.

Native fold syntax, already verified in Publisher loader/renderer:

::: {.publisher-clarification-note .publisher-fold-always title="Derivation: specific purpose"}

Optional deeper paragraphs and equations, with all original text retained.

:::

Root will enable publication.renderers.quarto.html_folding.enabled and mark pre-existing typed tables/other eligible blocks html_fold:never to prevent unintended automatic folds. Do not edit shared config yourself.

Parallel work: each author writes only assigned proposed chapter copies under this task folder plus an edit script/decision ledger. Never edit canonical reader files, shared plan/ledger/config or another author's outputs. Root integrates. After drafts are frozen, separate independent truth, wording, then reader-flow calls will cross-review other authors. Initial assessment is not final acceptance.

Required author outputs: proposed/content/chapters/<assigned>.md and .yaml; a reversible exact change list (before/after, ID/locus, reason); title decisions for every heading (old,new,contribution,support,retain/change); fold decisions (visible premise/result/conditions, hidden exact span, later dependent uses and why closed path works); paragraph purpose/order record (actual paragraphs and concrete retain/move/repair reasons, source hashes; no generic boilerplate). Keep all original prose unless a necessary connection repair is individually recorded. Sidecars: update title and section_list titles/summaries to match actual source; do not change old block content. Only root integrates project/plan/terminology.

Use plain words, no em dash or fancy phrasing. Model allocation: GPT-6.1-sol/high for meaning, math qualifications and reading order; root coordinates and performs deterministic integration. Use actual Get-Date checkpoints, root wall elapsed from task start, time since previous checkpoint, awake time unverified. Brief progress each few minutes and final summary. Persist status in this task folder; keep detailed output out of chat. Token stats unavailable unless actual measurements exist. Do not spend time on a full visual sweep or broad unrelated tests.
