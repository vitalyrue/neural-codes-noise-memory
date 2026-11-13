# Pedagogy Review Packet: Part 1 - Noise limits memory accuracy in continuous attractor models

This packet prepares review only. It does not approve the teaching quality.

A reviewer must cite exact passages before marking a requirement as satisfied.

Every substantial teaching unit below has its own required evidence fields.

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

## Part opening

<!-- pedagogy-unit: part:MECHANISMS::part-opening -->

Part ID: `part:MECHANISMS`

Purpose:

> A stable population pattern can retain a continuous value while fluctuations move that value along its family of persistent states. These chapters establish the neural and probability background, derive the surviving motion, and connect it to limits on information and readout.

Paragraphs in source order (complete `PARAGRAPH_REVIEW.json`):

No prose paragraphs in this unit; review its other content below.

Part opening required evidence:

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

## ch:FOUNDATIONS - Patterns of variable spikes can represent a value

Source file: `content/chapters/01-foundations.md`

Purpose: The eyes can hold a position after a brief movement command has ended. An animal can also keep track of its location while the activity of individual neurons fluctuates. Both abilities require a useful quantity to remain represented in a changing biological system. The three papers study different parts of this problem: the loss of a stored value, the origin of slow eye motion, and the arrangement of spatial firing patterns.

Prerequisites: None recorded

Sidecar sections: Patterns of firing rates represent a value, A variable spike count at a fixed rate, Mean squared displacement combines random spread with mean motion

Blocks: 1 figure(s), 0 equation(s), 0 code block(s)

Result labels: No Answer/Conclusion/Feedback label detected

<!-- pedagogy-unit: content/chapters/01-foundations.md::ch:FOUNDATIONS -->

### Chapter opening

Location: line 1, anchor `ch:FOUNDATIONS`

First content kind: `prose`

Opening passage line: 3
Closing passage line: 5

Paragraphs in source order (complete `PARAGRAPH_REVIEW.json`):

<!-- pedagogy-paragraph: p3 sha256 a521a39a30a16b014048563c26f3dfe0fb20b39c863178cc11f8ebe6c94bcbd6 -->
p3, lines 3-3; prose; priority: unchanged; previous: none; next: p5

> The eyes can hold a position after a brief movement command has ended. An animal can also keep track of its location while the activity of individual neurons fluctuates. Both abilities require a useful quantity to remain represented in a changing biological system. The three papers study different parts of this problem: the loss of a stored value, the origin of slow eye motion, and the arrangement of spatial firing patterns.

<!-- pedagogy-paragraph: p5 sha256 349745a3bca8cc6c0b5e35b2afe4c8d700f3ec45fd71542cb49304934d053b55 -->
p5, lines 5-5; prose; priority: unchanged; previous: p3; next: p9

> Before asking how a circuit keeps a value, we need to know how its activity represents that value and what makes the activity variable. We begin with the spikes that cells send and the patterns of firing rates across a population. A model of spike counts then shows why one brief observation can be uncertain and how combining counts from several cells can help. We then learn how to tell whether measurements vary together and how to separate random spreading from a change in the average value. Those distinctions will let us interpret both a memory model and measurements of eye motion.


Claim-bearing content: none

Claims to check:

- Claim c1, line 3: "Both abilities require a useful quantity to remain represented in a changing biological system." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]

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

<!-- pedagogy-unit: content/chapters/01-foundations.md::sec:FOUNDATIONS-SPIKES -->

### Patterns of firing rates represent a value

Location: line 7, anchor `sec:FOUNDATIONS-SPIKES`

First content kind: `prose`

Opening passage line: 9
Closing passage line: 35

Paragraphs in source order (complete `PARAGRAPH_REVIEW.json`):

<!-- pedagogy-paragraph: p9 sha256 562b776cafa4fdde4f262808ff451e434a3952147d5a717b407b067e54580f61 -->
p9, lines 9-9; prose; priority: unchanged; previous: p5; next: p11

> A neuron communicates through brief electrical events called [**spike**]{.definition-term custom-style="Definition Term"}s. A [**firing rate**]{.definition-term custom-style="Definition Term"} is the expected number of spikes per unit time. A rate of 20 hertz means an average of 20 spikes per second under the specified conditions, rather than a promise of one spike every 50 milliseconds.

<!-- pedagogy-paragraph: p11 sha256 4d3cc4e95280e3932902406bd9a62c3d8b417248e2d7de238b1212c703b13106 -->
p11, lines 11-11; prose; priority: unchanged; previous: p9; next: p13

> Neurons affect one another through connections called [**synapse**]{.definition-term custom-style="Definition Term"}s. In the models used here, inputs have two contrasting effects:

<!-- pedagogy-paragraph: p13 sha256 d2c75e23acc092e147a287eea92ac57e4a783d9af1ca17f55afb0a93724e5f5d -->
p13, lines 13-13; list_item; priority: unchanged; previous: p11; next: p14

> An [**excitatory input**]{.definition-term custom-style="Definition Term"} increases a receiving neuron's tendency to fire.

<!-- pedagogy-paragraph: p14 sha256 6602f1d39c47a221a82c470886bbdfecbec9d581d4833c8f9ef62b1061b117ab -->
p14, lines 14-14; list_item; priority: unchanged; previous: p13; next: p16

> An [**inhibitory input**]{.definition-term custom-style="Definition Term"} reduces it.

<!-- pedagogy-paragraph: p16 sha256 2605bb60988a4c666328265f40bdc07c6614459c3f2e51d301f9b9eae0eb6685 -->
p16, lines 16-16; prose; priority: unchanged; previous: p14; next: p18

> The effect of a spike can last beyond the spike itself because synaptic input decays over time. When neurons send signals back into the same population, the circuit has [**recurrent connectivity**]{.definition-term custom-style="Definition Term"}. Such feedback can maintain activity after an external signal disappears.

<!-- pedagogy-paragraph: p18 sha256 505ddd55889385dc027c32501228282bd74845f469d8fa8db1472dd3b0396eb0 -->
p18, lines 18-18; prose; priority: unchanged; previous: p16; next: p20

> A [**tuning curve**]{.definition-term custom-style="Definition Term"} gives a neuron's expected firing rate as a function of a represented variable. For eye angle $\theta$, a simple local model is $r_i(\theta)=b_i+k_i\theta$. Neuron $i$ has baseline rate $b_i$ in spikes per second and slope $k_i$ in spikes per second per degree. The linear expression can describe an active range, but it must be modified where it would predict negative firing. The eye paper includes a firing threshold and terms for movement as well as position.[^f-eye]

<!-- pedagogy-paragraph: p20 sha256 618e653c5c789ee690acee11ff3a8159592ca4b9a3c31c421b4d02a6f79322e9 -->
p20, lines 20-20; prose; priority: unchanged; previous: p18; next: p26

> Different cells have different tuning curves. The vector

<!-- pedagogy-paragraph: p26 sha256 08bfd24b39fefc97c9932be3b1b01c9925b3da8f737487e51a16fd55df7a7ef6 -->
p26, lines 26-26; prose; priority: unchanged; previous: p20; next: p28

> is a [**population code**]{.definition-term custom-style="Definition Term"}: the pattern across $N$ neurons carries information about $\theta$. The position of a cell in this vector is a neuron identity, rather than a location in physical space. Reading a value from observed spikes is [**decoding**]{.definition-term custom-style="Definition Term"}. Establishing a population pattern from an input is [**encoding**]{.definition-term custom-style="Definition Term"}. The 2012 paper asks how accurately the network can maintain such a pattern using its own noisy activity.

<!-- pedagogy-paragraph: p28 sha256 16b89813cd6f7218ef24356b4f155464f7a5bf5dd8c3a4ea0eb299f88e04141d -->
p28, lines 28-28; prose; priority: unchanged; previous: p26; next: p30

> Spatial tuning gives a second example. In the hippocampus, a brain structure involved in memory and navigation, a place cell fires strongly in one or more localized regions of an environment. A connected region of elevated spatial firing is a place field. One neuron can have several fields. A [**rate map**]{.definition-term custom-style="Definition Term"} estimates the rate at each position by dividing the spikes recorded there by the time spent there. Sparse visits, smoothing, and firing cutoffs therefore affect the estimated map and its fields. A field in a model's expected rate and a field extracted from finite recordings are related objects with different measurement uncertainties.[^f-place]

<!-- pedagogy-paragraph: p30 sha256 79571a034265749c7ab986239802498758b506b7da48f44f62f75687cbeba00f -->
p30, lines 30-30; prose; priority: unchanged; previous: p28; next: p32

> The hippocampal areas CA3 and CA1 contain place cells, but their connections differ:

<!-- pedagogy-paragraph: p32 sha256 8d66a647c59209337c098324aa7c6c2087ced241e1637c52f798b5da4df32619 -->
p32, lines 32-32; list_item; priority: unchanged; previous: p30; next: p33

> CA3 supplies major input to CA1 and has substantial recurrent excitation.

<!-- pedagogy-paragraph: p33 sha256 845567174595b6d1398650e58c477f85c95539d52eb9efd8fd6d17fb3334ef2c -->
p33, lines 33-33; list_item; priority: unchanged; previous: p32; next: p35

> CA1 also receives input from entorhinal cortex and has much less local recurrent excitation.

<!-- pedagogy-paragraph: p35 sha256 4ab1664e7db7b6e0bc61057ba2b6351a8323ac9d7ae07c46e4898a3443659aba -->
p35, lines 35-35; prose; priority: unchanged; previous: p33; next: p39

> A [**grid cell**]{.definition-term custom-style="Definition Term"}, found in entorhinal cortex, has repeated spatial fields that often form an approximately hexagonal pattern in a two-dimensional arena. These repeated grid fields and a place cell's irregular multiple fields should be kept distinct. A model explaining CA1's output maps need not identify where the animal's position estimate is maintained.[^f-anatomy]


Claim-bearing content: none

Claims to check:

- Claim c1, line 9: "A rate of 20 hertz means an average of 20 spikes per second under the specified conditions, rather than a promise of one spike every 50 milliseconds." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c2, line 18: "The linear expression can describe an active range, but it must be modified where it would predict negative firing." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c3, line 18: "The eye paper includes a firing threshold and terms for movement as well as position.[^f-eye]" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c4, line 28: "A field in a model's expected rate and a field extracted from finite recordings are related objects with different measurement uncertainties.[^f-place]" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c5, line 35: "A model explaining CA1's output maps need not identify where the animal's position estimate is maintained.[^f-anatomy]" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]

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

<!-- pedagogy-unit: content/chapters/01-foundations.md::sec:FOUNDATIONS-POISSON -->

### A variable spike count at a fixed rate

Location: line 37, anchor `sec:FOUNDATIONS-POISSON`

First content kind: `prose`

Opening passage line: 39
Closing passage line: 91

Paragraphs in source order (complete `PARAGRAPH_REVIEW.json`):

<!-- pedagogy-paragraph: p39 sha256 e8a2b3e91224abd9bf6f874a5921392a7e8cfdc098db94494e0e6f7d9b321ade -->
p39, lines 39-39; prose; priority: unchanged; previous: p35; next: p47

> A tuning curve describes expected activity, but a brief spike observation can differ each time the same value is represented. The 2012 model describes this variability with a [**Poisson process**]{.definition-term custom-style="Definition Term"}. At constant rate $r$, the number $K$ of spikes in an interval of length $\Delta t$ obeys

<!-- pedagogy-paragraph: p47 sha256 1fc8afb5020ca37a59bb1b469af13581157beef6b2b80f7962e8a5d631a63212 -->
p47, lines 47-47; prose; priority: unchanged; previous: p39; next: p56

> Here $\lambda$ is an expected count, so it has no units. For this distribution,

<!-- pedagogy-paragraph: p56 sha256 e95641c55780b3dd148cda9a6df2e3fcba1bcba855eb61da293a4a726fa34d78 -->
p56, lines 56-56; prose; priority: unchanged; previous: p47; next: p66

> The variance follows directly from the first two factorial moments. Summing $k\Pr(K=k)$ gives $\lambda$. Likewise, summing $k(k-1)\Pr(K=k)$ gives $\lambda^2$. Since $K^2=K(K-1)+K$,

<!-- pedagogy-paragraph: p66 sha256 eac77823b6ae97d0a8bea5168cb1a499f15d80a9d982cb04ddbeb48e0f7417b1 -->
p66, lines 66-66; prose; priority: unchanged; previous: p56; next: p68

> The count variance grows with rate, while its size relative to the mean falls. Its relative standard deviation is $\sqrt\lambda/\lambda=1/\sqrt\lambda$. This is why collecting more independent spikes can improve a rate estimate. It also means that increasing a firing-rate scale does not keep absolute noise amplitude fixed. Comparisons between networks must specify which quantities are held constant.[^f-poisson]

<!-- pedagogy-paragraph: p68 sha256 de5190c75864bb0d6d6d57097ed84558c02439b5c8b51ef7615c4c2086bfb541 -->
p68, lines 68-68; prose; priority: unchanged; previous: p66; next: p70

> [**Example: an apparently silent cell and an informative population**]{#sec-foundations-count-example}

<!-- pedagogy-paragraph: p70 sha256 49727cec7b7c9d422b9da09ae79ca4a2d06d25a042fe75aaea9ff64407297306 -->
p70, lines 70-70; prose; priority: unchanged; previous: p68; next: p72

> Suppose the expected rate is 20 spikes per second and an observation lasts 50 ms. The expected count is $20\times0.05=1$. The probability of seeing no spike is $e^{-1}=0.368$. A silent interval is therefore common even though the expected rate is positive.

<!-- pedagogy-paragraph: p72 sha256 ae84316193551d78420b4abb9422aeeae5a2ca31eeae43b7def87bb32ce16cbf -->
p72, lines 72-72; prose; priority: unchanged; previous: p70; next: p74

> Now suppose 20 conditionally independent cells each have that rate. Their total count is Poisson with mean 20 and standard deviation $\sqrt{20}=4.47$. The total rate estimate has a relative standard deviation of about 22.4%, compared with 100% for one cell. Population averaging helps because the independent count variances add while the mean signal adds directly. If cells share an additional fluctuating drive, that common variation will not disappear in the same way.

<!-- pedagogy-paragraph: p74 sha256 aa0421266ca1569fc3d93c4067c48a77f517a06c03ae930c267944756733d4de -->
p74, lines 74-74; prose; priority: unchanged; previous: p72; next: p76

> The two count distributions can be compared on the same rate per cell scale.

<!-- pedagogy-paragraph: p76 sha256 2c643bd85d3e8933fd7127e586cd0d302d74dcd69d691fc3921ef217cc019e39 -->
p76, lines 76-76; prose; priority: unchanged; previous: p74; next: p80

> <div class="figure-scroll">

<!-- pedagogy-paragraph: p80 sha256 aac32651b10f567c461b9b4f255d6fb1fa6859b5368d8bd9a51af920ab21cf23 -->
p80, lines 80-80; prose; priority: unchanged; previous: p76; next: p82

> </div>

<!-- pedagogy-paragraph: p82 sha256 2d7daa3d10f233631049c070dad41b91878e8ae242a46f9d770c721dd2d76c42 -->
p82, lines 82-82; prose; priority: unchanged; previous: p80; next: p84

> Dividing the pooled rate estimate by 20 keeps the expected rate per cell fixed, while independent averaging reduces its relative spread. See [Poisson count likelihood, SI Eq. S43, p. 9](../papers/burak-fiete-2012-persistent-activity-si.pdf#page=9).

<!-- pedagogy-paragraph: p84 sha256 117a7ab957084492c798962d1cbc2ef427e668aaabdbaea499bd7f21371d19a8 -->
p84, lines 84-84; prose; priority: unchanged; previous: p82; next: p86

> For changing rates, the expected count is the integral $\lambda=\int r(t)\,dt$. In a recurrent network, $r(t)$ itself depends on past activity. The useful independence statement is therefore conditional: given the current modeled state, the elementary spike-generation noise is independent across cells in the basic 2012 model. Averaging over the evolving state can still produce correlations across time and across neurons. This qualification prevents treating a recurrent Poisson network as a collection of independent complete spike trains.

<!-- pedagogy-paragraph: p86 sha256 f7479e6fe65552f1d30c902b4861a78a63e9e2f47637684302332ca719e1f38b -->
p86, lines 86-86; prose; priority: unchanged; previous: p84; next: p88

> Two other measurements describe different aspects of variability:

<!-- pedagogy-paragraph: p88 sha256 c4d1551c080302fc9e546405bfc30cbe604db1bce147e72833f925e82f84016f -->
p88, lines 88-88; list_item; priority: unchanged; previous: p86; next: p89

> The [**coefficient of variation**]{.definition-term custom-style="Definition Term"}, or CV, of interspike intervals, the times between successive spikes, is their standard deviation divided by their mean. A homogeneous Poisson process has exponential intervals and CV equal to one. More regular firing can have CV below one, as in the ocular motor neurons analyzed in 2022.

<!-- pedagogy-paragraph: p89 sha256 8cc6b4a04c87839efa37bcf229b5deacfb4db53d1f6ee3b8786599951d9d2837 -->
p89, lines 89-89; list_item; priority: unchanged; previous: p88; next: p91

> The count variance divided by mean count is the [**Fano factor**]{.definition-term custom-style="Definition Term"}; its value also depends on the counting interval.

<!-- pedagogy-paragraph: p91 sha256 31eda53b4f2ba55a576cc45a670ed43cb5ad4cd29ef9a1c1672b21edaef9959d -->
p91, lines 91-91; prose; priority: unchanged; previous: p89; next: p95

> CV and Fano factor cannot be substituted for one another without additional assumptions.


Claim-bearing content: figure

Claims to check:

- Claim c1, line 41: "$$ \Pr(K=k)=e^{-\lambda}\frac{\lambda^k}{k!}, \qquad \lambda=r\Delta t, \qquad k=0,1,2,\ldots . $$" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c2, line 56: "Likewise, summing $k(k-1)\Pr(K=k)$ gives $\lambda^2$." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c3, line 56: "Since $K^2=K(K-1)+K$," -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c4, line 58: "$$ \mathbb E[K^2]=\lambda^2+\lambda, \qquad \operatorname{Var}(K)=\mathbb E[K^2]-\mathbb E[K]^2=\lambda. $$" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c5, line 66: "Its relative standard deviation is $\sqrt\lambda/\lambda=1/\sqrt\lambda$." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c6, line 66: "Comparisons between networks must specify which quantities are held constant.[^f-poisson]" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c7, line 70: "Suppose the expected rate is 20 spikes per second and an observation lasts 50 ms." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c8, line 70: "The expected count is $20\times0.05=1$." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c9, line 70: "The probability of seeing no spike is $e^{-1}=0.368$." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c10, line 72: "Their total count is Poisson with mean 20 and standard deviation $\sqrt{20}=4.47$." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c11, line 72: "The total rate estimate has a relative standard deviation of about 22.4%, compared with 100% for one cell." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c12, line 78: "Caption: Analytic teaching construction for the chapter’s 20 Hz, 50 ms example. The count is Poisson with mean 1 for one cell and mean 20 for 20 conditionally independent cells. Both panels plot the rate per cell $K/(N\Delta t)$, so both estimates have mean 20 Hz; their standard deviations are 20..." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c13, line 82: "S43, p. 9](../papers/burak-fiete-2012-persistent-activity-si.pdf#page=9)." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c14, line 84: "This qualification prevents treating a recurrent Poisson network as a collection of independent complete spike trains." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c15, line 91: "CV and Fano factor cannot be substituted for one another without additional assumptions." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]

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

<!-- pedagogy-unit: content/chapters/01-foundations.md::sec:FOUNDATIONS-COVARIANCE -->

### Mean squared displacement combines random spread with mean motion

Location: line 93, anchor `sec:FOUNDATIONS-COVARIANCE`

First content kind: `prose`

Opening passage line: 95
Closing passage line: 128

Paragraphs in source order (complete `PARAGRAPH_REVIEW.json`):

<!-- pedagogy-paragraph: p95 sha256 456ec42a9ccba08e8e09254938b627962bbb970ee5f22e7835209db40c05eecf -->
p95, lines 95-95; prose; priority: unchanged; previous: p91; next: p97

> To identify where variability enters a pathway, the eye paper compares measurements that share some fluctuations and have other fluctuations of their own.

<!-- pedagogy-paragraph: p97 sha256 53b9b3b1c17e59f66c1e65a58fdf50e5c2aae917b4994c077c7ba77c790d3a75 -->
p97, lines 97-97; prose; priority: unchanged; previous: p95; next: p104

> For random variables $X$ and $Y$, [**covariance**]{.definition-term custom-style="Definition Term"} measures how their centered values vary together:

<!-- pedagogy-paragraph: p104 sha256 d04ad097432a91ff5275e854262962ac5c731b174981f97aeb9cce790217334c -->
p104, lines 104-104; prose; priority: unchanged; previous: p97; next: p112

> It has units equal to the product of the units of $X$ and $Y$. Variance is the special case $\operatorname{Cov}(X,X)$. Expanding a centered sum or difference gives

<!-- pedagogy-paragraph: p112 sha256 3ed7347d405ede1db4bcc0b483b7b3a26c2c15f0405886e55ad59e7d67623d7d -->
p112, lines 112-112; prose; priority: unchanged; previous: p104; next: p119

> Independence makes the covariance zero when the relevant moments exist. Zero covariance alone does not imply independence in general. The [**correlation coefficient**]{.definition-term custom-style="Definition Term"} rescales covariance:

<!-- pedagogy-paragraph: p119 sha256 fc208e639de255285c4cf7d1ed14dec85cc188102e5046b6e2541ec8d8b88936 -->
p119, lines 119-119; prose; priority: unchanged; previous: p112; next: p121

> It has no units and lies between $-1$ and $1$ for variables with nonzero variance. The magnitude of a correlation is not automatically the fraction of an output variance caused by a particular source. Establishing that interpretation requires a model of the signal, noise, and measurement gains. The [eye-drift covariance calculation](ch-eye-drift.html#sec-eye-chi) supplies that model for eye displacement.

<!-- pedagogy-paragraph: p121 sha256 5b53d10e8b02bc8b8139fbac1ee75f316ab16c3a14f7475f5302ee18c0bfd3f5 -->
p121, lines 121-121; prose; priority: unchanged; previous: p119; next: p128

> The quantity that changes between two times is a displacement $\Delta x=x(t+\ell)-x(t)$, where $\ell$ is a time lag. Its mean square splits into

<!-- pedagogy-paragraph: p128 sha256 eb28b92d03f26da97d3b70224465f8ad73f500aae18f4aa7c52df353bd0ef344 -->
p128, lines 128-128; prose; priority: unchanged; previous: p121; next: none

> Thus a growing mean squared displacement can contain random spread, a systematic change in the mean, or both. This identity will distinguish random memory diffusion from a biased or leaky integrator.


Claim-bearing content: none

Claims to check:

- Claim c1, line 119: "It has no units and lies between $-1$ and $1$ for variables with nonzero variance." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]

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

## ch:PERSISTENCE - Stable representations can accumulate error

Source file: `content/chapters/01b-persistence.md`

Purpose: The next distinction is between a value and the activity that represents it. Eye position is one number, but a circuit can represent it through thousands of neural activities. A disturbance can change those activities without changing the represented value. Another disturbance can leave a coherent activity pattern while changing the value. The geometry of these two changes will explain why a stable-looking circuit can still accumulate memory error.[^f-memory]

Prerequisites: ch:FOUNDATIONS

Sidecar sections: Stable activity with a vulnerable stored value, Independent steps with equal duration and variance give linear variance growth, A fixed spatial map differs from a value that wanders over time

Blocks: 3 figure(s), 0 equation(s), 0 code block(s)

Result labels: No Answer/Conclusion/Feedback label detected

<!-- pedagogy-unit: content/chapters/01b-persistence.md::ch:PERSISTENCE -->

### Chapter opening

Location: line 1, anchor `ch:PERSISTENCE`

First content kind: `prose`

Opening passage line: 3
Closing passage line: 5

Paragraphs in source order (complete `PARAGRAPH_REVIEW.json`):

<!-- pedagogy-paragraph: p3 sha256 d8c8c44b5c0cfc08a6e4eba66b470726ed01293e4d9311f1888417ebca398c2f -->
p3, lines 3-3; prose; priority: unchanged; previous: none; next: p5

> The next distinction is between a value and the activity that represents it. Eye position is one number, but a circuit can represent it through thousands of neural activities. A disturbance can change those activities without changing the represented value. Another disturbance can leave a coherent activity pattern while changing the value. The geometry of these two changes will explain why a stable-looking circuit can still accumulate memory error.[^f-memory]

<!-- pedagogy-paragraph: p5 sha256 f10c3e79618dd14b95691e110c0784d00b67cd5eea2031e53e030dfb8743296d -->
p5, lines 5-5; prose; priority: unchanged; previous: p3; next: p9

> We first build a small example in which some disturbances fade while others leave a different stored angle. We then ask what happens when small lasting changes arrive repeatedly, deriving how their spread grows with time and how a fixed bias changes that prediction. The final distinction is between this changing value and an irregular spatial map that stays fixed. It explains why the memory, eye-motion, and place-field papers need different models even though all three concern variable neural signals.


Claim-bearing content: none

Claims to check:

- Claim c1, line 3: "The geometry of these two changes will explain why a stable-looking circuit can still accumulate memory error.[^f-memory]" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c2, line 5: "We first build a small example in which some disturbances fade while others leave a different stored angle." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c3, line 5: "We then ask what happens when small lasting changes arrive repeatedly, deriving how their spread grows with time and how a fixed bias changes that prediction." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]

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

