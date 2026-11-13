# Pedagogy Review Packet: Front Matter and Appendices

This packet covers front matter and appendices. Short reference pages may use a shorter teaching form only when their linked teaching location has already established the reader's decision.

A reviewer must cite exact passages before marking a requirement as satisfied.
Use a line or paragraph number and a short explanation. Use `Not applicable: <reader-benefit reason>` only when the requirement truly does not apply.

## ch:READING-GUIDE - Reading path and paper copies

Source file: `content/chapters/00-reading-guide.md`

Purpose: Neural circuits must represent quantities such as location and eye position while individual spikes fluctuate. This guide develops the mathematics and experimental reasoning behind three papers on that problem. Its aim is to make the central calculations reconstructible, including the assumptions that make each step valid.

Prerequisites: None recorded

Sidecar sections: Starting knowledge and reading paths, The original papers, What the derivations and examples establish

Blocks: 0 figure(s), 0 equation(s), 0 code block(s)

Result labels: No Answer/Conclusion/Feedback label detected

<!-- pedagogy-unit: content/chapters/00-reading-guide.md::ch:READING-GUIDE -->

### Chapter opening

Location: line 1, anchor `ch:READING-GUIDE`

First content kind: `prose`

Opening passage line: 3
Closing passage line: 3

Paragraphs in source order (complete `PARAGRAPH_REVIEW.json`):

<!-- pedagogy-paragraph: p3 sha256 cadac9e02e4f9f3a03ae3d447b17dde510bd18d5e33e0e370f622e4e50b6fd7c -->
p3, lines 3-3; prose; priority: unchanged; previous: none; next: p7

> Neural circuits must represent quantities such as location and eye position while individual spikes fluctuate. This guide develops the mathematics and experimental reasoning behind three papers on that problem. Its aim is to make the central calculations reconstructible, including the assumptions that make each step valid.


Claim-bearing content: none

Claims to check:

- Claim c1, line 3: "Neural circuits must represent quantities such as location and eye position while individual spikes fluctuate." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]

Required evidence:

- Reader problem, observable limitation, or engineering decision: [cite an exact passage with a line or paragraph number, or write Not applicable: reader-benefit reason]
- Prerequisites, first use, and first teaching location: [cite an exact passage with a line or paragraph number, or write Not applicable: reader-benefit reason]
- Definition and emphasis: [cite an exact passage with a line or paragraph number, or write Not applicable: reader-benefit reason]
- Concrete wording and sentence contribution: phrase, plain-language paraphrase, actor, object, action or state change, condition or consequence, verdict, and replacement or retention reason: [cite an exact passage with a line or paragraph number, or write Not applicable: reader-benefit reason]
- Local relevance and paragraph continuity: [cite an exact passage with a line or paragraph number, or write Not applicable: reader-benefit reason]
- Operating mode and object roles, when relevant: [cite an exact passage with a line or paragraph number, or write Not applicable: reader-benefit reason]
- System setup and component relationships: [cite an exact passage with a line or paragraph number, or write Not applicable: reader-benefit reason]
- Representation bridge, when relevant: [cite an exact passage with a line or paragraph number, or write Not applicable: reader-benefit reason]
- Mechanism, calculation, or state change: [cite an exact passage with a line or paragraph number, or write Not applicable: reader-benefit reason]
- Concrete trace or example: [cite an exact passage with a line or paragraph number, or write Not applicable: reader-benefit reason]
- Example setup and conclusion: [cite an exact passage with a line or paragraph number, or write Not applicable: reader-benefit reason]
- Assumptions, limits, trade-offs, or failure modes: [cite an exact passage with a line or paragraph number, or write Not applicable: reader-benefit reason]
- Relevant alternatives, common criteria, and selection or scope: [cite an exact passage with a line or paragraph number, or write Not applicable: reader-benefit reason]
- Essential explanation beyond the checklist: [cite an exact passage with a line or paragraph number, or write Not applicable: reader-benefit reason]
- Result that motivates the next section: [cite an exact passage with a line or paragraph number, or write Not applicable: reader-benefit reason]
- Expert objection: [cite an exact passage with a line or paragraph number, or write Not applicable: reader-benefit reason]
- Verdict: Pending reviewer assessment

For the concrete-wording field, use this form: line N; phrase: ...; paraphrase: ...; actor: ...; object: ...; action: ...; condition or consequence: ...; verdict: retain, revise, or delete; replacement or retention reason: ....
Context review must explain the literal meaning, prerequisites, analogy limits when relevant, and reason for appearing here. If no correction is needed, give a specific retention reason; lint success is not evidence.
For System setup and component relationships, cite the passage and fill: setting: ...; roles: ...; objects and flow: ...; assumptions: ...; verdict: ....
For Relevant alternatives, common criteria, and selection or scope, cite the passage and fill: common problem: ...; options: ...; relationship: ...; criteria: ...; selection or scope: ...; verdict: ....
For Essential explanation beyond the checklist, cite the passage and fill: reader task: ...; dependencies checked: ...; reasoning chain: ...; unresolved: ....
For Expert objection, cite the passage and fill: objection: ...; kind: ...; target: ...; disposition: ...; reason: ....
For system setup and alternatives, an adequate review uses verdict: adequate. Where inapplicable, use Not applicable: line N; reason: <specific reader-benefit reason>.
Expert objection cannot be marked Not applicable. Write the strongest correction a domain expert would make to this unit's text or figures; set kind to correctness or wording; name its target passage or figure label; set disposition to fixed or does not apply; give the reason. An objection of none is not a review. The strongest correction is the one that would change what a reader believes or does. Aim first at what the unit claims: a promise word such as always, once, ensures or remains that is false or needs a condition; a named method described wrongly; code that does not do what the text says; a table cell; a diagnostic sequence that skips a stage; a verb without an actor; a label naming something other than what is drawn; a figure that disagrees with the text or another figure; and example content found in neither the chapter nor its sources. A unit whose claim-bearing content includes code, a table, an equation, or a figure needs a correctness objection; a wording objection alone does not count there.
Claims to check lists the unit's statements most likely to make checkable claims: every table row and every figure or table caption with its alt text, and each sentence with a promise word, a quantity or calculation, code font, a citation, or a section or figure reference. Footnote definitions are left to the citation checks. When packets compare with a revision, every changed statement is listed first and marked changed. For each claim, set verdict to true as written, condition stated, fixed, or not a claim, and after checked: say how it was checked, such as the code test, the recomputation, or the source and its location. The list is a floor, not the extent of the review.
For each code listing, write test: followed by the path, relative to the guide, of a test that runs it on the inputs the text makes claims about, or not run: followed by the reason and how its claims were checked instead.
Essential explanation cannot be marked Not applicable. Trace the reader's task and its dependencies, including gaps not covered by other fields. Record unresolved: none only after resolving essential gaps; otherwise describe them and keep the unit verdict open. A complete checklist is not proof of complete teaching.

<!-- pedagogy-unit: content/chapters/00-reading-guide.md::sec:READING-START -->

### Starting knowledge and reading paths

Location: line 5, anchor `sec:READING-START`

First content kind: `prose`

Opening passage line: 7
Closing passage line: 9

Paragraphs in source order (complete `PARAGRAPH_REVIEW.json`):

<!-- pedagogy-paragraph: p7 sha256 ac5e4980fddbecf0a69600a043a88c50fee29ea85acee03384c970a730f92d51 -->
p7, lines 7-7; prose; priority: unchanged; previous: p3; next: p9

> The guide assumes undergraduate calculus, basic probability, and linear algebra. Neuroscience terms and the required stochastic-process, information, filtering, and random-field ideas are taught where needed. The first chapter establishes spikes, population activity, fixed points, covariance, and diffusion. Chapters 2 and 3 derive the persistent-activity model and its information bound. Chapter 4 applies the dynamical ideas to eye drift. Chapter 5 develops spatial Gaussian processes and place-field geometry. Chapter 6 brings the results together and compares related work.

<!-- pedagogy-paragraph: p9 sha256 e2131c56370e84ead1eb57acaf23defd78c25c5b3c363946122169d4083c3b23 -->
p9, lines 9-9; prose; priority: unchanged; previous: p7; next: p13

> For the memory and eye papers, follow chapters 1 through 4 in order. For place fields, the relevant starting path is chapter 1 followed by chapter 5; its Gaussian-process calculation does not require every readout result in chapter 3. The Glossary gives short definitions for lookup after their first explanation. The References section gives full source details. The original paper figures are discussed by number and can be inspected in the linked PDFs.


Claim-bearing content: none

Claims to check:

- Claim c1, line 7: "Chapter 4 applies the dynamical ideas to eye drift." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c2, line 7: "Chapter 5 develops spatial Gaussian processes and place-field geometry." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c3, line 7: "Chapter 6 brings the results together and compares related work." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c4, line 9: "For place fields, the relevant starting path is chapter 1 followed by chapter 5; its Gaussian-process calculation does not require every readout result in chapter 3." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]

Required evidence:

- Reader problem, observable limitation, or engineering decision: [cite an exact passage with a line or paragraph number, or write Not applicable: reader-benefit reason]
- Prerequisites, first use, and first teaching location: [cite an exact passage with a line or paragraph number, or write Not applicable: reader-benefit reason]
- Definition and emphasis: [cite an exact passage with a line or paragraph number, or write Not applicable: reader-benefit reason]
- Concrete wording and sentence contribution: phrase, plain-language paraphrase, actor, object, action or state change, condition or consequence, verdict, and replacement or retention reason: [cite an exact passage with a line or paragraph number, or write Not applicable: reader-benefit reason]
- Local relevance and paragraph continuity: [cite an exact passage with a line or paragraph number, or write Not applicable: reader-benefit reason]
- Operating mode and object roles, when relevant: [cite an exact passage with a line or paragraph number, or write Not applicable: reader-benefit reason]
- System setup and component relationships: [cite an exact passage with a line or paragraph number, or write Not applicable: reader-benefit reason]
- Representation bridge, when relevant: [cite an exact passage with a line or paragraph number, or write Not applicable: reader-benefit reason]
- Mechanism, calculation, or state change: [cite an exact passage with a line or paragraph number, or write Not applicable: reader-benefit reason]
- Concrete trace or example: [cite an exact passage with a line or paragraph number, or write Not applicable: reader-benefit reason]
- Example setup and conclusion: [cite an exact passage with a line or paragraph number, or write Not applicable: reader-benefit reason]
- Assumptions, limits, trade-offs, or failure modes: [cite an exact passage with a line or paragraph number, or write Not applicable: reader-benefit reason]
- Relevant alternatives, common criteria, and selection or scope: [cite an exact passage with a line or paragraph number, or write Not applicable: reader-benefit reason]
- Essential explanation beyond the checklist: [cite an exact passage with a line or paragraph number, or write Not applicable: reader-benefit reason]
- Result that motivates the next section: [cite an exact passage with a line or paragraph number, or write Not applicable: reader-benefit reason]
- Expert objection: [cite an exact passage with a line or paragraph number, or write Not applicable: reader-benefit reason]
- Verdict: Pending reviewer assessment

