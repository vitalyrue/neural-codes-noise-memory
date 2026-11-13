# Pedagogy Review Packet: Front Matter and Appendices

This packet covers front matter and appendices. Short reference pages may use a shorter teaching form only when their linked teaching location has already established the reader's decision.

A reviewer must cite exact passages before marking a requirement as satisfied.
Use a line or paragraph number and a short explanation. Use `Not applicable: <reader-benefit reason>` only when the requirement truly does not apply.

## ch:READING-GUIDE - What the three papers establish

Source file: `content/chapters/00-reading-guide.md`

Purpose: These neuroscience papers study memory, eye control, and navigation. Their settings are mathematical models of stored values, eye-movement and neural recordings from macaque monkeys, and recordings of location-dependent neural activity in rodents and bats. This reading guide explains each study’s question, methods, findings, and limits.

Prerequisites: None recorded

Sidecar sections: Variable neural signals must support reliable behavior, Persistent activity can still lose memory accuracy, Eye drift points to a shared neural source, Smooth random maps explain the variety of place fields, Starting knowledge and reading paths, Neural mechanisms and mathematical derivations answer different questions, How to interpret the calculations and evidence, The original papers

Blocks: 0 figure(s), 0 equation(s), 0 code block(s)

Result labels: No Answer/Conclusion/Feedback label detected

<!-- pedagogy-unit: content/chapters/00-reading-guide.md::ch:READING-GUIDE -->

### Chapter opening

Location: line 1, anchor `ch:READING-GUIDE`

First content kind: `prose`

Opening passage line: 3
Closing passage line: 3

Paragraphs in source order (complete `PARAGRAPH_REVIEW.json`):

<!-- pedagogy-paragraph: p3 sha256 d25e4c56c1d3824d29333ac2a32b04595f82c0bf9e02af866f9da73ff39ebd72 -->
p3, lines 3-3; prose; priority: unchanged; previous: none; next: p7

> The subject is neuroscience: how groups of nerve cells represent information used in memory, eye control, and navigation. The three papers examine mathematical models that store a quantity such as an angle, eye movements and neural activity recorded in macaque monkeys, and location-dependent neural activity recorded in rodents and bats. [They ask how activity can retain a value, how an internal fluctuation can move the eyes, and why a cell can respond at several separate locations.]{.key-statement}


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

<!-- pedagogy-unit: content/chapters/00-reading-guide.md::sec:READING-FIELD -->

### Variable neural signals must support reliable behavior

Location: line 5, anchor `sec:READING-FIELD`

First content kind: `prose`

Opening passage line: 7
Closing passage line: 7

Paragraphs in source order (complete `PARAGRAPH_REVIEW.json`):

<!-- pedagogy-paragraph: p7 sha256 41eaa4768185b500f3520cd9b2324fb2ecc03c6ed56d8a341c9021870e41479f -->
p7, lines 7-7; prose; priority: unchanged; previous: p3; next: p11

> A remembered direction must remain useful after its cue disappears; the eyes must hold an angle while an animal looks at a target; a moving animal must keep track of where it is. These tasks depend on groups of [[**neuron**]{.definition-term custom-style="Definition Term"}s, the brain's signaling cells]{.definition-explanation}, whose electrical signals are brief and variable. Computational and systems neuroscience studies how these cells and their interactions support such behavior. Mathematical models connect assumptions about cells and their interactions to predictions; recordings test those predictions against neural activity and movement.


Claim-bearing content: none

Claims to check:

- Claim c1, line 7: "A remembered direction must remain useful after its cue disappears; the eyes must hold an angle while an animal looks at a target; a moving animal must keep track of where it is." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]

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

<!-- pedagogy-unit: content/chapters/00-reading-guide.md::sec:READING-MEMORY -->

### Persistent activity can still lose memory accuracy

Location: line 9, anchor `sec:READING-MEMORY`

First content kind: `prose`

Opening passage line: 11
Closing passage line: 15

Paragraphs in source order (complete `PARAGRAPH_REVIEW.json`):

<!-- pedagogy-paragraph: p11 sha256 edfccd0e3ddc97393e8c34648e4e3332551e05b64aff1baa08d2180397f1dc35 -->
p11, lines 11-11; prose; priority: unchanged; previous: p7; next: p13

> Burak and Fiete (2012) study short-term memory for a continuous quantity, such as a direction or eye angle. A proposed mechanism is that interacting neurons keep activity going after the original input ends. [Yet the remembered value can change while the activity persists.]{.key-statement} The problem is to explain how the properties of the cells and their connections set the rate of this loss of accuracy.

<!-- pedagogy-paragraph: p13 sha256 faecfa341c8fc0b24bb8eff894231fb32aa29457ffdd4dfe2e2ee9df76f7fad7 -->
p13, lines 13-13; prose; priority: unchanged; previous: p11; next: p15

> The authors analyze a network with a continuous family of persistent activity patterns, each representing a different value. Each cell sends signals at random times. They use an approximation for small fluctuations to derive how these signals move the stored value, compare the calculation with network simulations, and relate the motion to the best accuracy possible when estimating the stored value from those signals.

<!-- pedagogy-paragraph: p15 sha256 f446d223399963411a41106f2201bc2318b1eb2a63c8070d2dcfdb6c18742938 -->
p15, lines 15-15; prose; priority: unchanged; previous: p13; next: p19

> [Their central result is a lower bound: the uncertainty in reading the network's current value limits how slowly that value can wander.]{.key-statement} Under the model's assumptions, the variance of the memory error grows with storage time. Reading for longer also has diminishing benefit because the state continues moving during observation. This gives a benchmark for evaluating proposed memory circuits and their recall errors. It applies to the analyzed family of continuous-state memory models, with the required noise assumptions and no external signal anchoring the value. Chapters 3–6 develop the [diffusion calculation](../chapters/ch-memory-dynamics.html), its long-delay behavior, the [information bound](../chapters/ch-memory-information.html), and the limits of [readout](../chapters/ch-memory-readout.html).[^orientation-memory]


Claim-bearing content: none

Claims to check:

- Claim c1, line 13: "They use an approximation for small fluctuations to derive how these signals move the stored value, compare the calculation with network simulations, and relate the motion to the best accuracy possible when estimating the stored value from those signals." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c2, line 15: "Chapters 3–6 develop the [diffusion calculation](../chapters/ch-memory-dynamics.html), its long-delay behavior, the [information bound](../chapters/ch-memory-information.html), and the limits of [readout](../chapters/ch-memory-readout.html).[^orientation-memory]" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]

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

<!-- pedagogy-unit: content/chapters/00-reading-guide.md::sec:READING-EYE -->

### Eye drift points to a shared neural source

Location: line 17, anchor `sec:READING-EYE`

First content kind: `prose`

Opening passage line: 19
Closing passage line: 23

Paragraphs in source order (complete `PARAGRAPH_REVIEW.json`):

<!-- pedagogy-paragraph: p19 sha256 c44b940c0a9fc4c6d3df6158a4a411b9f5fc524801819bcb5a8182b88d40d881 -->
p19, lines 19-19; prose; priority: unchanged; previous: p15; next: p21

> [Even while gaze is held on a stationary target, the eyes move smoothly and irregularly between brief, rapid movements. This smooth motion is called [**fixational drift**]{.definition-term custom-style="Definition Term"}.]{.definition-explanation} It changes the image reaching the [[**retina**]{.definition-term custom-style="Definition Term"}, the light-sensitive tissue at the back of the eye]{.definition-explanation}. Understanding its source is therefore part of understanding the visual signals the brain receives. [Ben-Shushan and colleagues (2022) ask whether the motion begins mainly in muscles or in neural commands sent to them.]{.key-statement}

<!-- pedagogy-paragraph: p21 sha256 5530c40e518e38fdbdccbcf5180ae5ed6120bf2272a2eb05161d77496a5aada5 -->
p21, lines 21-21; prose; priority: unchanged; previous: p19; next: p23

> They reanalyze recordings from 57 neurons that send commands to eye muscles in two macaques, paired with precise eye-position measurements. They first calibrate the relation between each cell's activity and larger eye movements. They then use it during fixation to compare the movement predicted from one cell with the measured movement. A separate circuit model tests whether a wandering stored eye-position command could explain the movement's amplitude and time dependence.

<!-- pedagogy-paragraph: p23 sha256 0bfe93e919031032888f91408c30269d9f84873f4daaaf2896dc087a64c92387 -->
p23, lines 23-23; prose; priority: unchanged; previous: p21; next: p27

> For 350-millisecond intervals, their analysis estimates that about 82% of horizontal displacement variance comes from a common source before the final motor neurons, assuming the fitted movement relation also holds during fixation and the relevant noise contributions do not vary together. This supports a central neural contribution to drift. The memory-circuit model provides a possible explanation of that contribution, linking an internal storage error to observable behavior. The recordings do not uniquely locate the noise inside that memory circuit. Chapters 7–9 separate the [shared-drive inference](../chapters/ch-eye-drift.html), the [timing of drift](../chapters/ch-eye-timing.html), and the [proposed circuit mechanism](../chapters/ch-eye-circuit.html).[^orientation-eye]


Claim-bearing content: none

Claims to check:

- Claim c1, line 23: "For 350-millisecond intervals, their analysis estimates that about 82% of horizontal displacement variance comes from a common source before the final motor neurons, assuming the fitted movement relation also holds during fixation and the relevant noise contributions do not vary together." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c2, line 23: "Chapters 7–9 separate the [shared-drive inference](../chapters/ch-eye-drift.html), the [timing of drift](../chapters/ch-eye-timing.html), and the [proposed circuit mechanism](../chapters/ch-eye-circuit.html).[^orientation-eye]" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]

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