<!-- pedagogy-unit: content/chapters/01b-persistence.md::sec:FOUNDATIONS-ATTRACTOR -->

### Stable activity with a vulnerable stored value

Location: line 7, anchor `sec:FOUNDATIONS-ATTRACTOR`

First content kind: `prose`

Opening passage line: 9
Closing passage line: 54

Paragraphs in source order (complete `PARAGRAPH_REVIEW.json`):

<!-- pedagogy-paragraph: p9 sha256 ec62c241b63311d71d95e924d93adfceefca42f02fd527c17a0c55c2f59b4045 -->
p9, lines 9-9; prose; priority: unchanged; previous: p5; next: p11

> A circuit's current activities are its [**state**]{.definition-term custom-style="Definition Term"}. A dynamical equation specifies how that state changes. A [**fixed point**]{.definition-term custom-style="Definition Term"} is a state where the deterministic rate of change is zero. It is stable in a direction if a small disturbance in that direction decays.

<!-- pedagogy-paragraph: p11 sha256 66ffbc6b4ae123e301ce0e9fba9f61daec42211118a9652ac528cdd1c6ee2970 -->
p11, lines 11-11; prose; priority: unchanged; previous: p9; next: p13

> Memory of a continuous quantity calls for a family of persistent states. A [**continuous attractor**]{.definition-term custom-style="Definition Term"} is a continuous family of fixed points with restoring dynamics toward the family and a neutral direction along it. Neutral means that there is no restoring force along that direction in the ideal deterministic model. The family is an [**attractor manifold**]{.definition-term custom-style="Definition Term"}. Its dimension counts independent coordinates represented on it, rather than neurons in the circuit. A line attractor has one represented coordinate; a ring can represent a periodic coordinate such as heading.[^f-memory]

<!-- pedagogy-paragraph: p13 sha256 20bf2296bca45823292daeef9a4d081a0a0ad07808b54e7d812533491214ca62 -->
p13, lines 13-13; prose; priority: unchanged; previous: p11; next: p15

> [**Example: two disturbances to the same stored angle**]{#sec-foundations-attractor-example}

<!-- pedagogy-paragraph: p15 sha256 2df33ec0c10a2f3f8c8ed3f316c210d3d76be5465ff3d1685746997f0b66b6d4 -->
p15, lines 15-15; prose; priority: unchanged; previous: p13; next: p21

> Consider a teaching model with two activities $r_1,r_2$ in spikes per second. Let $b=40$ spikes per second and let $k=2$ spikes per second per degree. A stored angle $\theta$ corresponds to

<!-- pedagogy-paragraph: p21 sha256 95f000ec66c24f06913f5bde801beb9c39a1455720fe17fa322f985a9dc7e71d -->
p21, lines 21-21; prose; priority: unchanged; previous: p15; next: p29

> The fixed points lie on the line $r_1+r_2=2b$. Restrict attention to angles where both rates remain positive. Define the deviation in their mean activity and the represented angle as

<!-- pedagogy-paragraph: p29 sha256 ee9984e3707247939ce0832e0ddbf38183511c8d034bf3bfd21579d9fa4279dc -->
p29, lines 29-29; prose; priority: unchanged; previous: p21; next: p35

> Suppose each activity changes according to

<!-- pedagogy-paragraph: p35 sha256 8fcb790f0a0ad95fa8b469f231da0b99e7f09513b88d74d8350d785d3fe2d040 -->
p35, lines 35-35; prose; priority: unchanged; previous: p29; next: p41

> where $a>0$ has units inverse seconds. Adding and subtracting these equations gives

<!-- pedagogy-paragraph: p41 sha256 7db97decba35b60b8828ada87ee3d9128149429dee69a6f5c049b3ef09ca928f -->
p41, lines 41-41; prose; priority: unchanged; previous: p35; next: p43

> The first equation has solution $x(t)=x(0)e^{-at}$, so disturbances in the common activity decay. The second equation retains any angle set by the initial state.

<!-- pedagogy-paragraph: p43 sha256 06c0ab40d5067e29fce3f655566f6d80cb85bdb6f8ed3aff39027b89c913cfa9 -->
p43, lines 43-43; prose; priority: unchanged; previous: p41; next: p45

> At $\theta=5$ degrees, the rates are $(50,30)$. Compare two disturbances from this same state:

<!-- pedagogy-paragraph: p45 sha256 d029c2fdcefcbded0f314865d14dbf0ee2633db997ba41fef1a0ce8c04f669fe -->
p45, lines 45-45; list_item; priority: unchanged; previous: p43; next: p46

> A disturbance of $(+3,+3)$ changes the rates to $(53,33)$. It creates $x=3$ but leaves the represented angle at 5 degrees. The restoring dynamics return to $(50,30)$.

<!-- pedagogy-paragraph: p46 sha256 cce475b6a0e5add615d31a12e691b5520ad7a708eb5d7d6930c24f9d300bdf4d -->
p46, lines 46-46; list_item; priority: unchanged; previous: p45; next: p48

> A disturbance of $(+3,-3)$ gives $(53,27)$, with $x=0$ and angle $26/(2\times2)=6.5$ degrees. This state lies on the fixed-point line, so there is no restoring response.

<!-- pedagogy-paragraph: p48 sha256 454847f611714aa32ed70652cd5c8015cbe18c48e8677ef7eee5d7bb62785203 -->
p48, lines 48-48; prose; priority: unchanged; previous: p46; next: p50

> In the second case, the circuit remains coherent while holding the wrong angle.

<!-- pedagogy-paragraph: p50 sha256 548d9cd4a0000854f190d92f2284bce12b97e1fb384f626d7031d719228541d8 -->
p50, lines 50-50; prose; priority: unchanged; previous: p48; next: p54

> The two changes occupy different directions in the activity plane. The solid arrow in the figure is the restoring motion produced by the model. The dashed arrow shows the imposed disturbance along the fixed-point line, rather than a deterministic restoring flow.

<!-- pedagogy-paragraph: p54 sha256 2b29da13d43cea47b354e04ac92abc2ba9778ec443dd2c436be119e8ab091b8a -->
p54, lines 54-54; prose; priority: unchanged; previous: p50; next: p58

> This construction illustrates the geometry; it is not a fit to eye-neuron recordings. In a larger network, the direction that survives depends on its connection weights and cannot always be found by an ordinary perpendicular projection. The [network calculation](ch-memory-dynamics.html#sec-memory-linearization) derives the correct projection from the network's linearized dynamics.


Claim-bearing content: figure

Claims to check:

- Claim c1, line 9: "It is stable in a direction if a small disturbance in that direction decays." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c2, line 11: "A line attractor has one represented coordinate; a ring can represent a periodic coordinate such as heading.[^f-memory]" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c3, line 15: "Let $b=40$ spikes per second and let $k=2$ spikes per second per degree." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c4, line 17: "$$ r_1=b+k\theta,\qquad r_2=b-k\theta. $$" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c5, line 21: "The fixed points lie on the line $r_1+r_2=2b$." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c6, line 21: "Restrict attention to angles where both rates remain positive." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c7, line 23: "$$ x=\frac{r_1+r_2}{2}-b, \qquad \theta=\frac{r_1-r_2}{2k}. $$" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c8, line 31: "$$ \dot r_1=-a x,\qquad \dot r_2=-a x, $$" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c9, line 35: "where $a>0$ has units inverse seconds." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c10, line 37: "$$ \dot x=-a x,\qquad \dot\theta=0. $$" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c11, line 43: "At $\theta=5$ degrees, the rates are $(50,30)$." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c12, line 45: "A disturbance of $(+3,+3)$ changes the rates to $(53,33)$." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c13, line 45: "It creates $x=3$ but leaves the represented angle at 5 degrees." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c14, line 46: "A disturbance of $(+3,-3)$ gives $(53,27)$, with $x=0$ and angle $26/(2\times2)=6.5$ degrees." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c15, line 48: "In the second case, the circuit remains coherent while holding the wrong angle." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c16, line 52: "Caption: A common activity disturbance returns to the initial angle, while an along-line disturbance persists as a changed angle. The solid arrow is deterministic recovery; the dashed arrow is an imposed disturbance. This is the guide's two-activity construction, not experimental data. Alt: Two a..." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c17, line 54: "In a larger network, the direction that survives depends on its connection weights and cannot always be found by an ordinary perpendicular projection." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]

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

<!-- pedagogy-unit: content/chapters/01b-persistence.md::sec:FOUNDATIONS-DIFFUSION -->

### Independent steps with equal duration and variance give linear variance growth

Location: line 56, anchor `sec:FOUNDATIONS-DIFFUSION`

First content kind: `prose`

Opening passage line: 58
Closing passage line: 121

Paragraphs in source order (complete `PARAGRAPH_REVIEW.json`):

<!-- pedagogy-paragraph: p58 sha256 ce32e72bf288cd07bd1d262c4d4451f1ffa75e1e2c745f6c2da301cdd145d936 -->
p58, lines 58-58; prose; priority: unchanged; previous: p54; next: p60

> If persistent angular changes arrive repeatedly, their errors accumulate. Divide time into intervals of length $\Delta t$. Let $\xi_j$ be the change in the represented coordinate during interval $j$. The calculation assumes:

<!-- pedagogy-paragraph: p60 sha256 be96afcb4dd8dd876c0f97e0695b5f8d3f0a642e356b9f7e367d2d13d91908cc -->
p60, lines 60-60; list_item; priority: unchanged; previous: p58; next: p61

> increments are independent;

<!-- pedagogy-paragraph: p61 sha256 3c39389060f132b69c452002f3e58fc1a15ac30d791d264041ac1e3d4ffd4908 -->
p61, lines 61-61; list_item; priority: unchanged; previous: p60; next: p62

> each increment has mean zero;

<!-- pedagogy-paragraph: p62 sha256 cb0ee784ec71238f67ba967be2b430cfb838fa5c443647b29eb899f09370986b -->
p62, lines 62-62; list_item; priority: unchanged; previous: p61; next: p64

> each increment has variance $2D\Delta t$, where $D$ has units coordinate squared per time.

<!-- pedagogy-paragraph: p64 sha256 2c3a77659cd35740e564899700b353c5faf042d9e981bc2b4edb067a7739317d -->
p64, lines 64-64; prose; priority: unchanged; previous: p62; next: p74

> After $n$ intervals,

<!-- pedagogy-paragraph: p74 sha256 15b2418ad9711f3e9241582ca1b31324494cacfa37b61adb92c03c7267bd588a -->
p74, lines 74-74; prose; priority: unchanged; previous: p64; next: p82

> Writing $t=n\Delta t$ gives linear variance growth $2Dt$. In the continuous diffusion approximation this becomes

<!-- pedagogy-paragraph: p82 sha256 45390561c010e81c8b613f22ff2c6c9734cb7f1c6262df1c3adfcf7c954a5d16 -->
p82, lines 82-82; prose; priority: unchanged; previous: p74; next: p84

> The [**Brownian motion**]{.definition-term custom-style="Definition Term"} $W(t)$ starts at zero, has independent Gaussian increments, and satisfies $\operatorname{Var}[W(t)-W(s)]=t-s$ for $t\geq s$. It describes the limit of many small, suitably independent fluctuations. A physical network need only approach this description over the time and noise scales relevant to the calculation. The parameter $D$ is its diffusion coefficient. It measures the rate of variance growth; a single trajectory need not move monotonically away from its starting value.

<!-- pedagogy-paragraph: p84 sha256 ee8109d308c676ac855a3d589bc359bc0b9fdf0a1205b6e520e6e5d163a864d0 -->
p84, lines 84-84; prose; priority: unchanged; previous: p82; next: p86

> The mean squared displacement, or MSD, is the expected squared change across a lag. In the zero-mean diffusion just defined, MSD is $2Dt$. A [**root mean squared displacement**]{.definition-term custom-style="Definition Term"} is its square root, $\sqrt{2Dt}$, and has the same units as the represented coordinate. In several dimensions, adding independent coordinate contributions gives an overall MSD of $2dDt$ only when each of the $d$ coordinates has the same diffusion coefficient. A paper that defines its diffusion parameter as the entire two-dimensional MSD slope uses a different convention.

<!-- pedagogy-paragraph: p86 sha256 21fbcefc06de9f037ced501b987387ba259bc1823d6430862f48d7ea8aea7832 -->
p86, lines 86-86; prose; priority: unchanged; previous: p84; next: p88

> [**Example: why the noise grows slower than a fixed bias**]{#sec-foundations-diffusion-example}

<!-- pedagogy-paragraph: p88 sha256 25e2bea390536dc7b6928fb39b322736170a63078394c6c8f8517dba29c3d255 -->
p88, lines 88-88; prose; priority: unchanged; previous: p86; next: p90

> Take an illustrative angular diffusion coefficient $D=0.02$ degrees squared per second. At 0.35 s its variance is $0.014$ degrees squared and its root mean squared displacement is 0.118 degrees, or about 7.10 arcminutes. At 1 s the root mean squared displacement is 0.20 degrees. These are teaching values, not a new estimate from either monkey.

<!-- pedagogy-paragraph: p90 sha256 b65818f05ab22cc9b82ca82b30056d679efa0cda9041acec6e6b2a8f8474645d -->
p90, lines 90-90; prose; priority: unchanged; previous: p88; next: p98

> If there is also a constant bias velocity $v=0.10$ degrees per second, then

<!-- pedagogy-paragraph: p98 sha256 c283df8e5ce7370c9a2256c5fac1c8cb926884cdfca2b06ae9bf1a7fea058630 -->
p98, lines 98-98; prose; priority: unchanged; previous: p90; next: p100

> The deterministic and random contributions are equal at $t=2D/v^2=4$ seconds. Their equal contributions there are each $0.16$ degrees squared. At longer times the bias dominates this unbounded model even though it was small over a short observation. A theory of random diffusion must therefore account for systematic drift separately.

<!-- pedagogy-paragraph: p100 sha256 682ea9b57198e4f02f2b7a799d285f9e1d24a6720ad2306991490428ea9f3038 -->
p100, lines 100-100; prose; priority: unchanged; previous: p98; next: p102

> Sample paths show the irregular motion; exact displacement scales show how its spread differs from a fixed bias.

<!-- pedagogy-paragraph: p102 sha256 2c643bd85d3e8933fd7127e586cd0d302d74dcd69d691fc3921ef217cc019e39 -->
p102, lines 102-102; prose; priority: unchanged; previous: p100; next: p106

> <div class="figure-scroll">

<!-- pedagogy-paragraph: p106 sha256 aac32651b10f567c461b9b4f255d6fb1fa6859b5368d8bd9a51af920ab21cf23 -->
p106, lines 106-106; prose; priority: unchanged; previous: p102; next: p108

> </div>

<!-- pedagogy-paragraph: p108 sha256 4cef68e04567ad5a4ae61170f22c96b4f25c85410853a8de08dc0cb857c626d2 -->
p108, lines 108-108; prose; priority: unchanged; previous: p106; next: p110

> A single path can turn back toward zero even while the root mean squared displacement grows. A constant bias grows linearly, so it eventually exceeds the square root growth of the random displacement scale. See [Gaussian displacement density, SI Eq. S30, p. 7](../papers/burak-fiete-2012-persistent-activity-si.pdf#page=7).

<!-- pedagogy-paragraph: p110 sha256 d9d175c58f25bbeb55b5a695db7dcf469084c56df1b1eef3ab6d1ad40e73b4b6 -->
p110, lines 110-110; prose; priority: unchanged; previous: p108; next: p119

> Two times along a Brownian path are correlated even though its increments are independent. For $0\leq s\leq t$, write $W(t)=W(s)+[W(t)-W(s)]$. The bracketed increment is independent of $W(s)$ and has mean zero, giving

<!-- pedagogy-paragraph: p119 sha256 1e37ab0e3032ae94247421633fa7c4675ca56252f66c58558321d2d4e7582ccf -->
p119, lines 119-119; prose; priority: unchanged; previous: p110; next: p121

> The same argument gives covariance $2D\min(s,t)$ for a diffusing coordinate started at a fixed value. This identity is the intermediate step needed to compute the error from averaging a memory that moves during readout. It also helps explain why smoothing a diffusive input is different from smoothing a stationary noise source.

<!-- pedagogy-paragraph: p121 sha256 dbce08bec7cd169a953fe3677fe44214e91c8b79000f627545e651799aab93a5 -->
p121, lines 121-121; prose; priority: unchanged; previous: p119; next: p125

> A finite range, a periodic coordinate, external feedback, or a position-dependent diffusion coefficient changes long-time behavior. For example, ordinary squared angular distance on a ring cannot keep growing linearly forever. The basic $2Dt$ result is local or unbounded unless those conditions are treated separately.


Claim-bearing content: figure

Claims to check:

- Claim c1, line 66: "$$ \theta_n-\theta_0=\sum_{j=1}^{n}\xi_j, \qquad \operatorname{Var}(\theta_n-\theta_0) =\sum_{j=1}^{n}\operatorname{Var}(\xi_j) =2Dn\Delta t. $$" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c2, line 76: "$$ \theta(t)=\theta(0)+\sqrt{2D}\,W(t), \qquad \mathbb E[(\theta(t)-\theta(0))^2]=2Dt. $$" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c3, line 82: "It describes the limit of many small, suitably independent fluctuations." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c4, line 82: "A physical network need only approach this description over the time and noise scales relevant to the calculation." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c5, line 84: "In several dimensions, adding independent coordinate contributions gives an overall MSD of $2dDt$ only when each of the $d$ coordinates has the same diffusion coefficient." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c6, line 88: "Take an illustrative angular diffusion coefficient $D=0.02$ degrees squared per second." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c7, line 88: "At 0.35 s its variance is $0.014$ degrees squared and its root mean squared displacement is 0.118 degrees, or about 7.10 arcminutes." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c8, line 88: "At 1 s the root mean squared displacement is 0.20 degrees." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c9, line 90: "If there is also a constant bias velocity $v=0.10$ degrees per second, then" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c10, line 92: "$$ \theta(t)-\theta(0)=vt+\sqrt{2D}\,W(t), \qquad \operatorname{MSD}(t)=v^2t^2+2Dt. $$" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c11, line 98: "The deterministic and random contributions are equal at $t=2D/v^2=4$ seconds." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c12, line 98: "Their equal contributions there are each $0.16$ degrees squared." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c13, line 98: "At longer times the bias dominates this unbounded model even though it was small over a short observation." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c14, line 98: "A theory of random diffusion must therefore account for systematic drift separately." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c15, line 104: "Caption: Simulated Brownian teaching paths and analytic displacement scales for $D=0.02$ degrees squared per second and $v=0.10$ degrees per second. The upper paths have zero drift and start at zero; the dashed envelope is the exact root mean squared displacement, not a boundary on individual pat..." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c16, line 108: "S30, p. 7](../papers/burak-fiete-2012-persistent-activity-si.pdf#page=7)." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c17, line 121: "For example, ordinary squared angular distance on a ring cannot keep growing linearly forever." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]

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

<!-- pedagogy-unit: content/chapters/01b-persistence.md::sec:FOUNDATIONS-RANDOMNESS -->

### A fixed spatial map differs from a value that wanders over time

Location: line 123, anchor `sec:FOUNDATIONS-RANDOMNESS`

First content kind: `prose`

Opening passage line: 125
Closing passage line: 137

Paragraphs in source order (complete `PARAGRAPH_REVIEW.json`):

<!-- pedagogy-paragraph: p125 sha256 11a596f759327f7f1b8438c00bf80e55c9e6146ce6064848690130fe26d070cd -->
p125, lines 125-125; prose; priority: unchanged; previous: p121; next: p127

> The memory and eye papers study fluctuations that accumulate as time passes. The place-field paper instead starts with a random function of physical position. Once drawn for a cell and an environment, that function is fixed while the animal moves through the map. Revisiting a place evaluates the same expected-rate function, although the actual spikes can still vary from visit to visit.

<!-- pedagogy-paragraph: p127 sha256 361a7990cb20565a391565e6ea763ff112c8f91ef1ae9a58c276d51904a66476 -->
p127, lines 127-127; prose; priority: unchanged; previous: p125; next: p129

> These two kinds of randomness can occur together. A circuit may maintain a position estimate with time-dependent noise, while downstream cells respond to position through irregular but repeatable tuning curves. Observing irregular spatial maps does not tell us how fast the maintained position drifts. Conversely, finding diffusion of a stored value does not determine the shapes of individual place fields. The following chapters develop the dynamical calculation first, then the experiment that tests a possible consequence, and finally the spatial statistics.[^f-place]

<!-- pedagogy-paragraph: p129 sha256 7458f4f34d00d79016e4dc30cd71022a682247b81ac2f81c881b2611e1220d4b -->
p129, lines 129-129; prose; priority: unchanged; previous: p127; next: p131

> The three questions can now be placed beside the kind of variation each paper studies.

<!-- pedagogy-paragraph: p131 sha256 2c643bd85d3e8933fd7127e586cd0d302d74dcd69d691fc3921ef217cc019e39 -->
p131, lines 131-131; prose; priority: unchanged; previous: p129; next: p135

> <div class="figure-scroll">

<!-- pedagogy-paragraph: p135 sha256 aac32651b10f567c461b9b4f255d6fb1fa6859b5368d8bd9a51af920ab21cf23 -->
p135, lines 135-135; prose; priority: unchanged; previous: p131; next: p137

> </div>

<!-- pedagogy-paragraph: p137 sha256 6e04703a316755d87da48b203cc6506cd5a4de79fdaaf1bab268cb4e3d16a3bf -->
p137, lines 137-137; prose; priority: unchanged; previous: p135; next: none

> The rows compare different questions; they do not establish a single circuit connecting all three papers.


Claim-bearing content: figure

Claims to check:

- Claim c1, line 125: "Once drawn for a cell and an environment, that function is fixed while the animal moves through the map." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c2, line 127: "The following chapters develop the dynamical calculation first, then the experiment that tests a possible consequence, and finally the spatial statistics.[^f-place]" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c3, line 133: "Caption: Memory loss and eye drift concern changes over time; place-field statistics concern variation across a fixed spatial map. The eye pathway shows the proposed changing-command mechanism. Original guide schematic based on the three papers, with illustrative traces rather than recorded data...." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]

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

## ch:MEMORY-DYNAMICS - Spiking noise produces diffusion along the memory attractor

Source file: `content/chapters/02-memory-dynamics.md`

Purpose: A network can keep firing after a stimulus disappears and still lose the value that the stimulus supplied. The important question is whether the activity pattern stays in the right place, not just whether activity continues. Burak and Fiete study this distinction in a network whose stable activity patterns form a continuous set.[^p1-model]

Prerequisites: ch:PERSISTENCE

Sidecar sections: Recurrent spikes renew decaying synaptic activity, The network's return flow determines the lasting memory change, Projecting spike fluctuations gives the diffusion coefficient, Symmetric weights express diffusion through tuning curves

Blocks: 3 figure(s), 0 equation(s), 0 code block(s)

Result labels: No Answer/Conclusion/Feedback label detected

<!-- pedagogy-unit: content/chapters/02-memory-dynamics.md::ch:MEMORY-DYNAMICS -->

### Chapter opening

Location: line 1, anchor `ch:MEMORY-DYNAMICS`

First content kind: `prose`

Opening passage line: 3
Closing passage line: 9

Paragraphs in source order (complete `PARAGRAPH_REVIEW.json`):

<!-- pedagogy-paragraph: p3 sha256 5a0d37fcf3da8ff24026d22f2579f78e4798eeca5413a0e0d98de1cd64e13c9b -->
p3, lines 3-3; prose; priority: unchanged; previous: none; next: p5

> A network can keep firing after a stimulus disappears and still lose the value that the stimulus supplied. The important question is whether the activity pattern stays in the right place, not just whether activity continues. Burak and Fiete study this distinction in a network whose stable activity patterns form a continuous set.[^p1-model]

<!-- pedagogy-paragraph: p5 sha256 5e3ec024579c967e9286fba7a68836641bcd48abe4cccba26b5b82b97cd9ca2e -->
p5, lines 5-5; prose; priority: unchanged; previous: p3; next: p7

> To calculate the loss of accuracy, we first describe how spikes renew synaptic activity as it decays. We then follow a small disturbance through the circuit's return toward a stable pattern and identify the change in stored value that remains. Adding these lasting random changes gives a local rate of spreading. When connections have equal weights in both directions, we can express that rate using the cells' tuning curves and check its meaning in a two-cell example. The following chapter asks how this local prediction extends to longer delays.

<!-- pedagogy-paragraph: p7 sha256 61b4f34831993380986a61c2a77b024a8eac49c25deb9dcbcf2de2c053254d20 -->
p7, lines 7-7; prose; priority: unchanged; previous: p5; next: p9

> Paper and Supporting Information (SI) links open the cited PDF page, near the passage where the viewer supports it. Use the equation, figure, or paragraph label to find the passage; the PDFs have no numbered text lines.

<!-- pedagogy-paragraph: p9 sha256 8758a0c68055cd1d7a4b67d2144569b217a893ecb3046e52459d2db85a7e3a5a -->
p9, lines 9-9; prose; priority: unchanged; previous: p7; next: p14

> The memory coordinate is $\theta$. Its initial value is $\Theta$. A bar denotes a noise free steady state, so $\bar r_i(\theta)$ is neuron $i$'s steady firing rate at memory value $\theta$. The common synaptic time constant is $\tau$. A one dimensional diffusion coefficient $D$ has units of memory coordinate squared per time, with the convention $\operatorname{Var}[\theta(t)-\Theta]=2Dt$ when $D$ is constant and boundaries do not matter.


Claim-bearing content: none

Claims to check:

- Claim c1, line 3: "Burak and Fiete study this distinction in a network whose stable activity patterns form a continuous set.[^p1-model]" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c2, line 5: "We then follow a small disturbance through the circuit's return toward a stable pattern and identify the change in stored value that remains." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c3, line 9: "A one dimensional diffusion coefficient $D$ has units of memory coordinate squared per time, with the convention $\operatorname{Var}[\theta(t)-\Theta]=2Dt$ when $D$ is constant and boundaries do not matter." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]

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