For the concrete-wording field, use this form: line N; phrase: ...; paraphrase: ...; actor: ...; object: ...; action: ...; condition or consequence: ...; verdict: retain, revise, or delete; replacement or retention reason: ....
Context review must explain the literal meaning, prerequisites, analogy limits when relevant, and reason for appearing here. If no correction is needed, give a specific retention reason; lint success is not evidence.
For System setup and component relationships, cite the passage and fill: setting: ...; roles: ...; objects and flow: ...; assumptions: ...; verdict: ....
For Relevant alternatives, common criteria, and selection or scope, cite the passage and fill: common problem: ...; options: ...; relationship: ...; criteria: ...; selection or scope: ...; verdict: ....
For Essential explanation beyond the checklist, cite the passage and fill: reader task: ...; dependencies checked: ...; reasoning chain: ...; unresolved: ....
For Expert objection, cite the passage and fill: objection: ...; kind: ...; target: ...; disposition: ...; reason: ....
For system setup and alternatives, an adequate review uses verdict: adequate. Where inapplicable, use Not applicable: line N; reason: <specific reader-benefit reason>.
Expert objection cannot be marked Not applicable. Write the strongest correction a domain expert would make to this unit's text or figures; set kind to correctness or wording; name its target passage or figure label; set disposition to fixed or does not apply; give the reason. An objection of none is not a review. The strongest correction is the one that would change what a reader believes or does. Aim first at what the unit claims: a promise word such as always, once, ensures or remains that is false or needs a condition; a named method described wrongly; code that does not do what the text says; a table cell; a diagnostic sequence that skips a stage; a verb without an actor; a label naming something other than what is drawn; a figure that disagrees with the text or another figure; and example content found in neither the chapter nor its sources. A unit whose claim-bearing content includes code, a table, an equation, or a figure needs a correctness objection; a wording objection alone does not count there.
Claims to check lists the unit's statements most likely to make checkable claims: every table row and every figure or table caption with its alt text, and each sentence with a promise word, a quantity or calculation, code font, a citation, or a section or figure reference. Footnote definitions are left to the citation checks. When packets compare with a revision, every changed statement is listed first and marked changed. For each claim, set verdict to true as written, condition stated, fixed, or not a claim, and after checked: say how it was checked, such as the code test, the recomputation, or the source and its location. The list is a floor, not the extent of the review.
For each code listing, write test: followed by the path, relative to the guide, of a test that runs it on the inputs the text makes claims about, or not run: followed by the reason and how its claims were checked instead.
Essential explanation cannot be marked Not applicable. Trace the reader's task and its dependencies, including gaps not covered by other fields. Record unresolved: none only after resolving essential gaps; otherwise describe them and keep the unit verdict open. A complete checklist is not proof of complete teaching.

<!-- pedagogy-unit: content/chapters/00-reading-guide.md::sec:READING-PAPERS -->

### The original papers

Location: line 11, anchor `sec:READING-PAPERS`

First content kind: `prose`

Opening passage line: 13
Closing passage line: 19

Paragraphs in source order (complete `PARAGRAPH_REVIEW.json`):

<!-- pedagogy-paragraph: p13 sha256 2acb2a0d0b50d9774bd90f9e061cdc197f64556636feeb643c84175277b9a73d -->
p13, lines 13-13; prose; priority: unchanged; previous: p9; next: p15

> The copies are the published versions. Supporting information is linked separately.

<!-- pedagogy-paragraph: p15 sha256 5c1400cf7189b43399a8bae5d7bd14b2f13f734fd84e441d75af45953db1260b -->
p15, lines 15-15; list_item; priority: unchanged; previous: p13; next: p16