<!-- pedagogy-unit: content/chapters/00-reading-guide.md::sec:READING-PLACE -->

### Smooth random maps explain the variety of place fields

Location: line 25, anchor `sec:READING-PLACE`

First content kind: `prose`

Opening passage line: 27
Closing passage line: 33

Paragraphs in source order (complete `PARAGRAPH_REVIEW.json`):

<!-- pedagogy-paragraph: p27 sha256 c09c4f7a8643281520a275e35c1865f5774cf18979b161d7d05fb5a5d59b933a -->
p27, lines 27-27; prose; priority: unchanged; previous: p23; next: p29

> [A [**place cell**]{.definition-term custom-style="Definition Term"} in the [**hippocampus**]{.definition-term custom-style="Definition Term"}, a brain region involved in memory and navigation, becomes more active in particular locations.]{.definition-explanation} [Each connected region of elevated activity is a [**place field**]{.definition-term custom-style="Definition Term"}.]{.definition-explanation} Small environments encouraged a picture of one smooth field per cell. Larger environments reveal multiple fields with widely varying sizes and shapes. [Mainali, Azeredo da Silveira, and Burak (2025) ask whether one statistical account can explain this variety across species and spatial dimensions.]{.key-statement}

<!-- pedagogy-paragraph: p29 sha256 aa56fe28c5ef630ebb8b8df1d603bec472e16ce43a8ce2d733efd11be9e81e28 -->
p29, lines 29-29; prose; priority: unchanged; previous: p27; next: p31

> Their model gives each cell a smooth random function of location and allows activity where that function exceeds a threshold. The authors derive predictions for the resulting regions, simulate the model, and compare it with existing rodent and bat recordings from one-, two- and three-dimensional environments. Parameters fitted to field sizes and their spatial arrangement also support further tests of field shapes and connectedness.

<!-- pedagogy-paragraph: p31 sha256 a454cec32b8bafcb32c610ccd91d2b440052a5f475f34105f2b9bd85e27a5c46 -->
p31, lines 31-31; prose; priority: unchanged; previous: p29; next: p33

> The model explains different size distributions across dimensions and predicts additional features, such as multiple peaks within a field and inactive holes surrounded by activity. This makes irregular spatial responses quantitatively understandable and supports a common statistical description across the examined settings. Such statistics can arise when cells combine many inputs through largely random connections. The study does not directly measure those connections. Chapters 10–12 develop the [spatial model](../chapters/ch-place-fields.html), its [size and shape predictions](../chapters/ch-place-sizes.html), and the [tests and circuit interpretation](../chapters/ch-place-tests.html). They distinguish exact predictions, limiting approximations and empirical comparisons.[^orientation-place]

<!-- pedagogy-paragraph: p33 sha256 273375240276c08361d11f19a54fbd55abd5b1782bdcfbba08c7de99f8071133 -->
p33, lines 33-33; prose; priority: unchanged; previous: p31; next: p37

> The three contributions therefore have different meanings: a mathematical constraint on memory models, evidence about the source of eye movement, and a statistical explanation of spatial activity. Together they show how a representation can be described, maintained and related to behavior. Combining all three in one biological circuit remains a further research question, developed in [Chapter 13](../chapters/ch-synthesis.html).


Claim-bearing content: none

Claims to check:

- Claim c1, line 27: "[A [**place cell**]{.definition-term custom-style="Definition Term"} in the [**hippocampus**]{.definition-term custom-style="Definition Term"}, a brain region involved in memory and navigation, becomes more active in particular locations.]{.definition-explanation} [Each connected region of elevat..." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c2, line 31: "They distinguish exact predictions, limiting approximations and empirical comparisons.[^orientation-place]" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c3, line 33: "Combining all three in one biological circuit remains a further research question, developed in [Chapter 13](../chapters/ch-synthesis.html)." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]

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

Location: line 35, anchor `sec:READING-START`

First content kind: `prose`

Opening passage line: 37
Closing passage line: 54

Paragraphs in source order (complete `PARAGRAPH_REVIEW.json`):

<!-- pedagogy-paragraph: p37 sha256 5ca083045699b13d6b19227b2c3c9323a35f95544eca11bf397b9abac77023a5 -->
p37, lines 37-37; prose; priority: unchanged; previous: p33; next: p39

> The guide assumes undergraduate calculus, basic probability, and linear algebra. Neuroscience terms and the required stochastic-process, information, filtering, and random-field ideas are taught where needed. The reading path builds from the signals to the models and then their tests:

<!-- pedagogy-paragraph: p39 sha256 7c3aad18df4ab4066939ae937f6b1adb5213d2f842236cb6ca986d45a5b6cc52 -->
p39, lines 39-39; list_item; priority: unchanged; previous: p37; next: p40

> **Chapters 1–2:** establish [neural signals and variability](../chapters/ch-foundations.html), then [persistence and accumulated error](../chapters/ch-persistence.html).

<!-- pedagogy-paragraph: p40 sha256 3c4a824b67c774a220318f9a6a2b68ab74086f29731a712f1c868d8c9a54f035 -->
p40, lines 40-40; list_item; priority: unchanged; previous: p39; next: p41

> **Chapters 3–6:** derive memory diffusion, its long-delay behavior, the information bound, and readout.

<!-- pedagogy-paragraph: p41 sha256 43670723cb13a65840d96bd9f742f0b02134cb5d5f1f87d1262270d1b45c1b44 -->
p41, lines 41-41; list_item; priority: unchanged; previous: p40; next: p42

> **Chapters 7–9:** follow the eye study from shared-drive evidence through timing to a circuit model.

<!-- pedagogy-paragraph: p42 sha256 100ca4dd2ec84445fd887c17bab1cac8dbe652870f006fee61d5f0ca9e7f6206 -->
p42, lines 42-42; list_item; priority: unchanged; previous: p41; next: p43

> **Chapters 10–12:** develop spatial maps, their size predictions, and tests of their shapes and possible origins.

<!-- pedagogy-paragraph: p43 sha256 3a8541a9007de7b515534641d8fa4afa9a2a75ca55268d19c5e0a9df58a9ca56 -->
p43, lines 43-43; list_item; priority: unchanged; previous: p42; next: p45

> **Chapter 13:** connect the results and compare related work.

<!-- pedagogy-paragraph: p45 sha256 da856a718653ae796b8937456e1054d44cec71dfc4c2e5fa7c34763f6b66c09e -->
p45, lines 45-45; prose; priority: unchanged; previous: p43; next: p47

> For a path focused on particular papers:

<!-- pedagogy-paragraph: p47 sha256 1c7b5b703071ad02e7834f93f8d94063538a0f51eef22669ca3fdd66f81ac49d -->
p47, lines 47-47; list_item; priority: unchanged; previous: p45; next: p48

> **Memory and eye drift:** follow chapters 1 through 9 in order.

<!-- pedagogy-paragraph: p48 sha256 e0705d1b7787a44801faa8a671d8cbceab376e735359aef22745946975c37d68 -->
p48, lines 48-48; list_item; priority: unchanged; previous: p47; next: p50

> **Place fields:** read the two foundations chapters and then chapters 10–12. The spatial calculation does not require the readout derivation in chapter 6.

<!-- pedagogy-paragraph: p50 sha256 72f4bc943ca86ad5b01706bb4d619cdac016993b926d9b203c2ca5f3e9562db6 -->
p50, lines 50-50; prose; priority: unchanged; previous: p48; next: p52

> The Glossary gives short definitions for lookup after their first explanation. The References section gives full source details. The original paper figures are discussed by number and can be inspected in the linked PDFs.

<!-- pedagogy-paragraph: p52 sha256 3b736e6f98e0182dc2cd96d3e2611f7dc8070d8f657008ff9053c2f10dee72ba -->
p52, lines 52-52; prose; priority: unchanged; previous: p50; next: p54

> After the foundations, the [guide map](../chapters/ch-persistence.html#fig-foundations-paper-map) shows the three paper questions together.

<!-- pedagogy-paragraph: p54 sha256 27b11a655b45e3129ba6d3275aa01ccdd6c295aac15cb7be95a4e120a9791f07 -->
p54, lines 54-54; prose; priority: unchanged; previous: p52; next: p58

> On a first reading, follow the main text, figures, assumptions, and results. The expandable notes preserve longer calculations and extensions; open one when you want to check the steps behind a result. The explanations needed for the next section remain in the main text.


Claim-bearing content: none

Claims to check:

- Claim c1, line 43: "**Chapter 13:** connect the results and compare related work." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c2, line 54: "The explanations needed for the next section remain in the main text." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]

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

<!-- pedagogy-unit: content/chapters/00-reading-guide.md::sec:READING-MECHANISM-MATH -->

### Neural mechanisms and mathematical derivations answer different questions

Location: line 56, anchor `sec:READING-MECHANISM-MATH`

First content kind: `prose`

Opening passage line: 58
Closing passage line: 72

Paragraphs in source order (complete `PARAGRAPH_REVIEW.json`):

<!-- pedagogy-paragraph: p58 sha256 b46f839672ffffcea03cd46015850e008b76fd5de1c742fec5bb473fba936fe0 -->
p58, lines 58-58; prose; priority: unchanged; previous: p54; next: p60

> Chapters 3–6 explain [how interacting neurons can retain a value while random spike timing changes it.]{.key-statement} Their treatment of the Burak and Fiete appendix separates three parts of each substantial topic:

<!-- pedagogy-paragraph: p60 sha256 8ab345eb7450ba740136acba175f63038d7d09a21cbb621e391e12e359f6233e -->
p60, lines 60-60; list_item; priority: unchanged; previous: p58; next: p61

> **Neural mechanism:** which cells and signals interact, what changes, and which features are assumptions of the model. For readout, this part also states what an observer can measure and which value it must estimate.