<!-- pedagogy-unit: content/chapters/02-memory-dynamics.md::sec:MEMORY-SPIKES -->

### Recurrent spikes renew decaying synaptic activity

Location: line 12, anchor `sec:MEMORY-SPIKES`

First content kind: `prose`

Opening passage line: 14
Closing passage line: 88

Paragraphs in source order (complete `PARAGRAPH_REVIEW.json`):

<!-- pedagogy-paragraph: p14 sha256 51fa89c80bbdff90a122e75b0472861f87673f18dec7016a144ddbe4f2c9e838 -->
p14, lines 14-14; prose; priority: unchanged; previous: p9; next: p16

> How can brief spikes maintain a state for much longer than the duration of a spike? In this model, each spike leaves a synaptic activation that decays gradually. Incoming activations determine new firing rates; the resulting spikes renew those activations. This feedback can support activity after the external stimulus has ended.

<!-- pedagogy-paragraph: p16 sha256 61c32bf6c7d5010ea5cf1e69d2756805fc74d756d49004d89b08ff238b5fe5cf -->
p16, lines 16-16; prose; priority: unchanged; previous: p14; next: p22

> Let $N_i(t)$ count neuron $i$'s spikes up to time $t$. The activation $s_i$ rises by one at each of its spikes and otherwise decays:

<!-- pedagogy-paragraph: p22 sha256 316268840047bfdefb5b2118549103e5d7a5c7201e67211f937617deb83eabcb -->
p22, lines 22-22; prose; priority: unchanged; previous: p16; next: p28

> Equivalently, if its spikes occur at times $t_i^\alpha$,

<!-- pedagogy-paragraph: p28 sha256 9006951dd37db6f4eb03d5ade741a8ed42bfc433bf08dcbaa1d26dca3a1a22e3 -->
p28, lines 28-28; prose; priority: unchanged; previous: p22; next: p30

> after initial transients. Here $s_i$ is dimensionless in the convention that each spike adds one unit.

<!-- pedagogy-paragraph: p30 sha256 7eac28f467bb547ebcf147a697cbc1044361e75128de9e099d3ddeec6a0803df -->
p30, lines 30-30; prose; priority: unchanged; previous: p28; next: p32

> For five illustrative spike times, the plot shows the events and the activation they leave behind.

<!-- pedagogy-paragraph: p32 sha256 2c643bd85d3e8933fd7127e586cd0d302d74dcd69d691fc3921ef217cc019e39 -->
p32, lines 32-32; prose; priority: unchanged; previous: p30; next: p36

> <div class="figure-scroll">

<!-- pedagogy-paragraph: p36 sha256 aac32651b10f567c461b9b4f255d6fb1fa6859b5368d8bd9a51af920ab21cf23 -->
p36, lines 36-36; prose; priority: unchanged; previous: p32; next: p38

> </div>

<!-- pedagogy-paragraph: p38 sha256 7bcebc101fc3d68752aaaad0bd35d63537e6c9387555337d9cc1d87510883b8d -->
p38, lines 38-38; prose; priority: unchanged; previous: p36; next: p40

> The activation retains a decaying contribution from earlier spikes, so a spike train and its activation trace are different objects.

<!-- pedagogy-paragraph: p40 sha256 f185d2789a819913e453567a284f7f8ff493b18cb72d9a292c313a6546983289 -->
p40, lines 40-40; prose; priority: unchanged; previous: p38; next: p47

> The rate $r_i$ has units of spikes per second. The summed input and the firing rule are

<!-- pedagogy-paragraph: p47 sha256 c9479372f0fbd334d3e76ff7e00f7c7b296c4092d9ca049a5f3038512fa95061 -->
p47, lines 47-47; prose; priority: unchanged; previous: p40; next: p49