> **Burak and Fiete (2012):** [Paper PDF](../papers/burak-fiete-2012-persistent-activity.pdf) and [20-page supporting information PDF](../papers/burak-fiete-2012-persistent-activity-si.pdf). *Fundamental limits on persistent activity in networks of noisy neurons*. PNAS, 109(43), 17645–17650. [Published DOI](https://doi.org/10.1073/pnas.1117386109). The local main PDF uses the six-page Early Edition layout, so PDF page locators run from 1 to 6.

<!-- pedagogy-paragraph: p16 sha256 97b7cb44540829c1477760d342a1bde9778edfd0a73c427829330b418a449920 -->
p16, lines 16-16; list_item; priority: unchanged; previous: p15; next: p17

> **Ben-Shushan, Shaham, Joshua, and Burak (2022):** [Paper PDF](../papers/ben-shushan-2022-fixational-drift.pdf), [supplementary notes and figures PDF](../papers/ben-shushan-2022-supplement-1.pdf), and [open peer review PDF](../papers/ben-shushan-2022-supplement-2.pdf). *Fixational drift is driven by diffusive dynamics in central neural circuitry*. Nature Communications, 13, 1697. [Published DOI](https://doi.org/10.1038/s41467-022-29201-y). Ben-Shushan and Shaham contributed equally.

<!-- pedagogy-paragraph: p17 sha256 968b6545e1321cef300a98a9c4e4f457735a720837b2f439b4cd887b6bd1cab7 -->
p17, lines 17-17; list_item; priority: unchanged; previous: p16; next: p19

> **Mainali, Azeredo da Silveira, and Burak (2025):** [Paper and STAR Methods PDF](../papers/mainali-2025-universal-statistics.pdf) and [supplementary figures and Methods S1–S4 PDF](../papers/mainali-2025-supplement.pdf). *Universal statistics of hippocampal place fields across species and dimensionalities*. Neuron, 113(7), 1110–1120.e3. [Published DOI](https://doi.org/10.1016/j.neuron.2025.01.017). The main PDF has a cover before the article; guide citations distinguish printed and PDF page numbers when needed.

<!-- pedagogy-paragraph: p19 sha256 fe5d7ef4e9edc5abfe0fc3fc7e871a23f6bfe9742e9aabd47cdd5b25aa8400ae -->
p19, lines 19-19; prose; priority: unchanged; previous: p17; next: p23

> These links open PDF files. The supporting-information copies preserve their original formulas. Several printed intermediate equations require care; the guide identifies apparent inconsistencies beside the affected calculations and follows an explicitly shown derivation. Such observations are independent mathematical checks, not author-confirmed corrections.


Claim-bearing content: none

Claims to check:

- Claim c1, line 15: "**Burak and Fiete (2012):** [Paper PDF](../papers/burak-fiete-2012-persistent-activity.pdf) and [20-page supporting information PDF](../papers/burak-fiete-2012-persistent-activity-si.pdf)." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c2, line 15: "[Published DOI](https://doi.org/10.1073/pnas.1117386109)." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c3, line 16: "**Ben-Shushan, Shaham, Joshua, and Burak (2022):** [Paper PDF](../papers/ben-shushan-2022-fixational-drift.pdf), [supplementary notes and figures PDF](../papers/ben-shushan-2022-supplement-1.pdf), and [open peer review PDF](../papers/ben-shushan-2022-supplement-2.pdf)." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c4, line 16: "[Published DOI](https://doi.org/10.1038/s41467-022-29201-y)." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c5, line 17: "**Mainali, Azeredo da Silveira, and Burak (2025):** [Paper and STAR Methods PDF](../papers/mainali-2025-universal-statistics.pdf) and [supplementary figures and Methods S1–S4 PDF](../papers/mainali-2025-supplement.pdf)." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c6, line 17: "[Published DOI](https://doi.org/10.1016/j.neuron.2025.01.017)." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]

Required evidence:

- Reader problem, observable limitation, or engineering decision: [cite an exact passage with a line or paragraph number, or write Not applicable: reader-benefit reason]
- Prerequisites, first use, and first teaching location: [cite an exact passage with a line or paragraph number, or write Not applicable: reader-benefit reason]
- Definition and emphasis: [cite an exact passage with a line or paragraph number, or write Not applicable: reader-benefit reason]
- Concrete wording and sentence contribution: phrase, plain-language paraphrase, actor, object, action or state change, condition or consequence, verdict, and replacement or retention reason: [cite an exact passage with a line or paragraph number, or write Not applicable: reader-benefit reason]
- Local relevance and paragraph continuity: [cite an exact passage with a line or paragraph number, or write Not applicable: reader-benefit reason]
- Operating mode and object roles, when relevant: [cite an exact passage with a line or paragraph number, or write Not applicable: reader-benefit reason]
- System setup and component relationships: [cite an exact passage with a line or paragraph number, or write Not applicable: reader-benefit reason]
- Representation bridge, when relevant: [cite an exact passage with a line or paragraph number, or write Not applicable: reader-benefit reason]
- Mechanism, calculation, or state change: [cite an exact passage with a line or paragraph number, or write Not applicable: reader-benefit reason]
- Concrete trace or example: [cite an exact passage with a line or paragraph number, or write Not applicable: reader-benefit reason]
- Example setup and conclusion: [cite an exact passage with a line or paragraph number, or write Not applicable: reader-benefit reason]
- Assumptions, limits, trade-offs, or failure modes: [cite an exact passage with a line or paragraph number, or write Not applicable: reader-benefit reason]
- Relevant alternatives, common criteria, and selection or scope: [cite an exact passage with a line or paragraph number, or write Not applicable: reader-benefit reason]
- Essential explanation beyond the checklist: [cite an exact passage with a line or paragraph number, or write Not applicable: reader-benefit reason]
- Result that motivates the next section: [cite an exact passage with a line or paragraph number, or write Not applicable: reader-benefit reason]
- Expert objection: [cite an exact passage with a line or paragraph number, or write Not applicable: reader-benefit reason]
- Verdict: Pending reviewer assessment

For the concrete-wording field, use this form: line N; phrase: ...; paraphrase: ...; actor: ...; object: ...; action: ...; condition or consequence: ...; verdict: retain, revise, or delete; replacement or retention reason: ....
Context review must explain the literal meaning, prerequisites, analogy limits when relevant, and reason for appearing here. If no correction is needed, give a specific retention reason; lint success is not evidence.
For System setup and component relationships, cite the passage and fill: setting: ...; roles: ...; objects and flow: ...; assumptions: ...; verdict: ....
For Relevant alternatives, common criteria, and selection or scope, cite the passage and fill: common problem: ...; options: ...; relationship: ...; criteria: ...; selection or scope: ...; verdict: ....
For Essential explanation beyond the checklist, cite the passage and fill: reader task: ...; dependencies checked: ...; reasoning chain: ...; unresolved: ....
For Expert objection, cite the passage and fill: objection: ...; kind: ...; target: ...; disposition: ...; reason: ....
For system setup and alternatives, an adequate review uses verdict: adequate. Where inapplicable, use Not applicable: line N; reason: <specific reader-benefit reason>.
Expert objection cannot be marked Not applicable. Write the strongest correction a domain expert would make to this unit's text or figures; set kind to correctness or wording; name its target passage or figure label; set disposition to fixed or does not apply; give the reason. An objection of none is not a review. The strongest correction is the one that would change what a reader believes or does. Aim first at what the unit claims: a promise word such as always, once, ensures or remains that is false or needs a condition; a named method described wrongly; code that does not do what the text says; a table cell; a diagnostic sequence that skips a stage; a verb without an actor; a label naming something other than what is drawn; a figure that disagrees with the text or another figure; and example content found in neither the chapter nor its sources. A unit whose claim-bearing content includes code, a table, an equation, or a figure needs a correctness objection; a wording objection alone does not count there.
Claims to check lists the unit's statements most likely to make checkable claims: every table row and every figure or table caption with its alt text, and each sentence with a promise word, a quantity or calculation, code font, a citation, or a section or figure reference. Footnote definitions are left to the citation checks. When packets compare with a revision, every changed statement is listed first and marked changed. For each claim, set verdict to true as written, condition stated, fixed, or not a claim, and after checked: say how it was checked, such as the code test, the recomputation, or the source and its location. The list is a floor, not the extent of the review.
For each code listing, write test: followed by the path, relative to the guide, of a test that runs it on the inputs the text makes claims about, or not run: followed by the reason and how its claims were checked instead.
Essential explanation cannot be marked Not applicable. Trace the reader's task and its dependencies, including gaps not covered by other fields. Record unresolved: none only after resolving essential gaps; otherwise describe them and keep the unit verdict open. A complete checklist is not proof of complete teaching.

<!-- pedagogy-unit: content/chapters/00-reading-guide.md::sec:READING-SCOPE -->

### What the derivations and examples establish

Location: line 21, anchor `sec:READING-SCOPE`

First content kind: `prose`

Opening passage line: 23
Closing passage line: 27

Paragraphs in source order (complete `PARAGRAPH_REVIEW.json`):

<!-- pedagogy-paragraph: p23 sha256 0d3bd45e942b8a704d7092ff23c84550312fc307e97a4b9f414f55deef9343f7 -->
p23, lines 23-23; prose; priority: unchanged; previous: p19; next: p25

> The central theory is derived step by step. Examples chosen for the guide expose a distinction such as independent versus shared fluctuations, optimal versus incomplete readout, or exact crossing counts versus a rare-excursion approximation. Their numbers are checked separately from the published experimental measurements. A teaching reconstruction is labeled when its simplified model differs from the paper's full model.

<!-- pedagogy-paragraph: p25 sha256 04b64ec70930c743b2d99c568186ebe1290f5f3677019c541b47a184a18d28eb -->
p25, lines 25-25; prose; priority: unchanged; previous: p23; next: p27

> The guide explains how to interpret the experiments and their figures. It does not rerun the original animal recordings, data processing, or full neural-network simulations. A successful numerical check of a probability identity is different from an independent reproduction of a paper's empirical result. Related work is selected to clarify the assumptions and alternatives rather than to claim an exhaustive literature search.

<!-- pedagogy-paragraph: p27 sha256 889e5c8d6b7a74f343ac1b852a5f1eac4dc5762704fa9a509a99a450fe2cf7f0 -->
p27, lines 27-27; prose; priority: unchanged; previous: p25; next: none

> Throughout the guide, $D$ denotes a one-dimensional diffusion coefficient with MSD $2Dt$, and $d$ denotes spatial dimension. The memory chapters use $\theta$ for a represented coordinate. The place-field chapter uses $q$ for normalized threshold, which the paper calls $\theta$, and $C$ for its spatial covariance. Each chapter states further symbols and units before its equations depend on them.


Claim-bearing content: none

Claims to check:

No claim candidates detected. The expert objection still covers the unit.

Required evidence:

- Reader problem, observable limitation, or engineering decision: [cite an exact passage with a line or paragraph number, or write Not applicable: reader-benefit reason]
- Prerequisites, first use, and first teaching location: [cite an exact passage with a line or paragraph number, or write Not applicable: reader-benefit reason]
- Definition and emphasis: [cite an exact passage with a line or paragraph number, or write Not applicable: reader-benefit reason]
- Concrete wording and sentence contribution: phrase, plain-language paraphrase, actor, object, action or state change, condition or consequence, verdict, and replacement or retention reason: [cite an exact passage with a line or paragraph number, or write Not applicable: reader-benefit reason]
- Local relevance and paragraph continuity: [cite an exact passage with a line or paragraph number, or write Not applicable: reader-benefit reason]
- Operating mode and object roles, when relevant: [cite an exact passage with a line or paragraph number, or write Not applicable: reader-benefit reason]
- System setup and component relationships: [cite an exact passage with a line or paragraph number, or write Not applicable: reader-benefit reason]
- Representation bridge, when relevant: [cite an exact passage with a line or paragraph number, or write Not applicable: reader-benefit reason]
- Mechanism, calculation, or state change: [cite an exact passage with a line or paragraph number, or write Not applicable: reader-benefit reason]
- Concrete trace or example: [cite an exact passage with a line or paragraph number, or write Not applicable: reader-benefit reason]
- Example setup and conclusion: [cite an exact passage with a line or paragraph number, or write Not applicable: reader-benefit reason]
- Assumptions, limits, trade-offs, or failure modes: [cite an exact passage with a line or paragraph number, or write Not applicable: reader-benefit reason]
- Relevant alternatives, common criteria, and selection or scope: [cite an exact passage with a line or paragraph number, or write Not applicable: reader-benefit reason]
- Essential explanation beyond the checklist: [cite an exact passage with a line or paragraph number, or write Not applicable: reader-benefit reason]
- Result that motivates the next section: [cite an exact passage with a line or paragraph number, or write Not applicable: reader-benefit reason]
- Expert objection: [cite an exact passage with a line or paragraph number, or write Not applicable: reader-benefit reason]
- Verdict: Pending reviewer assessment

For the concrete-wording field, use this form: line N; phrase: ...; paraphrase: ...; actor: ...; object: ...; action: ...; condition or consequence: ...; verdict: retain, revise, or delete; replacement or retention reason: ....
Context review must explain the literal meaning, prerequisites, analogy limits when relevant, and reason for appearing here. If no correction is needed, give a specific retention reason; lint success is not evidence.
For System setup and component relationships, cite the passage and fill: setting: ...; roles: ...; objects and flow: ...; assumptions: ...; verdict: ....
For Relevant alternatives, common criteria, and selection or scope, cite the passage and fill: common problem: ...; options: ...; relationship: ...; criteria: ...; selection or scope: ...; verdict: ....
For Essential explanation beyond the checklist, cite the passage and fill: reader task: ...; dependencies checked: ...; reasoning chain: ...; unresolved: ....
For Expert objection, cite the passage and fill: objection: ...; kind: ...; target: ...; disposition: ...; reason: ....
For system setup and alternatives, an adequate review uses verdict: adequate. Where inapplicable, use Not applicable: line N; reason: <specific reader-benefit reason>.
Expert objection cannot be marked Not applicable. Write the strongest correction a domain expert would make to this unit's text or figures; set kind to correctness or wording; name its target passage or figure label; set disposition to fixed or does not apply; give the reason. An objection of none is not a review. The strongest correction is the one that would change what a reader believes or does. Aim first at what the unit claims: a promise word such as always, once, ensures or remains that is false or needs a condition; a named method described wrongly; code that does not do what the text says; a table cell; a diagnostic sequence that skips a stage; a verb without an actor; a label naming something other than what is drawn; a figure that disagrees with the text or another figure; and example content found in neither the chapter nor its sources. A unit whose claim-bearing content includes code, a table, an equation, or a figure needs a correctness objection; a wording objection alone does not count there.
Claims to check lists the unit's statements most likely to make checkable claims: every table row and every figure or table caption with its alt text, and each sentence with a promise word, a quantity or calculation, code font, a citation, or a section or figure reference. Footnote definitions are left to the citation checks. When packets compare with a revision, every changed statement is listed first and marked changed. For each claim, set verdict to true as written, condition stated, fixed, or not a claim, and after checked: say how it was checked, such as the code test, the recomputation, or the source and its location. The list is a floor, not the extent of the review.
For each code listing, write test: followed by the path, relative to the guide, of a test that runs it on the inputs the text makes claims about, or not run: followed by the reason and how its claims were checked instead.
Essential explanation cannot be marked Not applicable. Trace the reader's task and its dependencies, including gaps not covered by other fields. Record unresolved: none only after resolving essential gaps; otherwise describe them and keep the unit verdict open. A complete checklist is not proof of complete teaching.

## ch:GLOSSARY - Glossary

Source file: `content/chapters/glossary.md`

Purpose: These short definitions support lookup after the explanations and examples in the main chapters.

Prerequisites: None recorded

Sidecar sections: None recorded

Blocks: 0 figure(s), 0 equation(s), 0 code block(s)

Result labels: No Answer/Conclusion/Feedback label detected

<!-- pedagogy-unit: content/chapters/glossary.md::ch:GLOSSARY -->

### Chapter opening

Location: line 1, anchor `ch:GLOSSARY`

First content kind: `prose`

Opening passage line: 3
Closing passage line: 3

Paragraphs in source order (complete `PARAGRAPH_REVIEW.json`):

<!-- pedagogy-paragraph: p3 sha256 6610d5a3d2ea9ef700aad964e86c8efd5526bc9b2dcd4799a12a523e26e0608d -->
p3, lines 3-3; prose; priority: unchanged; previous: none; next: p5

> These short definitions support lookup after the explanations and examples in the main chapters.

<!-- pedagogy-paragraph: p5 sha256 199ccaf557f8ebb222f302e1b9c3e995f27b19ee00db849626da65b53ae470f6 -->
p5, lines 5-5; list_item; priority: unchanged; previous: p3; next: p6

> [**abducens nucleus:**]{.definition-term custom-style="Definition Term"} A brainstem group containing the motor neurons recorded in the eye-drift study; their axons activate the lateral rectus eye muscle.

<!-- pedagogy-paragraph: p6 sha256 f828b4fc0f9488f4a5362e9349b7b0f2bf6dc9dc5f6f68f677fd87527bd92a6d -->
p6, lines 6-6; list_item; priority: unchanged; previous: p5; next: p7

> [**activity bump:**]{.definition-term custom-style="Definition Term"} A localized peak of population firing rates across neurons ordered by their preferred represented values.

<!-- pedagogy-paragraph: p7 sha256 d64c02608a124abe62ce9e5646cdd40037b7fe658d968c089ef87a5f3acd8f75 -->
p7, lines 7-7; list_item; priority: unchanged; previous: p6; next: p8

> [**attractor manifold:**]{.definition-term custom-style="Definition Term"} The continuous family of persistent activity states, described by its represented coordinates rather than by every neural activity separately.

<!-- pedagogy-paragraph: p8 sha256 f8abb0f922a4768e0566584dfc7472f29b55b1cfe8c0f103fece338ad8d64fc7 -->
p8, lines 8-8; list_item; priority: unchanged; previous: p7; next: p9

> [**Betti numbers:**]{.definition-term custom-style="Definition Term"} Counts of independent connected components, loops, cavities, and their higher-dimensional counterparts.

<!-- pedagogy-paragraph: p9 sha256 81b76976e16ed9c4b2c7658a39fbcfc44548eaf3113f6a4db8c8e0733cb70738 -->
p9, lines 9-9; list_item; priority: unchanged; previous: p8; next: p10

> [**Brownian motion:**]{.definition-term custom-style="Definition Term"} A continuous random process starting at zero with independent Gaussian increments and increment variance equal to elapsed time.

<!-- pedagogy-paragraph: p10 sha256 de72e8f59c50a4d506c59b5a2209c7591f7c2cb54a567fd3ca270e9db4ee9f89 -->
p10, lines 10-10; list_item; priority: unchanged; previous: p9; next: p11

> [**causal filter:**]{.definition-term custom-style="Definition Term"} A rule whose current output depends only on present and past input.

<!-- pedagogy-paragraph: p11 sha256 13d4be0b4891d4feb3c9d67e459b1983031eae26d23c3dabff1a1a1bbf826a8b -->
p11, lines 11-11; list_item; priority: unchanged; previous: p10; next: p12

> [**coefficient of determination:**]{.definition-term custom-style="Definition Term"} For the optimal linear prediction with an intercept, the fraction of response variance removed by prediction; with one predictor it equals the squared correlation.

<!-- pedagogy-paragraph: p12 sha256 d0c8d1e992b7f9f35234b97a155ccb6c3af179695edb6c7025120d3d58f133b6 -->
p12, lines 12-12; list_item; priority: unchanged; previous: p11; next: p13

> [**coefficient of variation:**]{.definition-term custom-style="Definition Term"} Standard deviation divided by mean; in the spike-train discussion it is applied to interspike intervals.

<!-- pedagogy-paragraph: p13 sha256 24baf4007c3b4a658062ff954743aac29c9511042608df1c19c45d47757412ce -->
p13, lines 13-13; list_item; priority: unchanged; previous: p12; next: p14

> [**continuous attractor:**]{.definition-term custom-style="Definition Term"} A continuous family of fixed points with restoring dynamics toward the family and neutral motion along it in the ideal deterministic model.

<!-- pedagogy-paragraph: p14 sha256 9af80ab1f58efe51f894cfabafef42e4ed696456a693712fb84f3c5ab88882c1 -->
p14, lines 14-14; list_item; priority: unchanged; previous: p13; next: p15

> [**convolution:**]{.definition-term custom-style="Definition Term"} An integral or sum combining past input values with a shifted response kernel to obtain a filtered output.

<!-- pedagogy-paragraph: p15 sha256 ea5ea55b56674e27c1ea753925f8e5b1f54af57280f8f51ffa3451e4df5a84ea -->
p15, lines 15-15; list_item; priority: unchanged; previous: p14; next: p16

> [**correlation coefficient:**]{.definition-term custom-style="Definition Term"} Covariance divided by the product of standard deviations; a dimensionless measure of linear association.

<!-- pedagogy-paragraph: p16 sha256 b986d97fbfc6873c2fffffd23dfb6899d6367389311678457d928e124e22e1dc -->
p16, lines 16-16; list_item; priority: unchanged; previous: p15; next: p17

> [**covariance:**]{.definition-term custom-style="Definition Term"} The mean product of two centered random variables, measuring their shared variation.

<!-- pedagogy-paragraph: p17 sha256 17ccba508e8e71dcea268175875578ac1551cf44b2d1501c3d852158d6369897 -->
p17, lines 17-17; list_item; priority: unchanged; previous: p16; next: p18

> [**Cramér Rao bound:**]{.definition-term custom-style="Definition Term"} A lower bound on local unbiased estimation variance under the required regularity conditions, expressed through inverse Fisher information.

<!-- pedagogy-paragraph: p18 sha256 14eb9f6831772a66a704f3aa79be65155f4f6afd41a874b66d28a579e67ffc19 -->
p18, lines 18-18; list_item; priority: unchanged; previous: p17; next: p19

> [**decoding:**]{.definition-term custom-style="Definition Term"} Estimating a represented value from neural responses.

<!-- pedagogy-paragraph: p19 sha256 44909b02292d932e6ed9a2e2469fd9a4cf58ac9c123d2681d1f76c40a0f21958 -->
p19, lines 19-19; list_item; priority: unchanged; previous: p18; next: p20

> [**diffusion coefficient:**]{.definition-term custom-style="Definition Term"} The coefficient $D$ in the local one-dimensional displacement variance $2Dt$; its units are coordinate squared per time.

<!-- pedagogy-paragraph: p20 sha256 609314886aaccca3a3154e96ad3d96ac5e195622c2acda0592696c9556142999 -->
p20, lines 20-20; list_item; priority: unchanged; previous: p19; next: p21

> [**diffusion tensor:**]{.definition-term custom-style="Definition Term"} The matrix giving local coordinate-displacement covariances per twice the elapsed time.

<!-- pedagogy-paragraph: p21 sha256 17fae694192ca2a815d3693c0ca2e5d587adb828f4b13aeef419d26742b42419 -->
p21, lines 21-21; list_item; priority: unchanged; previous: p20; next: p22

> [**Dirac delta:**]{.definition-term custom-style="Definition Term"} A point-mass distribution; in the initial-condition equation all probability is concentrated at the specified coordinate.

<!-- pedagogy-paragraph: p22 sha256 54ba3bbeeb5b8db4d76906eea55eeaa36065e887407955c2de466f86618930da -->
p22, lines 22-22; list_item; priority: unchanged; previous: p21; next: p23

> [**Euler characteristic:**]{.definition-term custom-style="Definition Term"} The alternating sum of Betti numbers; in three dimensions, components minus independent loops plus enclosed cavities.

<!-- pedagogy-paragraph: p23 sha256 1fbb8c5710b819941283f6c77cea08eab95ba5c73f2cf519a71520c9c09377a6 -->
p23, lines 23-23; list_item; priority: unchanged; previous: p22; next: p24

> [**excursion set:**]{.definition-term custom-style="Definition Term"} The positions where a function exceeds a specified level.

<!-- pedagogy-paragraph: p24 sha256 b536842d4c328be9c556ed23e22ddc7f15dd851175b9953ebae36a3985c04986 -->
p24, lines 24-24; list_item; priority: unchanged; previous: p23; next: p25

> [**Fano factor:**]{.definition-term custom-style="Definition Term"} Spike-count variance divided by mean count, for a specified counting interval and condition.

<!-- pedagogy-paragraph: p25 sha256 2060822863c6e1d26d258b04f02387a49d72b4b57472cb33001eab87c0d23ee4 -->
p25, lines 25-25; list_item; priority: unchanged; previous: p24; next: p26

> [**firing rate:**]{.definition-term custom-style="Definition Term"} The expected number of spikes per unit time, conditional on the modeled circumstances.

<!-- pedagogy-paragraph: p26 sha256 ba93b3325539abf3d83d8aa80d51dafcb1bff8030a121bcf059b429bbd62662d -->
p26, lines 26-26; list_item; priority: unchanged; previous: p25; next: p27

> [**Fisher information:**]{.definition-term custom-style="Definition Term"} The expected squared score, quantifying the local sensitivity of a probability distribution to a parameter.

<!-- pedagogy-paragraph: p27 sha256 eb8c78329da21a38c836f7488e4398b7dd15406ae4d05f02576a2eb7418bc454 -->
p27, lines 27-27; list_item; priority: unchanged; previous: p26; next: p28

> [**fixational drift:**]{.definition-term custom-style="Definition Term"} Slow eye motion during attempted fixation, between rapid eye movements.

<!-- pedagogy-paragraph: p28 sha256 6943731cdee7bd2bb04e2f90f04a9d29e445352e9a65fbaa7c5fa9cb2df49113 -->
p28, lines 28-28; list_item; priority: unchanged; previous: p27; next: p29

> [**fixed point:**]{.definition-term custom-style="Definition Term"} A state whose deterministic rate of change is zero.

<!-- pedagogy-paragraph: p29 sha256 25f481e75b31369598067c173936bee1976f418c7b58a066ec74e80415aa4366 -->
p29, lines 29-29; list_item; priority: unchanged; previous: p28; next: p30

> [**Fokker Planck equation:**]{.definition-term custom-style="Definition Term"} An equation describing how a probability density evolves under drift and diffusion; the guide states the convention before using it.

<!-- pedagogy-paragraph: p30 sha256 0535ee1f5b5c0f2876d909c50b3bd165f91c9f7f1030be8d207529bbbf6acd9a -->
p30, lines 30-30; list_item; priority: unchanged; previous: p29; next: p31

> [**gain:**]{.definition-term custom-style="Definition Term"} The scale that converts a change in one signal into a change in another.

<!-- pedagogy-paragraph: p31 sha256 79c818b410e33957a9ad3fb073adf6651d3f34a9b844c41d52ec32281f5c8332 -->
p31, lines 31-31; list_item; priority: unchanged; previous: p30; next: p32

> [**Gaussian process:**]{.definition-term custom-style="Definition Term"} A distribution over functions whose values at any finite collection of positions have a joint Gaussian distribution.

<!-- pedagogy-paragraph: p32 sha256 4672318c305db2ef7cb2bb28575085d8f446f678f460daa62d48e2e8fcc11fb9 -->
p32, lines 32-32; list_item; priority: unchanged; previous: p31; next: p33

> [**grid cell:**]{.definition-term custom-style="Definition Term"} A spatially tuned entorhinal neuron with repeated firing fields, often approximately hexagonally arranged in a two-dimensional arena.

<!-- pedagogy-paragraph: p33 sha256 6f1477c326c053bd7f1e88a83cbbf6f1cc8cf428178a2e6f7ef508bdfd327b21 -->
p33, lines 33-33; list_item; priority: unchanged; previous: p32; next: p34

> [**Hessian:**]{.definition-term custom-style="Definition Term"} The matrix of second derivatives of a function with respect to its coordinates.

<!-- pedagogy-paragraph: p34 sha256 a528acc9336325a7aff4116f926c036bd9cd818329c326e9b8cd81921b021b0b -->
p34, lines 34-34; list_item; priority: unchanged; previous: p33; next: p35

> [**impulse response:**]{.definition-term custom-style="Definition Term"} The output of a linear filter in response to a unit-area input impulse, from which responses to general input can be assembled.

<!-- pedagogy-paragraph: p35 sha256 a20d3e51834243821f61746e5e35265a8d203cac98a3850da592fdc03d236aac -->
p35, lines 35-35; list_item; priority: unchanged; previous: p34; next: p36

> [**internal Fisher information rate:**]{.definition-term custom-style="Definition Term"} The local information per unit observation time about the instantaneous attractor coordinate, as defined by the 2012 spike model.

<!-- pedagogy-paragraph: p36 sha256 7d1ecd781a0cddeadabd5156a8e54273f7121a43fce6101386fac30551de7e42 -->
p36, lines 36-36; list_item; priority: unchanged; previous: p35; next: p37

> [**Isotropy:**]{.definition-term custom-style="Definition Term"} Invariance of the spatial probability law under rotations.

<!-- pedagogy-paragraph: p37 sha256 1e3379b9222bac988167d0fd67f425aa27a17d8cdc7cdf02b65ef04d5663d112 -->
p37, lines 37-37; list_item; priority: unchanged; previous: p36; next: p38

> [**Itô convention:**]{.definition-term custom-style="Definition Term"} A stochastic-increment convention that evaluates the noise coefficient at the beginning of each increment.

<!-- pedagogy-paragraph: p38 sha256 a0dc0c5e07fe7d14348d88120b07ed49762128df7a47e2408d7ca0b70e1cf912 -->
p38, lines 38-38; list_item; priority: unchanged; previous: p37; next: p39

> [**Kac–Rice formula:**]{.definition-term custom-style="Definition Term"} A way to compute expected crossing or critical-point counts from the joint distribution of a random function and its derivatives, under the relevant regularity assumptions.

<!-- pedagogy-paragraph: p39 sha256 53b980d74713cf252990a984f1e468390c3d9a5156e615c6cf8bd9038ea7c664 -->
p39, lines 39-39; list_item; priority: unchanged; previous: p38; next: p40

> [**left zero eigenvector:**]{.definition-term custom-style="Definition Term"} A vector $v$ with $v^T A=0$; with appropriate normalization it extracts the persistent coordinate from a small state disturbance.

<!-- pedagogy-paragraph: p40 sha256 775d80feb94b7672f437f24a669c6cc3daf58273db3a21e75505e6488357f057 -->
p40, lines 40-40; list_item; priority: unchanged; previous: p39; next: p41

> [**likelihood:**]{.definition-term custom-style="Definition Term"} The probability or density of the observed data considered as a function of a proposed parameter value.

<!-- pedagogy-paragraph: p41 sha256 9a92d8419c52b720f99035ee2472c1eee73929fde989f92e192a9dd8dd300959 -->
p41, lines 41-41; list_item; priority: unchanged; previous: p40; next: p42

> [**linearization:**]{.definition-term custom-style="Definition Term"} The first-order approximation to a dynamical equation near a reference state.

<!-- pedagogy-paragraph: p42 sha256 4767285c62fa6703475cf3eab5ad210652f491440bee09dc32ff32cf6889d1c0 -->
p42, lines 42-42; list_item; priority: unchanged; previous: p41; next: p43

> [**low pass filter:**]{.definition-term custom-style="Definition Term"} A filter that suppresses sufficiently rapid input changes relative to slower ones.

<!-- pedagogy-paragraph: p43 sha256 a113b97b3f5cf658d152df56b44c559fc8c2b4be6e91a7af4261b79236b2586d -->
p43, lines 43-43; list_item; priority: unchanged; previous: p42; next: p44

> [**mean squared displacement:**]{.definition-term custom-style="Definition Term"} The average squared change in a coordinate across a specified time lag.

<!-- pedagogy-paragraph: p44 sha256 f2499c844c2cbed494c47096480733dcf8bee473daf9a6fcaa535cf290bd82b2 -->
p44, lines 44-44; list_item; priority: unchanged; previous: p43; next: p45

> [**microsaccades:**]{.definition-term custom-style="Definition Term"} Brief, rapid eye movements that occur during attempted fixation.

<!-- pedagogy-paragraph: p45 sha256 b659ba01dc5464b622147fe0acdaf75d982a9d25a80d5c066683a1e0f4385e28 -->
p45, lines 45-45; list_item; priority: unchanged; previous: p44; next: p46

> [**neural transfer function:**]{.definition-term custom-style="Definition Term"} The modeled relationship between a neuron's input and its expected firing rate.

<!-- pedagogy-paragraph: p46 sha256 10e1e3743576521d2df39b68660631b6fac160c9d3750fd3ad49a4a729d59353 -->
p46, lines 46-46; list_item; priority: unchanged; previous: p45; next: p47

> [**ocular motoneurons (OMNs):**]{.definition-term custom-style="Definition Term"} Neurons whose spikes activate the eye muscles.

<!-- pedagogy-paragraph: p47 sha256 7c6b413fb99dda282fa214f11f47bfefed3df1434baca0e41c7c8d736bf425bd -->
p47, lines 47-47; list_item; priority: unchanged; previous: p46; next: p48

> [**ocular plant:**]{.definition-term custom-style="Definition Term"} The muscles and mechanical eye system that transform motor activity into eye motion.

<!-- pedagogy-paragraph: p48 sha256 4a1ed9c6696c52da5c5ed763c66720e2bdb9caaf481ae37b23cbc73fc3a6f22e -->
p48, lines 48-48; list_item; priority: unchanged; previous: p47; next: p49

> [**oculomotor integrator:**]{.definition-term custom-style="Definition Term"} A neural circuit that converts movement commands into a maintained eye-position command.

<!-- pedagogy-paragraph: p49 sha256 1c01f63939127b742ad731a7c272e49be05f8cee8582cf3d34b0fbbcc4e84fc4 -->
p49, lines 49-49; list_item; priority: unchanged; previous: p48; next: p50

> [**p value:**]{.definition-term custom-style="Definition Term"} Under the specified null comparison, the probability of a test statistic at least as extreme in the tested direction as the observed one.

<!-- pedagogy-paragraph: p50 sha256 c7478d68089ea0be309f78cfc26c43047cd7c66b0b9cf40f3136e01e048ad4c6 -->
p50, lines 50-50; list_item; priority: unchanged; previous: p49; next: p51

> [**place cell:**]{.definition-term custom-style="Definition Term"} A spatially selective hippocampal neuron that fires strongly in one or more localized regions of an environment.

<!-- pedagogy-paragraph: p51 sha256 16a07fccf901cb0c2b1af1d1770d25cd8a9e68151abfa4d27c4ee85a4c4ff231 -->
p51, lines 51-51; list_item; priority: unchanged; previous: p50; next: p52

> [**place field:**]{.definition-term custom-style="Definition Term"} A connected region of elevated spatial firing, as defined by the model or stated measurement procedure.

<!-- pedagogy-paragraph: p52 sha256 5623ceccdde832fd074fa7919215d7b18b0a1ac31e9df9bd99d086e2a8240747 -->
p52, lines 52-52; list_item; priority: unchanged; previous: p51; next: p53

> [**Poisson process:**]{.definition-term custom-style="Definition Term"} A counting process with independent increments and a deterministic constant or time-dependent event rate; its count over an interval has equal mean and variance. In a recurrent model, conditionally Poisson instantaneous spike generation does not make complete spike trains have independent increments.

<!-- pedagogy-paragraph: p53 sha256 dd1bb7b22c9c7844cd865560d560dda1ac9aed5d27b5276c1ce25f3e0d0b040f -->
p53, lines 53-53; list_item; priority: unchanged; previous: p52; next: p54

> [**population code:**]{.definition-term custom-style="Definition Term"} A representation carried by the pattern of responses across neurons.

<!-- pedagogy-paragraph: p54 sha256 2a054365896cba6c99759762b194d15dff32cefce07df7ab65122a4d7ccdd068 -->
p54, lines 54-54; list_item; priority: unchanged; previous: p53; next: p55

> [**precision:**]{.definition-term custom-style="Definition Term"} The reciprocal of variance for a scalar Gaussian estimate.

<!-- pedagogy-paragraph: p55 sha256 7493ae5a1a8dfc81077f793af2f77e59016616f3ab02d6e59e7038120eb16761 -->
p55, lines 55-55; list_item; priority: unchanged; previous: p54; next: p56

> [**preferred angle:**]{.definition-term custom-style="Definition Term"} An angle where a neuron's tuning curve peaks.

<!-- pedagogy-paragraph: p56 sha256 89d72519bcf31152675df1ee204a688db786b95ad4f0aedf1a08de561b092bf7 -->
p56, lines 56-56; list_item; priority: unchanged; previous: p55; next: p57

> [**prior distribution:**]{.definition-term custom-style="Definition Term"} A distribution representing knowledge about likely parameter values before observing the current data.

<!-- pedagogy-paragraph: p57 sha256 76de5a66e3a7dd59e29b883c2f3735d68e1edef1435034ae2f36d67c2dc4b3ed -->
p57, lines 57-57; list_item; priority: unchanged; previous: p56; next: p58

> [**rate map:**]{.definition-term custom-style="Definition Term"} An estimate of spatial firing rate from spikes per time spent at each position.

<!-- pedagogy-paragraph: p58 sha256 d837e38ee6cb5de21824b7fed9cdaa6cf9de7eafaf055c45d7669f9017513291 -->
p58, lines 58-58; list_item; priority: unchanged; previous: p57; next: p59

> [**recurrent connectivity:**]{.definition-term custom-style="Definition Term"} Connections that feed activity back into the same neuronal population.

<!-- pedagogy-paragraph: p59 sha256 6dfbfeea5d27bf94bfb466685a619ca9be263481f0f43637555ca92b2a15a2f7 -->
p59, lines 59-59; list_item; priority: unchanged; previous: p58; next: p60

> [**renewal process:**]{.definition-term custom-style="Definition Term"} An event process with independent, identically distributed intervals under the fixed conditions being modeled.

<!-- pedagogy-paragraph: p60 sha256 4d523e4e8281a300ffd36761c024c7b49fda209c727345e8f6cd8f0cfd07d0c9 -->
p60, lines 60-60; list_item; priority: unchanged; previous: p59; next: p61

> [**right zero eigenvector:**]{.definition-term custom-style="Definition Term"} A state-space direction $u$ satisfying $Au=0$ for the linearized dynamics.

<!-- pedagogy-paragraph: p61 sha256 05f13f91c4d04255f0bf5a3c0e5b4d9db7a5668142579f17587635944a7651dc -->
p61, lines 61-61; list_item; priority: unchanged; previous: p60; next: p62

> [**root mean squared displacement:**]{.definition-term custom-style="Definition Term"} The square root of mean squared displacement, expressed in the original coordinate's units.

<!-- pedagogy-paragraph: p62 sha256 6bf545c97edcf92181bea799ce81f0ea5aa52dc29da86d553e7376be96bc0abd -->
p62, lines 62-62; list_item; priority: unchanged; previous: p61; next: p63

> [**score:**]{.definition-term custom-style="Definition Term"} The derivative of log likelihood with respect to the parameter being estimated.

<!-- pedagogy-paragraph: p63 sha256 d86e3a3827d624ad7bbfea0a97e366def7900c6eae6ac0235241fc22f9a1eff7 -->
p63, lines 63-63; list_item; priority: unchanged; previous: p62; next: p64

> [**spike:**]{.definition-term custom-style="Definition Term"} A brief electrical event emitted by a neuron.

<!-- pedagogy-paragraph: p64 sha256 5f00c75da0d0d5b72c6bb9f46384d10047f1836b8938ae5a48deefbf50fbb2bd -->
p64, lines 64-64; list_item; priority: unchanged; previous: p63; next: p65

> [**standard error of the mean (SEM):**]{.definition-term custom-style="Definition Term"} An estimate of uncertainty in a sample mean. Its interpretation depends on which observations are treated as independent, such as trials, cells, or animals.

<!-- pedagogy-paragraph: p65 sha256 de0f4193eaf50c9b229cc5033e503eb66da78af06a7ac1bc58640c775fe3c2a7 -->
p65, lines 65-65; list_item; priority: unchanged; previous: p64; next: p66

> [**state:**]{.definition-term custom-style="Definition Term"} The quantities that specify a modeled system's current condition and determine its subsequent dynamics together with future inputs and noise.

<!-- pedagogy-paragraph: p66 sha256 56add8e070a4e4001f1d20b2d8c29d365a25ef496e3d305c35262bb241e48fb9 -->
p66, lines 66-66; list_item; priority: unchanged; previous: p65; next: p67

> [**Stationarity:**]{.definition-term custom-style="Definition Term"} In the place-field model, invariance of spatial statistics under translating the map.

<!-- pedagogy-paragraph: p67 sha256 ad963b97e45fffb7f2508b79bb9e7b1ec5c72ea1203724bbd2234d9d5c621459 -->
p67, lines 67-67; list_item; priority: unchanged; previous: p66; next: p68

> [**stationary process:**]{.definition-term custom-style="Definition Term"} A random process whose probability law is unchanged by shifting its time or position origin; weaker covariance-only stationarity must be specified when used.

<!-- pedagogy-paragraph: p68 sha256 ed7bbbcb1369547a0f5e0bdccef8574901bf85c00a3ed23c1197f5d846887472 -->
p68, lines 68-68; list_item; priority: unchanged; previous: p67; next: p69

> [**Stratonovich convention:**]{.definition-term custom-style="Definition Term"} A stochastic-increment convention using midpoint evaluation in the limiting increments.

<!-- pedagogy-paragraph: p69 sha256 8a624b615e3a235bdb083eabaecf643be054c332766f7f3feefce6c909d8c434 -->
p69, lines 69-69; list_item; priority: unchanged; previous: p68; next: p70

> [**sub-Poisson spiking:**]{.definition-term custom-style="Definition Term"} Spiking with less variability than a matched Poisson reference according to the stated measure and conditions.

<!-- pedagogy-paragraph: p70 sha256 18783ad65a37620810bfe4a3897af59713115fa900428b7cdd71eacae9958630 -->
p70, lines 70-70; list_item; priority: unchanged; previous: p69; next: p71

> [**superdiffusion:**]{.definition-term custom-style="Definition Term"} Mean squared displacement growing faster than linearly with lag over the range being described.

<!-- pedagogy-paragraph: p71 sha256 3e058f8c054b113f62aaa1a9df89bd909b08e3a7cd82c02b85b7fc254e38e2c9 -->
p71, lines 71-71; list_item; priority: unchanged; previous: p70; next: p72

> [**synapse:**]{.definition-term custom-style="Definition Term"} A connection through which one neuron influences another.

<!-- pedagogy-paragraph: p72 sha256 ad89bee310987401aa4da112356a105e6dbb78211f2a1b6c1e752ab836da13ca -->
p72, lines 72-72; list_item; priority: unchanged; previous: p71; next: p73

> [**systematic drift:**]{.definition-term custom-style="Definition Term"} A nonzero mean velocity of the represented coordinate, distinct from random spreading.

<!-- pedagogy-paragraph: p73 sha256 58d0d25f3590763282cfe029a41445431950a64ceb40fc008fbd18bbb3c605ff -->
p73, lines 73-73; list_item; priority: unchanged; previous: p72; next: p74

> [**tuning curve:**]{.definition-term custom-style="Definition Term"} A neuron's expected firing rate as a function of a represented variable.

<!-- pedagogy-paragraph: p74 sha256 99e6fd3874752b9739b803f0254b7c0ddcd9b00aa6a8ee5a9a16d1b4e35a320f -->
p74, lines 74-74; list_item; priority: unchanged; previous: p73; next: p75

> [**unbiased:**]{.definition-term custom-style="Definition Term"} Describes an estimator whose expected value equals the parameter locally under the conditions used in the estimation bound.

<!-- pedagogy-paragraph: p75 sha256 8bfaa455c678898a6e22fb3cceffdec64d4ce4a4be28901044e9b27a31102115 -->
p75, lines 75-75; list_item; priority: unchanged; previous: p74; next: p76

> [**weak fluctuation approximation:**]{.definition-term custom-style="Definition Term"} An expansion about the deterministic population dynamics in which the aggregate effects of many small spike contributions remain small.

<!-- pedagogy-paragraph: p76 sha256 a15c018600d02bf0860dd86269074a202bca8f58c6b5379f7be59702e0bd3c59 -->
p76, lines 76-76; list_item; priority: unchanged; previous: p75; next: p77

> [**Weibull distribution:**]{.definition-term custom-style="Definition Term"} A positive-variable distribution with survival probability $\exp[-(s/b)^k]$, scale $b>0$, and shape $k>0$.

<!-- pedagogy-paragraph: p77 sha256 d3ec1ee4d640003e0e51ef848f02e213546e2412751201165b44abbcc7cd9e1c -->
p77, lines 77-77; list_item; priority: unchanged; previous: p76; next: none

> [**White noise:**]{.definition-term custom-style="Definition Term"} An ideal noise input with zero covariance at unequal times and a delta-function covariance at equal times; its integrated increments have finite variance.


Claim-bearing content: none

Claims to check:

- Claim c1, line 7: "[**attractor manifold:**]{.definition-term custom-style="Definition Term"} The continuous family of persistent activity states, described by its represented coordinates rather than by every neural activity separately." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c2, line 10: "[**causal filter:**]{.definition-term custom-style="Definition Term"} A rule whose current output depends only on present and past input." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c3, line 39: "[**left zero eigenvector:**]{.definition-term custom-style="Definition Term"} A vector $v$ with $v^T A=0$; with appropriate normalization it extracts the persistent coordinate from a small state disturbance." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c4, line 60: "[**right zero eigenvector:**]{.definition-term custom-style="Definition Term"} A state-space direction $u$ satisfying $Au=0$ for the linearized dynamics." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c5, line 67: "[**stationary process:**]{.definition-term custom-style="Definition Term"} A random process whose probability law is unchanged by shifting its time or position origin; weaker covariance-only stationarity must be specified when used." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c6, line 75: "[**weak fluctuation approximation:**]{.definition-term custom-style="Definition Term"} An expansion about the deterministic population dynamics in which the aggregate effects of many small spike contributions remain small." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c7, line 76: "[**Weibull distribution:**]{.definition-term custom-style="Definition Term"} A positive-variable distribution with survival probability $\exp[-(s/b)^k]$, scale $b>0$, and shape $k>0$." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]

Required evidence:

- Reader problem, observable limitation, or engineering decision: [cite an exact passage with a line or paragraph number, or write Not applicable: reader-benefit reason]
- Prerequisites, first use, and first teaching location: [cite an exact passage with a line or paragraph number, or write Not applicable: reader-benefit reason]
- Definition and emphasis: [cite an exact passage with a line or paragraph number, or write Not applicable: reader-benefit reason]
- Concrete wording and sentence contribution: phrase, plain-language paraphrase, actor, object, action or state change, condition or consequence, verdict, and replacement or retention reason: [cite an exact passage with a line or paragraph number, or write Not applicable: reader-benefit reason]
- Local relevance and paragraph continuity: [cite an exact passage with a line or paragraph number, or write Not applicable: reader-benefit reason]
- Operating mode and object roles, when relevant: [cite an exact passage with a line or paragraph number, or write Not applicable: reader-benefit reason]
- System setup and component relationships: [cite an exact passage with a line or paragraph number, or write Not applicable: reader-benefit reason]
- Representation bridge, when relevant: [cite an exact passage with a line or paragraph number, or write Not applicable: reader-benefit reason]
- Mechanism, calculation, or state change: [cite an exact passage with a line or paragraph number, or write Not applicable: reader-benefit reason]
- Concrete trace or example: [cite an exact passage with a line or paragraph number, or write Not applicable: reader-benefit reason]
- Example setup and conclusion: [cite an exact passage with a line or paragraph number, or write Not applicable: reader-benefit reason]
- Assumptions, limits, trade-offs, or failure modes: [cite an exact passage with a line or paragraph number, or write Not applicable: reader-benefit reason]
- Relevant alternatives, common criteria, and selection or scope: [cite an exact passage with a line or paragraph number, or write Not applicable: reader-benefit reason]
- Essential explanation beyond the checklist: [cite an exact passage with a line or paragraph number, or write Not applicable: reader-benefit reason]
- Result that motivates the next section: [cite an exact passage with a line or paragraph number, or write Not applicable: reader-benefit reason]
- Expert objection: [cite an exact passage with a line or paragraph number, or write Not applicable: reader-benefit reason]
- Verdict: Pending reviewer assessment

For the concrete-wording field, use this form: line N; phrase: ...; paraphrase: ...; actor: ...; object: ...; action: ...; condition or consequence: ...; verdict: retain, revise, or delete; replacement or retention reason: ....
Context review must explain the literal meaning, prerequisites, analogy limits when relevant, and reason for appearing here. If no correction is needed, give a specific retention reason; lint success is not evidence.
For System setup and component relationships, cite the passage and fill: setting: ...; roles: ...; objects and flow: ...; assumptions: ...; verdict: ....
For Relevant alternatives, common criteria, and selection or scope, cite the passage and fill: common problem: ...; options: ...; relationship: ...; criteria: ...; selection or scope: ...; verdict: ....
For Essential explanation beyond the checklist, cite the passage and fill: reader task: ...; dependencies checked: ...; reasoning chain: ...; unresolved: ....
For Expert objection, cite the passage and fill: objection: ...; kind: ...; target: ...; disposition: ...; reason: ....
For system setup and alternatives, an adequate review uses verdict: adequate. Where inapplicable, use Not applicable: line N; reason: <specific reader-benefit reason>.
Expert objection cannot be marked Not applicable. Write the strongest correction a domain expert would make to this unit's text or figures; set kind to correctness or wording; name its target passage or figure label; set disposition to fixed or does not apply; give the reason. An objection of none is not a review. The strongest correction is the one that would change what a reader believes or does. Aim first at what the unit claims: a promise word such as always, once, ensures or remains that is false or needs a condition; a named method described wrongly; code that does not do what the text says; a table cell; a diagnostic sequence that skips a stage; a verb without an actor; a label naming something other than what is drawn; a figure that disagrees with the text or another figure; and example content found in neither the chapter nor its sources. A unit whose claim-bearing content includes code, a table, an equation, or a figure needs a correctness objection; a wording objection alone does not count there.
Claims to check lists the unit's statements most likely to make checkable claims: every table row and every figure or table caption with its alt text, and each sentence with a promise word, a quantity or calculation, code font, a citation, or a section or figure reference. Footnote definitions are left to the citation checks. When packets compare with a revision, every changed statement is listed first and marked changed. For each claim, set verdict to true as written, condition stated, fixed, or not a claim, and after checked: say how it was checked, such as the code test, the recomputation, or the source and its location. The list is a floor, not the extent of the review.
For each code listing, write test: followed by the path, relative to the guide, of a test that runs it on the inputs the text makes claims about, or not run: followed by the reason and how its claims were checked instead.
Essential explanation cannot be marked Not applicable. Trace the reader's task and its dependencies, including gaps not covered by other fields. Record unresolved: none only after resolving essential gaps; otherwise describe them and keep the unit verdict open. A complete checklist is not proof of complete teaching.

## ch:REFERENCES - References

Source file: `content/chapters/references.md`

Purpose: Entries follow their first use in the reading path and chapters. The paper's supporting information shares its main article entry. The author's mathematical notes are listed separately because the guide also uses them for the excursion derivation.

Prerequisites: None recorded

Sidecar sections: None recorded

Blocks: 0 figure(s), 0 equation(s), 0 code block(s)

Result labels: No Answer/Conclusion/Feedback label detected

<!-- pedagogy-unit: content/chapters/references.md::ch:REFERENCES -->

### Chapter opening

Location: line 1, anchor `ch:REFERENCES`

First content kind: `prose`

Opening passage line: 3
Closing passage line: 3

Paragraphs in source order (complete `PARAGRAPH_REVIEW.json`):

<!-- pedagogy-paragraph: p3 sha256 2180a56e77ae49b6c265ee1b2e23c5ae64bfe2f7305e35cd83672a56cfe6a02a -->
p3, lines 3-3; prose; priority: unchanged; previous: none; next: p5

> Entries follow their first use in the reading path and chapters. The paper's supporting information shares its main article entry. The author's mathematical notes are listed separately because the guide also uses them for the excursion derivation.

<!-- pedagogy-paragraph: p5 sha256 b38fda0c5568496c0f816eb028e38679c76646c7a0dd56996aefa4e6d9a66506 -->
p5, lines 5-5; list_item; priority: unchanged; previous: p3; next: p7

> Burak, Y.; Fiete, I. R. (2012). *Fundamental limits on persistent activity in networks of noisy neurons*. Proceedings of the National Academy of Sciences, 109(43), 17645–17650. [DOI](https://doi.org/10.1073/pnas.1117386109).

<!-- pedagogy-paragraph: p7 sha256 c0061d5ca7d9f67075416dfcd562768064652367cf1a6f92a48180ec7cf2c347 -->
p7, lines 7-7; list_item; priority: unchanged; previous: p5; next: p9

> Ben-Shushan, N.; Shaham, N.; Joshua, M.; Burak, Y. (2022). *Fixational drift is driven by diffusive dynamics in central neural circuitry*. Nature Communications, 13(1), 1697. [DOI](https://doi.org/10.1038/s41467-022-29201-y).

<!-- pedagogy-paragraph: p9 sha256 2ee70ff9d90a01dce67b92d52660f9b2e4a9f202e8d032493b8114f9e3c4fdb2 -->
p9, lines 9-9; list_item; priority: unchanged; previous: p7; next: p11

> Mainali, N.; Azeredo da Silveira, R.; Burak, Y. (2025). *Universal statistics of hippocampal place fields across species and dimensionalities*. Neuron, 113(7), 1110–1120.e3. [DOI](https://doi.org/10.1016/j.neuron.2025.01.017).

<!-- pedagogy-paragraph: p11 sha256 b4538a257c0a0d8f770cb2db8655fc9d9df9bc4e86ab488ea9da6671af0fc725 -->
p11, lines 11-11; list_item; priority: unchanged; previous: p9; next: p13

> Maimon, S. R.; Eliav, T.; Aljadeff, J.; Shalev, A.; Gronich, Y.; Finger, N. M.; Eveland, K. E.; Moss, C. F.; Las, L.; Ulanovsky, N. (2026). *Sparse-to-dense coding transformation between hippocampal areas CA3 and CA1*. Nature, 655(8125), 1242–1251. [DOI](https://doi.org/10.1038/s41586-026-10537-0).

<!-- pedagogy-paragraph: p13 sha256 12ebd3c536bf7b1f0fc2a1ab6a20bd2821f0ddf9f588e57022c53e4799b5cfd7 -->
p13, lines 13-13; list_item; priority: unchanged; previous: p11; next: p15

> Mainali, N. (2026, August 6). *Mathematical properties of Gaussian process neural code: Excursion geometry, spectral structure, and coding error*. [Author's mathematical notes](https://nischmainali.github.io/blog/gp-code-notes/).

<!-- pedagogy-paragraph: p15 sha256 e5aeb969184d0e3d547c9cefc12f83b441fa137d15e071cea0c30f7291304765 -->
p15, lines 15-15; list_item; priority: unchanged; previous: p13; next: p17

> Taylor, J. E. (2006). *A Gaussian kinematic formula*. The Annals of Probability, 34(1), 122–158. [DOI](https://doi.org/10.1214/009117905000000594).

<!-- pedagogy-paragraph: p17 sha256 4f86b02b233d85f9247cdd8ed47f28efa772b8de903caa4f9da872d7e1f5ec1e -->
p17, lines 17-17; list_item; priority: unchanged; previous: p15; next: p19

> Seung, H. S. (1996). *How the brain keeps the eyes still*. Proceedings of the National Academy of Sciences, 93(23), 13339–13344. [DOI](https://doi.org/10.1073/pnas.93.23.13339).

<!-- pedagogy-paragraph: p19 sha256 ab7f15bf4c8182a4534d2ff9b29efe803ad7cfe6431f53571788936d56f5823e -->
p19, lines 19-19; list_item; priority: unchanged; previous: p17; next: p21

> Aksay, E.; Olasagasti, I.; Mensh, B. D.; Baker, R.; Goldman, M. S.; Tank, D. W. (2007). *Functional dissection of circuitry in a neural integrator*. Nature Neuroscience, 10(4), 494–504. [DOI](https://doi.org/10.1038/nn1877).

<!-- pedagogy-paragraph: p21 sha256 5d99d69163e24c82217014f3e99f60442c2d2dcbc0a021bf958aaeb89b344339 -->
p21, lines 21-21; list_item; priority: unchanged; previous: p19; next: p23

> Burak, Y.; Fiete, I. R. (2009). *Accurate Path Integration in Continuous Attractor Network Models of Grid Cells*. PLoS Computational Biology, 5(2), e1000291. [DOI](https://doi.org/10.1371/journal.pcbi.1000291).

<!-- pedagogy-paragraph: p23 sha256 601b6e74cb1dc8840a205f41173ad74c7f7b4ca922ea31f906c2e90de5e82ecf -->
p23, lines 23-23; list_item; priority: unchanged; previous: p21; next: p25

> Koyluoglu, O. O.; Pertzov, Y.; Manohar, S.; Husain, M.; Fiete, I. R. (2017). *Fundamental bound on the persistence and capacity of short-term memory stored as graded persistent activity*. eLife, 6, e22225. [DOI](https://doi.org/10.7554/eLife.22225).

<!-- pedagogy-paragraph: p25 sha256 1351e84e03692615f8fee3dc575978b246c029ee90c11ca43c4a4d5a5dcfda01 -->
p25, lines 25-25; list_item; priority: unchanged; previous: p23; next: p27

> Seeholzer, A.; Deger, M.; Gerstner, W. (2019). *Stability of working memory in continuous attractor networks under the control of short-term plasticity*. PLOS Computational Biology, 15(4), e1006928. [DOI](https://doi.org/10.1371/journal.pcbi.1006928).

<!-- pedagogy-paragraph: p27 sha256 a8eef324d31b6a0405d57dea5f11432331d172cfbaa6db28e78cd83f51a1a6c2 -->
p27, lines 27-27; list_item; priority: unchanged; previous: p25; next: p29

> Eliav, T.; Maimon, S. R.; Aljadeff, J.; Tsodyks, M.; Ginosar, G.; Las, L.; Ulanovsky, N. (2021). *Multiscale representation of very large environments in the hippocampus of flying bats*. Science, 372(6545), eabg4020. [DOI](https://doi.org/10.1126/science.abg4020).

<!-- pedagogy-paragraph: p29 sha256 0707c920953b9e05b529d63b91de102ad5562c3b8878cf5c13adc548776219b3 -->
p29, lines 29-29; list_item; priority: unchanged; previous: p27; next: p31

> Harland, B.; Contreras, M.; Souder, M.; Fellous, J. M. (2021). *Dorsal CA1 hippocampal place cells form a multi-scale representation of megaspace*. Current Biology, 31(10), 2178–2190.e6. [DOI](https://doi.org/10.1016/j.cub.2021.03.003).

<!-- pedagogy-paragraph: p31 sha256 e4e9e691fc5244fdb9c275000df96b52d559ec6850997b6be6119709b8b4aace -->
p31, lines 31-31; list_item; priority: unchanged; previous: p29; next: p33

> Yartsev, M. M.; Ulanovsky, N. (2013). *Representation of Three-Dimensional Space in the Hippocampus of Flying Bats*. Science, 340(6130), 367–372. [DOI](https://doi.org/10.1126/science.1235338).

<!-- pedagogy-paragraph: p33 sha256 fc56d8db0e62c22a904460c0cfb5d4a3494ab725a5a02f58ebfb6803649b68a9 -->
p33, lines 33-33; list_item; priority: unchanged; previous: p31; next: p35

> Druckmann, S.; Feng, L.; Lee, B.; Yook, C.; Zhao, T.; Magee, J. C.; Kim, J. (2014). *Structured Synaptic Connectivity between Hippocampal Regions*. Neuron, 81(3), 629–640. [DOI](https://doi.org/10.1016/j.neuron.2013.11.026).

<!-- pedagogy-paragraph: p35 sha256 ed4e9e5578799f9f9c3f04db54cd6837e229cb8550a33c77d8f5556841fa1c5e -->
p35, lines 35-35; list_item; priority: unchanged; previous: p33; next: p37

> Bittner, K. C.; Milstein, A. D.; Grienberger, C.; Romani, S.; Magee, J. C. (2017). *Behavioral time scale synaptic plasticity underlies CA1 place fields*. Science, 357(6355), 1033–1036. [DOI](https://doi.org/10.1126/science.aan3846).

<!-- pedagogy-paragraph: p37 sha256 54d9a76280ea41a6830879113857364470ddb9143f0afa6ba003b2f21e5ac6b4 -->
p37, lines 37-37; list_item; priority: unchanged; previous: p35; next: none

> Nghiem, T. A. E.; Witten, J. L.; Dufour, O.; Harmening, W. M.; Azeredo da Silveira, R. (2025). *Fixational eye movements as active sensation for high visual acuity*. Proceedings of the National Academy of Sciences, 122(6), e2416266122. [DOI](https://doi.org/10.1073/pnas.2416266122).


Claim-bearing content: none

Claims to check:

- Claim c1, line 5: "[DOI](https://doi.org/10.1073/pnas.1117386109)." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c2, line 7: "[DOI](https://doi.org/10.1038/s41467-022-29201-y)." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c3, line 9: "[DOI](https://doi.org/10.1016/j.neuron.2025.01.017)." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c4, line 11: "*Sparse-to-dense coding transformation between hippocampal areas CA3 and CA1*." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c5, line 11: "[DOI](https://doi.org/10.1038/s41586-026-10537-0)." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c6, line 15: "[DOI](https://doi.org/10.1214/009117905000000594)." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c7, line 17: "[DOI](https://doi.org/10.1073/pnas.93.23.13339)." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c8, line 19: "[DOI](https://doi.org/10.1038/nn1877)." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c9, line 21: "[DOI](https://doi.org/10.1371/journal.pcbi.1000291)." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c10, line 23: "[DOI](https://doi.org/10.7554/eLife.22225)." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c11, line 25: "[DOI](https://doi.org/10.1371/journal.pcbi.1006928)." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c12, line 27: "[DOI](https://doi.org/10.1126/science.abg4020)." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c13, line 29: "[DOI](https://doi.org/10.1016/j.cub.2021.03.003)." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c14, line 31: "[DOI](https://doi.org/10.1126/science.1235338)." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c15, line 33: "[DOI](https://doi.org/10.1016/j.neuron.2013.11.026)." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c16, line 35: "[DOI](https://doi.org/10.1126/science.aan3846)." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c17, line 37: "[DOI](https://doi.org/10.1073/pnas.2416266122)." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]

Required evidence:

- Reader problem, observable limitation, or engineering decision: [cite an exact passage with a line or paragraph number, or write Not applicable: reader-benefit reason]
- Prerequisites, first use, and first teaching location: [cite an exact passage with a line or paragraph number, or write Not applicable: reader-benefit reason]
- Definition and emphasis: [cite an exact passage with a line or paragraph number, or write Not applicable: reader-benefit reason]
- Concrete wording and sentence contribution: phrase, plain-language paraphrase, actor, object, action or state change, condition or consequence, verdict, and replacement or retention reason: [cite an exact passage with a line or paragraph number, or write Not applicable: reader-benefit reason]
- Local relevance and paragraph continuity: [cite an exact passage with a line or paragraph number, or write Not applicable: reader-benefit reason]
- Operating mode and object roles, when relevant: [cite an exact passage with a line or paragraph number, or write Not applicable: reader-benefit reason]
- System setup and component relationships: [cite an exact passage with a line or paragraph number, or write Not applicable: reader-benefit reason]
- Representation bridge, when relevant: [cite an exact passage with a line or paragraph number, or write Not applicable: reader-benefit reason]
- Mechanism, calculation, or state change: [cite an exact passage with a line or paragraph number, or write Not applicable: reader-benefit reason]
- Concrete trace or example: [cite an exact passage with a line or paragraph number, or write Not applicable: reader-benefit reason]
- Example setup and conclusion: [cite an exact passage with a line or paragraph number, or write Not applicable: reader-benefit reason]
- Assumptions, limits, trade-offs, or failure modes: [cite an exact passage with a line or paragraph number, or write Not applicable: reader-benefit reason]
- Relevant alternatives, common criteria, and selection or scope: [cite an exact passage with a line or paragraph number, or write Not applicable: reader-benefit reason]
- Essential explanation beyond the checklist: [cite an exact passage with a line or paragraph number, or write Not applicable: reader-benefit reason]
- Result that motivates the next section: [cite an exact passage with a line or paragraph number, or write Not applicable: reader-benefit reason]
- Expert objection: [cite an exact passage with a line or paragraph number, or write Not applicable: reader-benefit reason]
- Verdict: Pending reviewer assessment

For the concrete-wording field, use this form: line N; phrase: ...; paraphrase: ...; actor: ...; object: ...; action: ...; condition or consequence: ...; verdict: retain, revise, or delete; replacement or retention reason: ....
Context review must explain the literal meaning, prerequisites, analogy limits when relevant, and reason for appearing here. If no correction is needed, give a specific retention reason; lint success is not evidence.
For System setup and component relationships, cite the passage and fill: setting: ...; roles: ...; objects and flow: ...; assumptions: ...; verdict: ....
For Relevant alternatives, common criteria, and selection or scope, cite the passage and fill: common problem: ...; options: ...; relationship: ...; criteria: ...; selection or scope: ...; verdict: ....
For Essential explanation beyond the checklist, cite the passage and fill: reader task: ...; dependencies checked: ...; reasoning chain: ...; unresolved: ....
For Expert objection, cite the passage and fill: objection: ...; kind: ...; target: ...; disposition: ...; reason: ....
For system setup and alternatives, an adequate review uses verdict: adequate. Where inapplicable, use Not applicable: line N; reason: <specific reader-benefit reason>.
Expert objection cannot be marked Not applicable. Write the strongest correction a domain expert would make to this unit's text or figures; set kind to correctness or wording; name its target passage or figure label; set disposition to fixed or does not apply; give the reason. An objection of none is not a review. The strongest correction is the one that would change what a reader believes or does. Aim first at what the unit claims: a promise word such as always, once, ensures or remains that is false or needs a condition; a named method described wrongly; code that does not do what the text says; a table cell; a diagnostic sequence that skips a stage; a verb without an actor; a label naming something other than what is drawn; a figure that disagrees with the text or another figure; and example content found in neither the chapter nor its sources. A unit whose claim-bearing content includes code, a table, an equation, or a figure needs a correctness objection; a wording objection alone does not count there.
Claims to check lists the unit's statements most likely to make checkable claims: every table row and every figure or table caption with its alt text, and each sentence with a promise word, a quantity or calculation, code font, a citation, or a section or figure reference. Footnote definitions are left to the citation checks. When packets compare with a revision, every changed statement is listed first and marked changed. For each claim, set verdict to true as written, condition stated, fixed, or not a claim, and after checked: say how it was checked, such as the code test, the recomputation, or the source and its location. The list is a floor, not the extent of the review.
For each code listing, write test: followed by the path, relative to the guide, of a test that runs it on the inputs the text makes claims about, or not run: followed by the reason and how its claims were checked instead.
Essential explanation cannot be marked Not applicable. Trace the reader's task and its dependencies, including gaps not covered by other fields. Record unresolved: none only after resolving essential gaps; otherwise describe them and keep the unit verdict open. A complete checklist is not proof of complete teaching.