<!-- pedagogy-paragraph: p61 sha256 123c9da49a0a0aa5148695e62c266506c7acc84615a1b18eb158103051d5dec8 -->
p61, lines 61-61; list_item; priority: unchanged; previous: p60; next: p62

> **Mathematical derivation:** the general tool, its conditions, and the calculation after neural quantities are assigned to the symbols.

<!-- pedagogy-paragraph: p62 sha256 da61f255b7a10d5a925ba26468dc7772a5cc2ffbfd89d8c99913db31879e9265 -->
p62, lines 62-62; list_item; priority: unchanged; previous: p61; next: p64

> **Interpretation:** what the result predicts about memory or readout, and what its assumptions leave unresolved.

<!-- pedagogy-paragraph: p64 sha256 7153efee5e6077acae3f25a95ae94eb8d3a6509a37739558c7e554dd2df332ab -->
p64, lines 64-64; prose; priority: unchanged; previous: p62; next: p66

> [An equation that specifies how a cell responds belongs to the model. A derivation works out what follows from that choice.]{.key-statement}

<!-- pedagogy-paragraph: p66 sha256 9e54b6003b4941f77164fc5209ca0e3872519197152f7659f8fb17c24fb5a3ae -->
p66, lines 66-66; prose; priority: unchanged; previous: p64; next: p68

> For example, a spike can disturb several cells' activity. The circuit's interactions remove some changes, while others leave the represented angle displaced. Linear algebra calculates which part survives; probability gives the spread of that displacement. The result then predicts how quickly memory errors accumulate in this model. The mathematical tools also apply to other systems, but this neural prediction depends on the circuit and spike statistics used in the calculation.

<!-- pedagogy-paragraph: p68 sha256 463566cc3c1ee58c500794f4a3af422151c1fa08b53e6196b21a306f04064eb5 -->
p68, lines 68-68; prose; priority: unchanged; previous: p66; next: p70

> The same distinction matters for readout. A calculation of the best possible estimate sets a benchmark under specified access to neural signals. Establishing that an animal's neurons implement the assumed computation requires separate evidence.

<!-- pedagogy-paragraph: p70 sha256 1b6f34504accd133b26e2c9c16430f015d8b97dae6c6da4d69c3d5c642d3f977 -->
p70, lines 70-70; prose; priority: unchanged; previous: p68; next: p72

> For a first conceptual pass, read the mechanism, inspect the displayed result and its variables, then read the interpretation. Follow the mathematical derivation when you want to understand why the result holds or calculate with it. Assumptions remain part of both readings.

<!-- pedagogy-paragraph: p72 sha256 8f658c5382ac8b01ddfa3e11f9378e0a20ee9d34a65cad7dbb3b9906b45d8e20 -->
p72, lines 72-72; prose; priority: unchanged; previous: p70; next: p78

> The [PNAS appendix](https://www.pnas.org/action/downloadSupplement?doi=10.1073%2Fpnas.1117386109&file=Appendix.pdf) supplies both neural-model choices and mathematical arguments. This map links its seven sections to the guide's explanations. Page links open the local copy; the guide sometimes uses an equivalent teaching derivation and identifies source inconsistencies beside the affected calculation.


Claim-bearing content: table

Claims to check:

- Claim c1, line 60: "For readout, this part also states what an observer can measure and which value it must estimate." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c2, line 70: "Assumptions remain part of both readings." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c3, line 72: "The [PNAS appendix](https://www.pnas.org/action/downloadSupplement?doi=10.1073%2Fpnas.1117386109&file=Appendix.pdf) supplies both neural-model choices and mathematical arguments." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c4, line 74: "Caption: Reading map for the Burak and Fiete supporting text. Page numbers refer to the appendix PDF." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c5, line 74: "| Appendix section: [I: large-network limit, p. 1](../papers/burak-fiete-2012-persistent-activity-si.pdf#page=1) | Neural question: How can many variable spike inputs produce small fluctuations in total input? | Mathematical explanation in the guide: [Mean and variance scaling; Gaussian approxima..." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c6, line 74: "| Appendix section: [II: diffusion coefficient, p. 3](../papers/burak-fiete-2012-persistent-activity-si.pdf#page=3) | Neural question: Which changes in neural activity leave the stored value displaced? | Mathematical explanation in the guide: [Linearization and projection](../chapters/ch-memory-d..." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c7, line 74: "| Appendix section: [III: motion along the attractor, p. 6](../papers/burak-fiete-2012-persistent-activity-si.pdf#page=6) | Neural question: How do memory errors grow over long delays or around an angular range? | Mathematical explanation in the guide: [Probability-density evolution and boundary..." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c8, line 74: "| Appendix section: [IV: internal Fisher information, p. 9](../papers/burak-fiete-2012-persistent-activity-si.pdf#page=9) | Neural question: How well can nearby stored values be distinguished from their spikes? | Mathematical explanation in the guide: [Spike likelihood and information per unit ti..." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c9, line 74: "| Appendix section: [V: information–diffusion inequality, p. 10](../papers/burak-fiete-2012-persistent-activity-si.pdf#page=10) | Neural question: How does uncertainty in the circuit’s own spikes constrain memory stability? | Mathematical explanation in the guide: [Scalar and matrix bounds, with..." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c10, line 74: "| Appendix section: [VI: readout, p. 12](../papers/burak-fiete-2012-persistent-activity-si.pdf#page=12) | Neural question: How much does longer observation help when the stored value keeps moving? | Mathematical explanation in the guide: [Storage and readout error](../chapters/ch-memory-readout.h..." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c11, line 74: "| Appendix section: [VII: model extensions, p. 17](../papers/burak-fiete-2012-persistent-activity-si.pdf#page=17) | Neural question: What changes when firing rates respond gradually or the noise law changes? | Mathematical explanation in the guide: [Two time scales and alternative noise statistic..." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]

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

### How to interpret the calculations and evidence

Location: line 76, anchor `sec:READING-SCOPE`

First content kind: `prose`

Opening passage line: 78
Closing passage line: 84

Paragraphs in source order (complete `PARAGRAPH_REVIEW.json`):

<!-- pedagogy-paragraph: p78 sha256 58aa7ee6a2dc1d3760f171fad7b705936f9b2dbb74cab5cf84f6ccc40aefd4eb -->
p78, lines 78-78; prose; priority: unchanged; previous: p72; next: p80

> Examples chosen for the guide distinguish independent from shared fluctuations, complete from limited access to neural signals, and exact formulas from approximations for rare fields. Their numbers are checked separately from the published experimental measurements. A teaching reconstruction is labeled when its simplified model differs from the paper's full model.

<!-- pedagogy-paragraph: p80 sha256 506f5ca021cc9c9bbe4199cc5166f82b50d8c7c7923323781ba6d3aaedae3a5b -->
p80, lines 80-80; prose; priority: unchanged; previous: p78; next: p82