> The fixed weights $W_{ij}$ say how neuron $j$ affects neuron $i$, and $b_i$ is a constant input. The [**neural transfer function**]{.definition-term custom-style="Definition Term"} $\phi$ converts total input into a nonnegative firing rate. For example, increasing input might increase firing linearly over some input range, or exponentially. The paper allows general connectivity and transfer functions at first ([Model, Eqs. 7–9, p. 5](../papers/burak-fiete-2012-persistent-activity.pdf#page=5&zoom=125,0,372)).[^p1-model]

<!-- pedagogy-paragraph: p49 sha256 276ae423dace37992865f8a7e17cf438d54dd4fedda2df6b07fc96aa814da51c -->
p49, lines 49-49; prose; priority: unchanged; previous: p47; next: p58

> Conditioned on the present rates, spike counts over a short interval $dt$ are independent Poisson variables. Thus

<!-- pedagogy-paragraph: p58 sha256 2d213217d67ac51d540f1da81d08b391967e49cb43712b3d9b80b46c48646890 -->
p58, lines 58-58; prose; priority: unchanged; previous: p49; next: p67

> The symbol $\delta_{ij}$ is one when $i=j$ and zero otherwise. Splitting the count into its mean and fluctuation gives

<!-- pedagogy-paragraph: p67 sha256 ab392351053c8facf1dd8fcb79ccc1b3e88f1b816b44bb79ad06cf887647c52e -->
p67, lines 67-67; prose; priority: unchanged; previous: p58; next: p75

> This is still a jump process. In the paper's [**weak fluctuation approximation**]{.definition-term custom-style="Definition Term"}, many individually small spike contributions produce only small changes in each neuron's total input. Their summed fluctuation can then be represented by Gaussian noise with the same leading mean and covariance:

<!-- pedagogy-paragraph: p75 sha256 849afd7acf5460fe44080c97cb7fa8543fd44984a98cc942ba3bbadb8ee2fbbe -->
p75, lines 75-75; prose; priority: unchanged; previous: p67; next: p77

> where the $B_i$ are independent standard Brownian processes. The noise coefficient has units $\mathrm{s}^{-1/2}$, so its product with $dB_i$ is a dimensionless activation increment. The Gaussian approximation is for small fluctuations in total input. It does not require each single neuron's entire spike train to look like a Gaussian process ([SI Eqs. S2–S5, p. 2](../papers/burak-fiete-2012-persistent-activity-si.pdf#page=2&zoom=125,0,128)).[^p1-weak]

<!-- pedagogy-paragraph: p77 sha256 3a1cb037dc05dc524f9d66a6e3a244a2cebb851c4b901d14345248dd9be897bb -->
p77, lines 77-77; prose; priority: unchanged; previous: p75; next: p79

> The supplement makes this limit concrete by replacing each population with $n$ equivalent neurons and dividing each connection weight by $n$. A summed input has a mean proportional to $n/n=1$, while its variance is proportional to $n/n^2=1/n$. Increasing population size therefore keeps the mean dynamics fixed and reduces input fluctuations. For a ring network, a neuron's [**preferred angle**]{.definition-term custom-style="Definition Term"} is an angle where its tuning curve peaks. Increasing the density of equally spaced preferred angles and scaling weights as $1/N$ serves the same purpose. The paper's formulas give the leading terms in this large population limit, rather than exact finite network identities.[^p1-large]

<!-- pedagogy-paragraph: p79 sha256 4f6cb8f2d857da75dc2cee6f02cc0f1f23c8e6230c7c66e10abc8b7a8b33dd3f -->
p79, lines 79-79; prose; priority: unchanged; previous: p77; next: p88

> Setting noise to zero gives the deterministic rate dynamics $\dot{\mathbf s}=\mathbf F(\mathbf s)$. A continuous attractor is a family of fixed points satisfying

<!-- pedagogy-paragraph: p88 sha256 f6efdfcbffc1cd29bd0d9acc4855839eff6ec3b0807dd55e80b054873923c92e -->
p88, lines 88-88; prose; priority: unchanged; previous: p79; next: p92

> The network must be tuned to possess this family. An arbitrary recurrent network will generally have isolated fixed points rather than a whole line or ring of them.


Claim-bearing content: figure

Claims to check:

- Claim c1, line 34: "Caption: Each spike adds one activation unit, which then decays with a 50 ms time constant. Closely spaced spikes add to the activation left by earlier spikes. The five spike times are an illustrative input, and the activation is calculated exactly from the chapter equation. Alt: Five spike marks..." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c2, line 47: "The paper allows general connectivity and transfer functions at first ([Model, Eqs. 7–9, p. 5](../papers/burak-fiete-2012-persistent-activity.pdf#page=5&zoom=125,0,372)).[^p1-model]" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c3, line 60: "$$ ds_i=\left[-\frac{s_i}{\tau}+\phi(g_i)\right]dt+dM_i, \qquad E[dM_i]=0, \quad E[dM_i dM_j]=\delta_{ij}r_i\,dt. $$" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c4, line 67: "In the paper's [**weak fluctuation approximation**]{.definition-term custom-style="Definition Term"}, many individually small spike contributions produce only small changes in each neuron's total input." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c5, line 75: "The noise coefficient has units $\mathrm{s}^{-1/2}$, so its product with $dB_i$ is a dimensionless activation increment." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c6, line 75: "The Gaussian approximation is for small fluctuations in total input." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c7, line 75: "S2–S5, p. 2](../papers/burak-fiete-2012-persistent-activity-si.pdf#page=2&zoom=125,0,128)).[^p1-weak]" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c8, line 77: "A summed input has a mean proportional to $n/n=1$, while its variance is proportional to $n/n^2=1/n$." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c9, line 77: "Increasing the density of equally spaced preferred angles and scaling weights as $1/N$ serves the same purpose." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c10, line 77: "The paper's formulas give the leading terms in this large population limit, rather than exact finite network identities.[^p1-large]" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c11, line 81: "$$ 0=-\frac{\bar s_i(\theta)}{\tau} +\phi[\bar g_i(\theta)], \qquad \bar s_i(\theta)=\tau\bar r_i(\theta). $$" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c12, line 88: "The network must be tuned to possess this family." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]

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

<!-- pedagogy-unit: content/chapters/02-memory-dynamics.md::sec:MEMORY-LINEARIZATION -->

### The network's return flow determines the lasting memory change

Location: line 90, anchor `sec:MEMORY-LINEARIZATION`

First content kind: `prose`

Opening passage line: 92
Closing passage line: 171

Paragraphs in source order (complete `PARAGRAPH_REVIEW.json`):

<!-- pedagogy-paragraph: p92 sha256 b2e6eae7e9c9e5aaee84f4405e64007436e30ab4583b71153d37c302d7c9b875 -->
p92, lines 92-92; prose; priority: unchanged; previous: p88; next: p94

> A spike perturbs many aspects of a network's state. Most of those changes decay as the state returns to the attractor. To calculate memory loss, we need the one change that survives: the displacement to a different fixed point.

<!-- pedagogy-paragraph: p94 sha256 8319ddadeca0fd8c0bb98180b67edd7fc92fb3ca80868050b939c4ba99c2518b -->
p94, lines 94-94; prose; priority: unchanged; previous: p92; next: p101

> Write the current activation as $\mathbf s=\bar{\mathbf s}(\theta)+\delta\mathbf s$. A [**linearization**]{.definition-term custom-style="Definition Term"} keeps the terms proportional to the small perturbation and drops terms quadratic or higher in it. Taylor expansion of the transfer function gives

<!-- pedagogy-paragraph: p101 sha256 b82818d5f554fd7324e052660a7f79577db59f4f81ab7b6dd3dccd85b08a497b -->
p101, lines 101-101; prose; priority: unchanged; previous: p94; next: p110

> The constant terms cancel because $\bar{\mathbf s}$ is a fixed point. Therefore

<!-- pedagogy-paragraph: p110 sha256 d7ebb275e853df3e3325fa2d46b421976ffcb73960bc72a8c240a3dbb1f3083c -->
p110, lines 110-110; prose; priority: unchanged; previous: p101; next: p112

> In this leading local calculation the noise strengths are evaluated at the fixed point. The entries of $K$ have units of inverse time.[^p1-projection]

<!-- pedagogy-paragraph: p112 sha256 304dd8dac46d7f3b9e61f07b014d18878e606a90f911a07cc0b6c13fef5d7479 -->
p112, lines 112-112; prose; priority: unchanged; previous: p110; next: p119

> Moving a little along the fixed point family changes the activation by

<!-- pedagogy-paragraph: p119 sha256 94f3ecaae1c4e3b7ccf9f8dbab75022e08dfc595dc1f5a6039b71bf06fa969c5 -->
p119, lines 119-119; prose; priority: unchanged; previous: p112; next: p125

> Differentiate the fixed point equation $\mathbf F[\bar{\mathbf s}(\theta)]=0$. The chain rule gives

<!-- pedagogy-paragraph: p125 sha256 9617e243fc62a1036c5064e0e7c9f88ef21a9abb250ae415ebf7802834e38d15 -->
p125, lines 125-125; prose; priority: unchanged; previous: p119; next: p127

> Thus $\mathbf u$ is a [**right zero eigenvector**]{.definition-term custom-style="Definition Term"}: a state direction that the linear dynamics neither restores nor amplifies. It is the tangent to the attractor. The other modes must decay for this local family to be attracting.

<!-- pedagogy-paragraph: p127 sha256 6d33166b50ec4d9c19dd72a849f8661e20bdda70192d682ed667385aa1f9aff0 -->
p127, lines 127-127; prose; priority: unchanged; previous: p125; next: p134

> We also need a [**left zero eigenvector**]{.definition-term custom-style="Definition Term"}, a vector $\mathbf v$ satisfying

<!-- pedagogy-paragraph: p134 sha256 c965fdaee89b0af4ec01f463b596c3e373caf60fb1cca82e5734731220db6503 -->
p134, lines 134-134; prose; priority: unchanged; previous: p127; next: p140

> Its purpose is to extract the lasting memory displacement from a general perturbation. The normalization makes $\mathbf v^T(\mathbf u\,\delta\theta)=\delta\theta$. If a stable mode $\mathbf z$ satisfies $K\mathbf z=\lambda\mathbf z$ with $\lambda\ne0$, then

<!-- pedagogy-paragraph: p140 sha256 032d09073de18240cb0e2555a92454e1776181d053cf55e28cc030a697624782 -->
p140, lines 140-140; prose; priority: unchanged; previous: p134; next: p147

> so $\mathbf v^T\mathbf z=0$. The left vector discards every decaying mode ([SI Eqs. S12–S13, p. 3](../papers/burak-fiete-2012-persistent-activity-si.pdf#page=3&zoom=125,0,409)). Consequently the surviving part of a small perturbation is

<!-- pedagogy-paragraph: p147 sha256 dfff97fd7a1cc19f6d1d2b3254415129fd526b4181701407ca2f9459a9403a30 -->
p147, lines 147-147; prose; priority: unchanged; previous: p140; next: p149

> This generally differs from a perpendicular geometric projection. Decay can be tilted relative to the tangent. Even symmetric synaptic weights do not usually make $K$ symmetric, because $\phi'(\bar g_i)$ multiplies different rows by different amounts.

<!-- pedagogy-paragraph: p149 sha256 b0c953b6a910b85c2b867e631416d32ff48ceea9fc18ce2c2cd7e6f0e9a0a292 -->
p149, lines 149-149; prose; priority: unchanged; previous: p147; next: p155

> **Example: a disturbance that slides while it decays.** To see the distinction without a neural simulation, consider the local system

<!-- pedagogy-paragraph: p155 sha256 b1514ac4ed7c28962acf3fba4e3240161c5afae143fc7f1e606483895133eb33 -->
p155, lines 155-155; prose; priority: unchanged; previous: p149; next: p161

> Every point with $y=0$ is fixed. Starting from $(x_0,y_0)$ gives $y(t)=y_0e^{-\lambda t}$ and

<!-- pedagogy-paragraph: p161 sha256 30704803871a50c23d14792d3d7da0805bcf6b8b557e68d9fb8cd4f71ba2f702 -->
p161, lines 161-161; prose; priority: unchanged; previous: p155; next: p163

> Here $\mathbf u=(1,0)^T$ and $\mathbf v=(1,a/\lambda)^T$. A vertical perturbation changes the final memory whenever $a\ne0$. A perpendicular projection would miss that change. This is a teaching example of the projection geometry, not an additional network used in the paper.

<!-- pedagogy-paragraph: p163 sha256 cbd60d5d374aed79fc143b711a962632fade5e2c9e293584ffc55ab168a42225 -->
p163, lines 163-163; prose; priority: unchanged; previous: p161; next: p165

> The exact trajectory in this example shows why the lasting displacement follows the flow rather than a perpendicular projection.

<!-- pedagogy-paragraph: p165 sha256 2c643bd85d3e8933fd7127e586cd0d302d74dcd69d691fc3921ef217cc019e39 -->
p165, lines 165-165; prose; priority: unchanged; previous: p163; next: p169

> <div class="figure-scroll">

<!-- pedagogy-paragraph: p169 sha256 aac32651b10f567c461b9b4f255d6fb1fa6859b5368d8bd9a51af920ab21cf23 -->
p169, lines 169-169; prose; priority: unchanged; previous: p165; next: p171

> </div>

<!-- pedagogy-paragraph: p171 sha256 03a8edd51e76caa56e6bd7989b3fa14bbea7073a778f351043f37bfbfed0ae00 -->
p171, lines 171-171; prose; priority: unchanged; previous: p169; next: p175

> As y decays, x changes by one; the left vector extracts that lasting shift.


Claim-bearing content: figure

Claims to check:

- Claim c1, line 94: "A [**linearization**]{.definition-term custom-style="Definition Term"} keeps the terms proportional to the small perturbation and drops terms quadratic or higher in it." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c2, line 103: "$$ d\delta\mathbf s=K\delta\mathbf s\,dt+R^{1/2}d\mathbf B, \qquad K_{ij}=-\frac{\delta_{ij}}{\tau}+\phi'(\bar g_i)W_{ij}, \qquad R=\operatorname{diag}(\bar r_i). $$" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c3, line 110: "The entries of $K$ have units of inverse time.[^p1-projection]" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c4, line 119: "Differentiate the fixed point equation $\mathbf F[\bar{\mathbf s}(\theta)]=0$." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c5, line 121: "$$ K\mathbf u=0. $$" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c6, line 125: "The other modes must decay for this local family to be attracting." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c7, line 129: "$$ \mathbf v^T K=0, \qquad \mathbf v^T\mathbf u=1. $$" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c8, line 136: "$$ 0=\mathbf v^T K\mathbf z=\lambda\mathbf v^T\mathbf z, $$" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c9, line 140: "so $\mathbf v^T\mathbf z=0$." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c10, line 140: "The left vector discards every decaying mode ([SI Eqs." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c11, line 140: "S12–S13, p. 3](../papers/burak-fiete-2012-persistent-activity-si.pdf#page=3&zoom=125,0,409))." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c12, line 140: "Consequently the surviving part of a small perturbation is" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c13, line 151: "$$ \dot x=ay,\qquad \dot y=-\lambda y,\quad\lambda>0. $$" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c14, line 155: "Every point with $y=0$ is fixed." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c15, line 157: "$$ x(\infty)=x_0+\frac{a}{\lambda}y_0. $$" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c16, line 167: "Caption: Original guide construction of the tilted decay example, with dimensionless coordinates and $a/\lambda=1/2$. After an imposed jump from $(0,0)$ to $(0,2)$, the state relaxes toward $(1,0)$; successive time marks crowd toward that endpoint. This illustrates the left and right zero vector..." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]

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

<!-- pedagogy-unit: content/chapters/02-memory-dynamics.md::sec:MEMORY-DIFFUSION -->

### Projecting spike fluctuations gives the diffusion coefficient

Location: line 173, anchor `sec:MEMORY-DIFFUSION`

First content kind: `prose`

Opening passage line: 175
Closing passage line: 211

Paragraphs in source order (complete `PARAGRAPH_REVIEW.json`):

<!-- pedagogy-paragraph: p175 sha256 a602eaff7e07e660c29d9926b36db914e7a1619c85400f1a62e847fca2b0f450 -->
p175, lines 175-175; prose; priority: unchanged; previous: p171; next: p182

> We can now calculate how much random displacement remains after the stable components have relaxed. Multiply the linear stochastic equation by $\mathbf v^T$. Since $\mathbf v^TK=0$,

<!-- pedagogy-paragraph: p182 sha256 5c74a0d27d21c01839a3300d9e65cac53c256ca43472bcd096cb523008ff32ae -->
p182, lines 182-182; prose; priority: unchanged; previous: p175; next: p190

> The independent Brownian increments have covariance $E[dB_i dB_j]=\delta_{ij}dt$, so

<!-- pedagogy-paragraph: p190 sha256 f6d0f96d9a6159839732cc45babceaab9ba468ab8593f19f30a795ab851af787 -->
p190, lines 190-190; prose; priority: unchanged; previous: p182; next: p196

> Matching this to $2D\,dt$ yields the general local result ([SI Eqs. S14–S15, p. 3](../papers/burak-fiete-2012-persistent-activity-si.pdf#page=3&zoom=125,0,576))

<!-- pedagogy-paragraph: p196 sha256 532cd1e5c915181388b884d2d6062044de68edfb21ad924f2ec9bc991f0864f2 -->
p196, lines 196-196; prose; priority: unchanged; previous: p190; next: p198

> Each neuron's contribution combines its spike variability, $\bar r_i$, with the squared effect of one activation fluctuation on the final memory, $v_i^2$. The formula does not say that neurons with high rates necessarily damage memory more: changing rates can also change the tuning curves and the projection weights. Those changes must be included in a comparison.[^p1-projection]

<!-- pedagogy-paragraph: p198 sha256 764a8f5ef559dc2fa44b4ef7f7e7c124437ad8b5313cf856a4d135fb1840c8df -->
p198, lines 198-198; prose; priority: unchanged; previous: p196; next: p200

> The result is local in state and leading order in weak noise. The time interval must satisfy two conditions:

<!-- pedagogy-paragraph: p200 sha256 77954ae8f645cf205c0e779e6ca9ff1b99bdc91cd2e81901ebcb3dfde9c777a2 -->
p200, lines 200-200; list_item; priority: unchanged; previous: p198; next: p201

> It must be long enough for the approximation based on many spike contributions to apply.

<!-- pedagogy-paragraph: p201 sha256 9fb7d0fbf782fba16b31d08130811f9a4b7ebc2ca21aa3a8ce164261529b920b -->
p201, lines 201-201; list_item; priority: unchanged; previous: p200; next: p203

> It must be short enough that the coefficients do not change substantially as the memory moves.

<!-- pedagogy-paragraph: p203 sha256 0b1bf57cb6140ce6936014e30fbb946e4836afed2c49014b376ee3d1bf9e959f -->
p203, lines 203-203; prose; priority: unchanged; previous: p201; next: p205

> These conditions justify a local spreading rate. Systematic drift requires a [separate check in the next chapter](ch-memory-long-delays.html#sec-memory-drift-scope).

<!-- pedagogy-paragraph: p205 sha256 a7caf8e53d34dfd94c6532d201b7126a46f9ed8d20a8483b3e2e3420977b6887 -->
p205, lines 205-205; prose; priority: unchanged; previous: p203; next: p211

> For several memory coordinates $\theta_\alpha$, choose tangent vectors $u_i^\alpha=\partial\bar s_i/\partial\theta_\alpha$ and left vectors with $\sum_i v_i^\alpha u_i^\beta=\delta_{\alpha\beta}$. The same covariance calculation gives

<!-- pedagogy-paragraph: p211 sha256 6758331797bc945136edf0fa1357405166737a65ef32ab595b1e2f0b484e8a8b -->
p211, lines 211-211; prose; priority: unchanged; previous: p205; next: p215

> The [**diffusion tensor**]{.definition-term custom-style="Definition Term"} is the matrix of displacement covariances per twice the elapsed time. Its diagonal entries describe spreading in individual coordinates; its other entries describe how coordinate displacements vary together. Even independently generated spike-count fluctuations can generate coupled motion of the represented coordinates.[^p1-multid]


Claim-bearing content: none

Claims to check:

- Claim c1, line 175: "We can now calculate how much random displacement remains after the stable components have relaxed." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c2, line 175: "Since $\mathbf v^TK=0$," -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c3, line 177: "$$ d\theta=\mathbf v^T R^{1/2}d\mathbf B =\sum_i v_i\sqrt{\bar r_i}\,dB_i. $$" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c4, line 190: "S14–S15, p. 3](../papers/burak-fiete-2012-persistent-activity-si.pdf#page=3&zoom=125,0,576))" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c5, line 196: "Those changes must be included in a comparison.[^p1-projection]" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c6, line 198: "The time interval must satisfy two conditions:" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c7, line 200: "It must be long enough for the approximation based on many spike contributions to apply." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c8, line 201: "It must be short enough that the coefficients do not change substantially as the memory moves." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c9, line 211: "Even independently generated spike-count fluctuations can generate coupled motion of the represented coordinates.[^p1-multid]" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]

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

<!-- pedagogy-unit: content/chapters/02-memory-dynamics.md::sec:MEMORY-SYMMETRIC -->

### Symmetric weights express diffusion through tuning curves

Location: line 213, anchor `sec:MEMORY-SYMMETRIC`

First content kind: `prose`

Opening passage line: 215
Closing passage line: 279

Paragraphs in source order (complete `PARAGRAPH_REVIEW.json`):

<!-- pedagogy-paragraph: p215 sha256 70b516275dfda33c11364667bb486fad1c19d383cbb4490b18879131ba57f1dc -->
p215, lines 215-215; prose; priority: unchanged; previous: p211; next: p217

> The general formula requires the left vector of the network dynamics. When $W_{ij}=W_{ji}$, can we write it using tuning curves and the input to rate rule?

<!-- pedagogy-paragraph: p217 sha256 5fa21457488bd4f0a7de030aba627f940ee57aaa5837e6332b0442eb8d24b5ee -->
p217, lines 217-217; prose; priority: unchanged; previous: p215; next: p224

> Let $g_i'=d\bar g_i/d\theta$ and $r_i'=d\bar r_i/d\theta$. Differentiating the fixed point identities gives

<!-- pedagogy-paragraph: p224 sha256 3841788895bc44b11ce452bf9b4364ea04bf263d1d50a4730c96be83d8bd5a18 -->
p224, lines 224-224; prose; priority: unchanged; previous: p217; next: p232

> With symmetric $W$, the transpose of the linearized matrix satisfies

<!-- pedagogy-paragraph: p232 sha256 9673a01c845cd7e003a82c5122e8e82f9d0dba368b95d91173ca45f4b2cee140 -->
p232, lines 232-232; prose; priority: unchanged; previous: p224; next: p238

> Therefore $\mathbf v$ is proportional to $\mathbf g'$. Its normalization is

<!-- pedagogy-paragraph: p238 sha256 b658ed49add2a1663519c0cbc9486df6e17b978e23730f7b645501991df41fd8 -->
p238, lines 238-238; prose; priority: unchanged; previous: p232; next: p248

> because $u_i=\tau r_i'$. Substituting into the noise projection gives

<!-- pedagogy-paragraph: p248 sha256 f10c032009f01fa07ed691a969e09efd0d7a0e2230363430cd3a878ca4705f86 -->
p248, lines 248-248; prose; priority: unchanged; previous: p238; next: p250

> This follows from [SI Eq. S18, p. 4](../papers/burak-fiete-2012-persistent-activity-si.pdf#page=4&zoom=125,0,239), with $\bar g_i=\phi^{-1}(\bar r_i)$ wherever the transfer function is invertible over the relevant range. The supplied Early Edition [main Eq. 2, p. 2](../papers/burak-fiete-2012-persistent-activity.pdf#page=2&zoom=125,0,88) appears to omit the square on $g_i'$ in the numerator; the projection calculation and SI S18 give the squared expression shown here. This is an independent source check, not an author-confirmed correction. The result requires:

<!-- pedagogy-paragraph: p250 sha256 8ebe26b1a3b5d8213f08181252d0d45fed87fbda10b1f7dd323112bb0fa98c4c -->
p250, lines 250-250; list_item; priority: unchanged; previous: p248; next: p251

> symmetric weights;

<!-- pedagogy-paragraph: p251 sha256 2b2ad979baa85c2535dc54f66f4b8b6362a547dbcfb846ce40923fd3e4c9c646 -->
p251, lines 251-251; list_item; priority: unchanged; previous: p250; next: p252

> a stable continuous family;

<!-- pedagogy-paragraph: p252 sha256 be68637cae580a2ed5197b7f05732f9941c97cef5e81164db6d2b9d4ee87bb05 -->
p252, lines 252-252; list_item; priority: unchanged; previous: p251; next: p254

> the noise assumptions already introduced.

<!-- pedagogy-paragraph: p254 sha256 e4015272f4dab7442d0651ee28c0594f13e2dbc08c902d5746c84d94a5a18b06 -->
p254, lines 254-254; prose; priority: unchanged; previous: p252; next: p256

> Translation symmetry is unnecessary.[^p1-symmetric]

<!-- pedagogy-paragraph: p256 sha256 9d86e68a09a296ccd5578f519b53ac707e646d8419eae91e318c9c0981f29452 -->
p256, lines 256-256; prose; priority: unchanged; previous: p254; next: p263

> **Example: opposite firing changes with constant diffusion.** Take two mutually inhibiting cells with $W_{12}=W_{21}=-1$, zero self weights, equal biases $b$, and $\phi(g)=g/\tau$ over the positive input range. Its fixed points obey

<!-- pedagogy-paragraph: p263 sha256 727e3daa89322194f5a1d2a0159334c3e5f7c2f860f6cd818c38f6a74e985885 -->
p263, lines 263-263; prose; priority: unchanged; previous: p256; next: p269

> The coordinate is $\theta=s_1-s_2$. The sum $s_1+s_2$ relaxes to $b$, while the difference is neutral. Here $\mathbf u=(1/2,-1/2)^T$, $\mathbf v=(1,-1)^T$, and

<!-- pedagogy-paragraph: p269 sha256 5e0fe6013cf0373bf78905c803b40a0a10662b61816cc6e7f11d15c0405dcfa5 -->
p269, lines 269-269; prose; priority: unchanged; previous: p263; next: p271

> Although the two firing rates change with the stored value, their summed spike variability is constant. Therefore this network has constant local diffusion throughout its valid range. Near an endpoint, a negative linear rate would be impossible; a physical implementation must alter the transfer rule, and the interior formula alone does not describe that boundary. This model underlies the mutual inhibition example in [Fig. 2E–G, p. 3](../papers/burak-fiete-2012-persistent-activity.pdf#page=3&zoom=125,0,205).[^p1-two]

<!-- pedagogy-paragraph: p271 sha256 0118ba3b04a5d2bc07b991fb121d3fb1eb616008aff18a0a0c58de3c6ebeac6c -->
p271, lines 271-271; prose; priority: unchanged; previous: p269; next: p273

> The plot uses $b=20$ activation units and $\tau=0.1\,\mathrm{s}$.

<!-- pedagogy-paragraph: p273 sha256 2c643bd85d3e8933fd7127e586cd0d302d74dcd69d691fc3921ef217cc019e39 -->
p273, lines 273-273; prose; priority: unchanged; previous: p271; next: p277

> <div class="figure-scroll">

<!-- pedagogy-paragraph: p277 sha256 aac32651b10f567c461b9b4f255d6fb1fa6859b5368d8bd9a51af920ab21cf23 -->
p277, lines 277-277; prose; priority: unchanged; previous: p273; next: p279

> </div>

<!-- pedagogy-paragraph: p279 sha256 9b987babdd52f18caef46b46255f445987a1748f8d5b48e81d5dacee72bd4883 -->
p279, lines 279-279; prose; priority: unchanged; previous: p277; next: none

> The dashed rate sum in the upper plot stays fixed, so the lower plot has the same $D$ at every interior value of $\theta$.


Claim-bearing content: figure

Claims to check:

- Claim c1, line 226: "$$ K^T\mathbf g' =-\mathbf g'/\tau+W\operatorname{diag}[\phi'(\bar g_i)]\mathbf g' =-\mathbf g'/\tau+W\mathbf r'=0. $$" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c2, line 248: "S18, p. 4](../papers/burak-fiete-2012-persistent-activity-si.pdf#page=4&zoom=125,0,239), with $\bar g_i=\phi^{-1}(\bar r_i)$ wherever the transfer function is invertible over the relevant range." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c3, line 248: "The supplied Early Edition [main Eq. 2, p. 2](../papers/burak-fiete-2012-persistent-activity.pdf#page=2&zoom=125,0,88) appears to omit the square on $g_i'$ in the numerator; the projection calculation and SI S18 give the squared expression shown here." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c4, line 254: "Translation symmetry is unnecessary.[^p1-symmetric]" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c5, line 256: "**Example: opposite firing changes with constant diffusion.** Take two mutually inhibiting cells with $W_{12}=W_{21}=-1$, zero self weights, equal biases $b$, and $\phi(g)=g/\tau$ over the positive input range." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c6, line 258: "$$ \bar s_1=\frac{b+\theta}{2},\qquad \bar s_2=\frac{b-\theta}{2},\qquad |\theta|<b. $$" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c7, line 263: "The coordinate is $\theta=s_1-s_2$." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c8, line 263: "The sum $s_1+s_2$ relaxes to $b$, while the difference is neutral." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c9, line 263: "Here $\mathbf u=(1/2,-1/2)^T$, $\mathbf v=(1,-1)^T$, and" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c10, line 265: "$$ 2D=\bar r_1+\bar r_2=b/\tau. $$" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c11, line 269: "Near an endpoint, a negative linear rate would be impossible; a physical implementation must alter the transfer rule, and the interior formula alone does not describe that boundary." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c12, line 269: "This model underlies the mutual inhibition example in [Fig. 2E–G, p. 3](../papers/burak-fiete-2012-persistent-activity.pdf#page=3&zoom=125,0,205).[^p1-two]" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c13, line 271: "The plot uses $b=20$ activation units and $\tau=0.1\,\mathrm{s}$." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c14, line 275: "Caption: For the chapter’s two mutually inhibiting cells, b = 20 activation units and tau = 0.1 s give opposite changes in the two rates. Their sum remains 200 spikes/s, so local D remains 100 coordinate units squared/s. Open endpoints mark the excluded boundaries; the linear interior model does..." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c15, line 279: "The dashed rate sum in the upper plot stays fixed, so the lower plot has the same $D$ at every interior value of $\theta$." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]

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

## ch:MEMORY-LONG-DELAYS - Boundaries and drift change memory error over long delays

Source file: `content/chapters/02b-memory-long-delays.md`

Purpose: A rate of random spreading measured near one stored value does not yet tell us how memory error behaves after a long wait. The value may approach a boundary, wrap around an angular range, or reach a region where the spreading rate differs. A consistent movement of the average value would also change the error without being captured by the rate of random spreading alone.

Prerequisites: ch:MEMORY-DYNAMICS

Sidecar sections: Long delay errors depend on boundaries and local diffusion, A diffusion calculation does not determine systematic drift, Figures distinguish memory motion from readout error and test diffusion

Blocks: 1 figure(s), 0 equation(s), 0 code block(s)

Result labels: No Answer/Conclusion/Feedback label detected

<!-- pedagogy-unit: content/chapters/02b-memory-long-delays.md::ch:MEMORY-LONG-DELAYS -->

### Chapter opening

Location: line 1, anchor `ch:MEMORY-LONG-DELAYS`

First content kind: `prose`

Opening passage line: 3
Closing passage line: 7

Paragraphs in source order (complete `PARAGRAPH_REVIEW.json`):

<!-- pedagogy-paragraph: p3 sha256 48c4117c0f693c0869429bf1f53b78bf93edb6bfb190d926bd801e5e82c8d626 -->
p3, lines 3-3; prose; priority: unchanged; previous: none; next: p5

> A rate of random spreading measured near one stored value does not yet tell us how memory error behaves after a long wait. The value may approach a boundary, wrap around an angular range, or reach a region where the spreading rate differs. A consistent movement of the average value would also change the error without being captured by the rate of random spreading alone.

<!-- pedagogy-paragraph: p5 sha256 24ae9d69eaf437eb15052f9f5211f48baf7c712c4038f6ade6c7b4877ad4c288 -->
p5, lines 5-5; prose; priority: unchanged; previous: p3; next: p7

> We begin by following the distribution of stored values across repeated trials, using the local diffusion coefficient derived in the preceding chapter. This shows why errors can keep growing on a line but level off when angular error is measured within one turn. We then separate random spreading from systematic drift and make the noise assumptions explicit. Finally, the paper's figures show what its network simulations test and distinguish movement of the memory from uncertainty when another circuit reads it. That second uncertainty motivates the information calculation that follows.

<!-- pedagogy-paragraph: p7 sha256 98f61808845505ea0ae7403dd4ee06e82bf061dfa9b33de987306e66b7843126 -->
p7, lines 7-7; prose; priority: unchanged; previous: p5; next: p11

> Here $\theta$ is the current stored value and $\Theta$ its common initial value across trials. The local diffusion coefficient $D(\theta)$ comes from the weak spike fluctuations derived in the [preceding chapter](ch-memory-dynamics.html#sec-memory-diffusion), after stable disturbances have relaxed. For constant $D$, displacement variance is $2Dt$ before boundaries matter and when there is no systematic drift.


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

<!-- pedagogy-unit: content/chapters/02b-memory-long-delays.md::sec:MEMORY-LONG-TIME -->

### Long delay errors depend on boundaries and local diffusion

Location: line 9, anchor `sec:MEMORY-LONG-TIME`

First content kind: `prose`

Opening passage line: 11
Closing passage line: 94

Paragraphs in source order (complete `PARAGRAPH_REVIEW.json`):

<!-- pedagogy-paragraph: p11 sha256 bc6bbaee194090fe702ec023f0a9f17ebf12530450912f2292a4969ffd8a0439 -->
p11, lines 11-11; prose; priority: unchanged; previous: p7; next: p13

> A local diffusion coefficient answers how variance initially grows. It does not by itself say that variance grows at the same rate forever. Boundaries and variation of $D$ can change the long time behavior.

<!-- pedagogy-paragraph: p13 sha256 9983eeaee961ed549d26eb3ec45335ebf4a1564a02304267668b43178ff715e7 -->
p13, lines 13-13; prose; priority: unchanged; previous: p11; next: p21

> Let $p(\theta,t)$ be the density of the memory coordinate across repeated trials initialized at $\Theta$. The [**Itô convention**]{.definition-term custom-style="Definition Term"} evaluates a state-dependent noise coefficient at the beginning of each increment. In the zero-drift diffusion approximation, this density evolves according to the [**Fokker Planck equation**]{.definition-term custom-style="Definition Term"}:

<!-- pedagogy-paragraph: p21 sha256 5088e2a3e70b3bf154a673f01baeb7eede4168f0c8bfe8a750273b32edb4d891 -->
p21, lines 21-21; prose; priority: unchanged; previous: p13; next: p28

> Here the [**Dirac delta**]{.definition-term custom-style="Definition Term"} denotes a point mass: initially all probability is at $\Theta$. It differs from the earlier zero-or-one symbol $\delta_{ij}$. For constant $D$ on an unbounded line, the Gaussian solution is

<!-- pedagogy-paragraph: p28 sha256 6aae533a0b9edff28fb603c071b0be2c61e7f32a223303d02222ab429740fbd0 -->
p28, lines 28-28; prose; priority: unchanged; previous: p21; next: p34

> Its variance is $2Dt$. For an angular coordinate, add the densities at all displacements $\theta-\Theta+2\pi k$, $k\in\mathbb Z$, to wrap the Gaussian around the circle. This teaches the content of [SI Eq. S31, p. 7](../papers/burak-fiete-2012-persistent-activity-si.pdf#page=7&zoom=125,0,483) without needing the special function notation used there. At long times the density approaches $1/(2\pi)$. If angular errors are reported in $[-\pi,\pi)$, their limiting mean squared value is

<!-- pedagogy-paragraph: p34 sha256 27e9fc73f2c149caafcda70829e2e3f1e509bdd596abe6eac61188488d506f0d -->
p34, lines 34-34; prose; priority: unchanged; previous: p28; next: p36

> The flattening of a ring network's error curve can therefore occur while its local noise mechanism remains unchanged. It reflects the bounded way angular error is reported.[^p1-fp]

<!-- pedagogy-paragraph: p36 sha256 f1ee245bbd0788846e584cf212e1c61cde231d0e38be1ace3f63043ca2e1a88d -->
p36, lines 36-36; prose; priority: unchanged; previous: p34; next: p38

> For $D=0.5\,\mathrm{rad}^2/\mathrm{s}$, the plots show how the density and squared error change with delay.

<!-- pedagogy-paragraph: p38 sha256 2c643bd85d3e8933fd7127e586cd0d302d74dcd69d691fc3921ef217cc019e39 -->
p38, lines 38-38; prose; priority: unchanged; previous: p36; next: p42

> <div class="figure-scroll">

<!-- pedagogy-paragraph: p42 sha256 aac32651b10f567c461b9b4f255d6fb1fa6859b5368d8bd9a51af920ab21cf23 -->
p42, lines 42-42; prose; priority: unchanged; previous: p38; next: p44

> </div>

<!-- pedagogy-paragraph: p44 sha256 e9416b94738f50b1f4130cb37e3107f2f8f1cfb59e262efbbf2d7515272c5a2d -->
p44, lines 44-44; prose; priority: unchanged; previous: p42; next: p48

> As the upper density approaches uniform, the wrapped error below approaches $\pi^2/3$; the line error keeps growing.

<!-- pedagogy-paragraph: p48 sha256 5b07edf8afc9be206828ba0d4eec67174912c4307c53c43a1769c6a2fbe975b7 -->
p48, lines 48-48; prose; priority: unchanged; previous: p44; next: p59

> To pass from random increments to a density equation, choose any smooth function $F(\theta)$. In a short interval $dt$, the zero-drift Itô increment has conditional mean zero and conditional second moment $2D(\theta)dt$. Taylor expansion at the starting coordinate gives

<!-- pedagogy-paragraph: p59 sha256 193f77f82798c9b294a4d81af5c66d6c83afbf3a57d24c46c4b785cafe0b3c6b -->
p59, lines 59-59; prose; priority: unchanged; previous: p48; next: p66

> The higher-order terms vanish faster than $dt$ in this diffusion approximation. Averaging over the starting-coordinate density and dividing by $dt$ gives

<!-- pedagogy-paragraph: p66 sha256 f14a654ceae79fb946e64a59c0fe3184a28da2fe13ef886cdd9ad0789e7ff1d0 -->
p66, lines 66-66; prose; priority: unchanged; previous: p59; next: p70

> Take $F$ to vanish outside an interior region, or use boundaries for which the integration terms vanish. Integrating by parts twice moves both derivatives from $F$ onto the product $Dp$. Because the resulting identity holds for every such smooth $F$, it gives the Fokker Planck equation shown above.

<!-- pedagogy-paragraph: p70 sha256 ea5c3563977ad59d1550994edb423cb89ccca680138134810d5ee346dde876be -->
p70, lines 70-70; prose; priority: unchanged; previous: p66; next: p78

> When $D$ varies with state, the zero drift stochastic equation is $d\theta=\sqrt{2D(\theta)}\,dB$ with the Itô convention. Under conditions that remove boundary terms, the density equation gives

<!-- pedagogy-paragraph: p78 sha256 e901b005f4e02d8dae4e1fce864e0d4acfd327804e21f886cfd83fbd404d17aa -->
p78, lines 78-78; prose; priority: unchanged; previous: p70; next: p85

> To obtain these identities, multiply the density equation by $\theta$ or $(\theta-\Theta)^2$, integrate over $\theta$, and integrate by parts twice. The second derivatives of these functions are respectively zero and two, giving the two identities. A similar calculation for the smooth function $D$ gives $dE[D]/dt=E[DD'']$. Expanding at $t=0$ therefore yields

<!-- pedagogy-paragraph: p85 sha256 502d82eb4a2d6c51255d6ea48a68a51b844ab63cf8c78424198a08ab34dba6d1 -->
p85, lines 85-85; prose; priority: unchanged; previous: p78; next: p87

> This is [SI Eq. S37, p. 8](../papers/burak-fiete-2012-persistent-activity-si.pdf#page=8&zoom=125,0,602). A state dependent $D$ need not produce a curved variance versus time graph. If $D$ is linear in $\theta$, then $E[D(\theta)]=D(E[\theta])=D(\Theta)$, so the variance remains linear while the process stays within the model's valid domain.[^p1-variable]

<!-- pedagogy-paragraph: p87 sha256 f0fe2402d5274dc367c73c0a19a26b2e608cecdd8828b69bf54e5638ff311b55 -->
p87, lines 87-87; prose; priority: unchanged; previous: p85; next: p94

> The supplement illustrates this with mutual excitation, $W_{12}=W_{21}=1$, biases $(b_0,-b_0)$, and the same linear transfer rule. The fixed activation states are $(\theta+b_0/2,\theta-b_0/2)$. Now $\mathbf u=(1,1)^T$, $\mathbf v=(1/2,1/2)^T$, and

<!-- pedagogy-paragraph: p94 sha256 2c33425f553f8d38b30e6b9f466e244f94b04f90b33e3b1df955dff324227257 -->
p94, lines 94-94; prose; priority: unchanged; previous: p87; next: p98

> The implied variance is $\Theta t/(2\tau)$, agreeing with [SI Eq. S41, p. 9](../papers/burak-fiete-2012-persistent-activity-si.pdf#page=9&zoom=125,0,383) and the slope tested in [Fig. S1, p. 10](../papers/burak-fiete-2012-persistent-activity-si.pdf#page=10&zoom=125,0,45). SI Eq. S40 instead prints $D=\theta/(2\tau)$. Under the convention used throughout this guide, that displayed value differs by a factor of two from the direct projection and S41. We keep the calculation explicit so the discrepancy does not become a hidden change of convention.[^p1-excitation]


Claim-bearing content: figure

Claims to check:

- Claim c1, line 28: "For an angular coordinate, add the densities at all displacements $\theta-\Theta+2\pi k$, $k\in\mathbb Z$, to wrap the Gaussian around the circle." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c2, line 28: "S31, p. 7](../papers/burak-fiete-2012-persistent-activity-si.pdf#page=7&zoom=125,0,483) without needing the special function notation used there." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c3, line 28: "At long times the density approaches $1/(2\pi)$." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c4, line 34: "The flattening of a ring network's error curve can therefore occur while its local noise mechanism remains unchanged." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c5, line 34: "It reflects the bounded way angular error is reported.[^p1-fp]" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c6, line 36: "For $D=0.5\,\mathrm{rad}^2/\mathrm{s}$, the plots show how the density and squared error change with delay." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c7, line 40: "Caption: With the same constant D = 0.5 rad²/s, wrapped Gaussian error densities widen toward 1/(2π). The unbounded line has mean squared error 2Dt; reporting angular error in $[-\pi,\pi)$ instead gives a mean squared error that approaches π²/3. The flattening comes from the bounded error convent..." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c8, line 44: "As the upper density approaches uniform, the wrapped error below approaches $\pi^2/3$; the line error keeps growing." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c9, line 66: "Because the resulting identity holds for every such smooth $F$, it gives the Fokker Planck equation shown above." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c10, line 72: "$$ \frac{d}{dt}E[\theta]=0, \qquad \frac{d}{dt}\operatorname{Var}(\theta)=2E[D(\theta)]. $$" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c11, line 78: "Expanding at $t=0$ therefore yields" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c12, line 80: "$$ \operatorname{Var}(\theta) =2D(\Theta)t+D(\Theta)D''(\Theta)t^2+O(t^3). $$" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c13, line 85: "S37, p. 8](../papers/burak-fiete-2012-persistent-activity-si.pdf#page=8&zoom=125,0,602)." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c14, line 85: "If $D$ is linear in $\theta$, then $E[D(\theta)]=D(E[\theta])=D(\Theta)$, so the variance remains linear while the process stays within the model's valid domain.[^p1-variable]" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c15, line 87: "The supplement illustrates this with mutual excitation, $W_{12}=W_{21}=1$, biases $(b_0,-b_0)$, and the same linear transfer rule." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c16, line 87: "The fixed activation states are $(\theta+b_0/2,\theta-b_0/2)$." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c17, line 87: "Now $\mathbf u=(1,1)^T$, $\mathbf v=(1/2,1/2)^T$, and" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c18, line 89: "$$ 2D=\frac{1}{4}(\bar r_1+\bar r_2)=\frac{\theta}{2\tau}, \qquad D=\frac{\theta}{4\tau}. $$" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c19, line 94: "S41, p. 9](../papers/burak-fiete-2012-persistent-activity-si.pdf#page=9&zoom=125,0,383) and the slope tested in [Fig." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c20, line 94: "S1, p. 10](../papers/burak-fiete-2012-persistent-activity-si.pdf#page=10&zoom=125,0,45)." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c21, line 94: "We keep the calculation explicit so the discrepancy does not become a hidden change of convention.[^p1-excitation]" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]

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

<!-- pedagogy-unit: content/chapters/02b-memory-long-delays.md::sec:MEMORY-DRIFT-SCOPE -->

### A diffusion calculation does not determine systematic drift

Location: line 96, anchor `sec:MEMORY-DRIFT-SCOPE`

First content kind: `prose`

Opening passage line: 98
Closing passage line: 106

Paragraphs in source order (complete `PARAGRAPH_REVIEW.json`):

<!-- pedagogy-paragraph: p98 sha256 fedcdd5651d3ba8bcead9c42ba18059558953309125613e9b8acfc09a0b38109 -->
p98, lines 98-98; prose; priority: unchanged; previous: p94; next: p100

> Repeated trials can spread apart even if their average stays at the original value. That random spreading differs from a reproducible movement in one direction. Both can occur, and the derivation of $D$ alone does not settle the second question.

<!-- pedagogy-paragraph: p100 sha256 d4f5a6210eec59b08f616c522908b3ce9aa6194bef15849c4159d5090e5fc73f -->
p100, lines 100-100; prose; priority: unchanged; previous: p98; next: p102

> The paper assumes that the network is tuned to eliminate [**systematic drift**]{.definition-term custom-style="Definition Term"}, meaning a nonzero mean velocity along the attractor. A deterministic mismatch in weights can create such a velocity. In addition, state dependent noise and curved network dynamics can create a small mean motion even if the noise free model has an exact continuous attractor. The supplement explains that deriving the exact mean motion requires the microscopic jump process, beyond the leading variance calculation ([SI “Systematic drift,” pp. 4–5](../papers/burak-fiete-2012-persistent-activity-si.pdf#page=4&zoom=125,0,362)).[^p1-systematic]

<!-- pedagogy-paragraph: p102 sha256 6afc51b98135f92653d7885dd9e82ae40712ab7816388379658ab0102b85d3d3 -->
p102, lines 102-102; prose; priority: unchanged; previous: p100; next: p104

> For state dependent $D$, where the coefficient is evaluated affects the process. The [**Stratonovich convention**]{.definition-term custom-style="Definition Term"} uses midpoint evaluation in its limiting increments. With the same written coefficient and zero written drift, it describes a different process from the Itô equation. Converting the Stratonovich equation into Itô form adds a drift $D'/2$. This follows from the conversion term $bb'/2$ with $b=\sqrt{2D}$ and $bb'=D'$. The supplement uses the difference to estimate a possible scale of noise induced drift, not to identify the exact drift of every neural network.

<!-- pedagogy-paragraph: p104 sha256 2501e5a6496e59e225d43c992aea5076f32345fae2a4f3a9020b945f2864ed5b -->
p104, lines 104-104; prose; priority: unchanged; previous: p102; next: p106

> With $D$ of order $1/N$, random displacement over $dt$ is of order $\sqrt{dt/N}$, while such a mean displacement is of order $dt/N$. The variance calculation captures the leading random term. Small changes to weights or biases might cancel the mean drift; they cannot remove the random increments by subtracting a known average. A known mean drift can in principle be accounted for by a decoder, but any actual implementation must know that drift and respect the domain and boundary conditions.

<!-- pedagogy-paragraph: p106 sha256 1137cfa0131f56bb6b6aa11cc27f8b5b8cbfee176d320b3f38212806524295be -->
p106, lines 106-106; prose; priority: unchanged; previous: p104; next: p110

> The independence assumption also has a precise scope. Newly generated spike-count fluctuations are conditionally independent given the present state. Shared recurrent fluctuations can still correlate the observed spike trains over time. An extra source of correlated fluctuations would change the projection formula to $2D=\mathbf v^TQ\mathbf v$, where $Q\,dt$ is their increment covariance. Calculating the corresponding Fisher information would require the matching joint likelihood. The paper discusses such correlated models as future extensions ([Discussion, p. 5, paragraph beginning “Our spiking model”](../papers/burak-fiete-2012-persistent-activity.pdf#page=5&zoom=125,0,142)); it does not prove that every correlated spiking model obeys its Poisson formulas.[^p1-correlation]


Claim-bearing content: none

Claims to check:

- Claim c1, line 100: "In addition, state dependent noise and curved network dynamics can create a small mean motion even if the noise free model has an exact continuous attractor." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c2, line 100: "The supplement explains that deriving the exact mean motion requires the microscopic jump process, beyond the leading variance calculation ([SI “Systematic drift,” pp. 4–5](../papers/burak-fiete-2012-persistent-activity-si.pdf#page=4&zoom=125,0,362)).[^p1-systematic]" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c3, line 102: "Converting the Stratonovich equation into Itô form adds a drift $D'/2$." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c4, line 102: "This follows from the conversion term $bb'/2$ with $b=\sqrt{2D}$ and $bb'=D'$." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c5, line 102: "The supplement uses the difference to estimate a possible scale of noise induced drift, not to identify the exact drift of every neural network." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c6, line 104: "With $D$ of order $1/N$, random displacement over $dt$ is of order $\sqrt{dt/N}$, while such a mean displacement is of order $dt/N$." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c7, line 104: "Small changes to weights or biases might cancel the mean drift; they cannot remove the random increments by subtracting a known average." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c8, line 104: "A known mean drift can in principle be accounted for by a decoder, but any actual implementation must know that drift and respect the domain and boundary conditions." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c9, line 106: "The paper discusses such correlated models as future extensions ([Discussion, p. 5, paragraph beginning “Our spiking model”](../papers/burak-fiete-2012-persistent-activity.pdf#page=5&zoom=125,0,142)); it does not prove that every correlated spiking model obeys its Poisson formulas.[^p1-correlation]" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]

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

<!-- pedagogy-unit: content/chapters/02b-memory-long-delays.md::sec:MEMORY-FIGURES -->

### Figures distinguish memory motion from readout error and test diffusion

Location: line 108, anchor `sec:MEMORY-FIGURES`

First content kind: `prose`

Opening passage line: 110
Closing passage line: 128

Paragraphs in source order (complete `PARAGRAPH_REVIEW.json`):

<!-- pedagogy-paragraph: p110 sha256 36926dcd5b7b10755e492087c48b714b89d45198479be0954e51ea51d11f8369 -->
p110, lines 110-110; prose; priority: unchanged; previous: p106; next: p112

> [Figure 1A, p. 2](../papers/burak-fiete-2012-persistent-activity.pdf#page=2&zoom=125,0,439) shows the definition of the memory coordinate. Start at a green point off the attractor and follow the noise free flow to the black point on it. This endpoint defines the instantaneous attractor state. After one noisy interval, repeat that flow. The difference between the two endpoints is the retained memory change. The relevant projection follows the flow, as in the [tilted two variable example](ch-memory-dynamics.html#sec-memory-linearization).

<!-- pedagogy-paragraph: p112 sha256 678bd5de54c7c67854ffe9f974db4e88638a971fcfd0c6720ce9580a84f8602f -->
p112, lines 112-112; prose; priority: unchanged; previous: p110; next: p114

> In Fig. 1B, an [**activity bump**]{.definition-term custom-style="Definition Term"} is a localized peak of population firing rates across the neurons' preferred angles. The figure separates two sources of error:

<!-- pedagogy-paragraph: p114 sha256 58ac67f0029cc968bea6eec6f7c6edb078232a5cb99beadb24a366ea6ce9347b -->
p114, lines 114-114; list_item; priority: unchanged; previous: p112; next: p115

> During storage, the bump's location has moved away from its initial value $\Theta$.

<!-- pedagogy-paragraph: p115 sha256 f805c290d89f946694a301282d1157f350eaf432d85ef18d4e2fb74ca5511874 -->
p115, lines 115-115; list_item; priority: unchanged; previous: p114; next: p117

> At the later time, an observer has additional uncertainty about the bump's current location because it sees only a finite sample of spikes.

<!-- pedagogy-paragraph: p117 sha256 c8581a6e00e7058c42c6194975a4174a38bdd089794b6f3377bfbedd11f3a41f -->
p117, lines 117-117; prose; priority: unchanged; previous: p115; next: p119

> The [information calculation](ch-memory-information.html#sec-memory-fi) measures this second uncertainty and relates it to diffusion; the [readout chapter](ch-memory-readout.html) then follows observation of the moving state.[^p1-fig1]

<!-- pedagogy-paragraph: p119 sha256 bd9665d48a36f2206a98a65d6c1e26a09197ab81435556997e9cd7b3c20ead47 -->
p119, lines 119-119; prose; priority: unchanged; previous: p117; next: p121

> [Figure 2, p. 3](../papers/burak-fiete-2012-persistent-activity.pdf#page=3&zoom=125,0,18) tests the diffusion calculation in two different network designs. Panel A shows a ring with weights determined by differences of preferred angles. In B, compare the firing rate curves and spike marks in the inset before reading the wandering angular trace. The curve describes rates; the marks are particular random spike events. The trace shows the represented angle rather than overall activity amplitude.

<!-- pedagogy-paragraph: p121 sha256 def759a89ac5e74d92ffff4fb064582b4be89cc7112b1bb0e5a4adcfe35723b0 -->
p121, lines 121-121; prose; priority: unchanged; previous: p119; next: p123

> Panels C and D test different parts of the prediction:

<!-- pedagogy-paragraph: p123 sha256 30356737de7b78a83165d336c4150ba10a37ad50655c9f784ad5d22db81aa12c -->
p123, lines 123-123; list_item; priority: unchanged; previous: p121; next: p124

> Panel C compares simulated mean squared angular displacements with the prediction from the tuning curves and transfer function. The gray exponential case and black sigmoidal, or S-shaped, case have different transfer functions. The dashed bound is a lower limit for the sigmoidal case, not a separate fitted trajectory. A model can lie above its information bound while still agreeing with the derived diffusion formula.

<!-- pedagogy-paragraph: p124 sha256 aab31dbab8967af7ebcf47bf6da0731c5884c3af5ea11cb64a5a52788d61f58b -->
p124, lines 124-124; list_item; priority: unchanged; previous: p123; next: p126

> Panel D follows angular error to longer intervals; its flattening uses angular wrapping, not a disappearance of noise. The expected limiting value with the caption's error convention is $\pi^2/3$.

<!-- pedagogy-paragraph: p126 sha256 47f9b036d057e294447370bf127f1daf8762de2ac3f5d8483008dc4c2b6c6ac6 -->
p126, lines 126-126; prose; priority: unchanged; previous: p124; next: p128

> Panels E to G use mutual inhibition rather than a ring. The two rates in F vary in opposite directions; their difference represents memory. Panel G compares their displacement statistics with the analytic prediction. This second design matters because the projection argument does not require rotational symmetry. These are simulations checking the model calculation. They are not direct measurements of memory noise in an animal.[^p1-fig2]

<!-- pedagogy-paragraph: p128 sha256 1f5cf531981995c9079f01236be4d4bca14e74209587f97fbeff10d0f05f3bc2 -->
p128, lines 128-128; prose; priority: unchanged; previous: p126; next: none

> The derivation has now supplied a dynamical quantity, $D$, from spike variability and the way a network returns to its attractor. We next derive a statistical quantity from the same tuning curves and ask why it puts a lower limit on $D$.


Claim-bearing content: none

Claims to check:

- Claim c1, line 110: "[Figure 1A, p. 2](../papers/burak-fiete-2012-persistent-activity.pdf#page=2&zoom=125,0,439) shows the definition of the memory coordinate." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c2, line 115: "At the later time, an observer has additional uncertainty about the bump's current location because it sees only a finite sample of spikes." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c3, line 117: "The [information calculation](ch-memory-information.html#sec-memory-fi) measures this second uncertainty and relates it to diffusion; the [readout chapter](ch-memory-readout.html) then follows observation of the moving state.[^p1-fig1]" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c4, line 119: "[Figure 2, p. 3](../papers/burak-fiete-2012-persistent-activity.pdf#page=3&zoom=125,0,18) tests the diffusion calculation in two different network designs." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c5, line 124: "The expected limiting value with the caption's error convention is $\pi^2/3$." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c6, line 126: "They are not direct measurements of memory noise in an animal.[^p1-fig2]" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]

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

## ch:MEMORY-INFORMATION - Spike information limits memory stability

Source file: `content/chapters/03-memory-information.md`

Purpose: A downstream neuron reads a memory through spikes. Collecting more spikes helps distinguish nearby activity patterns, but during collection the pattern itself keeps moving. The same variability that limits readout also perturbs the recurrent network. Burak and Fiete connect these two effects by deriving a lower bound on memory diffusion from the information in the spikes.[^p1-info-main]

Prerequisites: ch:MEMORY-DYNAMICS, ch:MEMORY-LONG-DELAYS

Sidecar sections: Rate slopes and spike variability determine local information, Spike information sets a lower bound on memory diffusion, Improving persistence depends on what a comparison holds fixed

Blocks: 2 figure(s), 0 equation(s), 0 code block(s)

Result labels: No Answer/Conclusion/Feedback label detected

<!-- pedagogy-unit: content/chapters/03-memory-information.md::ch:MEMORY-INFORMATION -->

### Chapter opening

Location: line 1, anchor `ch:MEMORY-INFORMATION`

First content kind: `prose`

Opening passage line: 3
Closing passage line: 7

Paragraphs in source order (complete `PARAGRAPH_REVIEW.json`):

<!-- pedagogy-paragraph: p3 sha256 6191fff00251c5633be222c3dec2a80444b5ee099479dc216fe6eb561e707ccd -->
p3, lines 3-3; prose; priority: unchanged; previous: none; next: p5

> A downstream neuron reads a memory through spikes. Collecting more spikes helps distinguish nearby activity patterns, but during collection the pattern itself keeps moving. The same variability that limits readout also perturbs the recurrent network. Burak and Fiete connect these two effects by deriving a lower bound on memory diffusion from the information in the spikes.[^p1-info-main]

<!-- pedagogy-paragraph: p5 sha256 970808faef104891679e1ddab0659932d6a4bde3192a5f85dc42b68228951e5e -->
p5, lines 5-5; prose; priority: unchanged; previous: p3; next: p7

> The useful quantity is how clearly a short spike sample distinguishes nearby memory values. Comparing that quantity with the random motion already derived gives a minimum rate of memory spreading. This is a limit for a particular network, so using it to compare different networks also requires keeping track of what changes and what stays fixed. More information can permit better stability without ensuring that a particular circuit achieves it.

<!-- pedagogy-paragraph: p7 sha256 eb385308e8e79422f09da8e48b70750ff8173daf1a9ad2a3a5185ae2dd5c9675 -->
p7, lines 7-7; prose; priority: unchanged; previous: p5; next: p11

> We retain the memory coordinate $\theta$, initial value $\Theta$, firing rate $\bar r_i(\theta)$, synaptic time constant $\tau$, and diffusion convention $\operatorname{Var}(\Delta\theta)=2D\Delta t$. The [network projection](ch-memory-dynamics.html#sec-memory-linearization) determines which activity changes remain as changes in the stored value.


Claim-bearing content: none

Claims to check:

- Claim c1, line 3: "Burak and Fiete connect these two effects by deriving a lower bound on memory diffusion from the information in the spikes.[^p1-info-main]" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c2, line 5: "More information can permit better stability without ensuring that a particular circuit achieves it." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c3, line 7: "We retain the memory coordinate $\theta$, initial value $\Theta$, firing rate $\bar r_i(\theta)$, synaptic time constant $\tau$, and diffusion convention $\operatorname{Var}(\Delta\theta)=2D\Delta t$." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c4, line 7: "The [network projection](ch-memory-dynamics.html#sec-memory-linearization) determines which activity changes remain as changes in the stored value." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]

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

<!-- pedagogy-unit: content/chapters/03-memory-information.md::sec:MEMORY-FI -->

### Rate slopes and spike variability determine local information

Location: line 9, anchor `sec:MEMORY-FI`

First content kind: `prose`

Opening passage line: 11
Closing passage line: 76

Paragraphs in source order (complete `PARAGRAPH_REVIEW.json`):

<!-- pedagogy-paragraph: p11 sha256 bc7da85dce9ca17901f7fc1b654e339d6d23d46afbce30d14075af6f6730277f -->
p11, lines 11-11; prose; priority: unchanged; previous: p7; next: p13

> Suppose two nearby memory values produce almost identical rates. A short spike sample cannot reliably tell them apart. If a small change in memory instead produces a large rate change relative to spike variability, that sample is more useful. We need a quantity that measures this local distinction.

<!-- pedagogy-paragraph: p13 sha256 861f19594ab949fcbddf9831408517bd032156171df8b7709e46323f639ac150 -->
p13, lines 13-13; prose; priority: unchanged; previous: p11; next: p20

> A [**likelihood**]{.definition-term custom-style="Definition Term"} is the probability of observed data as a function of a proposed parameter value. In a short interval $h$, let $n_i$ be neuron $i$'s count. Treat the state as locally constant and use the conditional independent Poisson approximation. Then

<!-- pedagogy-paragraph: p20 sha256 8675fc7625752639bc4e701e8586b1c0c3c753143fcc06891f0dce5c927e29c3 -->
p20, lines 20-20; prose; priority: unchanged; previous: p13; next: p32

> Taking the logarithm turns the product into a sum. With $r_i'=d\bar r_i/d\theta$,

<!-- pedagogy-paragraph: p32 sha256 6ac56f470344248152a00e58c29791bacf38ceb3d89fb7dc08de4b4a9b11da95 -->
p32, lines 32-32; prose; priority: unchanged; previous: p20; next: p40

> The [**score**]{.definition-term custom-style="Definition Term"} $S$ measures how the log likelihood changes when the proposed memory value changes. Its mean is zero because $E[n_i]=\bar r_i h$. Its mean square is

<!-- pedagogy-paragraph: p40 sha256 20b3629f30116e3467c933569c360ca3f742f626b59d7d2bb75a2bb8fb296eda -->
p40, lines 40-40; prose; priority: unchanged; previous: p32; next: p46

> The cross terms vanish by conditional independence, and Poisson variance supplies $\operatorname{Var}(n_i)=\bar r_i h$. [**Fisher information**]{.definition-term custom-style="Definition Term"} is this expected squared score. The paper divides it by observation duration and calls the result the [**internal Fisher information rate**]{.definition-term custom-style="Definition Term"}:

<!-- pedagogy-paragraph: p46 sha256 2d288e79fc801acb0fec31c66675a226b359deecf9b91e2b62b5c83773dd2271 -->
p46, lines 46-46; prose; priority: unchanged; previous: p40; next: p48

> If the coordinate is an angle in radians, $J$ has units $\mathrm{rad}^{-2}\mathrm{s}^{-1}$. The information in a locally stationary interval of duration $h$ is $Jh$, not $J$. We write formulas for positive rates; a vanishing rate requires a suitable limit and regularity of the likelihood.[^p1-fi-source]

<!-- pedagogy-paragraph: p48 sha256 c2dd721fa485480c1c8d6cf6019f775807c42b22327ae42d0808ff5a69371ef1 -->
p48, lines 48-48; prose; priority: unchanged; previous: p46; next: p50

> Each cell contributes squared slope divided by its count variance per unit time. High rates with zero slope do not distinguish neighboring values, so they contribute no local information. A sharply changing rate can be informative even if it is smaller than another cell's peak rate. The coordinate here describes the network's present internal state. It need not be a currently visible external stimulus. Sensory Fisher information has the same Poisson formula only when the stimulus dependent tuning curves are the relevant rates.

<!-- pedagogy-paragraph: p50 sha256 f29106c553aa7acdd0925dfb40c80806c4ab456f94f990ad895b1823551e3b53 -->
p50, lines 50-50; prose; priority: unchanged; previous: p48; next: p52

> Two positive tuning curves with the same changing part isolate the effect of extra baseline firing.

<!-- pedagogy-paragraph: p52 sha256 2c643bd85d3e8933fd7127e586cd0d302d74dcd69d691fc3921ef217cc019e39 -->
p52, lines 52-52; prose; priority: unchanged; previous: p50; next: p56

> <div class="figure-scroll">

<!-- pedagogy-paragraph: p56 sha256 aac32651b10f567c461b9b4f255d6fb1fa6859b5368d8bd9a51af920ab21cf23 -->
p56, lines 56-56; prose; priority: unchanged; previous: p52; next: p58

> </div>

<!-- pedagogy-paragraph: p58 sha256 12b8515ac2dd1bfafa84bbd6fd8f06aeee05e2d705481e258766d410578b6be0 -->
p58, lines 58-58; prose; priority: unchanged; previous: p56; next: p60

> The rate peak has zero local slope, so it contributes no local information at that point. Extra spikes from a constant baseline increase Poisson variability without making nearby values easier to distinguish. See [Internal Fisher information, Eq. 3, p. 2](../papers/burak-fiete-2012-persistent-activity.pdf#page=2).

<!-- pedagogy-paragraph: p60 sha256 d760f92cf5a0fd307c44845c7925f225a3d91b32e1fda54ea47f72e046a43db9 -->
p60, lines 60-60; prose; priority: unchanged; previous: p58; next: p68

> To understand why inverse information is an error scale, let $\hat\theta(\mathbf n)$ be an estimator whose mean equals $\theta$ locally. Such an estimator is [**unbiased**]{.definition-term custom-style="Definition Term"}. Differentiate $E_\theta[\hat\theta]=\theta$ with respect to $\theta$. Under the usual conditions allowing differentiation through the sum over data,

<!-- pedagogy-paragraph: p68 sha256 182b9d66412774e0d5a6ed8f029abc79d7aed0042a49fe1ff6dd1f7d2c2ed080 -->
p68, lines 68-68; prose; priority: unchanged; previous: p60; next: p76

> The last equality uses $E[S]=0$. Cauchy Schwarz now gives

<!-- pedagogy-paragraph: p76 sha256 6605fb3a50ff2fabbc5f2c6ad29d2bd31019f4df65449d6c27a5760a8c04e31b -->
p76, lines 76-76; prose; priority: unchanged; previous: p68; next: p80

> This is the [**Cramér Rao bound**]{.definition-term custom-style="Definition Term"}. It is a local bound for regular unbiased estimation. It does not guarantee that every finite spike sample admits an estimator attaining it. The paper works in a weak noise, informative sample regime where local likelihoods can be approximated as Gaussian and efficient estimation can approach the bound. A [**prior distribution**]{.definition-term custom-style="Definition Term"} represents knowledge about likely parameter values before observing the spikes. A strong prior, bias, boundaries, or globally ambiguous tuning changes the estimation problem.[^p1-cr]


Claim-bearing content: figure

Claims to check:

- Claim c1, line 11: "A short spike sample cannot reliably tell them apart." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c2, line 11: "If a small change in memory instead produces a large rate change relative to spike variability, that sample is more useful." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c3, line 46: "If the coordinate is an angle in radians, $J$ has units $\mathrm{rad}^{-2}\mathrm{s}^{-1}$." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c4, line 46: "We write formulas for positive rates; a vanishing rate requires a suitable limit and regularity of the likelihood.[^p1-fi-source]" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c5, line 48: "Sensory Fisher information has the same Poisson formula only when the stimulus dependent tuning curves are the relevant rates." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c6, line 50: "Two positive tuning curves with the same changing part isolate the effect of extra baseline firing." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c7, line 54: "Caption: Analytic teaching curves $r_A(\theta)=5+35e^{-\theta^2/(2w^2)}$ and $r_B(\theta)=r_A(\theta)+20$, in spikes per second, with chosen width $w=0.6$ rad. The rates have the same derivative. Their individual Poisson information contributions $(r_i^{\prime})^2/r_i$ vanish at the rate peak, wh..." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c8, line 58: "See [Internal Fisher information, Eq. 3, p. 2](../papers/burak-fiete-2012-persistent-activity.pdf#page=2)." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c9, line 62: "$$ 1=\sum_{\mathbf n}\hat\theta(\mathbf n)\partial_\theta p(\mathbf n\mid\theta) =E[\hat\theta S] =E[(\hat\theta-\theta)S]. $$" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c10, line 68: "The last equality uses $E[S]=0$." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c11, line 76: "It does not guarantee that every finite spike sample admits an estimator attaining it." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c12, line 76: "A strong prior, bias, boundaries, or globally ambiguous tuning changes the estimation problem.[^p1-cr]" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]

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

<!-- pedagogy-unit: content/chapters/03-memory-information.md::sec:MEMORY-BOUND -->

### Spike information sets a lower bound on memory diffusion

Location: line 78, anchor `sec:MEMORY-BOUND`

First content kind: `prose`

Opening passage line: 80
Closing passage line: 189

Paragraphs in source order (complete `PARAGRAPH_REVIEW.json`):

<!-- pedagogy-paragraph: p80 sha256 b5fd76335916403a33f212d352a14bcda5c0b5774eac4097c43573d4ccd4ccb5 -->
p80, lines 80-80; prose; priority: unchanged; previous: p76; next: p82

> The network has no access to its exact firing rates as noiseless numbers. Its recurrent input is built from the same random spikes that an external observer sees. The lower bound on diffusion follows directly by comparing the state sensitivity of the network with the spike information.

<!-- pedagogy-paragraph: p82 sha256 5182049e16b5b8aede69708e071e253a588cace0dd21effa224e4d2242d4e623 -->
p82, lines 82-82; prose; priority: unchanged; previous: p80; next: p92

> From the [projection and diffusion calculation](ch-memory-dynamics.html#sec-memory-diffusion),

<!-- pedagogy-paragraph: p92 sha256 dbab6cd1e6f5b341d1032b319082425b63326bce59172c62dbc1ca1c51c5d08d -->
p92, lines 92-92; prose; priority: unchanged; previous: p82; next: p98

> Define two vectors $a_i=v_i\sqrt{\bar r_i}$ and $b_i=r_i'/\sqrt{\bar r_i}$. Their dot product is

<!-- pedagogy-paragraph: p98 sha256 f6bc85f837a7728267cdffc4d585986e9e19e26600bf48140711da33b500bc06 -->
p98, lines 98-98; prose; priority: unchanged; previous: p92; next: p105

> Their squared lengths are $\sum_i a_i^2=2D$ and $\sum_i b_i^2=J$. Cauchy Schwarz therefore gives

<!-- pedagogy-paragraph: p105 sha256 7175517a370b5cd2e664e3fd29c4ea9db5ce17058eb9772fe090a5485e49dad6 -->
p105, lines 105-105; prose; priority: unchanged; previous: p98; next: p111

> or

<!-- pedagogy-paragraph: p111 sha256 fe6dcbe3ead3a6f709bf7a9b6c375cd15b3cd50941122646a229dc7159d3d11b -->
p111, lines 111-111; prose; priority: unchanged; previous: p105; next: p113

> This proof uses the general left vector formula, so symmetric weights are unnecessary. It is a shorter teaching reconstruction of the scalar proof in SI Section V. Its assumptions are those used to derive $D$ and $J$; it is not a general statement about all possible noisy memory systems.[^p1-bound-source]

<!-- pedagogy-paragraph: p113 sha256 ee400a007343d450f4390920e6f2c1c21728513d48239f7f25dfab3ac0faf0e0 -->
p113, lines 113-113; prose; priority: unchanged; previous: p111; next: p115

> The units agree: $\tau^2J$ has units of time per coordinate squared, so its reciprocal has the units of diffusion. Small internal information forces a large minimum diffusion coefficient. Large information allows small diffusion, but does not guarantee it.

<!-- pedagogy-paragraph: p115 sha256 0c9831243006b6797ffda8d6d883e7bb6a6dc2924136d27e35f9468bffb37be1 -->
p115, lines 115-115; prose; priority: unchanged; previous: p113; next: p123

> Equality requires the two vectors in the proof to be proportional:

<!-- pedagogy-paragraph: p123 sha256 dfc33d22ddb0ba8f65c80296ba82c108112af50a8ffb2780dc8003d442af481e -->
p123, lines 123-123; prose; priority: unchanged; previous: p115; next: p129

> Cells with zero tuning slope cannot contribute extra projected noise if equality is to hold. In a symmetric network, $v_i$ is proportional to $g_i'$, and $r_i'=\phi'(\bar g_i)g_i'$. At each state, the participating cells therefore need a common value of $\phi'(\bar g_i)/\phi(\bar g_i)$. A sufficient way to satisfy this at all states is to choose that ratio equal to the same constant $k$ throughout the relevant input range. Solving

<!-- pedagogy-paragraph: p129 sha256 ddf3f88412da4ae766c8ea27acf73ee02afc7d167520c7f3fb74b40fb8bbabb2 -->
p129, lines 129-129; prose; priority: unchanged; previous: p123; next: p133

> gives $\phi(g)=A e^{kg}$. This exponential family attains equality for symmetric weights with Poisson noise, under the other model assumptions. It is a sufficient condition, rather than a general necessity: the common ratio may depend on the current memory state.[^p1-equality]

<!-- pedagogy-paragraph: p133 sha256 82a9d107a520b63ba62ee40b3131a0e82c65d4bc530472d51218e2f1df14d7a1 -->
p133, lines 133-133; prose; priority: unchanged; previous: p129; next: p141

> The [mutual-excitation example](ch-memory-long-delays.html#sec-memory-long-time) supplies a counterexample to the unrestricted converse. Set its bias $b_0=0$ and use the linear rule $\phi(g)=g/\tau$ on positive inputs. Its fixed states are $s_1=s_2=\theta>0$, with $\mathbf u=(1,1)^T$ and $\mathbf v=(1/2,1/2)^T$. Both rates are $\theta/\tau$, and both rate derivatives are $1/\tau$. Therefore

<!-- pedagogy-paragraph: p141 sha256 c5b6833a882b9e80c85d92d71986387bcf2ba53e0f44f6cf7c759bfee0dd1950 -->
p141, lines 141-141; prose; priority: unchanged; previous: p133; next: p145

> Equality holds throughout this family even though its transfer rule is linear. At each state both cells receive the same input, and the ratio $\phi'/\phi=1/\theta$ changes between states. A converse that forces an exponential rule needs additional restrictions linking the participating input values across cells and states. Continuous variation of the represented value alone does not supply them. This qualification concerns the source's claimed converse, while leaving the information–diffusion inequality intact.

<!-- pedagogy-paragraph: p145 sha256 38c60f164717c6a757b28f37c46546b04cbdb14f187638ea07343665b54af5ae -->
p145, lines 145-145; prose; priority: unchanged; previous: p141; next: p152

> **Example: the same diffusion with a looser information bound.** In the two cell mutual inhibition model, use $b=200$ activation units and $\tau=0.1\,\mathrm{s}$. The memory coordinate is an activation difference, not an angle. At $\theta=0$ both rates are $1000\,\mathrm{s}^{-1}$ and their slopes are $\pm5\,\mathrm{s}^{-1}$ per activation unit. Thus

<!-- pedagogy-paragraph: p152 sha256 940604609743e6367eadb6b3c496c3eaa2e792df6f81dc2a06c57ddf863f78dc -->
p152, lines 152-152; prose; priority: unchanged; previous: p145; next: p159

> Here $J$ has units of inverse activation unit squared per second, and $D$ has activation unit squared per second. The bound is $1/(2\tau^2J)=1000$, so equality holds at this balanced state. At $\theta=100$, the rates become $1500$ and $500\,\mathrm{s}^{-1}$, while their slopes stay $\pm5$. Now

<!-- pedagogy-paragraph: p159 sha256 78ebd202d0a70719c29bf03421c45bbf2659f344fe50b14b8bc5eb8d76a4d740 -->
p159, lines 159-159; prose; priority: unchanged; previous: p152; next: p161

> The actual diffusion remains $1000$. The inequality is strict because these two unequal rates no longer align the network's projection weights with the information optimal weights. This also shows why equality at a special state does not force the transfer function to be exponential on its whole domain. A constant lower bound attained everywhere and an accidental equality at one state are different claims.

<!-- pedagogy-paragraph: p161 sha256 f942006068f2c20d65d1b18c218043a94cc30ab31a67af82bc808be80c0befce -->
p161, lines 161-161; prose; priority: unchanged; previous: p159; next: p163

> The chapter’s two cell example makes the difference between a lower bound and the actual diffusion visible.

<!-- pedagogy-paragraph: p163 sha256 2c643bd85d3e8933fd7127e586cd0d302d74dcd69d691fc3921ef217cc019e39 -->
p163, lines 163-163; prose; priority: unchanged; previous: p161; next: p167

> <div class="figure-scroll">

<!-- pedagogy-paragraph: p167 sha256 aac32651b10f567c461b9b4f255d6fb1fa6859b5368d8bd9a51af920ab21cf23 -->
p167, lines 167-167; prose; priority: unchanged; previous: p163; next: p169

> </div>

<!-- pedagogy-paragraph: p169 sha256 998c132a3d415d042cc86eea6027aba1f5cc9b69dfdafe2c6e97443e96a26239 -->
p169, lines 169-169; prose; priority: unchanged; previous: p167; next: p171

> The gap at $\theta=100$ shows why a lower minimum allowed by the inequality is not a reduction in the network’s actual diffusion. See [Diffusion bound, Eq. 4, p. 3](../papers/burak-fiete-2012-persistent-activity.pdf#page=3).

<!-- pedagogy-paragraph: p171 sha256 502a0595ffa468f48a16ec725c7c293b1fe2fdb93b09b9962bdfb40c0b2dd424 -->
p171, lines 171-171; prose; priority: unchanged; previous: p169; next: p179

> For $m$ memory coordinates the information is a matrix,

<!-- pedagogy-paragraph: p179 sha256 e79e40e18566fe4fdc5fdec1c82a34fd80a0a420b7f8482f2ebd59dc8ce577c3 -->
p179, lines 179-179; prose; priority: unchanged; previous: p171; next: p185

> The matrix bound $2D\succeq\tau^{-2}J^{-1}$ means that every linear combination of coordinate displacements obeys the corresponding variance lower bound. Here $A\succeq B$ means $\mathbf z^T(A-B)\mathbf z\ge0$ for every real vector $\mathbf z$. To derive it, form $N\times m$ matrices $U_{i\alpha}=u_i^\alpha/\sqrt{\bar r_i}$ and $V_{i\alpha}=v_i^\alpha\sqrt{\bar r_i}$. Then

<!-- pedagogy-paragraph: p185 sha256 9b8afe6a0b2f66fda0c7733c075358665564568e751ccdbfad6bbfb3ada10f7b -->
p185, lines 185-185; prose; priority: unchanged; previous: p179; next: p189

> The matrix inequality applies when every independent small coordinate change can be distinguished through a change in rates, so $J$ is invertible. It also explains why a scalar bound in each coordinate separately would miss coupled directions.[^p1-matrix]

<!-- pedagogy-paragraph: p189 sha256 3ebe84417bb4edca036016b413a1e0ee2b9de9642f60067fe5349d0c07c669dc -->
p189, lines 189-189; prose; priority: unchanged; previous: p185; next: p200

> Set $Q=V-U(U^TU)^{-1}$. Expanding $Q^TQ$ and using $U^TV=I$ gives


Claim-bearing content: figure

Claims to check:

- Claim c1, line 84: "$$ 2D=\sum_i v_i^2\bar r_i, \qquad u_i=\tau r_i', \qquad \sum_i v_i u_i=1. $$" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c2, line 98: "Their squared lengths are $\sum_i a_i^2=2D$ and $\sum_i b_i^2=J$." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c3, line 100: "$$ \left(\frac1\tau\right)^2 \le\left(\sum_i a_i^2\right)\left(\sum_i b_i^2\right)=2DJ, $$" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c4, line 111: "It is a shorter teaching reconstruction of the scalar proof in SI Section V." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c5, line 111: "Its assumptions are those used to derive $D$ and $J$; it is not a general statement about all possible noisy memory systems.[^p1-bound-source]" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c6, line 113: "Small internal information forces a large minimum diffusion coefficient." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c7, line 113: "Large information allows small diffusion, but does not guarantee it." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c8, line 117: "$$ v_i=c\frac{r_i'}{\bar r_i} \quad\text{for every contributing cell}, \qquad c=\frac{1}{\tau J}. $$" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c9, line 123: "Cells with zero tuning slope cannot contribute extra projected noise if equality is to hold." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c10, line 129: "It is a sufficient condition, rather than a general necessity: the common ratio may depend on the current memory state.[^p1-equality]" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c11, line 133: "Set its bias $b_0=0$ and use the linear rule $\phi(g)=g/\tau$ on positive inputs." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c12, line 133: "Its fixed states are $s_1=s_2=\theta>0$, with $\mathbf u=(1,1)^T$ and $\mathbf v=(1/2,1/2)^T$." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c13, line 133: "Both rates are $\theta/\tau$, and both rate derivatives are $1/\tau$." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c14, line 141: "At each state both cells receive the same input, and the ratio $\phi'/\phi=1/\theta$ changes between states." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c15, line 145: "**Example: the same diffusion with a looser information bound.** In the two cell mutual inhibition model, use $b=200$ activation units and $\tau=0.1\,\mathrm{s}$." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c16, line 145: "At $\theta=0$ both rates are $1000\,\mathrm{s}^{-1}$ and their slopes are $\pm5\,\mathrm{s}^{-1}$ per activation unit." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c17, line 147: "$$ J=\frac{25}{1000}+\frac{25}{1000}=0.05, \qquad D=\frac{b}{2\tau}=1000. $$" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c18, line 152: "The bound is $1/(2\tau^2J)=1000$, so equality holds at this balanced state." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c19, line 152: "At $\theta=100$, the rates become $1500$ and $500\,\mathrm{s}^{-1}$, while their slopes stay $\pm5$." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c20, line 154: "$$ J=\frac{25}{1500}+\frac{25}{500}=\frac1{15}\simeq0.06667, \qquad \frac1{2\tau^2J}=750. $$" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c21, line 159: "The actual diffusion remains $1000$." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c22, line 165: "Caption: Analytic teaching calculation for the chapter’s mutual inhibition example, with $b=200$ activation units and $\tau=0.1$ s. The coordinate $\theta$ is an activation difference. For positive rates $r_{1,2}=(b\pm\theta)/(2\tau)$, $J=2000/(40000-\theta^2)$ while $D=1000$ activation units squ..." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c23, line 169: "The gap at $\theta=100$ shows why a lower minimum allowed by the inequality is not a reduction in the network’s actual diffusion." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c24, line 169: "See [Diffusion bound, Eq. 4, p. 3](../papers/burak-fiete-2012-persistent-activity.pdf#page=3)." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c25, line 179: "The matrix bound $2D\succeq\tau^{-2}J^{-1}$ means that every linear combination of coordinate displacements obeys the corresponding variance lower bound." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c26, line 179: "Here $A\succeq B$ means $\mathbf z^T(A-B)\mathbf z\ge0$ for every real vector $\mathbf z$." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c27, line 181: "$$ U^TV=I,\qquad U^TU=\tau^2J,\qquad V^TV=2D. $$" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c28, line 185: "The matrix inequality applies when every independent small coordinate change can be distinguished through a change in rates, so $J$ is invertible." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c29, line 185: "It also explains why a scalar bound in each coordinate separately would miss coupled directions.[^p1-matrix]" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c30, line 189: "Set $Q=V-U(U^TU)^{-1}$." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c31, line 191: "$$ Q^TQ=V^TV-(U^TU)^{-1} =2D-\tau^{-2}J^{-1}\succeq0. $$" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]

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

<!-- pedagogy-unit: content/chapters/03-memory-information.md::sec:MEMORY-COMPARISONS -->

### Improving persistence depends on what a comparison holds fixed

Location: line 198, anchor `sec:MEMORY-COMPARISONS`

First content kind: `prose`

Opening passage line: 200
Closing passage line: 240

Paragraphs in source order (complete `PARAGRAPH_REVIEW.json`):

<!-- pedagogy-paragraph: p200 sha256 a24889a582458a0a746c00054f7fd472794d3429ceb23c07461860959191d460 -->
p200, lines 200-200; prose; priority: unchanged; previous: p189; next: p202

> The inequality compares diffusion and information for the same network. To compare different networks, we must say what stays fixed. Otherwise an apparent benefit of a parameter change may come from changing another property at the same time.

<!-- pedagogy-paragraph: p202 sha256 fd14ad98272e5066f8d8935f2bb71df7fc5265fe86f1a356d7cbcc2d0b39e441 -->
p202, lines 202-202; prose; priority: unchanged; previous: p200; next: p204

> Increasing $N$ while retaining the same distribution of tuning curves and scaling weights as $1/N$ keeps individual inputs and rates fixed. The sums in the symmetric formula scale as $N$ in the numerator and $N^2$ in the denominator. Consequently $D\propto1/N$, while $J\propto N$. This is a controlled density or population replication comparison, not a promise about adding arbitrary neurons.

<!-- pedagogy-paragraph: p204 sha256 1321b00b920330fee1ccaeed4ef60a07818b3266fea1fece4a7328e8b3332312 -->
p204, lines 204-204; prose; priority: unchanged; previous: p202; next: p206

> If all tuning rates are multiplied by a factor $a$, their slopes are also multiplied by $a$, so $J\mapsto aJ$. For equality achieving exponential networks, $D\mapsto D/a$ immediately follows. The same scaling follows from the symmetric diffusion formula when the change preserves $g_i'$ up to a common scale and preserves the tuning geometry. For a general fixed nonlinear transfer rule, multiplying rates need not preserve those quantities or even the attractor. The paper's rate comparison is made with the tuning shapes and appropriate network scaling held under control.[^p1-scaling]

<!-- pedagogy-paragraph: p206 sha256 d07a622e3cf39cf97fba57c34ce935e504e2d2b400dca179ff84ea5815a7cc8f -->
p206, lines 206-206; prose; priority: unchanged; previous: p204; next: p208

> Changing $\tau$ while holding the rate tuning curves and their input relation fixed gives $D\propto\tau^{-2}$ in the symmetric formula. Maintaining those curves requires retuning the network, because $\bar s=\tau\bar r$. In contrast, holding activation curves and dimensionless weights fixed in the linear two cell example makes rates scale as $1/\tau$, so $D=b/(2\tau)\propto\tau^{-1}$. These two statements concern different controlled comparisons. A larger cellular time constant can improve memory stability while the exponent of its effect depends on what the experiment keeps fixed.

<!-- pedagogy-paragraph: p208 sha256 68e6a4ec09b735c96bc02cb4ea46477457eb27c084e055f1e0a5fa2961c61902 -->
p208, lines 208-208; prose; priority: unchanged; previous: p206; next: p210

> The paper also links tuning width to memory persistence. The reason for its opposite predictions in one and three dimensions can be derived from the number of active cells and their slopes. This derivation is a teaching reconstruction of the tuning width argument cited in the main text, rather than a proof that every tuning family follows one power law.[^p1-width]

<!-- pedagogy-paragraph: p210 sha256 4ec9786980965a1ab2cbe0f2dabf4b275835f6ac725ca92d14d00201ce370f5d -->
p210, lines 210-210; prose; priority: unchanged; previous: p208; next: p217

> Assume preferred positions $\mathbf c$ have uniform density $\rho$ in a $d$ dimensional stimulus or memory space. Away from boundaries, let identical tuning curves have fixed peak rate $a$ and a common shape $f$:

<!-- pedagogy-paragraph: p217 sha256 91f974e3d492e5d68c89a5e8b11475ca77a37c048c12cd618dfdd69398b6768e -->
p217, lines 217-217; prose; priority: unchanged; previous: p210; next: p227

> The width $w$ is varied while $a$, $\rho$, and the shape $f$ are fixed. For one coordinate direction $\alpha$, replace the population sum by an integral and substitute $\mathbf z=(\boldsymbol\theta-\mathbf c)/w$:

<!-- pedagogy-paragraph: p227 sha256 4c5795f73905ba5665ef7b465b67ae6c5271020338924e0cd8af18757157c968 -->
p227, lines 227-227; prose; priority: unchanged; previous: p217; next: p229

> Two factors determine how information changes with tuning width:

<!-- pedagogy-paragraph: p229 sha256 a6d7c88d5dcfaf936b3c4f4528da08eeea73202aa54dcfb98d0bbf872f6c339e -->
p229, lines 229-229; list_item; priority: unchanged; previous: p227; next: p230

> The volume element contributes $w^d$ because broader fields recruit more neurons.

<!-- pedagogy-paragraph: p230 sha256 ab0b63ce72cafdb9fc8796cf4e226baf8dd46ad9ea8659f5be81aef6f2ed3621 -->
p230, lines 230-230; list_item; priority: unchanged; previous: p229; next: p232

> The squared slope contributes $w^{-2}$ because broader curves change more slowly.

<!-- pedagogy-paragraph: p232 sha256 4e4a322a0fbd2e91884a4f0da0f5d7b13351033f1786b7fa691d06ae8a7a3697 -->
p232, lines 232-232; prose; priority: unchanged; previous: p230; next: p234

> Under these assumptions $J\propto w^{d-2}$. In an equality achieving isotropic exponential network, diffusion in each coordinate consequently scales as $D\propto w^{2-d}$. The resulting comparisons are:

<!-- pedagogy-paragraph: p234 sha256 84ef728d20e64e01bb1f04ffb6ff45fbfaca3a0c072f45f3dde4389d1dd7a179 -->
p234, lines 234-234; list_item; priority: unchanged; previous: p232; next: p235

> Narrower curves help in $d=1$.

<!-- pedagogy-paragraph: p235 sha256 df3c4bfa25c1b3d2285ae09eca3f69a0dae5c185411a8f1041d476cb67126801 -->
p235, lines 235-235; list_item; priority: unchanged; previous: p234; next: p236

> Width has no leading effect in $d=2$.

<!-- pedagogy-paragraph: p236 sha256 abe1badbcc8962e249e45920a9b75890735b8a4d0a67a4880dc1c49174d2ed00 -->
p236, lines 236-236; list_item; priority: unchanged; previous: p235; next: p238

> Broader curves help in $d=3$.

<!-- pedagogy-paragraph: p238 sha256 31e0ae5dc1494abaa149309d34072f700d0297fd59913e18253726869fafb6a3 -->
p238, lines 238-238; prose; priority: unchanged; previous: p236; next: p240

> These conclusions change under another resource constraint. Fixing the total population spike rate instead of peak rate makes $a\propto w^{-d}$, giving $J\propto w^{-2}$ in every dimension. Sparse coverage, a large baseline rate, finite boundaries, correlated noise, or a width too small for the population integral can also change the comparison. Attaining equality means the network reaches the diffusion lower bound for its information rate and synaptic time constant. Minimizing diffusion still requires deciding how much information the allowed architecture and firing budget can supply.

<!-- pedagogy-paragraph: p240 sha256 e2c4833b9ac4506adc89ea2af71478dd8df6471247cf4f691628d2d9bc628677 -->
p240, lines 240-240; prose; priority: unchanged; previous: p238; next: none

> If an external stimulus produces the same tuning curves as the network's input free memory states, the sensory and internal Fisher information are equal. In a symmetric exponential network, maximizing this information then improves sensory estimation and minimizes memory diffusion together. This is why the paper suggests that one circuit could support both sensory estimation and memory storage. The mathematical compatibility does not establish where a particular animal stores a memory, and the equality of tuning curves must be checked rather than inferred from the shared formula.[^p1-colocation]


Claim-bearing content: none

Claims to check:

- Claim c1, line 200: "To compare different networks, we must say what stays fixed." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c2, line 202: "Increasing $N$ while retaining the same distribution of tuning curves and scaling weights as $1/N$ keeps individual inputs and rates fixed." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c3, line 202: "Consequently $D\propto1/N$, while $J\propto N$." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c4, line 204: "The paper's rate comparison is made with the tuning shapes and appropriate network scaling held under control.[^p1-scaling]" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c5, line 206: "Changing $\tau$ while holding the rate tuning curves and their input relation fixed gives $D\propto\tau^{-2}$ in the symmetric formula." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c6, line 206: "In contrast, holding activation curves and dimensionless weights fixed in the linear two cell example makes rates scale as $1/\tau$, so $D=b/(2\tau)\propto\tau^{-1}$." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c7, line 208: "This derivation is a teaching reconstruction of the tuning width argument cited in the main text, rather than a proof that every tuning family follows one power law.[^p1-width]" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c8, line 219: "$$ J_{\alpha\alpha} \simeq\rho\int d^d c\, \frac{a^2w^{-2}(\partial_\alpha f)^2}{af} =\rho a w^{d-2} \int d^d z\,\frac{(\partial_\alpha f)^2}{f}. $$" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c9, line 230: "The squared slope contributes $w^{-2}$ because broader curves change more slowly." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c10, line 232: "Under these assumptions $J\propto w^{d-2}$." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c11, line 232: "In an equality achieving isotropic exponential network, diffusion in each coordinate consequently scales as $D\propto w^{2-d}$." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c12, line 234: "Narrower curves help in $d=1$." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c13, line 235: "Width has no leading effect in $d=2$." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c14, line 236: "Broader curves help in $d=3$." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c15, line 238: "Fixing the total population spike rate instead of peak rate makes $a\propto w^{-d}$, giving $J\propto w^{-2}$ in every dimension." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c16, line 238: "Sparse coverage, a large baseline rate, finite boundaries, correlated noise, or a width too small for the population integral can also change the comparison." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c17, line 240: "The mathematical compatibility does not establish where a particular animal stores a memory, and the equality of tuning curves must be checked rather than inferred from the shared formula.[^p1-colocation]" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]

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

## ch:MEMORY-READOUT - Readout accuracy depends on how a moving memory is observed

Source file: `content/chapters/03b-memory-readout.md`

Purpose: When a recall cue arrives, the stored value has already moved. Later spikes can help estimate the value present at that cue, but they cannot reveal the particular random displacements that occurred before it. Waiting for more spikes also allows the network to move further. The question is how much observation helps when the value being read keeps changing.

Prerequisites: ch:MEMORY-INFORMATION

Sidecar sections: Storage loss and readout error add under specific assumptions, Equal weighting becomes harmful when observation lasts too long, Accounting for diffusion makes readout improve toward a limit, Limited access can make observation slower, Time scales and noise laws change the bound and its equality condition, Readout saturates, and one printed error bound needs qualification

Blocks: 2 figure(s), 0 equation(s), 0 code block(s)

Result labels: No Answer/Conclusion/Feedback label detected

<!-- pedagogy-unit: content/chapters/03b-memory-readout.md::ch:MEMORY-READOUT -->

### Chapter opening

Location: line 1, anchor `ch:MEMORY-READOUT`

First content kind: `prose`

Opening passage line: 3
Closing passage line: 7

Paragraphs in source order (complete `PARAGRAPH_REVIEW.json`):

<!-- pedagogy-paragraph: p3 sha256 b55041ac695108770cc314de6356ca18aadcadf94aef178b680a7a5bce6bc643 -->
p3, lines 3-3; prose; priority: unchanged; previous: none; next: p5

> When a recall cue arrives, the stored value has already moved. Later spikes can help estimate the value present at that cue, but they cannot reveal the particular random displacements that occurred before it. Waiting for more spikes also allows the network to move further. The question is how much observation helps when the value being read keeps changing.

<!-- pedagogy-paragraph: p5 sha256 296884bd282413ce02949cb4b629040180e84a2e811ad08b4047e8c2257b4cca -->
p5, lines 5-5; prose; priority: unchanged; previous: p3; next: p7

> Separating the error accumulated during storage from the error of reading the cue state makes that question precise. Equal weighting of later observations shows why simply waiting can become harmful. Allowing for the state's motion then shows how observation can keep helping toward a limit, and how access to only some spikes changes the useful duration. The time constants and noise assumptions also need checking before the resulting limits can be compared with the paper's final error claim.

<!-- pedagogy-paragraph: p7 sha256 8173688b34db5ac3840b45034e235498931760bd1acbea78625826edff43f535 -->
p7, lines 7-7; prose; priority: unchanged; previous: p5; next: p11

> As before, the memory coordinate is $\theta$, its initial value is $\Theta$, and its displacement variance is $2Dt$ for constant diffusion coefficient $D$ without boundaries or systematic drift. The storage delay $T$ ends at the recall cue; the observation interval $L$ begins there. The [spike information rate $J$](ch-memory-information.html#sec-memory-fi) measures how clearly nearby present states can be distinguished, and $\tau$ is the basic model's common synaptic time constant.


Claim-bearing content: none

Claims to check:

- Claim c1, line 3: "Later spikes can help estimate the value present at that cue, but they cannot reveal the particular random displacements that occurred before it." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c2, line 5: "Allowing for the state's motion then shows how observation can keep helping toward a limit, and how access to only some spikes changes the useful duration." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]

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

<!-- pedagogy-unit: content/chapters/03b-memory-readout.md::sec:MEMORY-READOUT-SETUP -->

### Storage loss and readout error add under specific assumptions

Location: line 9, anchor `sec:MEMORY-READOUT-SETUP`

First content kind: `prose`

Opening passage line: 11
Closing passage line: 56

Paragraphs in source order (complete `PARAGRAPH_REVIEW.json`):

<!-- pedagogy-paragraph: p11 sha256 e84c639673a7ab9fc2605d3db9023574477d25f3a0f18f6a1f91c6b3725b0877 -->
p11, lines 11-11; prose; priority: unchanged; previous: p7; next: p13

> At time $T$, a recall cue arrives. The observer now wants the original value $\Theta$, but only has access to future spikes. The network has already diffused during storage. Even perfect knowledge of the state $\theta(T)$ cannot recover its particular earlier random displacements.

<!-- pedagogy-paragraph: p13 sha256 dcdbbc7fd7b22312931f031b7d316e7fb6ea60f88a720fe0f2971b5bff7a5d31 -->
p13, lines 13-13; prose; priority: unchanged; previous: p11; next: p21

> For an unbounded coordinate with constant $D$ and no drift, let $x=\theta(T)$ and let $\widehat x$ estimate that state from later spikes. Write the storage displacement as $s=x-\Theta$ and the readout error as $e=\widehat x-x$. The total recall error is their sum:

<!-- pedagogy-paragraph: p21 sha256 4f1f4f6b69bf996292b76620eb17de7a1ade128c208a6c2da49fbb1207fb9bec -->
p21, lines 21-21; prose; priority: unchanged; previous: p13; next: p27

> Assume the readout is locally unbiased at every possible $x$ and the future noise is independent of the storage history. Conditional on that history, the readout error then has mean zero. Since $s$ is fixed by the history, $\mathbb E[se]=\mathbb E[s\,\mathbb E(e\mid\text{storage history})]=0$. Both errors have zero mean, so their covariance vanishes. In this readout model, [**translation invariance**]{.definition-term custom-style="Definition Term"} means that shifting the represented value does not change the statistics of the readout error. Its variance is therefore the same at every $x$; denote it by $V_{\mathrm{read}}(L)$. Using $\operatorname{Var}(s)=2DT$ gives

<!-- pedagogy-paragraph: p27 sha256 aa9fade502e5b83d65d25efa07d75a8b367b3d90f9c74c105c3a8792d4ffd355 -->
p27, lines 27-27; prose; priority: unchanged; previous: p21; next: p29

> The two terms describe different sources of error:

<!-- pedagogy-paragraph: p29 sha256 f459ad3a1a021b515af4f91f5dff132162c846c5d21b84e8626f271c44907a51 -->
p29, lines 29-29; list_item; priority: unchanged; previous: p27; next: p30

> $2DT$ comes from storage.

<!-- pedagogy-paragraph: p30 sha256 9dfb364848af2b364e5fc77e7e24766b7b8180c5a7d217ea21f8d8f5cece73c6 -->
p30, lines 30-30; list_item; priority: unchanged; previous: p29; next: p32

> $V_{\mathrm{read}}(L)$ concerns estimation of $\theta(T)$ from spikes after $T$.

<!-- pedagogy-paragraph: p32 sha256 39fed7813e7e6e0aeaaa4e3078fe40b08e0f7ab7ec5f696b531b0b641a94663c -->
p32, lines 32-32; prose; priority: unchanged; previous: p30; next: p34

> The supplement derives this decomposition for a locally translation invariant diffusion and readout model; state dependence, boundaries, informative priors, or uncertain initial encoding require corresponding changes.[^p1-read-setup]

<!-- pedagogy-paragraph: p34 sha256 4b36a2489b8b6a1ef4f20f37dd473a54057747f5babbcc9b1d88122fc98a08b2 -->
p34, lines 34-34; prose; priority: unchanged; previous: p32; next: p36

> A timeline separates the displacement accumulated before the cue from the error in estimating the cue state afterward.

<!-- pedagogy-paragraph: p36 sha256 2c643bd85d3e8933fd7127e586cd0d302d74dcd69d691fc3921ef217cc019e39 -->
p36, lines 36-36; prose; priority: unchanged; previous: p34; next: p40

> <div class="figure-scroll">

<!-- pedagogy-paragraph: p40 sha256 aac32651b10f567c461b9b4f255d6fb1fa6859b5368d8bd9a51af920ab21cf23 -->
p40, lines 40-40; prose; priority: unchanged; previous: p36; next: p42

> </div>

<!-- pedagogy-paragraph: p42 sha256 1c012bc4378dc71427b679c6b5fc9381b5d275a6bd81f04be4e9077a09f831e4 -->
p42, lines 42-42; prose; priority: unchanged; previous: p40; next: p44

> Later spikes can improve the estimate of $x=\theta(T)$; they do not reveal the particular storage displacements that separated $x$ from $\Theta$.

<!-- pedagogy-paragraph: p44 sha256 268c7a2733040a00b92d589d2f22e49c292a3229e2ca65e50c805559a7241505 -->
p44, lines 44-44; prose; priority: unchanged; previous: p42; next: p56

> To solve the readout problem, the supplement approximates the likelihood from each short bin as Gaussian. Let $x=\theta(T)$ and index subsequent bins by $k$. The equivalent observation model is

<!-- pedagogy-paragraph: p56 sha256 901370ff351a205eed6eb148b04dd45d0c1ce4f3fa37852df28f77f67d2fcb8a -->
p56, lines 56-56; prose; priority: unchanged; previous: p44; next: p60

> The Gaussian increments and observation errors are independent in this approximation. The value $y_k$ summarizes information about the state from that bin's population spikes; it is not an additional directly measured physical coordinate. The continuous limit is a convenient mathematical description of the many spike, weak fluctuation regime. It does not assert that an arbitrarily short physical bin already contains enough spikes for a Gaussian fit. The derivations below are exact within this local Gaussian readout model.[^p1-read-gaussian]


Claim-bearing content: figure

Claims to check:

- Claim c1, line 11: "The observer now wants the original value $\Theta$, but only has access to future spikes." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c2, line 11: "Even perfect knowledge of the state $\theta(T)$ cannot recover its particular earlier random displacements." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c3, line 15: "$$ \widehat x-\Theta=s+e,\qquad \operatorname{Var}(s+e)=\operatorname{Var}(s)+\operatorname{Var}(e) +2\operatorname{Cov}(s,e). $$" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c4, line 21: "Assume the readout is locally unbiased at every possible $x$ and the future noise is independent of the storage history." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c5, line 21: "Since $s$ is fixed by the history, $\mathbb E[se]=\mathbb E[s\,\mathbb E(e\mid\text{storage history})]=0$." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c6, line 21: "Its variance is therefore the same at every $x$; denote it by $V_{\mathrm{read}}(L)$." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c7, line 21: "Using $\operatorname{Var}(s)=2DT$ gives" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c8, line 23: "$$ V_{\mathrm{total}}(T,L)=2DT+V_{\mathrm{read}}(L). $$" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c9, line 32: "The supplement derives this decomposition for a locally translation invariant diffusion and readout model; state dependence, boundaries, informative priors, or uncertain initial encoding require corresponding changes.[^p1-read-setup]" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c10, line 38: "Caption: Original guide construction of storage and cue state readout, based on Burak and Fiete (2012), Supporting Text, p. 12, Eq. S57. The illustrated path is one possible construction, and the orange estimate concerns the state at the cue rather than the state at the end of observation. With t..." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c11, line 46: "$$ \theta_{k+1}=\theta_k+\eta_k, \qquad y_k=\theta_k+\epsilon_k, $$" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c12, line 51: "$$ \operatorname{Var}(\eta_k)=2Dh, \qquad \operatorname{Var}(\epsilon_k)=\frac1{Jh}. $$" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c13, line 56: "The derivations below are exact within this local Gaussian readout model.[^p1-read-gaussian]" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]

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

<!-- pedagogy-unit: content/chapters/03b-memory-readout.md::sec:MEMORY-NAIVE -->

### Equal weighting becomes harmful when observation lasts too long

Location: line 58, anchor `sec:MEMORY-NAIVE`

First content kind: `prose`

Opening passage line: 60
Closing passage line: 109

Paragraphs in source order (complete `PARAGRAPH_REVIEW.json`):

<!-- pedagogy-paragraph: p60 sha256 0e0fd63c85aee3e203690aa307d1ef4ff9a0957a64346326a5ba8f1c8acde7ba -->
p60, lines 60-60; prose; priority: unchanged; previous: p56; next: p62

> A decoder designed for a stationary state averages its observations with equal weight. That reduces independent observation noise, but late observations reflect a state that has moved further from $x$.

<!-- pedagogy-paragraph: p62 sha256 8e8cbce1e02ad14a81b24ffbda097686d7ce8e0a97ae43b5eb4a5e4de2f17461 -->
p62, lines 62-62; prose; priority: unchanged; previous: p60; next: p68

> Write $\theta(T+t)=x+B_D(t)$, where $B_D$ has Brownian covariance

<!-- pedagogy-paragraph: p68 sha256 621aeaafc66d672886b5101b551c746c026f13ee783cb41ec29148e47d490899 -->
p68, lines 68-68; prose; priority: unchanged; previous: p62; next: p74

> The covariance arises because the two values share increments up to the earlier time. Their later increments are independent. The continuous average is

<!-- pedagogy-paragraph: p74 sha256 275eb9fc796445fb7a0be35d4ca97785c2be69f0d7ee9ba355e24e26e367eb68 -->
p74, lines 74-74; prose; priority: unchanged; previous: p68; next: p80

> Count noise contributes $1/(JL)$: $n=L/h$ bins, each of variance $1/(Jh)$, give average variance $[n/(Jh)]/n^2=1/(JL)$. The motion contribution is

<!-- pedagogy-paragraph: p80 sha256 5fd3e8d69b760e6a85e6db1c657c8bd802c64fecc2eaa235d37be5a0206a1c84 -->
p80, lines 80-80; prose; priority: unchanged; previous: p74; next: p88

> Split the square into its two equal triangles. On the triangle $0\le s\le t\le L$, the minimum is $s$. Therefore

<!-- pedagogy-paragraph: p88 sha256 ba69c22f467e0337d40fed4f0dc8d8e1ebc46d11e38828df6b4efe7e734affcd -->
p88, lines 88-88; prose; priority: unchanged; previous: p80; next: p94

> Combining the terms gives

<!-- pedagogy-paragraph: p94 sha256 c5b5017854e89ddd428d65b5bc9393ff97e2d2deab8c036a9bca08f298954bf6 -->
p94, lines 94-94; prose; priority: unchanged; previous: p88; next: p102

> The two contributions have opposite dependence on $L$. Differentiating,

<!-- pedagogy-paragraph: p102 sha256 0745849b93458f3c978bafcc6900eb5228e0b7a4d9d772df43a0ec943ac2aca9 -->
p102, lines 102-102; prose; priority: unchanged; previous: p94; next: p109

> At that duration the two error terms are equal, and

<!-- pedagogy-paragraph: p109 sha256 d22fa791a259c0c5735e5cef3fd7c9360cf53abfc9b86845c3a35f59f2fa4b79 -->
p109, lines 109-109; prose; priority: unchanged; previous: p102; next: p113

> Waiting longer eventually increases error, even with more spikes available. The problem is their equal weighting for a moving state.[^p1-naive]


Claim-bearing content: none

Claims to check:

- Claim c1, line 64: "$$ E[B_D(t)B_D(s)]=2D\min(t,s). $$" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c2, line 74: "Count noise contributes $1/(JL)$: $n=L/h$ bins, each of variance $1/(Jh)$, give average variance $[n/(Jh)]/n^2=1/(JL)$." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c3, line 82: "$$ \int_0^L\int_0^L\min(t,s)\,dt\,ds =2\int_0^L\!dt\int_0^t\!s\,ds =\int_0^L t^2dt=\frac{L^3}{3}. $$" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c4, line 96: "$$ \frac{dV_{\mathrm{naive}}}{dL}=\frac{2D}{3}-\frac1{JL^2}=0 \quad\Longrightarrow\quad L_{\mathrm{naive}}^*=\sqrt{\frac3{2DJ}}. $$" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c5, line 109: "The problem is their equal weighting for a moving state.[^p1-naive]" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]

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

<!-- pedagogy-unit: content/chapters/03b-memory-readout.md::sec:MEMORY-IDEAL -->

### Accounting for diffusion makes readout improve toward a limit

Location: line 111, anchor `sec:MEMORY-IDEAL`

First content kind: `prose`

Opening passage line: 113
Closing passage line: 191

Paragraphs in source order (complete `PARAGRAPH_REVIEW.json`):

<!-- pedagogy-paragraph: p113 sha256 a80ccc578b1c57e25dbe7da4db476edb7cd17d57aa22789602b5a3ccd3871bf2 -->
p113, lines 113-113; prose; priority: unchanged; previous: p109; next: p115

> An observer that accounts for diffusion can use later observations without confusing them with direct measurements of $x$. Their value is limited by the motion separating them from $x$. We can derive its error by combining information backward from the end of the observation interval.

<!-- pedagogy-paragraph: p115 sha256 86f7e4394709f0df4297c2124198201c0ffc3c66a2c8548b8b4abc18c84a299c -->
p115, lines 115-115; prose; priority: unchanged; previous: p113; next: p117

> The [**precision**]{.definition-term custom-style="Definition Term"} of a scalar Gaussian estimate is the reciprocal of its variance. Independent Gaussian measurements of one value add precisions. To verify this, multiply likelihoods proportional to $\exp[-(x-a)^2/(2V_a)]$ and $\exp[-(x-b)^2/(2V_b)]$: the coefficient of $x^2/2$ becomes $1/V_a+1/V_b$.

<!-- pedagogy-paragraph: p117 sha256 be315f5e2f12bb66389eeb344834000684b317697297e6aa79cd7e0613ae0966 -->
p117, lines 117-117; prose; priority: unchanged; previous: p115; next: p123

> Let $P(L)$ be the precision about the state at the beginning of an interval of length $L$, using all observations in that interval and no informative prior. Suppose we have already compressed the later part into a likelihood about the next bin's state with variance $1/P$. Bringing that likelihood one step backward adds transition variance $q=2Dh$, since the next state equals the earlier state plus an independent Gaussian increment. Its precision about the earlier state is therefore

<!-- pedagogy-paragraph: p123 sha256 edfd5f9575918ce96071d38a7d25e7e6f55a8cc9c3be4fa576c7642dabda177d -->
p123, lines 123-123; prose; priority: unchanged; previous: p117; next: p129

> The new earliest observation adds precision $Jh$. Thus, up to bin endpoint conventions that disappear as $h\to0$,

<!-- pedagogy-paragraph: p129 sha256 6b371bf4c033c420669b6bec309fc0de452748eaf6d787ea16edb0b5359c8916 -->
p129, lines 129-129; prose; priority: unchanged; previous: p123; next: p135

> Expand the denominator for small $h$:

<!-- pedagogy-paragraph: p135 sha256 199651e26a065c615ceed7e00e1e83d367a4155c3c429622728d1704be6dc038 -->
p135, lines 135-135; prose; priority: unchanged; previous: p129; next: p142

> The continuous equation and starting condition are

<!-- pedagogy-paragraph: p142 sha256 994fd0c01419ec58b5718b3ae8ce58d43c893a47d2f44a306215d32199383acf -->
p142, lines 142-142; prose; priority: unchanged; previous: p135; next: p150

> The [**hyperbolic tangent**]{.definition-term custom-style="Definition Term"} is $\tanh z=(e^z-e^{-z})/(e^z+e^{-z})$. Its [**inverse hyperbolic tangent**]{.definition-term custom-style="Definition Term"} on $(-1,1)$ is $\operatorname{artanh}z=\tfrac12\log[(1+z)/(1-z)]$, whose derivative is $1/(1-z^2)$. Initially no observation means zero precision. The term $J$ adds new information; the term $2DP^2$ accounts for uncertainty when carrying that information backward through diffusion. Set $a=\sqrt{J/(2D)}$ and $k=\sqrt{2DJ}$. Separating variables gives

<!-- pedagogy-paragraph: p150 sha256 88c9a085af48fa59a242107a3cf6ffe864f536f0695a8e290f7a0c647be912d4 -->
p150, lines 150-150; prose; priority: unchanged; previous: p142; next: p161

> Taking the inverse function and then the reciprocal yields

<!-- pedagogy-paragraph: p161 sha256 83944ffc0b356f995654d4e4dd0dd3944d85644733126d271d6434981f7fff60 -->
p161, lines 161-161; prose; priority: unchanged; previous: p150; next: p163

> The [**hyperbolic cotangent**]{.definition-term custom-style="Definition Term"} is $\coth z=1/\tanh z$. This backward precision derivation is a teaching reconstruction equivalent to the Gaussian covariance calculation in SI Eqs. S58–S75. It makes explicit how diffusion limits the value of later observations.[^p1-ideal]

<!-- pedagogy-paragraph: p163 sha256 04b96a48bb82516937ab34cc134d3bf14892fe53c4edde59fd013a72a30b5861 -->
p163, lines 163-163; prose; priority: unchanged; previous: p161; next: p169

> For short intervals, $\coth z=1/z+z/3+O(z^3)$, so

<!-- pedagogy-paragraph: p169 sha256 5b7d4ffa870009d857b19c15b26b9cc1ca13460daee3b2350e666c71274aecd5 -->
p169, lines 169-169; prose; priority: unchanged; previous: p163; next: p176

> The naive and ideal estimators therefore agree through the displayed terms. For long intervals,

<!-- pedagogy-paragraph: p176 sha256 a69dfd676542790f39ad32dd4799b5140b78d5c9565ab91d84354fd7fad449ba -->
p176, lines 176-176; prose; priority: unchanged; previous: p169; next: p178

> The ideal observer keeps improving, but the improvement becomes small. Its variance relative to the limiting variance is:

<!-- pedagogy-paragraph: p178 sha256 e4518d8f37792c677e25743c7ca92aebcdba98e7b1a65d6e4aaa94739976b60c -->
p178, lines 178-178; list_item; priority: unchanged; previous: p176; next: p179

> $1.313$ at $L=L^*$.

<!-- pedagogy-paragraph: p179 sha256 e44a0e36cfd4d34eabe8a5b02a93321cf96645429988b772a73346f5179a32ef -->
p179, lines 179-179; list_item; priority: unchanged; previous: p178; next: p180

> $1.037$ at $2L^*$.

<!-- pedagogy-paragraph: p180 sha256 10f30326a0eafaaa0388bd5091f588f3d944d1a60cbef10f6ce86bbc47213a11 -->
p180, lines 180-180; list_item; priority: unchanged; previous: p179; next: p182

> $1.005$ at $3L^*$.

<!-- pedagogy-paragraph: p182 sha256 0dff0718a81fde19361b16b23543d677cf9c646cffbf4362cba21abb09179116 -->
p182, lines 182-182; prose; priority: unchanged; previous: p180; next: p184

> These are variances, so their ratios are not ratios of standard deviations.

<!-- pedagogy-paragraph: p184 sha256 d6d2e932ebc11c3a2bffb2b58633c8d9c85e4bfc99b0e7ed60095ac25c710495 -->
p184, lines 184-184; prose; priority: unchanged; previous: p182; next: p191

> Using $2DJ\ge\tau^{-2}$ gives

<!-- pedagogy-paragraph: p191 sha256 f496e881a93ecf56b07a3819a948b9bd3693cc2c20e61f743f4be322ec86b7b3 -->
p191, lines 191-191; prose; priority: unchanged; previous: p184; next: p195

> Thus the paper's statement about readout within a cellular time constant concerns a characteristic saturation time under full spike access. It does not mean all benefit ends abruptly at $\tau$. The naive observer's best variance is only $2/\sqrt3\simeq1.155$ times the ideal observer's asymptotic variance. Its best standard deviation is about $1.075$ times as large.[^p1-time]


Claim-bearing content: none

Claims to check:

- Claim c1, line 115: "To verify this, multiply likelihoods proportional to $\exp[-(x-a)^2/(2V_a)]$ and $\exp[-(x-b)^2/(2V_b)]$: the coefficient of $x^2/2$ becomes $1/V_a+1/V_b$." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c2, line 117: "Suppose we have already compressed the later part into a likelihood about the next bin's state with variance $1/P$." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c3, line 117: "Bringing that likelihood one step backward adds transition variance $q=2Dh$, since the next state equals the earlier state plus an independent Gaussian increment." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c4, line 119: "$$ \frac{1}{1/P+q}=\frac{P}{1+2DhP}. $$" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c5, line 125: "$$ P(L+h)=Jh+\frac{P(L)}{1+2DhP(L)}. $$" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c6, line 129: "Expand the denominator for small $h$:" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c7, line 131: "$$ P(L+h)=P(L)+[J-2DP(L)^2]h+O(h^2). $$" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c8, line 137: "$$ \frac{dP}{dL}=J-2DP^2, \qquad P(0)=0. $$" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c9, line 142: "Its [**inverse hyperbolic tangent**]{.definition-term custom-style="Definition Term"} on $(-1,1)$ is $\operatorname{artanh}z=\tfrac12\log[(1+z)/(1-z)]$, whose derivative is $1/(1-z^2)$." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c10, line 144: "$$ \int_0^{P/a}\frac{dz}{1-z^2}=kL, \qquad \operatorname{artanh}(P/a)=kL. $$" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c11, line 161: "The [**hyperbolic cotangent**]{.definition-term custom-style="Definition Term"} is $\coth z=1/\tanh z$." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c12, line 161: "It makes explicit how diffusion limits the value of later observations.[^p1-ideal]" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c13, line 163: "For short intervals, $\coth z=1/z+z/3+O(z^3)$, so" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c14, line 176: "The ideal observer keeps improving, but the improvement becomes small." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c15, line 178: "$1.313$ at $L=L^*$." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c16, line 179: "$1.037$ at $2L^*$." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c17, line 180: "$1.005$ at $3L^*$." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c18, line 184: "Using $2DJ\ge\tau^{-2}$ gives" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c19, line 191: "The naive observer's best variance is only $2/\sqrt3\simeq1.155$ times the ideal observer's asymptotic variance." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c20, line 191: "Its best standard deviation is about $1.075$ times as large.[^p1-time]" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]

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

<!-- pedagogy-unit: content/chapters/03b-memory-readout.md::sec:MEMORY-PARTIAL -->

### Limited access can make observation slower

Location: line 193, anchor `sec:MEMORY-PARTIAL`

First content kind: `prose`

Opening passage line: 195
Closing passage line: 216

Paragraphs in source order (complete `PARAGRAPH_REVIEW.json`):

<!-- pedagogy-paragraph: p195 sha256 7496c31af7f91ec6d3e946c427642c89e36121cf08d315453685a84190456e35 -->
p195, lines 195-195; prose; priority: unchanged; previous: p191; next: p197

> A downstream area may receive only some of the memory network's spikes. That reduces its information without reducing the fluctuations that already move the full memory network.

<!-- pedagogy-paragraph: p197 sha256 4feb8b434aa2e295c58d93f3ba40b5f4aab7081f72c73d3a5ff7bed72e07b2f0 -->
p197, lines 197-197; prose; priority: unchanged; previous: p195; next: p203

> If every spike is independently retained with probability $\alpha$, the observed rates and their slopes both scale by $\alpha$. Substitution in the Poisson information formula gives

<!-- pedagogy-paragraph: p203 sha256 9f71cfc6b7de514912fdda3b3099ce78ea033dc604f57f6448f2f7c3a8249cff -->
p203, lines 203-203; prose; priority: unchanged; previous: p197; next: p212

> The network diffusion coefficient stays $D$. Hence

<!-- pedagogy-paragraph: p212 sha256 8c7a128d6c51d0dc288fd56d521b202efda402bfad585c91be85238ef4c6dea2 -->
p212, lines 212-212; prose; priority: unchanged; previous: p203; next: p214

> The same factor $1/\sqrt\alpha$ multiplies the naive optimal interval and its minimum variance. The information bound implies $L_{\mathrm{obs}}^*\le\tau/\sqrt\alpha$, which can exceed $\tau$. A selected subset of neurons has exactly $\alpha J$ only when it carries that fraction of the information; a fraction of neurons or spikes chosen by a biased rule need not do so.[^p1-partial]

<!-- pedagogy-paragraph: p214 sha256 5689fa7c68274c5253f79f4426d0d9f3e8c9a79c7cc1fb0b79be1248271d30f5 -->
p214, lines 214-214; prose; priority: unchanged; previous: p212; next: p216

> **Example: limited spike access changes the useful interval.** Take $\tau=0.1\,\mathrm{s}$, $J=10{,}000\,\mathrm{rad}^{-2}\mathrm{s}^{-1}$, and $D=0.005\,\mathrm{rad}^2/\mathrm{s}$. These values attain the information bound. Full access gives $L^*=0.1\,\mathrm{s}$ and limiting readout variance $0.001\,\mathrm{rad}^2$. The naive optimum is $0.1732\,\mathrm{s}$ with variance $0.001155\,\mathrm{rad}^2$.

<!-- pedagogy-paragraph: p216 sha256 4f8e717a0711891a0de3a803bb06dc5d3628b1f78c0013b06889e20c790cacdd -->
p216, lines 216-216; prose; priority: unchanged; previous: p214; next: p220

> If $\alpha=0.1$, then $J_{\mathrm{obs}}=1000\,\mathrm{rad}^{-2}\mathrm{s}^{-1}$. The ideal characteristic interval becomes $0.3162\,\mathrm{s}$ and its limiting variance becomes $0.003162\,\mathrm{rad}^2$. The naive optimum becomes $0.5477\,\mathrm{s}$. A two second storage delay contributes $2DT=0.020\,\mathrm{rad}^2$ in both cases, giving total ideal asymptotic variances $0.021$ and $0.023162\,\mathrm{rad}^2$. Longer observation can reduce the readout cost; it cannot undo the random displacement during the delay.


Claim-bearing content: none

Claims to check:

- Claim c1, line 195: "A downstream area may receive only some of the memory network's spikes." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c2, line 197: "If every spike is independently retained with probability $\alpha$, the observed rates and their slopes both scale by $\alpha$." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c3, line 212: "The same factor $1/\sqrt\alpha$ multiplies the naive optimal interval and its minimum variance." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c4, line 212: "A selected subset of neurons has exactly $\alpha J$ only when it carries that fraction of the information; a fraction of neurons or spikes chosen by a biased rule need not do so.[^p1-partial]" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c5, line 214: "**Example: limited spike access changes the useful interval.** Take $\tau=0.1\,\mathrm{s}$, $J=10{,}000\,\mathrm{rad}^{-2}\mathrm{s}^{-1}$, and $D=0.005\,\mathrm{rad}^2/\mathrm{s}$." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c6, line 214: "Full access gives $L^*=0.1\,\mathrm{s}$ and limiting readout variance $0.001\,\mathrm{rad}^2$." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c7, line 214: "The naive optimum is $0.1732\,\mathrm{s}$ with variance $0.001155\,\mathrm{rad}^2$." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c8, line 216: "If $\alpha=0.1$, then $J_{\mathrm{obs}}=1000\,\mathrm{rad}^{-2}\mathrm{s}^{-1}$." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c9, line 216: "The ideal characteristic interval becomes $0.3162\,\mathrm{s}$ and its limiting variance becomes $0.003162\,\mathrm{rad}^2$." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c10, line 216: "The naive optimum becomes $0.5477\,\mathrm{s}$." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c11, line 216: "A two second storage delay contributes $2DT=0.020\,\mathrm{rad}^2$ in both cases, giving total ideal asymptotic variances $0.021$ and $0.023162\,\mathrm{rad}^2$." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c12, line 216: "Longer observation can reduce the readout cost; it cannot undo the random displacement during the delay." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]

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

<!-- pedagogy-unit: content/chapters/03b-memory-readout.md::sec:MEMORY-EXTENSIONS -->

### Time scales and noise laws change the bound and its equality condition

Location: line 218, anchor `sec:MEMORY-EXTENSIONS`

First content kind: `prose`

Opening passage line: 220
Closing passage line: 264

Paragraphs in source order (complete `PARAGRAPH_REVIEW.json`):

<!-- pedagogy-paragraph: p220 sha256 ddd05bb8f0c1013e29baae21784eb0f6a39d5745c8324ad8bcca7bcd068972cc -->
p220, lines 220-220; prose; priority: unchanged; previous: p216; next: p222

> The time constant in the inequality comes from the dynamics that carry an activation fluctuation into a lasting memory change. If those dynamics contain both synaptic and rate relaxation, which time constant matters?

<!-- pedagogy-paragraph: p222 sha256 ef6398e829dab87a2f03f34c1d16d88438e4c840e2ee50f4ff974f8cb62e15bd -->
p222, lines 222-222; prose; priority: unchanged; previous: p220; next: p230

> The supplement adds rate relaxation with time constant $\tau_m$:

<!-- pedagogy-paragraph: p230 sha256 a71b565d33f6187f9ccfecc944a03f2544727006fe801d95598f51255f0dbc0b -->
p230, lines 230-230; prose; priority: unchanged; previous: p222; next: p239

> The activation noise retains its Poisson strength. In this symmetric weight extension, the linear state is $(\delta\mathbf s,\delta\mathbf r)$ and its deterministic matrix is

<!-- pedagogy-paragraph: p239 sha256 d6b124af7adcbacb6691e50da402d7bb5a0563a8b8226c23018e81387baf36d2 -->
p239, lines 239-239; prose; priority: unchanged; previous: p230; next: p245

> The right tangent is $(\tau\mathbf r',\mathbf r')$. Write the left zero vector as $(\mathbf a,\mathbf b)$. The second block of $(\mathbf a^T,\mathbf b^T)A=0$ gives $\mathbf b=\tau_m\mathbf a$. The first then gives $W^T\operatorname{diag}(\phi')\mathbf a=\mathbf a/\tau$, so symmetry again permits $\mathbf a\propto\mathbf g'$. Normalizing its dot product with the right tangent yields

<!-- pedagogy-paragraph: p245 sha256 028d2e9a6fdd34e338dec61c4a6d69de61f9630270af3a0a55c57a3a08585a57 -->
p245, lines 245-245; prose; priority: unchanged; previous: p239; next: p254

> Only the $s$ block receives the modeled spike noise, so $2D=\sum_i a_i^2\bar r_i$. The symmetric formula consequently becomes

<!-- pedagogy-paragraph: p254 sha256 74862eb03e34123caf9238c409901563c8eb4e90aea7e0f23f43351b418989be -->
p254, lines 254-254; prose; priority: unchanged; previous: p245; next: p256

> The sum of the two time constants replaces $\tau$. The larger one dominates when they are very different. This result belongs to the two stage model and noise placement just described; the paper does not prove that arbitrary collections of biological time constants can always be added.[^p1-two-times]

<!-- pedagogy-paragraph: p256 sha256 d645abd7cfd277353cf6a5f616bcb140e047180c1f9ba881bb112bb068724d7e -->
p256, lines 256-256; prose; priority: unchanged; previous: p254; next: p262

> The equality condition also depends on the noise law. To see why, replace Poisson spike-count fluctuations with independent additive Gaussian noise of constant strength $q>0$:

<!-- pedagogy-paragraph: p262 sha256 831f73ed04fbe9f2deaadb28883e4c2b4bcdc0484aed8c5da2febb9bb613b40a -->
p262, lines 262-262; prose; priority: unchanged; previous: p256; next: p264

> The short interval observation of the mean rate is now Gaussian with variance $q/h$. Repeating the score calculation gives $J=\sum_i(r_i')^2/q$, while projection gives $2D=q\sum_i v_i^2$. The same Cauchy Schwarz proof yields $2DJ\ge\tau^{-2}$. Equality requires $v_i\propto r_i'$ because all cells have the same noise strength. In a symmetric network $v_i\propto g_i'$, so a linear transfer rule supplies the condition by keeping $\phi'(g)$ constant across participating inputs. In the Poisson case, variance grows with rate and an exponential rule is a sufficient way to attain equality. The pointwise projection condition remains the general criterion, including the [linear-family counterexample](ch-memory-information.html#sec-memory-bound) already derived. The difference between these sufficient classes follows from the noise weighting, not from linearity being universally preferable.[^p1-gaussian]

<!-- pedagogy-paragraph: p264 sha256 80b66cb68052ab95a4fc7c0bd4b0b46fda0ff1ed2de6d5dda3d5c5bf8b89ed93 -->
p264, lines 264-264; prose; priority: unchanged; previous: p262; next: p268

> This explicit $q$ formulation is a teaching reconstruction that keeps dimensions and the noise normalization visible. The supplement's Gaussian subsection establishes the change in equality condition. Here the matched noise and likelihood derivation supplies all factors of $q$ and $\tau$ without requiring the reader to infer a normalization from SI Eqs. S94–S95.


Claim-bearing content: none

Claims to check:

- Claim c1, line 239: "The second block of $(\mathbf a^T,\mathbf b^T)A=0$ gives $\mathbf b=\tau_m\mathbf a$." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c2, line 245: "Only the $s$ block receives the modeled spike noise, so $2D=\sum_i a_i^2\bar r_i$." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c3, line 247: "$$ 2D=\frac{\sum_i\bar r_i(g_i')^2} {(\tau+\tau_m)^2[\sum_i g_i'r_i']^2}, \qquad 2D\ge\frac{J^{-1}}{(\tau+\tau_m)^2}. $$" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c4, line 254: "This result belongs to the two stage model and noise placement just described; the paper does not prove that arbitrary collections of biological time constants can always be added.[^p1-two-times]" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c5, line 256: "To see why, replace Poisson spike-count fluctuations with independent additive Gaussian noise of constant strength $q>0$:" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c6, line 262: "Repeating the score calculation gives $J=\sum_i(r_i')^2/q$, while projection gives $2D=q\sum_i v_i^2$." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c7, line 262: "The same Cauchy Schwarz proof yields $2DJ\ge\tau^{-2}$." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c8, line 262: "The pointwise projection condition remains the general criterion, including the [linear-family counterexample](ch-memory-information.html#sec-memory-bound) already derived." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c9, line 262: "The difference between these sufficient classes follows from the noise weighting, not from linearity being universally preferable.[^p1-gaussian]" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]

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

<!-- pedagogy-unit: content/chapters/03b-memory-readout.md::sec:MEMORY-FIG3-AND-CAUTION -->

### Readout saturates, and one printed error bound needs qualification

Location: line 266, anchor `sec:MEMORY-FIG3-AND-CAUTION`

First content kind: `prose`

Opening passage line: 268
Closing passage line: 307

Paragraphs in source order (complete `PARAGRAPH_REVIEW.json`):

<!-- pedagogy-paragraph: p268 sha256 5c370e45e4c2b98aef994308da3cc023a6557af5bb9e117d3f4860abea460400 -->
p268, lines 268-268; prose; priority: unchanged; previous: p264; next: p270

> Figure 3 isolates readout uncertainty, rescaling variance by $\sqrt{2D/J}$ and duration by $L^*$. In these axes the ideal curve is $\coth z$ and the naive curve is $z/3+1/z$. Both diverge like $1/z$ at short durations because too few spikes are available. The plotted features are:

<!-- pedagogy-paragraph: p270 sha256 b0bee7594f35653136bcc64e084439579779f652c2b628b2d19624f18d377633 -->
p270, lines 270-270; list_item; priority: unchanged; previous: p268; next: p271

> The ideal solid curve approaches one.

<!-- pedagogy-paragraph: p271 sha256 6f4fd36218daab805fef5f0fb2c6d311005cf36dde97ea3bd6d6cfb33ccd7038 -->
p271, lines 271-271; list_item; priority: unchanged; previous: p270; next: p272

> The naive dashed curve reaches $2/\sqrt3$ at $z=\sqrt3$, then rises because its equal weighting gives increasing importance to displaced states.

<!-- pedagogy-paragraph: p272 sha256 63dbf6ae7b3b7e53911b65edd8d5cf3e5391a28283b9ce55239d4499d66145a1 -->
p272, lines 272-272; list_item; priority: unchanged; previous: p271; next: p274

> The dotted vertical line marks that naive optimum.

<!-- pedagogy-paragraph: p274 sha256 4517d8077c663f27683bd28143ef451df6fb956a97c8394631a8c7e6deee50b9 -->
p274, lines 274-274; prose; priority: unchanged; previous: p272; next: p276

> The storage delay contribution $2DT$ is not part of these rescaled curves. Figure S2 repeats the comparison for partial access, showing the rightward and upward shifts when $\alpha=0.1$.[^p1-fig3]

<!-- pedagogy-paragraph: p276 sha256 c7cd0339fb8f4fbe454c921582e0aac55ead92c370d6b1a1acf2afcf5366a702 -->
p276, lines 276-276; prose; priority: unchanged; previous: p274; next: p278

> The normalized curves make the eventual cost of equal weighting visible.

<!-- pedagogy-paragraph: p278 sha256 2c643bd85d3e8933fd7127e586cd0d302d74dcd69d691fc3921ef217cc019e39 -->
p278, lines 278-278; prose; priority: unchanged; previous: p276; next: p282

> <div class="figure-scroll">

<!-- pedagogy-paragraph: p282 sha256 aac32651b10f567c461b9b4f255d6fb1fa6859b5368d8bd9a51af920ab21cf23 -->
p282, lines 282-282; prose; priority: unchanged; previous: p278; next: p284

> </div>

<!-- pedagogy-paragraph: p284 sha256 03a4d49f4c862c7602aee33b8190a77c04e08a78e753d54c1e1d13ae7b2b318f -->
p284, lines 284-284; prose; priority: unchanged; previous: p282; next: p286

> More observation keeps helping the ideal reader, with diminishing benefit, while equal weighting eventually gives too much influence to a state that has moved.

<!-- pedagogy-paragraph: p286 sha256 c2ea3385ff619df62f1c98b33b431c6040b6915bead815facce9d183375d84ea -->
p286, lines 286-286; prose; priority: unchanged; previous: p284; next: p296

> One printed inequality deserves special care. Main Eq. 6 says that total error is at least $2D(T+\tau)$; SI Eq. S83 likewise uses a lower bound with readout term $2D\tau/\sqrt\alpha$. But the paper's other derived results imply

<!-- pedagogy-paragraph: p296 sha256 5f2f4a121c37c1c9680c371f8a7b67111e5456a0fabf6126d3f5691ebb5f17a6 -->
p296, lines 296-296; prose; priority: unchanged; previous: p286; next: p303

> Thus the ideal asymptotic readout term is at most $2D\tau$, with equality when the information diffusion inequality is saturated. Substituting an upper bound for this term cannot establish the printed universal lower bound on total error. Within the local Gaussian model, the defensible statement is

<!-- pedagogy-paragraph: p303 sha256 43d292731d7eadbad6393b23c08685830afe1cf58e3635049815f74f24a01d6e -->
p303, lines 303-303; prose; priority: unchanged; previous: p296; next: p305

> with equality approached as $L\to\infty$ for the ideal observer. At saturation this asymptotic expression becomes $2D(T+\tau)$. For partial access the same issue occurs with the factor $1/\sqrt\alpha$. This is an apparent inconsistency between printed formulas, identified by algebra using the supplied sources. It is not a claim that the authors issued a correction.[^p1-printed]

<!-- pedagogy-paragraph: p305 sha256 019a560ae5696ac844dffa19563786e5949882d9a541fb68c94f4912154f86f5 -->
p305, lines 305-305; prose; priority: unchanged; previous: p303; next: p307

> For a concrete strict inequality case, keep $\tau=0.1\,\mathrm{s}$ and $D=0.005\,\mathrm{rad}^2/\mathrm{s}$ but set $J=40{,}000\,\mathrm{rad}^{-2}\mathrm{s}^{-1}$. Then $2DJ=400\,\mathrm{s}^{-2}$ exceeds $\tau^{-2}=100\,\mathrm{s}^{-2}$. The limiting readout variance is $0.0005\,\mathrm{rad}^2$, whereas $2D\tau=0.001\,\mathrm{rad}^2$. At $T=2\,\mathrm{s}$, the Gaussian ideal total limit is $0.0205\,\mathrm{rad}^2$, below $2D(T+\tau)=0.021\,\mathrm{rad}^2$. These values expose the algebraic problem without assuming the bound is saturated.

<!-- pedagogy-paragraph: p307 sha256 cf1ea8596827b92b23789a962cd2d903919685a7e4eb6df23bb1804c8f051dc6 -->
p307, lines 307-307; prose; priority: unchanged; previous: p305; next: none

> The short readout interval is not a short lifetime of the underlying integrator. A tuned integrator can continue to represent the mean of accumulated inputs while its variance grows. A leak would instead pull its mean toward a particular value. Diffusion limits the accuracy of the integral and the usefulness of long observation; it does not by itself introduce that restoring pull. Applying these predictions to an animal also requires checking its spike statistics, tuning, drift, access to spikes, and other sources of movement noise.[^p1-integrator]


Claim-bearing content: figure

Claims to check:

- Claim c1, line 268: "Figure 3 isolates readout uncertainty, rescaling variance by $\sqrt{2D/J}$ and duration by $L^*$." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c2, line 268: "In these axes the ideal curve is $\coth z$ and the naive curve is $z/3+1/z$." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c3, line 268: "Both diverge like $1/z$ at short durations because too few spikes are available." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c4, line 271: "The naive dashed curve reaches $2/\sqrt3$ at $z=\sqrt3$, then rises because its equal weighting gives increasing importance to displaced states." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c5, line 274: "Figure S2 repeats the comparison for partial access, showing the rightward and upward shifts when $\alpha=0.1$.[^p1-fig3]" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c6, line 280: "Caption: Original guide construction from the analytic readout formulas in Burak and Fiete (2012), Fig. 3 and Supporting Text, Eqs. S75 and S79–S81, rather than digitized data. Ideal readout approaches a normalized variance of one; simple averaging reaches $2/\sqrt3$ at $z=\sqrt3$ and then worsen..." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c7, line 288: "$$ 2DJ\ge\tau^{-2} \quad\Longrightarrow\quad J\ge\frac1{2D\tau^2} \quad\Longrightarrow\quad \sqrt{\frac{2D}{J}}\le2D\tau. $$" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c8, line 296: "Substituting an upper bound for this term cannot establish the printed universal lower bound on total error." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c9, line 303: "For partial access the same issue occurs with the factor $1/\sqrt\alpha$." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c10, line 303: "It is not a claim that the authors issued a correction.[^p1-printed]" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c11, line 305: "For a concrete strict inequality case, keep $\tau=0.1\,\mathrm{s}$ and $D=0.005\,\mathrm{rad}^2/\mathrm{s}$ but set $J=40{,}000\,\mathrm{rad}^{-2}\mathrm{s}^{-1}$." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c12, line 305: "Then $2DJ=400\,\mathrm{s}^{-2}$ exceeds $\tau^{-2}=100\,\mathrm{s}^{-2}$." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c13, line 305: "The limiting readout variance is $0.0005\,\mathrm{rad}^2$, whereas $2D\tau=0.001\,\mathrm{rad}^2$." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c14, line 305: "At $T=2\,\mathrm{s}$, the Gaussian ideal total limit is $0.0205\,\mathrm{rad}^2$, below $2D(T+\tau)=0.021\,\mathrm{rad}^2$." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c15, line 307: "Applying these predictions to an animal also requires checking its spike statistics, tuning, drift, access to spikes, and other sources of movement noise.[^p1-integrator]" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]

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