> The guide explains how to interpret the experiments and their figures. It does not rerun the original animal recordings, data processing, or full neural-network simulations. [A successful numerical check of a probability identity is different from an independent reproduction of a paper's empirical result.]{.key-statement} Related work is selected to clarify the assumptions and alternatives rather than to claim an exhaustive literature search.

<!-- pedagogy-paragraph: p82 sha256 0e7eef1e0f47774e05331a6a6314a5161aa3aeaee62c7f621ce1d6c1cf05a304 -->
p82, lines 82-82; prose; priority: unchanged; previous: p80; next: p84

> Throughout the guide, $D$ denotes the [[**diffusion coefficient**]{.definition-term custom-style="Definition Term"}, which sets how quickly uncertainty spreads]{.definition-explanation}. In the basic one-dimensional model, $D$ is constant, neither direction is favored, and no boundary limits the motion. Its [[**mean squared displacement**]{.definition-term custom-style="Definition Term"} (MSD), the average squared change in the represented coordinate after elapsed time $t$]{.definition-explanation}, is $2Dt$. [Chapter 2](../chapters/ch-persistence.html#sec-foundations-diffusion) explains this model and its assumptions.

<!-- pedagogy-paragraph: p84 sha256 2f270b131b5f9c540d30adfdd0819901ca25d9d043288c3c0b01bcc052956a1c -->
p84, lines 84-84; prose; priority: unchanged; previous: p82; next: p86

> The other recurring symbols are:

<!-- pedagogy-paragraph: p86 sha256 f0b9eafe783112b3d284e08a74a6683d885d467cd5bb00ba7aa38885a755fb67 -->
p86, lines 86-86; list_item; priority: unchanged; previous: p84; next: p87

> $d$: spatial dimension.

<!-- pedagogy-paragraph: p87 sha256 ed450a7255de7003923f2e5cdd1acc62bc0d3dbe63dbcfefa10a1d677b5b6551 -->
p87, lines 87-87; list_item; priority: unchanged; previous: p86; next: p88

> $\theta$: the represented coordinate in the memory chapters.

<!-- pedagogy-paragraph: p88 sha256 ff2491df8146e9ec6749f16801009940dec0cda8ce0751e9f228439bb071249f -->
p88, lines 88-88; list_item; priority: unchanged; previous: p87; next: p89

> $q$: the normalized threshold in the place-field chapters, called $\theta$ in that paper.

<!-- pedagogy-paragraph: p89 sha256 0f23a6991ea9d33504983cb1645f9e6ff93aaa999e0b7f26bcd06381a60a1c30 -->
p89, lines 89-89; list_item; priority: unchanged; previous: p88; next: p93

> $C$: the spatial covariance in the place-field chapters.


Claim-bearing content: none

Claims to check:

- Claim c1, line 82: "[Chapter 2](../chapters/ch-persistence.html#sec-foundations-diffusion) explains this model and its assumptions." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]

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

Location: line 91, anchor `sec:READING-PAPERS`

First content kind: `prose`

Opening passage line: 93
Closing passage line: 99

Paragraphs in source order (complete `PARAGRAPH_REVIEW.json`):

<!-- pedagogy-paragraph: p93 sha256 2acb2a0d0b50d9774bd90f9e061cdc197f64556636feeb643c84175277b9a73d -->
p93, lines 93-93; prose; priority: unchanged; previous: p89; next: p95

> The copies are the published versions. Supporting information is linked separately.

<!-- pedagogy-paragraph: p95 sha256 5c1400cf7189b43399a8bae5d7bd14b2f13f734fd84e441d75af45953db1260b -->
p95, lines 95-95; list_item; priority: unchanged; previous: p93; next: p96

> **Burak and Fiete (2012):** [Paper PDF](../papers/burak-fiete-2012-persistent-activity.pdf) and [20-page supporting information PDF](../papers/burak-fiete-2012-persistent-activity-si.pdf). *Fundamental limits on persistent activity in networks of noisy neurons*. PNAS, 109(43), 17645–17650. [Published DOI](https://doi.org/10.1073/pnas.1117386109). The local main PDF uses the six-page Early Edition layout, so PDF page locators run from 1 to 6.

<!-- pedagogy-paragraph: p96 sha256 97b7cb44540829c1477760d342a1bde9778edfd0a73c427829330b418a449920 -->
p96, lines 96-96; list_item; priority: unchanged; previous: p95; next: p97

> **Ben-Shushan, Shaham, Joshua, and Burak (2022):** [Paper PDF](../papers/ben-shushan-2022-fixational-drift.pdf), [supplementary notes and figures PDF](../papers/ben-shushan-2022-supplement-1.pdf), and [open peer review PDF](../papers/ben-shushan-2022-supplement-2.pdf). *Fixational drift is driven by diffusive dynamics in central neural circuitry*. Nature Communications, 13, 1697. [Published DOI](https://doi.org/10.1038/s41467-022-29201-y). Ben-Shushan and Shaham contributed equally.

<!-- pedagogy-paragraph: p97 sha256 968b6545e1321cef300a98a9c4e4f457735a720837b2f439b4cd887b6bd1cab7 -->
p97, lines 97-97; list_item; priority: unchanged; previous: p96; next: p99

> **Mainali, Azeredo da Silveira, and Burak (2025):** [Paper and STAR Methods PDF](../papers/mainali-2025-universal-statistics.pdf) and [supplementary figures and Methods S1–S4 PDF](../papers/mainali-2025-supplement.pdf). *Universal statistics of hippocampal place fields across species and dimensionalities*. Neuron, 113(7), 1110–1120.e3. [Published DOI](https://doi.org/10.1016/j.neuron.2025.01.017). The main PDF has a cover before the article; guide citations distinguish printed and PDF page numbers when needed.

<!-- pedagogy-paragraph: p99 sha256 fe5d7ef4e9edc5abfe0fc3fc7e871a23f6bfe9742e9aabd47cdd5b25aa8400ae -->
p99, lines 99-99; prose; priority: unchanged; previous: p97; next: none

> These links open PDF files. The supporting-information copies preserve their original formulas. Several printed intermediate equations require care; the guide identifies apparent inconsistencies beside the affected calculations and follows an explicitly shown derivation. Such observations are independent mathematical checks, not author-confirmed corrections.


Claim-bearing content: none

Claims to check:

- Claim c1, line 95: "**Burak and Fiete (2012):** [Paper PDF](../papers/burak-fiete-2012-persistent-activity.pdf) and [20-page supporting information PDF](../papers/burak-fiete-2012-persistent-activity-si.pdf)." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c2, line 95: "[Published DOI](https://doi.org/10.1073/pnas.1117386109)." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c3, line 96: "**Ben-Shushan, Shaham, Joshua, and Burak (2022):** [Paper PDF](../papers/ben-shushan-2022-fixational-drift.pdf), [supplementary notes and figures PDF](../papers/ben-shushan-2022-supplement-1.pdf), and [open peer review PDF](../papers/ben-shushan-2022-supplement-2.pdf)." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c4, line 96: "[Published DOI](https://doi.org/10.1038/s41467-022-29201-y)." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c5, line 97: "**Mainali, Azeredo da Silveira, and Burak (2025):** [Paper and STAR Methods PDF](../papers/mainali-2025-universal-statistics.pdf) and [supplementary figures and Methods S1–S4 PDF](../papers/mainali-2025-supplement.pdf)." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c6, line 97: "[Published DOI](https://doi.org/10.1016/j.neuron.2025.01.017)." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]

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

<!-- pedagogy-paragraph: p5 sha256 9929e0c8265e8ebd8d733c457615ea7e3cedfb80006e76c685e0760ecc61c4ea -->
p5, lines 5-5; list_item; priority: unchanged; previous: p3; next: p6

> [[**abducens nucleus:**]{.definition-term custom-style="Definition Term"} A brainstem group containing the motor neurons recorded in the eye-drift study; their axons activate the lateral rectus eye muscle.]{.definition-explanation}

<!-- pedagogy-paragraph: p6 sha256 436969ac3aea1ede3770b6ff0555410bb5b979439e2178605122fde9e9b907c2 -->
p6, lines 6-6; list_item; priority: unchanged; previous: p5; next: p7

> [[**activity bump:**]{.definition-term custom-style="Definition Term"} A localized peak of population firing rates across neurons ordered by their preferred represented values.]{.definition-explanation}

<!-- pedagogy-paragraph: p7 sha256 6e58bc67ccdc2dddcc3c1ffb5c7902ccd4dfccc5214b846903b21661fa927b71 -->
p7, lines 7-7; list_item; priority: unchanged; previous: p6; next: p8

> [[**attractor manifold:**]{.definition-term custom-style="Definition Term"} The continuous family of persistent activity states, described by its represented coordinates rather than by every neural activity separately.]{.definition-explanation}

<!-- pedagogy-paragraph: p8 sha256 eda2de8dba8b87793250c46bbaed2c2db3d2ed6db04caed49ef95285ae81a28b -->
p8, lines 8-8; list_item; priority: unchanged; previous: p7; next: p9

> [[**Betti numbers:**]{.definition-term custom-style="Definition Term"} Counts of independent connected components, loops, cavities, and their higher-dimensional counterparts.]{.definition-explanation}

<!-- pedagogy-paragraph: p9 sha256 8085572fce5f8b517c7a76d91fcc4777b65efcb3f3a59fae59efa6c3dd832dbd -->
p9, lines 9-9; list_item; priority: unchanged; previous: p8; next: p10

> [[**Brownian motion:**]{.definition-term custom-style="Definition Term"} A continuous random process starting at zero with independent Gaussian increments of mean zero and variance equal to elapsed time.]{.definition-explanation}

<!-- pedagogy-paragraph: p10 sha256 9ac3c616539093730a79df77798e869553c3ee60de8829c6fce62e5ce81a08df -->
p10, lines 10-10; list_item; priority: unchanged; previous: p9; next: p11

> [[**causal filter:**]{.definition-term custom-style="Definition Term"} A rule whose current output depends only on present and past input.]{.definition-explanation}

<!-- pedagogy-paragraph: p11 sha256 a404a0bc8831c549fb19cf0442278bedf031e6e012dd96907f5fdb35ce13ad66 -->
p11, lines 11-11; list_item; priority: unchanged; previous: p10; next: p12

> [[**coefficient of determination:**]{.definition-term custom-style="Definition Term"} For the optimal linear prediction with an intercept, the fraction of response variance removed by prediction; with one predictor it equals the squared correlation.]{.definition-explanation}

<!-- pedagogy-paragraph: p12 sha256 223fa3660e8de28ab1e424112dc64671d47dbfc17d8e34ef5645d074d2364fd8 -->
p12, lines 12-12; list_item; priority: unchanged; previous: p11; next: p13

> [[**coefficient of variation:**]{.definition-term custom-style="Definition Term"} Standard deviation divided by mean; in the spike-train discussion it is applied to interspike intervals.]{.definition-explanation}

<!-- pedagogy-paragraph: p13 sha256 5f0a11e6ce9d21e6283a88c124bbd248f451f55a9071e96b1a24cf5ea374fb5b -->
p13, lines 13-13; list_item; priority: unchanged; previous: p12; next: p14

> [[**continuous attractor:**]{.definition-term custom-style="Definition Term"} A continuous family of fixed points with restoring dynamics toward the family and neutral motion along it in the ideal deterministic model.]{.definition-explanation}

<!-- pedagogy-paragraph: p14 sha256 e389027ee70e6cf13f0ca3cd0cc3b255c20c6e94525f9c4ac0568e01fd768b39 -->
p14, lines 14-14; list_item; priority: unchanged; previous: p13; next: p15

> [[**convolution:**]{.definition-term custom-style="Definition Term"} An integral or sum combining past input values with a shifted response kernel to obtain a filtered output.]{.definition-explanation}

<!-- pedagogy-paragraph: p15 sha256 308eb850d27797196dc7890621e8606ec06384be49389f0c849c608d9a9ea2c9 -->
p15, lines 15-15; list_item; priority: unchanged; previous: p14; next: p16

> [[**correlation coefficient:**]{.definition-term custom-style="Definition Term"} Covariance divided by the product of standard deviations; a dimensionless measure of linear association.]{.definition-explanation}

<!-- pedagogy-paragraph: p16 sha256 849a4920653c2b9a85d798e477852f0177e561c6228170e067f1a80792ac6458 -->
p16, lines 16-16; list_item; priority: unchanged; previous: p15; next: p17

> [[**covariance:**]{.definition-term custom-style="Definition Term"} The mean product of two centered random variables, measuring their shared variation.]{.definition-explanation}

<!-- pedagogy-paragraph: p17 sha256 89c84732df5de1e7435ea58efcf6c5230227d94684eb54d2911e58eff5cf12c9 -->
p17, lines 17-17; list_item; priority: unchanged; previous: p16; next: p18

> [[**Cramér Rao bound:**]{.definition-term custom-style="Definition Term"} A lower bound on local unbiased estimation variance under the required regularity conditions, expressed through inverse Fisher information.]{.definition-explanation}

<!-- pedagogy-paragraph: p18 sha256 bcb754169b6227db99b9ebdfc07adf6ada41d5e2568df7f369c295ec06738e33 -->
p18, lines 18-18; list_item; priority: unchanged; previous: p17; next: p19

> [[**critical point:**]{.definition-term custom-style="Definition Term"} A point where a function's gradient is zero. The Euler calculation also requires invertible Hessians.]{.definition-explanation}

<!-- pedagogy-paragraph: p19 sha256 1e3c1b56f3a18382591736237a8129baf33ea5fc24af599b42e42d7e9bb9c59f -->
p19, lines 19-19; list_item; priority: unchanged; previous: p18; next: p20

> [[**decoding:**]{.definition-term custom-style="Definition Term"} Estimating a represented value from neural responses.]{.definition-explanation}

<!-- pedagogy-paragraph: p20 sha256 5709c309bd1190162e0177cd6a0a0e349e398e46d07cb87245c13968ee09f462 -->
p20, lines 20-20; list_item; priority: unchanged; previous: p19; next: p21

> [[**dendrite:**]{.definition-term custom-style="Definition Term"} A branching input structure of a neuron.]{.definition-explanation}

<!-- pedagogy-paragraph: p21 sha256 f238b8aed977e11eae20423223cbb816bc6b9cd1bf21fa1b813bc8cbb925e267 -->
p21, lines 21-21; list_item; priority: unchanged; previous: p20; next: p22

> [[**diffusion coefficient:**]{.definition-term custom-style="Definition Term"} The coefficient $D$ in the local one-dimensional displacement variance $2Dt$; its units are coordinate squared per time.]{.definition-explanation}

<!-- pedagogy-paragraph: p22 sha256 182107079d75fd1fcf00d9d2a7340628c799b1147c98754a5fe6ebd4143bfc06 -->
p22, lines 22-22; list_item; priority: unchanged; previous: p21; next: p23

> [[**diffusion tensor:**]{.definition-term custom-style="Definition Term"} The matrix giving local coordinate-displacement covariances per twice the elapsed time.]{.definition-explanation}

<!-- pedagogy-paragraph: p23 sha256 ab37978a7aa32bf1e6440a33602f453e0ec661459958bd3724ce9f2f3bd8d415 -->
p23, lines 23-23; list_item; priority: unchanged; previous: p22; next: p24

> [[**Dirac delta:**]{.definition-term custom-style="Definition Term"} A point-mass distribution; in the initial-condition equation all probability is concentrated at the specified coordinate.]{.definition-explanation}

<!-- pedagogy-paragraph: p24 sha256 48c18162f4246b9d5cfade386b19a08ba9581b2c6b01f1d445bbf0015e8d10d6 -->
p24, lines 24-24; list_item; priority: unchanged; previous: p23; next: p25

> [[**encoding:**]{.definition-term custom-style="Definition Term"} Establishing a population activity pattern from an input.]{.definition-explanation}

<!-- pedagogy-paragraph: p25 sha256 d3c61ac01916daa4e95cfff0186382cc3fa61a21df2ed771a7e3cde5ffdb12f4 -->
p25, lines 25-25; list_item; priority: unchanged; previous: p24; next: p26

> [[**Euler characteristic:**]{.definition-term custom-style="Definition Term"} The alternating sum of Betti numbers; in three dimensions, components minus independent loops plus enclosed cavities.]{.definition-explanation}

<!-- pedagogy-paragraph: p26 sha256 aaafa516629ca763c4b4f2af4a4ea7dde67bb7bd063e7314fd014201687cfadf -->
p26, lines 26-26; list_item; priority: unchanged; previous: p25; next: p27

> [[**excess kurtosis:**]{.definition-term custom-style="Definition Term"} The fourth centered moment divided by the squared variance, minus three. It is zero for a Gaussian population.]{.definition-explanation}

<!-- pedagogy-paragraph: p27 sha256 78b4dade2786b4be6b6346e04440718e0d498d1a8fc02c0f19c9f55dadede4f6 -->
p27, lines 27-27; list_item; priority: unchanged; previous: p26; next: p28

> [[**excitatory input:**]{.definition-term custom-style="Definition Term"} In the models used here, an input that increases a receiving neuron's tendency to fire.]{.definition-explanation}

<!-- pedagogy-paragraph: p28 sha256 900dc5c2fd78bc4762654c0f83dd84f353c9c4ade380da1c256ee8e5320aa557 -->
p28, lines 28-28; list_item; priority: unchanged; previous: p27; next: p29

> [[**excursion set:**]{.definition-term custom-style="Definition Term"} The positions where a function exceeds a specified level.]{.definition-explanation}

<!-- pedagogy-paragraph: p29 sha256 38c5f1b7655b11e6950065472e1d875366330cd59824e27fdfb31feb49bf358e -->
p29, lines 29-29; list_item; priority: unchanged; previous: p28; next: p30

> [[**Fano factor:**]{.definition-term custom-style="Definition Term"} Spike-count variance divided by mean count, for a specified counting interval and condition.]{.definition-explanation}

<!-- pedagogy-paragraph: p30 sha256 a62e76a5bf5765654b9c34490476407d8a4482b93929cfc5433dd38a6769e4e4 -->
p30, lines 30-30; list_item; priority: unchanged; previous: p29; next: p31

> [[**firing rate:**]{.definition-term custom-style="Definition Term"} The expected number of spikes per unit time, conditional on the modeled circumstances.]{.definition-explanation}

<!-- pedagogy-paragraph: p31 sha256 e2b965b5a18031c4e244ffa92dd69cac4561eece36e93de5a6e7a91d2999bbea -->
p31, lines 31-31; list_item; priority: unchanged; previous: p30; next: p32

> [[**Fisher information:**]{.definition-term custom-style="Definition Term"} The expected squared score, quantifying the local sensitivity of a probability distribution to a parameter.]{.definition-explanation}

<!-- pedagogy-paragraph: p32 sha256 e6dd8b4bef2ee6f470bba82e8a44c415d7a52eb85c6411568117fd5270b5e4bf -->
p32, lines 32-32; list_item; priority: unchanged; previous: p31; next: p33

> [[**fixational drift:**]{.definition-term custom-style="Definition Term"} Slow eye motion during attempted fixation, between rapid eye movements.]{.definition-explanation}

<!-- pedagogy-paragraph: p33 sha256 ee08ed2aabbecbb292a12bf5d460a139495578b952f5eb37dd5c30253664aaba -->
p33, lines 33-33; list_item; priority: unchanged; previous: p32; next: p34

> [[**fixed point:**]{.definition-term custom-style="Definition Term"} A state whose deterministic rate of change is zero.]{.definition-explanation}

<!-- pedagogy-paragraph: p34 sha256 d80a3ce96ecb6422faa05baf868904277bd12574951b68a98dd840f73c341ca4 -->
p34, lines 34-34; list_item; priority: unchanged; previous: p33; next: p35

> [[**Fokker Planck equation:**]{.definition-term custom-style="Definition Term"} An equation describing how a probability density evolves under drift and diffusion; the guide states the convention before using it.]{.definition-explanation}

<!-- pedagogy-paragraph: p35 sha256 cfd27f8f9d1ded8a2b033694979657f22682d37f0847b1946d5cc882c767ab1b -->
p35, lines 35-35; list_item; priority: unchanged; previous: p34; next: p36

> [[**gain:**]{.definition-term custom-style="Definition Term"} The scale that converts a change in one signal into a change in another.]{.definition-explanation}

<!-- pedagogy-paragraph: p36 sha256 3baddea346713215543a6642565727708aff42c06eb8cfac17f65714532ccc9a -->
p36, lines 36-36; list_item; priority: unchanged; previous: p35; next: p37

> [[**gamma function:**]{.definition-term custom-style="Definition Term"} The function $\Gamma(t)=\int_0^\infty u^{t-1}e^{-u}\,du$ for $t>0$, extending factorials through $\Gamma(n+1)=n!$.]{.definition-explanation}

<!-- pedagogy-paragraph: p37 sha256 a6a44d60593adc9fd204195119f0b17a46beaa1316fbbf1d69588bb9f58b302e -->
p37, lines 37-37; list_item; priority: unchanged; previous: p36; next: p38

> [[**Gaussian curvature:**]{.definition-term custom-style="Definition Term"} For a surface in three dimensions, the product of its two principal curvatures.]{.definition-explanation}

<!-- pedagogy-paragraph: p38 sha256 445565fc0f01d869db4611bd9e892300624f9d90a726b1f8888c9f992adca550 -->
p38, lines 38-38; list_item; priority: unchanged; previous: p37; next: p39

> [[**Gaussian process:**]{.definition-term custom-style="Definition Term"} A distribution over functions whose values at any finite collection of positions have a joint Gaussian distribution.]{.definition-explanation}

<!-- pedagogy-paragraph: p39 sha256 3d4e605f74ad1c059c7cc93d6529bd0ab9415453ba889f9dae1a67cb7b826617 -->
p39, lines 39-39; list_item; priority: unchanged; previous: p38; next: p40

> [[**grid cell:**]{.definition-term custom-style="Definition Term"} A spatially tuned entorhinal neuron with repeated firing fields, often approximately hexagonally arranged in a two-dimensional arena.]{.definition-explanation}

<!-- pedagogy-paragraph: p40 sha256 110d2a904928e976f248b20779c374fba0e7e8e121c408ff1cedee32c5cb2911 -->
p40, lines 40-40; list_item; priority: unchanged; previous: p39; next: p41

> [[**Hessian:**]{.definition-term custom-style="Definition Term"} The matrix of second derivatives of a function with respect to its coordinates.]{.definition-explanation}

<!-- pedagogy-paragraph: p41 sha256 678a6b9406b94238b3243187e0c448f3ea650292a4df08ca167c58d966cb88b0 -->
p41, lines 41-41; list_item; priority: unchanged; previous: p40; next: p42

> [[**hippocampus:**]{.definition-term custom-style="Definition Term"} A brain region involved in memory and navigation.]{.definition-explanation}

<!-- pedagogy-paragraph: p42 sha256 fe539bb5389dc6f0a232f0ae307da084832c1d6b5d8ddefefdbf6b70de8201da -->
p42, lines 42-42; list_item; priority: unchanged; previous: p41; next: p43

> [[**hyperbolic cotangent:**]{.definition-term custom-style="Definition Term"} The function $\coth z=1/\tanh z$, for real $z\ne0$.]{.definition-explanation}

<!-- pedagogy-paragraph: p43 sha256 7fd4a3cf571d99fce4f12e50c5047427e2eedd4bdd60968c50aef9820c895ede -->
p43, lines 43-43; list_item; priority: unchanged; previous: p42; next: p44

> [[**hyperbolic tangent:**]{.definition-term custom-style="Definition Term"} The function $\tanh z=(e^z-e^{-z})/(e^z+e^{-z})$.]{.definition-explanation}

<!-- pedagogy-paragraph: p44 sha256 4bc5058d07c8e7c8e85b230c7078c147ff2dbb60ed022947a5dd96d902b742a0 -->
p44, lines 44-44; list_item; priority: unchanged; previous: p43; next: p45

> [[**impulse response:**]{.definition-term custom-style="Definition Term"} The output of a linear filter in response to a unit-area input impulse, from which responses to general input can be assembled.]{.definition-explanation}

<!-- pedagogy-paragraph: p45 sha256 2408e48f6e09c45a56cad9443c3891f77ab7dd750f47d6a55d2708b18177bf0f -->
p45, lines 45-45; list_item; priority: unchanged; previous: p44; next: p46

> [[**inhibitory input:**]{.definition-term custom-style="Definition Term"} In the models used here, an input that reduces a receiving neuron's tendency to fire.]{.definition-explanation}

<!-- pedagogy-paragraph: p46 sha256 cf882288bf2e78bc9084bf0e62757c14e4fd58fe03ad31f4e75344ca6fc80724 -->
p46, lines 46-46; list_item; priority: unchanged; previous: p45; next: p47

> [[**internal Fisher information rate:**]{.definition-term custom-style="Definition Term"} The local information per unit observation time about the instantaneous attractor coordinate, as defined by the 2012 spike model.]{.definition-explanation}

<!-- pedagogy-paragraph: p47 sha256 3dace707f05928365994aee6d8d0ce81a798c5672b416fd6283ea3a24af14eaf -->
p47, lines 47-47; list_item; priority: unchanged; previous: p46; next: p48

> [[**inverse hyperbolic tangent:**]{.definition-term custom-style="Definition Term"} The inverse of $\tanh$ on $(-1,1)$, given by $\operatorname{artanh}z=\tfrac12\log[(1+z)/(1-z)]$.]{.definition-explanation}

<!-- pedagogy-paragraph: p48 sha256 76173769ac6ec95f7cfce36f20dd103cb9db7375b220efd1d51d0378c56d6f9f -->
p48, lines 48-48; list_item; priority: unchanged; previous: p47; next: p49

> [[**Isotropy:**]{.definition-term custom-style="Definition Term"} Invariance of the spatial probability law under rotations.]{.definition-explanation}

<!-- pedagogy-paragraph: p49 sha256 d8a1052d85df7ad6f3a6eac8c39af9191eb16572d81901972ece57ee2e1a0bf2 -->
p49, lines 49-49; list_item; priority: unchanged; previous: p48; next: p50

> [[**Itô convention:**]{.definition-term custom-style="Definition Term"} A stochastic-increment convention that evaluates the noise coefficient at the beginning of each increment.]{.definition-explanation}

<!-- pedagogy-paragraph: p50 sha256 d22110c1709f92d778c3e5cf2209c8d79facd4929e9fe28b16cb9ea5ed17c006 -->
p50, lines 50-50; list_item; priority: unchanged; previous: p49; next: p51

> [[**jointly Gaussian vector:**]{.definition-term custom-style="Definition Term"} A random vector for which every linear combination of its entries is Gaussian.]{.definition-explanation}

<!-- pedagogy-paragraph: p51 sha256 aa2967adf4b7713c76ef4354f2ca8e9beafbe6fa3be169bc698a74e608ee827f -->
p51, lines 51-51; list_item; priority: unchanged; previous: p50; next: p52

> [[**Kac–Rice formula:**]{.definition-term custom-style="Definition Term"} A way to compute expected crossing or critical-point counts from the joint distribution of a random function and its derivatives, under the relevant regularity assumptions.]{.definition-explanation}

<!-- pedagogy-paragraph: p52 sha256 cb6fdbeb2a6ba7355358146bc2e7cc6fba7d96b07acb3cf7c3a1da3b4785c8e4 -->
p52, lines 52-52; list_item; priority: unchanged; previous: p51; next: p53

> [[**left zero eigenvector:**]{.definition-term custom-style="Definition Term"} A vector $v$ with $v^T A=0$; with appropriate normalization it extracts the persistent coordinate from a small state disturbance.]{.definition-explanation}

<!-- pedagogy-paragraph: p53 sha256 b90ba0cb3396b7d52b8954814d1b6fab1a44071bee11d6a0c36c5f6294ceab26 -->
p53, lines 53-53; list_item; priority: unchanged; previous: p52; next: p54

> [[**likelihood:**]{.definition-term custom-style="Definition Term"} The probability or density of the observed data considered as a function of a proposed parameter value.]{.definition-explanation}

<!-- pedagogy-paragraph: p54 sha256 694b75e2dbce9f0e3661eafe9d3720884e7e5f02f9f73967522b1ef1ae6fe027 -->
p54, lines 54-54; list_item; priority: unchanged; previous: p53; next: p55

> [[**linearization:**]{.definition-term custom-style="Definition Term"} The first-order approximation to a dynamical equation near a reference state.]{.definition-explanation}

<!-- pedagogy-paragraph: p55 sha256 9ecea02d5565b1dd882d112c2800d8396e37181775d30ecf3f173bc4516bf540 -->
p55, lines 55-55; list_item; priority: unchanged; previous: p54; next: p56

> [[**lognormal distribution:**]{.definition-term custom-style="Definition Term"} A distribution of positive values whose logarithms are Gaussian.]{.definition-explanation}

<!-- pedagogy-paragraph: p56 sha256 8dd9eb76ca779fd7f8514322363dbc78ae7d882bc4535b959c5526533784fdda -->
p56, lines 56-56; list_item; priority: unchanged; previous: p55; next: p57

> [[**low pass filter:**]{.definition-term custom-style="Definition Term"} A filter that suppresses sufficiently rapid input changes relative to slower ones.]{.definition-explanation}

<!-- pedagogy-paragraph: p57 sha256 48c35119021883a1f8a3e86458f92e6b9298286661c61b2c1502428ee6972d23 -->
p57, lines 57-57; list_item; priority: unchanged; previous: p56; next: p58

> [[**mean curvature:**]{.definition-term custom-style="Definition Term"} For a surface in three dimensions, the average of its two principal curvatures.]{.definition-explanation}

<!-- pedagogy-paragraph: p58 sha256 96aff7fbf6d589ff75150662df0598ca785ca894472758c90ccb563ae581e71c -->
p58, lines 58-58; list_item; priority: unchanged; previous: p57; next: p59

> [[**mean squared displacement:**]{.definition-term custom-style="Definition Term"} The average squared change in a coordinate across a specified time lag.]{.definition-explanation}

<!-- pedagogy-paragraph: p59 sha256 c3a4384d48046820c5391a3ced4e190c917da58e690a534791fa7a5522baff97 -->
p59, lines 59-59; list_item; priority: unchanged; previous: p58; next: p60

> [[**microsaccades:**]{.definition-term custom-style="Definition Term"} Brief, rapid eye movements that occur during attempted fixation.]{.definition-explanation}

<!-- pedagogy-paragraph: p60 sha256 5ff1c18f889c3054c9c6013da2598782ede6e13f9ee73f2f8a21d70d2c401164 -->
p60, lines 60-60; list_item; priority: unchanged; previous: p59; next: p61

> [[**Morse theory:**]{.definition-term custom-style="Definition Term"} A theory relating the topology of a function's level-set regions to its critical points. The guide uses a signed critical-point count under its smoothness and nondegeneracy assumptions, including boundary contributions.]{.definition-explanation}

<!-- pedagogy-paragraph: p61 sha256 8439f291ffcbc82a8a6f928af220f4f7559a72c4465fc1a30c6070b930d59df9 -->
p61, lines 61-61; list_item; priority: unchanged; previous: p60; next: p62

> [[**neural transfer function:**]{.definition-term custom-style="Definition Term"} The modeled relationship between a neuron's input and its expected firing rate.]{.definition-explanation}

<!-- pedagogy-paragraph: p62 sha256 1d7d459c47f3670941d373e7ccea3c213cce2124e868073805f05bd003900a6b -->
p62, lines 62-62; list_item; priority: unchanged; previous: p61; next: p63

> [[**neuron:**]{.definition-term custom-style="Definition Term"} A signaling cell in the nervous system.]{.definition-explanation}

<!-- pedagogy-paragraph: p63 sha256 959ec7f76648f97fd77ad8d22f5fe0901a7eb90e885d85607571de6b9280ab99 -->
p63, lines 63-63; list_item; priority: unchanged; previous: p62; next: p64

> [[**ocular motoneurons (OMNs):**]{.definition-term custom-style="Definition Term"} Neurons whose spikes activate the eye muscles.]{.definition-explanation}

<!-- pedagogy-paragraph: p64 sha256 5c4d849dc12b6b0b9dc813bd93bf815d15c299baf4ee233dd5f3887e64bc7ccd -->
p64, lines 64-64; list_item; priority: unchanged; previous: p63; next: p65

> [[**ocular plant:**]{.definition-term custom-style="Definition Term"} The muscles and mechanical eye system that transform motor activity into eye motion.]{.definition-explanation}

<!-- pedagogy-paragraph: p65 sha256 b0c4ef2f957bfc55c614464b694aadc11990217d74703aed47eda755884fd3ff -->
p65, lines 65-65; list_item; priority: unchanged; previous: p64; next: p66

> [[**oculomotor integrator:**]{.definition-term custom-style="Definition Term"} A neural circuit that converts movement commands into a maintained eye-position command.]{.definition-explanation}

<!-- pedagogy-paragraph: p66 sha256 b3d9b05b16702ead862c62e9ea4d22fe40ae1ef60552f5769c10a88618af0ed8 -->
p66, lines 66-66; list_item; priority: unchanged; previous: p65; next: p67

> [[**p value:**]{.definition-term custom-style="Definition Term"} Under the specified null comparison, the probability of a test statistic at least as extreme in the tested direction as the observed one.]{.definition-explanation}

<!-- pedagogy-paragraph: p67 sha256 afb8e9f9401c98ca4743925643e226c406a89df6c239c0e1219749a45ce58843 -->
p67, lines 67-67; list_item; priority: unchanged; previous: p66; next: p68

> [[**path integration:**]{.definition-term custom-style="Definition Term"} Updating an estimate of position from movement.]{.definition-explanation}

<!-- pedagogy-paragraph: p68 sha256 b45498d2d26b90f4355a017de89622f3afc3d32d914ea33c795604a9e55a6cea -->
p68, lines 68-68; list_item; priority: unchanged; previous: p67; next: p69

> [[**place cell:**]{.definition-term custom-style="Definition Term"} A spatially selective hippocampal neuron that fires strongly in one or more localized regions of an environment.]{.definition-explanation}

<!-- pedagogy-paragraph: p69 sha256 c240d0fa50445afdc9e4b21f6297976623f885f635ff17bb491bfe65c44fd0bf -->
p69, lines 69-69; list_item; priority: unchanged; previous: p68; next: p70

> [[**place field:**]{.definition-term custom-style="Definition Term"} A connected region of elevated spatial firing, as defined by the model or stated measurement procedure.]{.definition-explanation}

<!-- pedagogy-paragraph: p70 sha256 688090b938deee64249d76f50f5386c80e80777ca8785efa1574691abd512808 -->
p70, lines 70-70; list_item; priority: unchanged; previous: p69; next: p71

> [[**Poisson process:**]{.definition-term custom-style="Definition Term"} A counting process with independent increments and a deterministic constant or time-dependent event rate; its count over an interval has equal mean and variance. In a recurrent model, conditionally Poisson instantaneous spike generation does not make complete spike trains have independent increments.]{.definition-explanation}

<!-- pedagogy-paragraph: p71 sha256 5a1def69838ee2ce343b2e02665999d9a43f2d353a6d196a0a5c3c409f77ab4f -->
p71, lines 71-71; list_item; priority: unchanged; previous: p70; next: p72

> [[**population code:**]{.definition-term custom-style="Definition Term"} A representation carried by the pattern of responses across neurons.]{.definition-explanation}

<!-- pedagogy-paragraph: p72 sha256 a56a52c651b6c80b17f095b41698fa40654d9f3ffa61160a04276595b7ce0565 -->
p72, lines 72-72; list_item; priority: unchanged; previous: p71; next: p73

> [[**precision:**]{.definition-term custom-style="Definition Term"} The reciprocal of variance for a scalar Gaussian estimate.]{.definition-explanation}

<!-- pedagogy-paragraph: p73 sha256 12ba26e8665b28207a52ef453f3f43a782903bce8d1cff9dd22be0c84e6f1c75 -->
p73, lines 73-73; list_item; priority: unchanged; previous: p72; next: p74

> [[**preferred angle:**]{.definition-term custom-style="Definition Term"} An angle where a neuron's tuning curve peaks.]{.definition-explanation}

<!-- pedagogy-paragraph: p74 sha256 1b3759dc7098eb25fb7efb83f1e0de69264fdb622f68f1e2c50ccc558e00b177 -->
p74, lines 74-74; list_item; priority: unchanged; previous: p73; next: p75

> [[**prior distribution:**]{.definition-term custom-style="Definition Term"} A distribution representing knowledge about likely parameter values before observing the current data.]{.definition-explanation}

<!-- pedagogy-paragraph: p75 sha256 56a0b9fb4d9db0b9c47486008af0430eb89fd2e695e2e9c391fd0511d4e7f5e5 -->
p75, lines 75-75; list_item; priority: unchanged; previous: p74; next: p76

> [[**rate map:**]{.definition-term custom-style="Definition Term"} An estimate of spatial firing rate from spikes per time spent at each position.]{.definition-explanation}

<!-- pedagogy-paragraph: p76 sha256 08ad5d61990c1be6e595ec327f835295462c728fb7d6104400e95b1335f373d3 -->
p76, lines 76-76; list_item; priority: unchanged; previous: p75; next: p77

> [[**Rayleigh distribution:**]{.definition-term custom-style="Definition Term"} The distribution of a positive variable that is a scaled square root of an exponential variable.]{.definition-explanation}

<!-- pedagogy-paragraph: p77 sha256 e54599b145d49af6ca64d943e8bf18877488cb0eae5cf00fb5f155af313bf492 -->
p77, lines 77-77; list_item; priority: unchanged; previous: p76; next: p78

> [[**recurrent connectivity:**]{.definition-term custom-style="Definition Term"} Connections that feed activity back into the same neuronal population.]{.definition-explanation}

<!-- pedagogy-paragraph: p78 sha256 8562773882c1e9ecb4123eaf3a18b26fc90b88f1a9b6e38065e5a9cc123b7faf -->
p78, lines 78-78; list_item; priority: unchanged; previous: p77; next: p79

> [[**renewal process:**]{.definition-term custom-style="Definition Term"} An event process with independent, identically distributed intervals under the fixed conditions being modeled.]{.definition-explanation}

<!-- pedagogy-paragraph: p79 sha256 d511d7fd51ce26f1a240d16eb86ab5f23623f239257e456aaaf20858f4ea7fd1 -->
p79, lines 79-79; list_item; priority: unchanged; previous: p78; next: p80

> [[**retina:**]{.definition-term custom-style="Definition Term"} The light-sensitive tissue at the back of the eye.]{.definition-explanation}

<!-- pedagogy-paragraph: p80 sha256 f9f5a8713e6077b0c4d7d6dddb3595008fdeeaddd515a9698383d0dfdc0cdf38 -->
p80, lines 80-80; list_item; priority: unchanged; previous: p79; next: p81

> [[**right zero eigenvector:**]{.definition-term custom-style="Definition Term"} A state-space direction $u$ satisfying $Au=0$ for the linearized dynamics.]{.definition-explanation}

<!-- pedagogy-paragraph: p81 sha256 1b62cce2bdf340aa885aafc6a4086b56545de5bbf1871e5da4714be6b10b1dda -->
p81, lines 81-81; list_item; priority: unchanged; previous: p80; next: p82

> [[**root mean squared displacement:**]{.definition-term custom-style="Definition Term"} The square root of mean squared displacement, expressed in the original coordinate's units.]{.definition-explanation}

<!-- pedagogy-paragraph: p82 sha256 585d46dd74811d48acf6ae86a559c486ce66e339b7a0d2378b8cf6c1c6cc700d -->
p82, lines 82-82; list_item; priority: unchanged; previous: p81; next: p83

> [[**score:**]{.definition-term custom-style="Definition Term"} The derivative of log likelihood with respect to the parameter being estimated.]{.definition-explanation}

<!-- pedagogy-paragraph: p83 sha256 9dd9f3bda0e2d4e9304a26b6ccb28f8f809a623826ed9b8c0849471ba28bb94f -->
p83, lines 83-83; list_item; priority: unchanged; previous: p82; next: p84

> [[**skew:**]{.definition-term custom-style="Definition Term"} The third centered moment divided by the variance to the power $3/2$, measuring asymmetry.]{.definition-explanation}

<!-- pedagogy-paragraph: p84 sha256 8429f1081b96499bb2c463d0e64ea99136387bf00c96c722953e9b8504343a57 -->
p84, lines 84-84; list_item; priority: unchanged; previous: p83; next: p85

> [[**Smoothness:**]{.definition-term custom-style="Definition Term"} The existence and regularity of derivatives of a function. The crossing and peak calculations require different derivative orders.]{.definition-explanation}

<!-- pedagogy-paragraph: p85 sha256 88873f86d63902fa490045b52fafc6eac882fdaaa29f1c86597c7ae6a94cc718 -->
p85, lines 85-85; list_item; priority: unchanged; previous: p84; next: p86

> [[**spike:**]{.definition-term custom-style="Definition Term"} A brief electrical event emitted by a neuron.]{.definition-explanation}

<!-- pedagogy-paragraph: p86 sha256 c6aa2b9d26862f4964a19af8ab473beb83e88e393e7519da875b74e4b06a441d -->
p86, lines 86-86; list_item; priority: unchanged; previous: p85; next: p87

> [[**standard error of the mean (SEM):**]{.definition-term custom-style="Definition Term"} An estimate of uncertainty in a sample mean. Its interpretation depends on which observations are treated as independent, such as trials, cells, or animals.]{.definition-explanation}

<!-- pedagogy-paragraph: p87 sha256 a9e487aad5bb2ddfe5d23eaf468a31c8f7e1df9d29410d0af0530d30687e7d18 -->
p87, lines 87-87; list_item; priority: unchanged; previous: p86; next: p88

> [[**state:**]{.definition-term custom-style="Definition Term"} The quantities that specify a modeled system's current condition and determine its subsequent dynamics together with future inputs and noise.]{.definition-explanation}

<!-- pedagogy-paragraph: p88 sha256 7eaffa234fbf378ad58bba2288e1120f1e50c3e62f7c4bfbfe73f916ae538737 -->
p88, lines 88-88; list_item; priority: unchanged; previous: p87; next: p89

> [[**Stationarity:**]{.definition-term custom-style="Definition Term"} In the place-field model, invariance of spatial statistics under translating the map.]{.definition-explanation}

<!-- pedagogy-paragraph: p89 sha256 0bac14794d0fcd964aeb9aca42004705f76185cbd97e18854dba5d751389ac1c -->
p89, lines 89-89; list_item; priority: unchanged; previous: p88; next: p90

> [[**stationary process:**]{.definition-term custom-style="Definition Term"} A random process whose probability law is unchanged by shifting its time or position origin; weaker covariance-only stationarity must be specified when used.]{.definition-explanation}

<!-- pedagogy-paragraph: p90 sha256 74c28e1d5887313a88cd53347af953b2c1c3805d871352b2511c7b4969a2c13f -->
p90, lines 90-90; list_item; priority: unchanged; previous: p89; next: p91

> [[**Stratonovich convention:**]{.definition-term custom-style="Definition Term"} A stochastic-increment convention using midpoint evaluation in the limiting increments.]{.definition-explanation}

<!-- pedagogy-paragraph: p91 sha256 f82962e613047e7b77c4391cee8732c15c65d8977d235ceb3045e38d20b71e79 -->
p91, lines 91-91; list_item; priority: unchanged; previous: p90; next: p92

> [[**sub-Poisson spiking:**]{.definition-term custom-style="Definition Term"} Spiking with less variability than a matched Poisson reference according to the stated measure and conditions.]{.definition-explanation}

<!-- pedagogy-paragraph: p92 sha256 5c203edc6a74f94161dcf9eb043485847344320bd6d06bba5b294425214d7979 -->
p92, lines 92-92; list_item; priority: unchanged; previous: p91; next: p93

> [[**superdiffusion:**]{.definition-term custom-style="Definition Term"} Mean squared displacement growing faster than linearly with lag over the range being described.]{.definition-explanation}

<!-- pedagogy-paragraph: p93 sha256 637330ccfbfdd50b5dd238cffae2e9bad9ccc5d0a9cb5894e5bc28f8444c470c -->
p93, lines 93-93; list_item; priority: unchanged; previous: p92; next: p94

> [[**synapse:**]{.definition-term custom-style="Definition Term"} A connection through which one neuron influences another.]{.definition-explanation}

<!-- pedagogy-paragraph: p94 sha256 b15f90b738977b69d6061bf908febfb2a51d5ca8f039d86495cec3d59065a812 -->
p94, lines 94-94; list_item; priority: unchanged; previous: p93; next: p95

> [[**systematic drift:**]{.definition-term custom-style="Definition Term"} A nonzero mean velocity of the represented coordinate, distinct from random spreading.]{.definition-explanation}

<!-- pedagogy-paragraph: p95 sha256 add58c9c9fdb433cb93d1d08eca583d7ddce269d6e47c9b5413f3395f1212b46 -->
p95, lines 95-95; list_item; priority: unchanged; previous: p94; next: p96

> [[**Translation invariance:**]{.definition-term custom-style="Definition Term"} In the readout model, invariance under shifts of the represented value. It makes the readout variance independent of the cue state.]{.definition-explanation}

<!-- pedagogy-paragraph: p96 sha256 26627989e0eb43229da9b182a40edc229ee1e7890cd7d239d900926a93d99dab -->
p96, lines 96-96; list_item; priority: unchanged; previous: p95; next: p97

> [[**tuning curve:**]{.definition-term custom-style="Definition Term"} A neuron's expected firing rate as a function of a represented variable.]{.definition-explanation}

<!-- pedagogy-paragraph: p97 sha256 cd16101a39aa57087045d7e30812c3e460a27f27c45d7132eef7ec3b5bd44f20 -->
p97, lines 97-97; list_item; priority: unchanged; previous: p96; next: p98

> [[**unbiased:**]{.definition-term custom-style="Definition Term"} Describes an estimator whose expected value equals the parameter locally under the conditions used in the estimation bound.]{.definition-explanation}

<!-- pedagogy-paragraph: p98 sha256 b6432da06435bf4894113d26c6e193230d51742e162aab68dbd6cb61f60dd8a4 -->
p98, lines 98-98; list_item; priority: unchanged; previous: p97; next: p99

> [[**upcrossing:**]{.definition-term custom-style="Definition Term"} A point where a function crosses upward through a specified threshold.]{.definition-explanation}

<!-- pedagogy-paragraph: p99 sha256 71a55d6a88dfc03e7a9ca8a9bd5d20aa0c9ee8b4ba7739947de2cc379d8b6f43 -->
p99, lines 99-99; list_item; priority: unchanged; previous: p98; next: p100

> [[**weak fluctuation approximation:**]{.definition-term custom-style="Definition Term"} An expansion about the deterministic population dynamics in which the aggregate effects of many small spike contributions remain small.]{.definition-explanation}

<!-- pedagogy-paragraph: p100 sha256 95bd0285613127a8607c38091510e3a4ac1cc6cb28f5715b4ab6739f7bc5f639 -->
p100, lines 100-100; list_item; priority: unchanged; previous: p99; next: p101

> [[**Weibull distribution:**]{.definition-term custom-style="Definition Term"} A positive-variable distribution with survival probability $\exp[-(s/b)^k]$, scale $b>0$, and shape $k>0$.]{.definition-explanation}

<!-- pedagogy-paragraph: p101 sha256 44ed76c733e3c60021947b3a0eb1c84e66f970db1b212921ecc161cce2e83c3c -->
p101, lines 101-101; list_item; priority: unchanged; previous: p100; next: none

> [[**White noise:**]{.definition-term custom-style="Definition Term"} An ideal noise input with zero covariance at unequal times and a delta-function covariance at equal times; its integrated increments have finite variance.]{.definition-explanation}


Claim-bearing content: none

Claims to check:

- Claim c1, line 7: "[[**attractor manifold:**]{.definition-term custom-style="Definition Term"} The continuous family of persistent activity states, described by its represented coordinates rather than by every neural activity separately.]{.definition-explanation}" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c2, line 10: "[[**causal filter:**]{.definition-term custom-style="Definition Term"} A rule whose current output depends only on present and past input.]{.definition-explanation}" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c3, line 36: "[[**gamma function:**]{.definition-term custom-style="Definition Term"} The function $\Gamma(t)=\int_0^\infty u^{t-1}e^{-u}\,du$ for $t>0$, extending factorials through $\Gamma(n+1)=n!$.]{.definition-explanation}" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c4, line 42: "[[**hyperbolic cotangent:**]{.definition-term custom-style="Definition Term"} The function $\coth z=1/\tanh z$, for real $z\ne0$.]{.definition-explanation}" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c5, line 47: "[[**inverse hyperbolic tangent:**]{.definition-term custom-style="Definition Term"} The inverse of $\tanh$ on $(-1,1)$, given by $\operatorname{artanh}z=\tfrac12\log[(1+z)/(1-z)]$.]{.definition-explanation}" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c6, line 50: "[[**jointly Gaussian vector:**]{.definition-term custom-style="Definition Term"} A random vector for which every linear combination of its entries is Gaussian.]{.definition-explanation}" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c7, line 52: "[[**left zero eigenvector:**]{.definition-term custom-style="Definition Term"} A vector $v$ with $v^T A=0$; with appropriate normalization it extracts the persistent coordinate from a small state disturbance.]{.definition-explanation}" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c8, line 80: "[[**right zero eigenvector:**]{.definition-term custom-style="Definition Term"} A state-space direction $u$ satisfying $Au=0$ for the linearized dynamics.]{.definition-explanation}" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c9, line 83: "[[**skew:**]{.definition-term custom-style="Definition Term"} The third centered moment divided by the variance to the power $3/2$, measuring asymmetry.]{.definition-explanation}" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c10, line 89: "[[**stationary process:**]{.definition-term custom-style="Definition Term"} A random process whose probability law is unchanged by shifting its time or position origin; weaker covariance-only stationarity must be specified when used.]{.definition-explanation}" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c11, line 99: "[[**weak fluctuation approximation:**]{.definition-term custom-style="Definition Term"} An expansion about the deterministic population dynamics in which the aggregate effects of many small spike contributions remain small.]{.definition-explanation}" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c12, line 100: "[[**Weibull distribution:**]{.definition-term custom-style="Definition Term"} A positive-variable distribution with survival probability $\exp[-(s/b)^k]$, scale $b>0$, and shape $k>0$.]{.definition-explanation}" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]

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
