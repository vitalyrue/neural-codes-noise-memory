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

> In a model neural circuit, the pattern of firing rates across many nerve cells can represent a remembered angle. Random spike timing can change that angle even while the circuit sustains its activity. Chapters 1–2 explain neural signals and how activity stores a value. Chapters 3–4 derive how that value wanders over time. Chapters 5–6 connect its stability to how accurately it can be estimated from the cells’ spikes.

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

Purpose: Nerve cells communicate with brief electrical spikes. This chapter explains how firing rates across a group of cells can represent an eye angle or an animal’s location, and how variable spike timing affects that representation. These ideas supply the biological and probability background for the three papers.

Prerequisites: None recorded

Sidecar sections: Patterns of firing rates represent a value, A variable spike count at a fixed rate, Shared neural signals and a biased command leave different signs in eye motion

Blocks: 1 figure(s), 0 equation(s), 0 code block(s)

Result labels: No Answer/Conclusion/Feedback label detected

<!-- pedagogy-unit: content/chapters/01-foundations.md::ch:FOUNDATIONS -->

### Chapter opening

Location: line 1, anchor `ch:FOUNDATIONS`

First content kind: `prose`

Opening passage line: 3
Closing passage line: 9

Paragraphs in source order (complete `PARAGRAPH_REVIEW.json`):

<!-- pedagogy-paragraph: p3 sha256 a92a961aef4958eded840175ddc0d24b58ea89ce089dec73c300019cd5460b78 -->
p3, lines 3-7; prose; priority: unchanged; previous: none; next: p9

> <!-- vale ai-tells.CataphoricForecasting = NO --> <!-- vale ai-tells.VerbTricolon = NO --> The eyes can hold a position after a brief movement command has ended. An animal can also keep track of its location while the activity of individual neurons fluctuates. [Both abilities require a useful quantity to remain represented in a changing biological system.]{.key-statement} The three papers study different parts of this problem: the loss of a stored value, the origin of slow eye motion, and the arrangement of spatial firing patterns. <!-- vale ai-tells.VerbTricolon = YES --> <!-- vale ai-tells.CataphoricForecasting = YES -->

<!-- pedagogy-paragraph: p9 sha256 349745a3bca8cc6c0b5e35b2afe4c8d700f3ec45fd71542cb49304934d053b55 -->
p9, lines 9-9; prose; priority: unchanged; previous: p3; next: p13

> Before asking how a circuit keeps a value, we need to know how its activity represents that value and what makes the activity variable. We begin with the spikes that cells send and the patterns of firing rates across a population. A model of spike counts then shows why one brief observation can be uncertain and how combining counts from several cells can help. We then learn how to tell whether measurements vary together and how to separate random spreading from a change in the average value. Those distinctions will let us interpret both a memory model and measurements of eye motion.


Claim-bearing content: none

Claims to check:

- Claim c1, line 3: "[Both abilities require a useful quantity to remain represented in a changing biological system.]{.key-statement} The three papers study different parts of this problem: the loss of a stored value, the origin of slow eye motion, and the arrangement of spatial firing patterns. <!-- vale ai-tells.V..." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]

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

Location: line 11, anchor `sec:FOUNDATIONS-SPIKES`

First content kind: `prose`

Opening passage line: 13
Closing passage line: 47

Paragraphs in source order (complete `PARAGRAPH_REVIEW.json`):

<!-- pedagogy-paragraph: p13 sha256 b10fc37e9e445123c225f9d995b2b29c296e52f6950c5723de3068daf05ca193 -->
p13, lines 13-15; prose; priority: unchanged; previous: p9; next: p17

> <!-- vale ai-tells.StrawmanContrast = NO --> [A neuron communicates through brief electrical events called [**spike**]{.definition-term custom-style="Definition Term"}s.]{.definition-explanation} [A [**firing rate**]{.definition-term custom-style="Definition Term"} is the expected number of spikes per unit time.]{.definition-explanation} A rate of 20 hertz means an average of 20 spikes per second under the specified conditions, rather than a promise of one spike every 50 milliseconds. <!-- vale ai-tells.StrawmanContrast = YES -->

<!-- pedagogy-paragraph: p17 sha256 da8d0c0efe9e2242c7f890b7999b2c921e9742ce14615f42f7fcafaf7ac7e0d5 -->
p17, lines 17-17; prose; priority: unchanged; previous: p13; next: p19

> [Neurons affect one another through connections called [**synapse**]{.definition-term custom-style="Definition Term"}s.]{.definition-explanation} In the models used here, inputs have two contrasting effects:

<!-- pedagogy-paragraph: p19 sha256 43f43d3811706384cde790643db04e668196b24ac2eecf694689fca486b51907 -->
p19, lines 19-19; list_item; priority: unchanged; previous: p17; next: p20

> [An [**excitatory input**]{.definition-term custom-style="Definition Term"} increases a receiving neuron's tendency to fire.]{.definition-explanation}

<!-- pedagogy-paragraph: p20 sha256 895f530452816d01ef5fc238e914b4b688d58023c828c1f8f3761e7b1d2a1c2d -->
p20, lines 20-20; list_item; priority: unchanged; previous: p19; next: p22

> [An [**inhibitory input**]{.definition-term custom-style="Definition Term"} reduces it.]{.definition-explanation}

<!-- pedagogy-paragraph: p22 sha256 b5bc51d61ef2a6363e3855db85c534ac33911c1ad380cdd8079188c2db293e27 -->
p22, lines 22-22; prose; priority: unchanged; previous: p20; next: p24

> The effect of a spike can last beyond the spike itself because synaptic input decays over time. [When neurons send signals back into the same population, the circuit has [**recurrent connectivity**]{.definition-term custom-style="Definition Term"}.]{.definition-explanation} Such feedback can maintain activity after an external signal disappears.

<!-- pedagogy-paragraph: p24 sha256 8bbed07638785fdc1a1c5723bed08b18df47882e51371b6e4db57bbda3337036 -->
p24, lines 24-24; prose; priority: unchanged; previous: p22; next: p26

> [A [**tuning curve**]{.definition-term custom-style="Definition Term"} gives a neuron's expected firing rate as a function of a represented variable.]{.definition-explanation} For eye angle $\theta$, a simple local model is $r_i(\theta)=b_i+k_i\theta$. Neuron $i$ has baseline rate $b_i$ in spikes per second and slope $k_i$ in spikes per second per degree. The linear expression can describe an active range, but it must be modified where it would predict negative firing. The eye paper includes a firing threshold and terms for movement as well as position.[^f-eye]

<!-- pedagogy-paragraph: p26 sha256 618e653c5c789ee690acee11ff3a8159592ca4b9a3c31c421b4d02a6f79322e9 -->
p26, lines 26-26; prose; priority: unchanged; previous: p24; next: p32

> Different cells have different tuning curves. The vector

<!-- pedagogy-paragraph: p32 sha256 d92c478376942a23fda407f53ac966b1f1c1310f7f2eae990f679e2b7f9a4d7d -->
p32, lines 32-36; prose; priority: unchanged; previous: p26; next: p38

> <!-- vale ai-tells.FigurativeCarries = NO --> <!-- vale ai-tells.StrawmanContrast = NO --> [is a [**population code**]{.definition-term custom-style="Definition Term"}: the pattern across $N$ neurons carries information about $\theta$.]{.definition-explanation} The position of a cell in this vector is a neuron identity, rather than a location in physical space. [Reading a value from observed spikes is [**decoding**]{.definition-term custom-style="Definition Term"}.]{.definition-explanation} [Establishing a population pattern from an input is [**encoding**]{.definition-term custom-style="Definition Term"}.]{.definition-explanation} [The 2012 paper asks how accurately the network can maintain such a pattern using its own noisy activity.]{.key-statement} <!-- vale ai-tells.StrawmanContrast = YES --> <!-- vale ai-tells.FigurativeCarries = YES -->

<!-- pedagogy-paragraph: p38 sha256 125f6a786e70caba6fc57d6ee4aee66abd76bff9ca78d24d12fcbf1b9120bbbd -->
p38, lines 38-40; prose; priority: unchanged; previous: p32; next: p42

> <!-- vale ai-tells.FormalTransitions = NO --> Spatial tuning gives a second example. In the hippocampus, a brain structure involved in memory and navigation, a place cell fires strongly in one or more localized regions of an environment. A connected region of elevated spatial firing is a place field. One neuron can have several fields. [A [**rate map**]{.definition-term custom-style="Definition Term"} estimates the rate at each position by dividing the spikes recorded there by the time spent there.]{.definition-explanation} Sparse visits, smoothing, and firing cutoffs therefore affect the estimated map and its fields. A field in a model's expected rate and a field extracted from finite recordings are related objects with different measurement uncertainties.[^f-place] <!-- vale ai-tells.FormalTransitions = YES -->

<!-- pedagogy-paragraph: p42 sha256 79571a034265749c7ab986239802498758b506b7da48f44f62f75687cbeba00f -->
p42, lines 42-42; prose; priority: unchanged; previous: p38; next: p44

> The hippocampal areas CA3 and CA1 contain place cells, but their connections differ:

<!-- pedagogy-paragraph: p44 sha256 8d66a647c59209337c098324aa7c6c2087ced241e1637c52f798b5da4df32619 -->
p44, lines 44-44; list_item; priority: unchanged; previous: p42; next: p45

> CA3 supplies major input to CA1 and has substantial recurrent excitation.

<!-- pedagogy-paragraph: p45 sha256 845567174595b6d1398650e58c477f85c95539d52eb9efd8fd6d17fb3334ef2c -->
p45, lines 45-45; list_item; priority: unchanged; previous: p44; next: p47

> CA1 also receives input from entorhinal cortex and has much less local recurrent excitation.

<!-- pedagogy-paragraph: p47 sha256 db3d26b23afab3d2eca093e0832cf53c212bf16d0e2ccc49a70a3a42bb776a99 -->
p47, lines 47-47; prose; priority: unchanged; previous: p45; next: p51

> [A [**grid cell**]{.definition-term custom-style="Definition Term"}, found in entorhinal cortex, has repeated spatial fields that often form an approximately hexagonal pattern in a two-dimensional arena.]{.definition-explanation} These repeated grid fields and a place cell's irregular multiple fields should be kept distinct. A model explaining CA1's output maps need not identify where the animal's position estimate is maintained.[^f-anatomy]


Claim-bearing content: none

Claims to check:

- Claim c1, line 13: "<!-- vale ai-tells.StrawmanContrast = NO --> [A neuron communicates through brief electrical events called [**spike**]{.definition-term custom-style="Definition Term"}s.]{.definition-explanation} [A [**firing rate**]{.definition-term custom-style="Definition Term"} is the expected number of spike..." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c2, line 24: "The linear expression can describe an active range, but it must be modified where it would predict negative firing." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c3, line 24: "The eye paper includes a firing threshold and terms for movement as well as position.[^f-eye]" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c4, line 38: "A field in a model's expected rate and a field extracted from finite recordings are related objects with different measurement uncertainties.[^f-place] <!-- vale ai-tells.FormalTransitions = YES -->" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c5, line 47: "A model explaining CA1's output maps need not identify where the animal's position estimate is maintained.[^f-anatomy]" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]

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

Location: line 49, anchor `sec:FOUNDATIONS-POISSON`

First content kind: `prose`

Opening passage line: 51
Closing passage line: 119

Paragraphs in source order (complete `PARAGRAPH_REVIEW.json`):

<!-- pedagogy-paragraph: p51 sha256 9bce26d2761d78584eceeff4cc47afea747ff5511d345fed166d276d28aa70f7 -->
p51, lines 51-51; prose; priority: unchanged; previous: p47; next: p59

> A tuning curve describes expected activity, but a brief spike observation can differ each time the same value is represented. [The 2012 model describes this variability with a [**Poisson process**]{.definition-term custom-style="Definition Term"}. At constant rate $r$, the number $K$ of spikes in an interval of length $\Delta t$ obeys]{.definition-explanation}

<!-- pedagogy-paragraph: p59 sha256 1fc8afb5020ca37a59bb1b469af13581157beef6b2b80f7962e8a5d631a63212 -->
p59, lines 59-59; prose; priority: unchanged; previous: p51; next: p68

> Here $\lambda$ is an expected count, so it has no units. For this distribution,

<!-- pedagogy-paragraph: p68 sha256 e4279ae0d6b455c52ae76879c65e2195d146d12d812a5809b52d1e9c0c0f2367 -->
p68, lines 68-70; prose; priority: unchanged; previous: p59; next: p80

> <!-- vale ai-tells.FormalTransitions = NO --> Summing $k\Pr(K=k)$ gives $\lambda$. Likewise, summing $k(k-1)\Pr(K=k)$ gives $\lambda^2$. Since $K^2=K(K-1)+K$, <!-- vale ai-tells.FormalTransitions = YES -->

<!-- pedagogy-paragraph: p80 sha256 88dc01a3d73cd7d3af9b7786543e45b6cf10fe37a39d31e8c8b20c0fea633879 -->
p80, lines 80-82; prose; priority: unchanged; previous: p68; next: p84

> <!-- vale ai-tells.FormalTransitions = NO --> The count variance grows with rate, while its size relative to the mean falls. Its relative standard deviation is $\sqrt\lambda/\lambda=1/\sqrt\lambda$. This is why collecting more independent spikes can improve a rate estimate. It also means that increasing a firing-rate scale does not keep absolute noise amplitude fixed. Comparisons between networks must specify which quantities are held constant.[^f-poisson] <!-- vale ai-tells.FormalTransitions = YES -->

<!-- pedagogy-paragraph: p84 sha256 8e19185c156210567a045f638d7d3d1269765f40e35d9cff42cebc457898c408 -->
p84, lines 84-84; prose; priority: unchanged; previous: p80; next: p86

> <div class="publisher-worked-calculation publisher-fold-always">

<!-- pedagogy-paragraph: p86 sha256 de5190c75864bb0d6d6d57097ed84558c02439b5c8b51ef7615c4c2086bfb541 -->
p86, lines 86-86; prose; priority: unchanged; previous: p84; next: p88

> [**Example: an apparently silent cell and an informative population**]{#sec-foundations-count-example}

<!-- pedagogy-paragraph: p88 sha256 2dc9008302cec48685446799824ffff4d963dd3d156cbad49cc45f47dd724611 -->
p88, lines 88-90; prose; priority: unchanged; previous: p86; next: p92

> <!-- vale ai-tells.FormalTransitions = NO --> Suppose the expected rate is 20 spikes per second and an observation lasts 50 ms. The expected count is $20\times0.05=1$. The probability of seeing no spike is $e^{-1}=0.368$. A silent interval is therefore common even though the expected rate is positive. <!-- vale ai-tells.FormalTransitions = YES -->

<!-- pedagogy-paragraph: p92 sha256 3ce3668a138be58465ad7b5f3ea0e687090eb91612ad1858dac1c3f17a7b7ffb -->
p92, lines 92-92; prose; priority: unchanged; previous: p88; next: p94

> Now suppose 20 conditionally independent cells each have that rate. Their total count is Poisson with mean 20 and standard deviation $\sqrt{20}=4.47$. The total rate estimate has a relative standard deviation of about 22.4%, compared with 100% for one cell. [Population averaging helps because the independent count variances add while the mean signal adds directly. If a common varying input makes several cells' firing rates rise and fall together, that shared variation will not disappear in the same way.]{.key-statement}

<!-- pedagogy-paragraph: p94 sha256 bb68c216e407bc6b8c1e677686df64c2005fdf2c2d9d377844bc689c9d672d5f -->
p94, lines 94-96; prose; priority: unchanged; previous: p92; next: p98

> <!-- vale ai-tells.CataphoricForecasting = NO --> The two count distributions can be compared on the same rate per cell scale. <!-- vale ai-tells.CataphoricForecasting = YES -->

<!-- pedagogy-paragraph: p98 sha256 2c643bd85d3e8933fd7127e586cd0d302d74dcd69d691fc3921ef217cc019e39 -->
p98, lines 98-98; prose; priority: unchanged; previous: p94; next: p102

> <div class="figure-scroll">

<!-- pedagogy-paragraph: p102 sha256 aac32651b10f567c461b9b4f255d6fb1fa6859b5368d8bd9a51af920ab21cf23 -->
p102, lines 102-102; prose; priority: unchanged; previous: p98; next: p104

> </div>

<!-- pedagogy-paragraph: p104 sha256 2d7daa3d10f233631049c070dad41b91878e8ae242a46f9d770c721dd2d76c42 -->
p104, lines 104-104; prose; priority: unchanged; previous: p102; next: p106

> Dividing the pooled rate estimate by 20 keeps the expected rate per cell fixed, while independent averaging reduces its relative spread. See [Poisson count likelihood, SI Eq. S43, p. 9](../papers/burak-fiete-2012-persistent-activity-si.pdf#page=9).

<!-- pedagogy-paragraph: p106 sha256 aac32651b10f567c461b9b4f255d6fb1fa6859b5368d8bd9a51af920ab21cf23 -->
p106, lines 106-106; prose; priority: unchanged; previous: p104; next: p108

> </div>

<!-- pedagogy-paragraph: p108 sha256 19dab7e66caa94ce98b374ef6bc6a3f4f529354210dbc6aa73479e77e299b9ef -->
p108, lines 108-110; prose; priority: unchanged; previous: p106; next: p112

> <!-- vale ai-tells.FormalTransitions = NO --> For changing rates, the expected count is the integral $\lambda=\int r(t)\,dt$. In a recurrent network, $r(t)$ itself depends on past activity. The useful independence statement is therefore conditional: given the current modeled state, the elementary spike-generation noise is independent across cells in the basic 2012 model. Averaging over the changing state can still produce correlations across time and across neurons. This qualification prevents treating a recurrent Poisson network as a collection of independent complete spike trains. <!-- vale ai-tells.FormalTransitions = YES -->

<!-- pedagogy-paragraph: p112 sha256 3d64eaeebee806c5862b18a32d2664acbfe527361dde61eb581a62159c8b0891 -->
p112, lines 112-114; prose; priority: unchanged; previous: p108; next: p116

> <!-- vale ai-tells.CataphoricForecasting = NO --> Two other measurements describe different aspects of variability: <!-- vale ai-tells.CataphoricForecasting = YES -->

<!-- pedagogy-paragraph: p116 sha256 dd818f62bbdd72e80e9d96c68464b5a2fa217473d78118cbb94661601a0a4c82 -->
p116, lines 116-116; list_item; priority: unchanged; previous: p112; next: p117

> [The [**coefficient of variation**]{.definition-term custom-style="Definition Term"}, or CV, of interspike intervals, the times between successive spikes, is their standard deviation divided by their mean.]{.definition-explanation} A homogeneous Poisson process has exponential intervals and CV equal to one. More regular firing can have CV below one, as in the ocular motor neurons analyzed in 2022.

<!-- pedagogy-paragraph: p117 sha256 3c09645155c25775d9dd1c399f43a66ed15d3ab6da9697b92ce55d1ae0dcb95f -->
p117, lines 117-117; list_item; priority: unchanged; previous: p116; next: p119

> [The count variance divided by mean count is the [**Fano factor**]{.definition-term custom-style="Definition Term"}]{.definition-explanation}. Its value also depends on the counting interval.

<!-- pedagogy-paragraph: p119 sha256 31eda53b4f2ba55a576cc45a670ed43cb5ad4cd29ef9a1c1672b21edaef9959d -->
p119, lines 119-119; prose; priority: unchanged; previous: p117; next: p123

> CV and Fano factor cannot be substituted for one another without additional assumptions.


Claim-bearing content: figure

Claims to check:

- Claim c1, line 53: "$$ \Pr(K=k)=e^{-\lambda}\frac{\lambda^k}{k!}, \qquad \lambda=r\Delta t, \qquad k=0,1,2,\ldots . $$" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c2, line 68: "Likewise, summing $k(k-1)\Pr(K=k)$ gives $\lambda^2$." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c3, line 68: "Since $K^2=K(K-1)+K$, <!-- vale ai-tells.FormalTransitions = YES -->" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c4, line 72: "$$ \mathbb E[K^2]=\lambda^2+\lambda, \qquad \operatorname{Var}(K)=\mathbb E[K^2]-\mathbb E[K]^2=\lambda. $$" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c5, line 80: "Its relative standard deviation is $\sqrt\lambda/\lambda=1/\sqrt\lambda$." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c6, line 80: "Comparisons between networks must specify which quantities are held constant.[^f-poisson] <!-- vale ai-tells.FormalTransitions = YES -->" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c7, line 84: "<div class="publisher-worked-calculation publisher-fold-always">" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c8, line 88: "<!-- vale ai-tells.FormalTransitions = NO --> Suppose the expected rate is 20 spikes per second and an observation lasts 50 ms." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c9, line 88: "The expected count is $20\times0.05=1$." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c10, line 88: "The probability of seeing no spike is $e^{-1}=0.368$." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c11, line 92: "Their total count is Poisson with mean 20 and standard deviation $\sqrt{20}=4.47$." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c12, line 92: "The total rate estimate has a relative standard deviation of about 22.4%, compared with 100% for one cell." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c13, line 100: "Caption: Analytic teaching construction for the chapter’s 20 Hz, 50 ms example. The count is Poisson with mean 1 for one cell and mean 20 for 20 conditionally independent cells. Both panels plot the rate per cell $K/(N\Delta t)$, so both estimates have mean 20 Hz. Their standard deviations are 20..." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c14, line 104: "S43, p. 9](../papers/burak-fiete-2012-persistent-activity-si.pdf#page=9)." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c15, line 108: "This qualification prevents treating a recurrent Poisson network as a collection of independent complete spike trains. <!-- vale ai-tells.FormalTransitions = YES -->" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c16, line 119: "CV and Fano factor cannot be substituted for one another without additional assumptions." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]

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

### Shared neural signals and a biased command leave different signs in eye motion

Location: line 121, anchor `sec:FOUNDATIONS-COVARIANCE`

First content kind: `prose`

Opening passage line: 123
Closing passage line: 226

Paragraphs in source order (complete `PARAGRAPH_REVIEW.json`):

<!-- pedagogy-paragraph: p123 sha256 5e2ce175701cffff398bc188d749c26f9d33daa54b23d9441832b91349231e69 -->
p123, lines 123-123; prose; priority: unchanged; previous: p119; next: p125

> During fixation, a monkey tries to keep looking at a stationary target, yet its eye moves slightly. A changing command from the brain can make many motor neurons change their firing together. Their spikes act on the eye muscles, which turn the eye. An individual motor neuron also adds spike variability of its own. The 2022 paper asks how much of the observed movement follows a shared neural command, and whether that command itself wanders over time.[^f-eye]

<!-- pedagogy-paragraph: p125 sha256 06be8a62e2fc4c76e1b69470976cf0072126b886716295ce4e5de9c1ab5077b5 -->
p125, lines 125-127; prose; priority: unchanged; previous: p123; next: p129

> <!-- vale ai-tells.NegatedSubject = NO --> [Covariance asks which recorded changes occur together. Displacement statistics ask how far the eye moves and how that movement grows with elapsed time.]{.key-statement} Neither measurement by itself identifies the neural circuit responsible. <!-- vale ai-tells.NegatedSubject = YES -->

<!-- pedagogy-paragraph: p129 sha256 449c3bda9262930be271b3ded5bb6391035f431a2f5bb8823abf2c46a865015f -->
p129, lines 129-131; prose; priority: unchanged; previous: p125; next: p133

> <!-- vale ai-tells.ContrastiveFormulas = NO --> **Physical meaning: a shared command can survive averaging across neurons.** If a common input raises the firing of many motor neurons that pull the eye in the same direction, their effects add. Independent extra and missing spikes partly cancel when those neurons act together. The paper compares the measured eye displacement with a displacement predicted from one neuron's spikes, after converting both to degrees. That prediction is an analysis of a recording, not an extra command sent to the muscles. A relationship between the two is evidence to test against a model of shared input and private noise. It does not mean that the one recorded cell causes all the movement. <!-- vale ai-tells.ContrastiveFormulas = YES -->

<!-- pedagogy-paragraph: p133 sha256 19c7860866ddf6dc190ba6da79bff096a8f4538135e9468b3fcf32e5ac604c1c -->
p133, lines 133-133; prose; priority: unchanged; previous: p129; next: p137

> [**Covariance**]{.definition-term custom-style="Definition Term"} [measures whether two signals tend to be above their own averages together or on opposite sides of those averages.]{.definition-explanation} Positive covariance between the two displacements means that above-average changes in the neural prediction tend to accompany above-average changes in eye position. [The [**correlation coefficient**]{.definition-term custom-style="Definition Term"}, written $\rho$, expresses this shared variation relative to the spread of each signal.]{.definition-explanation} Extra private noise can lower $\rho$ even when the shared drive has not weakened. The [eye-drift calculation](ch-eye-drift.html#sec-eye-chi) explains why a modest correlation need not mean a small shared contribution to movement.

<!-- pedagogy-paragraph: p137 sha256 206b2ba07dd15d67eaa819bdd1ec5cbde16ca989767704fabd96e9b9eeacaea9 -->
p137, lines 137-137; prose; priority: unchanged; previous: p133; next: p143

> Let $X$ and $Y$ be the two displacements, in degrees, across repeated intervals of the same duration. Subtracting each average leaves its fluctuation. Their covariance is

<!-- pedagogy-paragraph: p143 sha256 ca92311b459636e54ca5a7356eec5afeb789b34b92f60d85c8bd0cdbac73e38a -->
p143, lines 143-143; prose; priority: unchanged; previous: p137; next: p149

> Here it has units degrees squared. In general its units are the product of the two signals' units. Variance is $\operatorname{Cov}(X,X)$. Expanding the square of a centered sum or difference gives

<!-- pedagogy-paragraph: p149 sha256 b7c88fc555ebe3aca6acebdb5379a4d0d05869bf72e5b9ab58fded7348a1a728 -->
p149, lines 149-149; prose; priority: unchanged; previous: p143; next: p155

> For nonzero variances, correlation is

<!-- pedagogy-paragraph: p155 sha256 8dab498f2415af1815a3fa15901f1634c79fc51e4079fc35c018a920b3252664 -->
p155, lines 155-159; prose; priority: unchanged; previous: p149; next: p161

> <!-- vale ai-tells.NegatedObject = NO --> <!-- vale ai-tells.ParallelStaccato = NO --> It is dimensionless and lies between $-1$ and $1$. Independence gives zero covariance when these moments exist. Zero covariance alone does not imply independence. <!-- vale ai-tells.ParallelStaccato = YES --> <!-- vale ai-tells.NegatedObject = YES -->

<!-- pedagogy-paragraph: p161 sha256 17b14d803368ea16ef8b1c4a3d2b3b8cba436f9a1bed3727b0ebe255cc8639d1 -->
p161, lines 161-161; prose; priority: unchanged; previous: p155; next: p168

> To see the physical roles, write $X=g_X S+\epsilon_X$ and $Y=g_Y S+\epsilon_Y$. Here $S$ is a shared displacement signal in degrees, the dimensionless [**gain**]{.definition-term custom-style="Definition Term"}s $g_X,g_Y$ multiply its contribution in each recording, and $\epsilon_X,\epsilon_Y$ are private contributions in degrees. If all three random contributions are independent,

<!-- pedagogy-paragraph: p168 sha256 73d642ac8ac36f69e6e4f21bd214feea7a28706a0f03761a006f1b288acb0dc9 -->
p168, lines 168-168; prose; priority: unchanged; previous: p161; next: p172

> Increasing private variance increases the denominator of $\rho$ without increasing the covariance. Changing a gain changes the measured covariance even if the shared source is unchanged. This simple construction explains the need for calibration and explicit noise assumptions. It is not the paper's full inference model.

<!-- pedagogy-paragraph: p172 sha256 3fad765f29f8ead5c2adc712e824dfc61c353cb708e9cee096e85613f9885fe4 -->
p172, lines 172-172; prose; priority: unchanged; previous: p168; next: p174

> **Physical meaning: random wandering differs from a persistent directional error.** Let $x(t)$ be horizontal eye angle in degrees and let $\ell$ be the time between two measurements, called the lag, in seconds. [The [**displacement**]{.definition-term custom-style="Definition Term"} $\Delta x=x(t+\ell)-x(t)$ is the change in that angle.]{.definition-explanation} A random change in the maintained command can move the eye left in one interval and right in another. The average displacement can then be close to zero while individual displacements are large. A persistent imbalance in the command can instead make the average displacement grow in one direction. Muscles smooth the command before it becomes eye movement, so the timescale of the observation also matters.

<!-- pedagogy-paragraph: p174 sha256 693f2d1ddb89efe8a982872d996c4f4e1e1ae2903f1213e20b836e86039572ba -->
p174, lines 174-174; prose; priority: unchanged; previous: p172; next: p180

> [The **mean squared displacement**, or MSD, averages $(\Delta x)^2$ across repeated intervals and has units degrees squared.]{.definition-explanation} Its two contributions are

<!-- pedagogy-paragraph: p180 sha256 4b32802427b6b013651e12436e2fa8bd74136a80a443da1603225d46d2d4f25c -->
p180, lines 180-182; prose; priority: unchanged; previous: p174; next: p186

> <!-- vale ai-tells.VerbTricolon = NO --> [A larger MSD can mean stronger random movement, a larger directional bias, or both. Measuring the mean displacement separately prevents mistaking bias for increased noise.]{.key-statement} <!-- vale ai-tells.VerbTricolon = YES -->

<!-- pedagogy-paragraph: p186 sha256 4bcb2ef0a73986997005cb0adeae4fe33e653ff7e11a15cd8267a0e927402389 -->
p186, lines 186-186; prose; priority: unchanged; previous: p180; next: p193

> Write $\mu=\mathbb E[\Delta x]$ and $\eta=\Delta x-\mu$, so $\mathbb E[\eta]=0$. Squaring and averaging gives

<!-- pedagogy-paragraph: p193 sha256 3bb7e52e20eec36ed3b9372b10f989ae975189ca7a24edf8ca940ccea8518c06 -->
p193, lines 193-193; prose; priority: unchanged; previous: p186; next: p197

> The cross term vanishes because the fluctuations are measured relative to their own mean. This identity needs finite second moments, but no diffusion assumption.

<!-- pedagogy-paragraph: p197 sha256 62f9606ed7401c3a6568e9f6d033966a73a3c4586aa755bc0190ad2a672e76ef -->
p197, lines 197-197; prose; priority: unchanged; previous: p193; next: p199

> **What changes the physical movement?** The model must say which part of the pathway a parameter controls:

<!-- pedagogy-paragraph: p199 sha256 eb09169d0e6b97a10d4624d5027edf074841619e665b9935feaf4a485362ac33 -->
p199, lines 199-200; list_item; priority: unchanged; previous: p197; next: p201

> **Random changes in the stored command:** more frequent or larger lasting changes make the stored angle spread faster. The next chapter calls this rate of spreading the diffusion coefficient $D$ and explains why it depends on spike variability and the circuit's response to each spike. <!-- vale ai-tells.LabelAndExplain = NO -->

<!-- pedagogy-paragraph: p201 sha256 1534504c2047edaf683e41b26d3b95bae765dca1adbc8ceedc915caa8650721b -->
p201, lines 201-202; list_item; priority: unchanged; previous: p199; next: p203

> **A persistent directional imbalance:** this changes the mean displacement. In a constant-velocity approximation, doubling that velocity doubles the mean displacement at a fixed lag and quadruples its squared contribution to MSD. <!-- vale ai-tells.LabelAndExplain = YES -->

<!-- pedagogy-paragraph: p203 sha256 3d99d5a4bc3f4e3254c4a0c4dcbf146fdace33ef44f4fa4848ef09930f09a861 -->
p203, lines 203-203; list_item; priority: unchanged; previous: p201; next: p204

> **The gain from command to eye angle:** multiplying the command's contribution to each displacement by a gain $G$ multiplies that contribution's variance and MSD by $G^2$, with the input fluctuations held fixed. Any noise added after that gain needs to be counted separately. A fitted tuning slope, which describes rate as a function of angle, is not by itself a causal muscle gain.

<!-- pedagogy-paragraph: p204 sha256 45070397f7c3a5af31b9e025748a573b1a9d139a0d0a36cc9869ad0ded3754ce -->
p204, lines 204-204; list_item; priority: unchanged; previous: p203; next: p206

> **Muscle response time:** a slower response smooths rapid command changes more strongly. It changes the short-lag shape of the MSD curve, not just its height. The [timing chapter](ch-eye-timing.html#sec-eye-filtered-msd) separates this smoothing from growth of noise inside the memory circuit.

<!-- pedagogy-paragraph: p206 sha256 cd176d8a0c4fa6a3c8af9b1260c26885bc4cd4106b754ba804b8ff4bf429f3fe -->
p206, lines 206-208; prose; priority: unchanged; previous: p204; next: p210

> <!-- vale ai-tells.FormalTransitions = NO --> Measurement error is a separate contribution: it changes recorded positions without moving the eye. Independent zero-mean position errors, each of variance $\sigma_m^2$ and independent of true motion, add $2\sigma_m^2$ to displacement MSD at nonzero lags. Thus an upward shift in the observed curve need not be a physical increase in movement. The [measurement-noise calculation](ch-eye-timing.html#sec-eye-measurement-noise) shows the conditions needed to remove it. <!-- vale ai-tells.FormalTransitions = YES -->

<!-- pedagogy-paragraph: p210 sha256 60159beca4e1453bc1fa4daa9cfb62f48dd81e81da781f8a153c6475fb9ece2a -->
p210, lines 210-210; prose; priority: unchanged; previous: p206; next: p212

> The next chapter follows the proposed source upstream: how a circuit can keep a pattern of activity while random spikes change the angle that pattern represents.

<!-- pedagogy-paragraph: p212 sha256 c434e91454241a31e310a239ac3a093d91ab1fcd15b7ac3b333458ba63f49376 -->
p212, lines 212-212; prose; priority: unchanged; previous: p210; next: p214

> <!-- vale ai-tells.EmDashUsage = NO -->

<!-- pedagogy-paragraph: p214 sha256 6e36e79bce1447ac7eddc2fb19787ace984308e97fbb90fe3fbe309f14b460ff -->
p214, lines 214-214; prose; priority: unchanged; previous: p212; next: p216

> <!-- vale ai-tells.EmDashUsage = YES -->

<!-- pedagogy-paragraph: p216 sha256 c434e91454241a31e310a239ac3a093d91ab1fcd15b7ac3b333458ba63f49376 -->
p216, lines 216-216; prose; priority: unchanged; previous: p214; next: p218

> <!-- vale ai-tells.EmDashUsage = NO -->

<!-- pedagogy-paragraph: p218 sha256 6e36e79bce1447ac7eddc2fb19787ace984308e97fbb90fe3fbe309f14b460ff -->
p218, lines 218-218; prose; priority: unchanged; previous: p216; next: p220

> <!-- vale ai-tells.EmDashUsage = YES -->

<!-- pedagogy-paragraph: p220 sha256 c434e91454241a31e310a239ac3a093d91ab1fcd15b7ac3b333458ba63f49376 -->
p220, lines 220-220; prose; priority: unchanged; previous: p218; next: p222

> <!-- vale ai-tells.EmDashUsage = NO -->

<!-- pedagogy-paragraph: p222 sha256 6e36e79bce1447ac7eddc2fb19787ace984308e97fbb90fe3fbe309f14b460ff -->
p222, lines 222-222; prose; priority: unchanged; previous: p220; next: p224

> <!-- vale ai-tells.EmDashUsage = YES -->

<!-- pedagogy-paragraph: p224 sha256 c434e91454241a31e310a239ac3a093d91ab1fcd15b7ac3b333458ba63f49376 -->
p224, lines 224-224; prose; priority: unchanged; previous: p222; next: p226

> <!-- vale ai-tells.EmDashUsage = NO -->

<!-- pedagogy-paragraph: p226 sha256 6e36e79bce1447ac7eddc2fb19787ace984308e97fbb90fe3fbe309f14b460ff -->
p226, lines 226-226; prose; priority: unchanged; previous: p224; next: none

> <!-- vale ai-tells.EmDashUsage = YES -->


Claim-bearing content: none

Claims to check:

- Claim c1, line 123: "The 2022 paper asks how much of the observed movement follows a shared neural command, and whether that command itself wanders over time.[^f-eye]" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c2, line 133: "The [eye-drift calculation](ch-eye-drift.html#sec-eye-chi) explains why a modest correlation need not mean a small shared contribution to movement." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c3, line 155: "<!-- vale ai-tells.NegatedObject = NO --> <!-- vale ai-tells.ParallelStaccato = NO --> It is dimensionless and lies between $-1$ and $1$." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c4, line 180: "Measuring the mean displacement separately prevents mistaking bias for increased noise.]{.key-statement} <!-- vale ai-tells.VerbTricolon = YES -->" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c5, line 186: "Write $\mu=\mathbb E[\Delta x]$ and $\eta=\Delta x-\mu$, so $\mathbb E[\eta]=0$." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c6, line 188: "$$ \mathbb E[(\mu+\eta)^2]=\mu^2+2\mu\mathbb E[\eta]+\mathbb E[\eta^2] =\mu^2+\operatorname{Var}(\Delta x). $$" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c7, line 197: "**What changes the physical movement?** The model must say which part of the pathway a parameter controls:" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]

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

Purpose: A neural circuit can sustain its firing while the value represented by that firing changes. Using eye angle as an example, this chapter separates changes in the activity of the cells from changes in the stored value. That distinction explains how persistent activity can still accumulate memory error.

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

<!-- pedagogy-paragraph: p5 sha256 3f2739c8d9d1d879cb5042b6d1723969c2ad7345e2773b9db4afbee823e2b8b5 -->
p5, lines 5-7; prose; priority: unchanged; previous: p3; next: p11

> <!-- vale ai-tells.FigurativeStays = NO --> We first build a small example in which some disturbances fade while others leave a different stored angle. We then ask what happens when small lasting changes arrive repeatedly, deriving how their spread grows with time and how a fixed bias changes that prediction. The final distinction is between this changing value and an irregular spatial map that stays fixed. It explains why the memory, eye-motion, and place-field papers need different models even though all three concern variable neural signals. <!-- vale ai-tells.FigurativeStays = YES -->


Claim-bearing content: none

Claims to check:

- Claim c1, line 3: "The geometry of these two changes will explain why a stable-looking circuit can still accumulate memory error.[^f-memory]" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c2, line 5: "<!-- vale ai-tells.FigurativeStays = NO --> We first build a small example in which some disturbances fade while others leave a different stored angle." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
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

Location: line 9, anchor `sec:FOUNDATIONS-ATTRACTOR`

First content kind: `prose`

Opening passage line: 11
Closing passage line: 76

Paragraphs in source order (complete `PARAGRAPH_REVIEW.json`):

<!-- pedagogy-paragraph: p11 sha256 da31a7bb3409d6244403646520f5479228ebbd6ad75b18e85792bb826a736067 -->
p11, lines 11-15; prose; priority: unchanged; previous: p5; next: p17

> <!-- vale ai-tells.FigurativeKeeps = NO --> <!-- vale ai-tells.FormalTransitions = NO --> Imagine a group of neurons maintaining a pattern that represents an eye angle after a movement command has ended. Random spikes disturb that pattern. Recurrent input can correct some disturbances by changing the cells' firing back toward a persistent pattern. But if a disturbance produces the pattern for a different angle, an ideal memory circuit has no record of which angle was originally intended. [Keeping a pattern stable is therefore different from keeping the stored value correct.]{.key-statement} <!-- vale ai-tells.FormalTransitions = YES --> <!-- vale ai-tells.FigurativeKeeps = YES -->

<!-- pedagogy-paragraph: p17 sha256 2629dd9df04444c44cf02725a174af8fa9d46a5fa226583573c60561067f9920 -->
p17, lines 17-17; prose; priority: unchanged; previous: p11; next: p19

> [A circuit's current activities are its [**state**]{.definition-term custom-style="Definition Term"}.]{.definition-explanation} A dynamical equation specifies how that state changes. [A [**fixed point**]{.definition-term custom-style="Definition Term"} is a state where the deterministic rate of change is zero.]{.definition-explanation} It is stable in a direction if a small disturbance in that direction decays.

<!-- pedagogy-paragraph: p19 sha256 5623e5926f89d1d98428c5a593fc3c4299013bde73efc14178ce060b1bf86759 -->
p19, lines 19-19; prose; priority: unchanged; previous: p17; next: p21

> Memory of a continuous quantity calls for a family of persistent states. [A [**continuous attractor**]{.definition-term custom-style="Definition Term"} is a continuous family of fixed points with restoring dynamics toward the family and a neutral direction along it. Neutral means that there is no restoring force along that direction in the ideal deterministic model.]{.definition-explanation} [The family is an [**attractor manifold**]{.definition-term custom-style="Definition Term"}. Its dimension counts independent coordinates represented on it, rather than neurons in the circuit.]{.definition-explanation} A line attractor has one represented coordinate. A ring can represent a periodic coordinate such as heading.[^f-memory]

<!-- pedagogy-paragraph: p21 sha256 54dfa0f662d33ab3497dfb3e9562a37668b802fd0f830a1e5e7741733cfc9400 -->
p21, lines 21-21; prose; priority: unchanged; previous: p19; next: p23

> In the illustrative two-cell model below, the difference between the firing rates represents the angle. Raising both rates equally leaves that difference unchanged. The model's feedback removes the common increase. Raising one rate while lowering the other changes the represented angle. That second change persists. The calculation makes these two responses explicit. It is not a fitted biological circuit.

<!-- pedagogy-paragraph: p23 sha256 8e19185c156210567a045f638d7d3d1269765f40e35d9cff42cebc457898c408 -->
p23, lines 23-23; prose; priority: unchanged; previous: p21; next: p25

> <div class="publisher-worked-calculation publisher-fold-always">

<!-- pedagogy-paragraph: p25 sha256 20bf2296bca45823292daeef9a4d081a0a0ad07808b54e7d812533491214ca62 -->
p25, lines 25-25; prose; priority: unchanged; previous: p23; next: p27

> [**Example: two disturbances to the same stored angle**]{#sec-foundations-attractor-example}

<!-- pedagogy-paragraph: p27 sha256 1bc7456fdcee91a79a0ef786320f4601ac83af52a14e212a4e933af2377e62eb -->
p27, lines 27-29; prose; priority: unchanged; previous: p25; next: p35

> <!-- vale ai-tells.AnthropomorphicCognition = NO --> Consider a teaching model with two activities $r_1,r_2$ in spikes per second. Let $b=40$ spikes per second and let $k=2$ spikes per second per degree. A stored angle $\theta$ corresponds to <!-- vale ai-tells.AnthropomorphicCognition = YES -->

<!-- pedagogy-paragraph: p35 sha256 95f000ec66c24f06913f5bde801beb9c39a1455720fe17fa322f985a9dc7e71d -->
p35, lines 35-35; prose; priority: unchanged; previous: p27; next: p43

> The fixed points lie on the line $r_1+r_2=2b$. Restrict attention to angles where both rates remain positive. Define the deviation in their mean activity and the represented angle as

<!-- pedagogy-paragraph: p43 sha256 ee9984e3707247939ce0832e0ddbf38183511c8d034bf3bfd21579d9fa4279dc -->
p43, lines 43-43; prose; priority: unchanged; previous: p35; next: p49

> Suppose each activity changes according to

<!-- pedagogy-paragraph: p49 sha256 8fcb790f0a0ad95fa8b469f231da0b99e7f09513b88d74d8350d785d3fe2d040 -->
p49, lines 49-49; prose; priority: unchanged; previous: p43; next: p55

> where $a>0$ has units inverse seconds. Adding and subtracting these equations gives

<!-- pedagogy-paragraph: p55 sha256 7db97decba35b60b8828ada87ee3d9128149429dee69a6f5c049b3ef09ca928f -->
p55, lines 55-55; prose; priority: unchanged; previous: p49; next: p57

> The first equation has solution $x(t)=x(0)e^{-at}$, so disturbances in the common activity decay. The second equation retains any angle set by the initial state.

<!-- pedagogy-paragraph: p57 sha256 57ff19526b7c306c03f76b4e72fc305697ab28fffa0cffc8dca07f6d59e705c9 -->
p57, lines 57-57; prose; priority: unchanged; previous: p55; next: p59

> Increasing $a$ shortens the recovery time $1/a$ for the common activity disturbance. It does not correct the angle error, because $\dot\theta$ is still zero. At fixed rate disturbance, a larger tuning slope $k$ gives a smaller decoded angle change through division by $2k$. Changing $k$ in an actual circuit may also change its dynamics.

<!-- pedagogy-paragraph: p59 sha256 06c0ab40d5067e29fce3f655566f6d80cb85bdb6f8ed3aff39027b89c913cfa9 -->
p59, lines 59-59; prose; priority: unchanged; previous: p57; next: p61

> At $\theta=5$ degrees, the rates are $(50,30)$. Compare two disturbances from this same state:

<!-- pedagogy-paragraph: p61 sha256 d029c2fdcefcbded0f314865d14dbf0ee2633db997ba41fef1a0ce8c04f669fe -->
p61, lines 61-61; list_item; priority: unchanged; previous: p59; next: p62

> A disturbance of $(+3,+3)$ changes the rates to $(53,33)$. It creates $x=3$ but leaves the represented angle at 5 degrees. The restoring dynamics return to $(50,30)$.

<!-- pedagogy-paragraph: p62 sha256 cce475b6a0e5add615d31a12e691b5520ad7a708eb5d7d6930c24f9d300bdf4d -->
p62, lines 62-62; list_item; priority: unchanged; previous: p61; next: p64

> A disturbance of $(+3,-3)$ gives $(53,27)$, with $x=0$ and angle $26/(2\times2)=6.5$ degrees. This state lies on the fixed-point line, so there is no restoring response.

<!-- pedagogy-paragraph: p64 sha256 2e8a408287bff5b7f0a4a58bad63ef38ed7dc21e0a5935be5b5c783b2d31764e -->
p64, lines 64-64; prose; priority: unchanged; previous: p62; next: p66

> [In the second case, the circuit remains coherent while holding the wrong angle.]{.key-statement}

<!-- pedagogy-paragraph: p66 sha256 7c4cd0b619c9f0f950d5a8aa62af5bfa455079ea85d5ed0dbbaae3878ce84579 -->
p66, lines 66-70; prose; priority: unchanged; previous: p64; next: p74

> <!-- vale ai-tells.CataphoricForecasting = NO --> <!-- vale ai-tells.StrawmanContrast = NO --> The two changes occupy different directions in the activity plane. The solid arrow in the figure is the restoring motion produced by the model. The dashed arrow shows the imposed disturbance along the fixed-point line, rather than a deterministic restoring flow. <!-- vale ai-tells.StrawmanContrast = YES --> <!-- vale ai-tells.CataphoricForecasting = YES -->

<!-- pedagogy-paragraph: p74 sha256 dcefec6c9b28ce48fcbeb6e9c88374afdbf41de560868bdd366287407602911f -->
p74, lines 74-74; prose; priority: unchanged; previous: p66; next: p76

> In a larger network, the lasting change depends on its connection weights and cannot always be found by an ordinary perpendicular projection. The [network calculation](ch-memory-dynamics.html#sec-memory-linearization) derives the correct projection from the network's linearized dynamics.

<!-- pedagogy-paragraph: p76 sha256 aac32651b10f567c461b9b4f255d6fb1fa6859b5368d8bd9a51af920ab21cf23 -->
p76, lines 76-76; prose; priority: unchanged; previous: p74; next: p80

> </div>


Claim-bearing content: figure

Claims to check:

- Claim c1, line 17: "[A [**fixed point**]{.definition-term custom-style="Definition Term"} is a state where the deterministic rate of change is zero.]{.definition-explanation} It is stable in a direction if a small disturbance in that direction decays." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c2, line 19: "A ring can represent a periodic coordinate such as heading.[^f-memory]" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c3, line 23: "<div class="publisher-worked-calculation publisher-fold-always">" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c4, line 27: "Let $b=40$ spikes per second and let $k=2$ spikes per second per degree." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c5, line 31: "$$ r_1=b+k\theta,\qquad r_2=b-k\theta. $$" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c6, line 35: "The fixed points lie on the line $r_1+r_2=2b$." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c7, line 35: "Restrict attention to angles where both rates remain positive." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c8, line 37: "$$ x=\frac{r_1+r_2}{2}-b, \qquad \theta=\frac{r_1-r_2}{2k}. $$" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c9, line 45: "$$ \dot r_1=-a x,\qquad \dot r_2=-a x, $$" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c10, line 49: "where $a>0$ has units inverse seconds." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c11, line 51: "$$ \dot x=-a x,\qquad \dot\theta=0. $$" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c12, line 57: "Increasing $a$ shortens the recovery time $1/a$ for the common activity disturbance." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c13, line 59: "At $\theta=5$ degrees, the rates are $(50,30)$." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c14, line 61: "A disturbance of $(+3,+3)$ changes the rates to $(53,33)$." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c15, line 61: "It creates $x=3$ but leaves the represented angle at 5 degrees." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c16, line 62: "A disturbance of $(+3,-3)$ gives $(53,27)$, with $x=0$ and angle $26/(2\times2)=6.5$ degrees." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c17, line 64: "[In the second case, the circuit remains coherent while holding the wrong angle.]{.key-statement}" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c18, line 72: "Caption: A common activity disturbance returns to the initial angle, while an along-line disturbance persists as a changed angle. The solid arrow is deterministic recovery. The dashed arrow is an imposed disturbance. This is the guide's two-activity construction, not experimental data. Alt: Two a..." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c19, line 74: "In a larger network, the lasting change depends on its connection weights and cannot always be found by an ordinary perpendicular projection." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]

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

Location: line 78, anchor `sec:FOUNDATIONS-DIFFUSION`

First content kind: `prose`

Opening passage line: 80
Closing passage line: 175

Paragraphs in source order (complete `PARAGRAPH_REVIEW.json`):

<!-- pedagogy-paragraph: p80 sha256 c641bc0682485aa38af4ae56cb5b8597cb44df0325a008458a186892be9667f5 -->
p80, lines 80-82; prose; priority: unchanged; previous: p76; next: p86

> <!-- vale ai-tells.ContrastiveFormulas = NO --> Each extra or missing spike changes synaptic input. After the circuit has corrected the disturbances it can remove, a small change in the represented angle may remain. Repeating this process makes trials that began at the same angle gradually spread apart. We first model these lasting changes as independent, with no preferred direction and a constant variance per unit time. These are assumptions about the surviving changes, not about complete spike trains. <!-- vale ai-tells.ContrastiveFormulas = YES -->

<!-- pedagogy-paragraph: p86 sha256 b5f78c1a2441679842ce28a9d4c91d05cb56f367c938d33f9e62a06869a986c8 -->
p86, lines 86-86; prose; priority: unchanged; previous: p80; next: p88

> Divide time into intervals of length $\Delta t$. Let $\xi_j$ be the change in the represented coordinate during interval $j$. The calculation assumes:

<!-- pedagogy-paragraph: p88 sha256 303dbbc942443eae889b928b14bea0fc8be29c932b399917a322cab988935399 -->
p88, lines 88-88; list_item; priority: unchanged; previous: p86; next: p89

> Increments are independent.

<!-- pedagogy-paragraph: p89 sha256 470aed20aad4a5e1f3b854ca125c6f8a768ef5b1b66ee8551dda053cb2e11757 -->
p89, lines 89-89; list_item; priority: unchanged; previous: p88; next: p90

> Each increment has mean zero.

<!-- pedagogy-paragraph: p90 sha256 e9e4bde6c506e4d1381f0072bad57428e583742255bf336af8e108ead4b2b98f -->
p90, lines 90-90; list_item; priority: unchanged; previous: p89; next: p92

> Each increment has variance $2D\Delta t$, where $D$ has units coordinate squared per time.

<!-- pedagogy-paragraph: p92 sha256 2c3a77659cd35740e564899700b353c5faf042d9e981bc2b4edb067a7739317d -->
p92, lines 92-92; prose; priority: unchanged; previous: p90; next: p102

> After $n$ intervals,

<!-- pedagogy-paragraph: p102 sha256 ca955cdec98cc4700184426053ffe8d3d701bba21194c29ef9b7e8b85708a1f0 -->
p102, lines 102-102; prose; priority: unchanged; previous: p92; next: p104

> Writing $t=n\Delta t$ gives linear variance growth $2Dt$. [To describe this limit with a continuous path, use [**Brownian motion**]{.definition-term custom-style="Definition Term"} $W(t)$. It starts at zero, has continuous paths and independent Gaussian increments with mean zero, and satisfies $\operatorname{Var}[W(t)-W(s)]=t-s$ for $t\geq s$.]{.definition-explanation} It describes the limit of many small, suitably independent fluctuations. A physical network need only approach this description over the time and noise scales relevant to the calculation.

<!-- pedagogy-paragraph: p104 sha256 912f1cca24e717e78cd516efd420af678ee5dfb0c0bb7d11144cd4ad8839b3f8 -->
p104, lines 104-104; prose; priority: unchanged; previous: p102; next: p114

> In this continuous diffusion approximation,

<!-- pedagogy-paragraph: p114 sha256 e4bd9ad5a0394ee83c0e175f171ede5353dc1e8d3c7b69be9d3f9a1cee7f5121 -->
p114, lines 114-114; prose; priority: unchanged; previous: p104; next: p120

> [The **diffusion coefficient** $D$ measures half the rate at which the variance of the stored angle grows.]{.definition-explanation} With independent, zero-mean increments of constant variance per unit time,

<!-- pedagogy-paragraph: p120 sha256 ae867915557455dea873a6098622e5a62b4bf6f8060f0fc640f479a9329db809 -->
p120, lines 120-122; prose; priority: unchanged; previous: p114; next: p124

> <!-- vale ai-tells.FillerIntensifier = NO --> Here $D$ has units degrees squared per second when $\theta$ is in degrees. More frequent retained disturbances, or larger ones at the same frequency, increase $D$. At a fixed delay, doubling $D$ doubles error variance and multiplies its standard deviation by $\sqrt{2}$. [A single memory trajectory can turn back even while the spread across trials grows.]{.key-statement} The [network calculation](ch-memory-dynamics.html#sec-memory-diffusion) obtains $D$ from the spike variability and the lasting effect of each cell's disturbance. <!-- vale ai-tells.FillerIntensifier = YES -->

<!-- pedagogy-paragraph: p124 sha256 6d40d46edfa0cfe0417336be6451dd3e8b813f2e4338938d278bfec982c08416 -->
p124, lines 124-124; prose; priority: unchanged; previous: p120; next: p126

> The mean squared displacement, or MSD, is the expected squared change across a lag. In the zero-mean diffusion just defined, MSD is $2Dt$. [A [**root mean squared displacement**]{.definition-term custom-style="Definition Term"} is its square root, $\sqrt{2Dt}$, and has the same units as the represented coordinate.]{.definition-explanation} In several dimensions, adding independent coordinate contributions gives an overall MSD of $2dDt$ only when each of the $d$ coordinates has the same diffusion coefficient. A paper that defines its diffusion parameter as the entire two-dimensional MSD slope uses a different convention.

<!-- pedagogy-paragraph: p126 sha256 8e19185c156210567a045f638d7d3d1269765f40e35d9cff42cebc457898c408 -->
p126, lines 126-126; prose; priority: unchanged; previous: p124; next: p128

> <div class="publisher-worked-calculation publisher-fold-always">

<!-- pedagogy-paragraph: p128 sha256 21fbcefc06de9f037ced501b987387ba259bc1823d6430862f48d7ea8aea7832 -->
p128, lines 128-128; prose; priority: unchanged; previous: p126; next: p130

> [**Example: why the noise grows slower than a fixed bias**]{#sec-foundations-diffusion-example}

<!-- pedagogy-paragraph: p130 sha256 6f7c15dbc1e1419c6d3aaed6cf35574c64ba357e5fd72f8fe4d54ae610128af9 -->
p130, lines 130-132; prose; priority: unchanged; previous: p128; next: p134

> <!-- vale ai-tells.NounString = NO --> Take an illustrative angular diffusion coefficient $D=0.02$ degrees squared per second. At 0.35 s its variance is $0.014$ degrees squared and its root mean squared displacement is 0.118 degrees, or about 7.10 arcminutes. At 1 s the root mean squared displacement is 0.20 degrees. <!-- vale ai-tells.NounString = YES -->

<!-- pedagogy-paragraph: p134 sha256 b65818f05ab22cc9b82ca82b30056d679efa0cda9041acec6e6b2a8f8474645d -->
p134, lines 134-134; prose; priority: unchanged; previous: p130; next: p142

> If there is also a constant bias velocity $v=0.10$ degrees per second, then

<!-- pedagogy-paragraph: p142 sha256 17a1fcad042c40d4723e4b6cb4196285ea579fda6e767735752f4a556c1bd63e -->
p142, lines 142-142; prose; priority: unchanged; previous: p134; next: p144

> The deterministic and random contributions are equal at $t=2D/v^2=4$ seconds. Their equal contributions there are each $0.16$ degrees squared. At longer times the bias dominates this unbounded model even though it was small over a short observation. A theory of random diffusion must account separately for [**systematic drift**]{.definition-term custom-style="Definition Term"}, a nonzero mean velocity.

<!-- pedagogy-paragraph: p144 sha256 03d74fd5b23faf7dabfc1285d439637939ceacd9336ef9ceb4915b645e0e9abb -->
p144, lines 144-144; prose; priority: unchanged; previous: p142; next: p146

> Sample paths show the irregular motion. Exact displacement scales show how its spread differs from a fixed bias.

<!-- pedagogy-paragraph: p146 sha256 2c643bd85d3e8933fd7127e586cd0d302d74dcd69d691fc3921ef217cc019e39 -->
p146, lines 146-146; prose; priority: unchanged; previous: p144; next: p150

> <div class="figure-scroll">

<!-- pedagogy-paragraph: p150 sha256 aac32651b10f567c461b9b4f255d6fb1fa6859b5368d8bd9a51af920ab21cf23 -->
p150, lines 150-150; prose; priority: unchanged; previous: p146; next: p152

> </div>

<!-- pedagogy-paragraph: p152 sha256 afcd2f2744212b269f6209e7cf4b2356d01791aee6bfd80651a25e6c8ee3a0e1 -->
p152, lines 152-152; prose; priority: unchanged; previous: p150; next: p154

> A constant bias grows linearly, so it eventually exceeds the square root growth of the random displacement scale. See [Gaussian displacement density, SI Eq. S30, p. 7](../papers/burak-fiete-2012-persistent-activity-si.pdf#page=7).

<!-- pedagogy-paragraph: p154 sha256 aac32651b10f567c461b9b4f255d6fb1fa6859b5368d8bd9a51af920ab21cf23 -->
p154, lines 154-154; prose; priority: unchanged; previous: p152; next: p156

> </div>

<!-- pedagogy-paragraph: p156 sha256 58bb55c0fa621284da6ac2cad284981e7c48d2bc06c0fa2934b0d6ff3d9c9cce -->
p156, lines 156-158; prose; priority: unchanged; previous: p154; next: p162

> <!-- vale ai-tells.FormalTransitions = NO --> A later memory state contains earlier accumulated errors as well as new ones. Observing it twice therefore does not give two independent copies of the original memory. The covariance calculation below quantifies the shared history used in the readout chapter. <!-- vale ai-tells.FormalTransitions = YES -->

<!-- pedagogy-paragraph: p162 sha256 d9d175c58f25bbeb55b5a695db7dcf469084c56df1b1eef3ab6d1ad40e73b4b6 -->
p162, lines 162-162; prose; priority: unchanged; previous: p156; next: p171

> Two times along a Brownian path are correlated even though its increments are independent. For $0\leq s\leq t$, write $W(t)=W(s)+[W(t)-W(s)]$. The bracketed increment is independent of $W(s)$ and has mean zero, giving

<!-- pedagogy-paragraph: p171 sha256 1e37ab0e3032ae94247421633fa7c4675ca56252f66c58558321d2d4e7582ccf -->
p171, lines 171-171; prose; priority: unchanged; previous: p162; next: p175

> The same argument gives covariance $2D\min(s,t)$ for a diffusing coordinate started at a fixed value. This identity is the intermediate step needed to compute the error from averaging a memory that moves during readout. It also helps explain why smoothing a diffusive input is different from smoothing a stationary noise source.

<!-- pedagogy-paragraph: p175 sha256 71217eeb9fda7077597664f1fded61b391152ccfc7ef26ee20da6830b1caee70 -->
p175, lines 175-177; prose; priority: unchanged; previous: p171; next: p181

> <!-- vale ai-tells.FormalTransitions = NO --> A finite range, a periodic coordinate, external feedback, or a position-dependent diffusion coefficient changes long-time behavior. For example, ordinary squared angular distance on a ring cannot keep growing linearly forever. The basic $2Dt$ result is local or unbounded unless those conditions are treated separately. <!-- vale ai-tells.FormalTransitions = YES -->


Claim-bearing content: figure

Claims to check:

- Claim c1, line 80: "After the circuit has corrected the disturbances it can remove, a small change in the represented angle may remain." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c2, line 94: "$$ \theta_n-\theta_0=\sum_{j=1}^{n}\xi_j, \qquad \operatorname{Var}(\theta_n-\theta_0) =\sum_{j=1}^{n}\operatorname{Var}(\xi_j) =2Dn\Delta t. $$" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c3, line 102: "It starts at zero, has continuous paths and independent Gaussian increments with mean zero, and satisfies $\operatorname{Var}[W(t)-W(s)]=t-s$ for $t\geq s$.]{.definition-explanation} It describes the limit of many small, suitably independent fluctuations." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c4, line 102: "A physical network need only approach this description over the time and noise scales relevant to the calculation." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c5, line 106: "$$ \theta(t)=\theta(0)+\sqrt{2D}\,W(t), \qquad \mathbb E[(\theta(t)-\theta(0))^2]=2Dt. $$" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c6, line 116: "$$ \operatorname{Var}[\theta(t)-\theta(0)]=2Dt. $$" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c7, line 124: "[A [**root mean squared displacement**]{.definition-term custom-style="Definition Term"} is its square root, $\sqrt{2Dt}$, and has the same units as the represented coordinate.]{.definition-explanation} In several dimensions, adding independent coordinate contributions gives an overall MSD of $2d..." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c8, line 126: "<div class="publisher-worked-calculation publisher-fold-always">" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c9, line 130: "<!-- vale ai-tells.NounString = NO --> Take an illustrative angular diffusion coefficient $D=0.02$ degrees squared per second." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c10, line 130: "At 0.35 s its variance is $0.014$ degrees squared and its root mean squared displacement is 0.118 degrees, or about 7.10 arcminutes." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c11, line 130: "At 1 s the root mean squared displacement is 0.20 degrees. <!-- vale ai-tells.NounString = YES -->" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c12, line 134: "If there is also a constant bias velocity $v=0.10$ degrees per second, then" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c13, line 136: "$$ \theta(t)-\theta(0)=vt+\sqrt{2D}\,W(t), \qquad \operatorname{MSD}(t)=v^2t^2+2Dt. $$" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c14, line 142: "The deterministic and random contributions are equal at $t=2D/v^2=4$ seconds." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c15, line 142: "Their equal contributions there are each $0.16$ degrees squared." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c16, line 142: "At longer times the bias dominates this unbounded model even though it was small over a short observation." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c17, line 142: "A theory of random diffusion must account separately for [**systematic drift**]{.definition-term custom-style="Definition Term"}, a nonzero mean velocity." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c18, line 148: "Caption: Simulated Brownian teaching paths and analytic displacement scales for $D=0.02$ degrees squared per second and $v=0.10$ degrees per second. The upper paths have zero drift and start at zero. The dashed envelope is the exact root mean squared displacement, not a boundary on individual pat..." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c19, line 152: "S30, p. 7](../papers/burak-fiete-2012-persistent-activity-si.pdf#page=7)." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c20, line 175: "For example, ordinary squared angular distance on a ring cannot keep growing linearly forever." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]

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

Location: line 179, anchor `sec:FOUNDATIONS-RANDOMNESS`

First content kind: `prose`

Opening passage line: 181
Closing passage line: 205

Paragraphs in source order (complete `PARAGRAPH_REVIEW.json`):

<!-- pedagogy-paragraph: p181 sha256 11a596f759327f7f1b8438c00bf80e55c9e6146ce6064848690130fe26d070cd -->
p181, lines 181-181; prose; priority: unchanged; previous: p175; next: p183

> The memory and eye papers study fluctuations that accumulate as time passes. The place-field paper instead starts with a random function of physical position. Once drawn for a cell and an environment, that function is fixed while the animal moves through the map. Revisiting a place evaluates the same expected-rate function, although the actual spikes can still vary from visit to visit.

<!-- pedagogy-paragraph: p183 sha256 e4049bef50c71c4684af6383a27a96b3df023b392a6a13d50c10ad422748eef4 -->
p183, lines 183-185; prose; priority: unchanged; previous: p181; next: p187

> <!-- vale ai-tells.FormalTransitions = NO --> These two kinds of randomness can occur together. A circuit may maintain a position estimate with time-dependent noise, while downstream cells respond to position through irregular but repeatable tuning curves. [Observing irregular spatial maps does not tell us how fast the maintained position drifts. Conversely, finding diffusion of a stored value does not determine the shapes of individual place fields.]{.key-statement} The following chapters develop the dynamical calculation first, then the experiment that tests a possible consequence, and finally the spatial statistics.[^f-place] <!-- vale ai-tells.FormalTransitions = YES -->

<!-- pedagogy-paragraph: p187 sha256 cd9ee58f049bbdb25943a23aa2fdd4c9bcd57daad93f2ec319fda1d62b0c1c4b -->
p187, lines 187-189; prose; priority: unchanged; previous: p183; next: p191

> <!-- vale ai-tells.CataphoricForecasting = NO --> The three questions can now be placed beside the kind of variation each paper studies. <!-- vale ai-tells.CataphoricForecasting = YES -->

<!-- pedagogy-paragraph: p191 sha256 2c643bd85d3e8933fd7127e586cd0d302d74dcd69d691fc3921ef217cc019e39 -->
p191, lines 191-191; prose; priority: unchanged; previous: p187; next: p195

> <div class="figure-scroll">

<!-- pedagogy-paragraph: p195 sha256 aac32651b10f567c461b9b4f255d6fb1fa6859b5368d8bd9a51af920ab21cf23 -->
p195, lines 195-195; prose; priority: unchanged; previous: p191; next: p197

> </div>

<!-- pedagogy-paragraph: p197 sha256 30802284de9326a7516e7b173e7e6b093aebaf699da69c3fec293ee1bfd26b04 -->
p197, lines 197-197; prose; priority: unchanged; previous: p195; next: p199

> The rows compare different questions. They do not establish one circuit connecting all three papers.

<!-- pedagogy-paragraph: p199 sha256 c434e91454241a31e310a239ac3a093d91ab1fcd15b7ac3b333458ba63f49376 -->
p199, lines 199-199; prose; priority: unchanged; previous: p197; next: p201

> <!-- vale ai-tells.EmDashUsage = NO -->

<!-- pedagogy-paragraph: p201 sha256 6e36e79bce1447ac7eddc2fb19787ace984308e97fbb90fe3fbe309f14b460ff -->
p201, lines 201-201; prose; priority: unchanged; previous: p199; next: p203

> <!-- vale ai-tells.EmDashUsage = YES -->

<!-- pedagogy-paragraph: p203 sha256 c434e91454241a31e310a239ac3a093d91ab1fcd15b7ac3b333458ba63f49376 -->
p203, lines 203-203; prose; priority: unchanged; previous: p201; next: p205

> <!-- vale ai-tells.EmDashUsage = NO -->

<!-- pedagogy-paragraph: p205 sha256 6e36e79bce1447ac7eddc2fb19787ace984308e97fbb90fe3fbe309f14b460ff -->
p205, lines 205-205; prose; priority: unchanged; previous: p203; next: none

> <!-- vale ai-tells.EmDashUsage = YES -->


Claim-bearing content: figure

Claims to check:

- Claim c1, line 181: "Once drawn for a cell and an environment, that function is fixed while the animal moves through the map." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c2, line 183: "Conversely, finding diffusion of a stored value does not determine the shapes of individual place fields.]{.key-statement} The following chapters develop the dynamical calculation first, then the experiment that tests a possible consequence, and finally the spatial statistics.[^f-place] <!-- vale..." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c3, line 193: "Caption: Memory loss and eye drift concern changes over time. Place-field statistics concern variation across a fixed spatial map. The eye pathway shows the proposed changing-command mechanism. Original guide schematic based on the three papers, with illustrative traces rather than recorded data...." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]

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

Purpose: Burak and Fiete model a group of interacting neurons that retains a continuous value after an input ends. This chapter follows spikes through their effects at synapses and back into firing, then derives how random spike timing displaces the stored value.

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

<!-- pedagogy-paragraph: p3 sha256 8b9397304e9152c4e410e51e9a0d38d07a0eda61691fb277a59f5c898529754b -->
p3, lines 3-3; prose; priority: unchanged; previous: none; next: p5

> [A network can keep firing after a stimulus disappears and still lose the value that the stimulus supplied.]{.key-statement} Burak and Fiete study this distinction in a network whose stable activity patterns form a continuous set.[^p1-model]

<!-- pedagogy-paragraph: p5 sha256 6c20e92e5d70dd5f7e5f408841489b34e3802a8dcc03c26066a0778bda5e1e15 -->
p5, lines 5-5; prose; priority: unchanged; previous: p3; next: p7

> To calculate the loss of accuracy, we first describe how spikes renew synaptic activity as it decays. We then follow a small disturbance through the circuit's return toward a stable pattern and identify the change in stored value that remains. Adding these lasting random changes gives a local rate of spreading. When connections have equal weights in both directions, we can express that rate using the cells' tuning curves and check its meaning in a two-cell example. The following chapter extends this local prediction to longer delays.

<!-- pedagogy-paragraph: p7 sha256 612bb399a917947736f70e4ed32bc1debe8bdc75c49c2abcebccff65cde3bdd9 -->
p7, lines 7-7; prose; priority: unchanged; previous: p5; next: p9

> Paper and Supporting Information (SI) links open the cited PDF page, near the passage where the viewer supports it. Use the equation, figure, or paragraph label to find the passage. The PDFs have no numbered text lines.

<!-- pedagogy-paragraph: p9 sha256 8758a0c68055cd1d7a4b67d2144569b217a893ecb3046e52459d2db85a7e3a5a -->
p9, lines 9-9; prose; priority: unchanged; previous: p7; next: p13

> The memory coordinate is $\theta$. Its initial value is $\Theta$. A bar denotes a noise free steady state, so $\bar r_i(\theta)$ is neuron $i$'s steady firing rate at memory value $\theta$. The common synaptic time constant is $\tau$. A one dimensional diffusion coefficient $D$ has units of memory coordinate squared per time, with the convention $\operatorname{Var}[\theta(t)-\Theta]=2Dt$ when $D$ is constant and boundaries do not matter.


Claim-bearing content: none

Claims to check:

- Claim c1, line 3: "[A network can keep firing after a stimulus disappears and still lose the value that the stimulus supplied.]{.key-statement} Burak and Fiete study this distinction in a network whose stable activity patterns form a continuous set.[^p1-model]" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
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

Location: line 11, anchor `sec:MEMORY-SPIKES`

First content kind: `prose`

Opening passage line: 13
Closing passage line: 103

Paragraphs in source order (complete `PARAGRAPH_REVIEW.json`):

<!-- pedagogy-paragraph: p13 sha256 84f9d03bf675e4483b4ace34225617e67a75d0211fd4d0316e64656c1e9d3eb3 -->
p13, lines 13-13; prose; priority: unchanged; previous: p9; next: p15

> **Neural mechanism.** How can brief spikes maintain a state for much longer than the duration of a spike? In this model, each spike leaves a synaptic activation that decays gradually. [Incoming activations determine new firing rates. The resulting spikes renew those activations. This feedback can support activity after the external stimulus has ended.]{.key-statement}

<!-- pedagogy-paragraph: p15 sha256 798d2642412ad274eccad2b0c6faa2b19cee372d8374b690095ffcb895b74676 -->
p15, lines 15-15; prose; priority: unchanged; previous: p13; next: p17

> The model assumes fixed connection weights, constant biases, a common synaptic decay time, and independent Poisson spike counts conditional on the present rates. The connections are tuned to a continuous family of steady patterns. The Gaussian description below also assumes weak fluctuations in total input.

<!-- pedagogy-paragraph: p17 sha256 0e0618e483b9a778a506e7c824aee9e67f4037c2fb77519905143cbd1ae175b7 -->
p17, lines 17-17; prose; priority: unchanged; previous: p15; next: p23

> **Mathematical derivation.** To combine discrete events with continuous decay, a count process records the events and a decay equation records how their effects fade. Here $N_i(t)$ counts neuron $i$'s spikes up to time $t$. The activation $s_i$ tracks the decaying synaptic effect of those outgoing spikes on receiving cells. It rises by one at each spike and otherwise decays:

<!-- pedagogy-paragraph: p23 sha256 316268840047bfdefb5b2118549103e5d7a5c7201e67211f937617deb83eabcb -->
p23, lines 23-23; prose; priority: unchanged; previous: p17; next: p29

> Equivalently, if its spikes occur at times $t_i^\alpha$,

<!-- pedagogy-paragraph: p29 sha256 9006951dd37db6f4eb03d5ade741a8ed42bfc433bf08dcbaa1d26dca3a1a22e3 -->
p29, lines 29-29; prose; priority: unchanged; previous: p23; next: p31

> after initial transients. Here $s_i$ is dimensionless in the convention that each spike adds one unit.

<!-- pedagogy-paragraph: p31 sha256 7eac28f467bb547ebcf147a697cbc1044361e75128de9e099d3ddeec6a0803df -->
p31, lines 31-31; prose; priority: unchanged; previous: p29; next: p33

> For five illustrative spike times, the plot shows the events and the activation they leave behind.

<!-- pedagogy-paragraph: p33 sha256 2c643bd85d3e8933fd7127e586cd0d302d74dcd69d691fc3921ef217cc019e39 -->
p33, lines 33-33; prose; priority: unchanged; previous: p31; next: p37

> <div class="figure-scroll">

<!-- pedagogy-paragraph: p37 sha256 aac32651b10f567c461b9b4f255d6fb1fa6859b5368d8bd9a51af920ab21cf23 -->
p37, lines 37-37; prose; priority: unchanged; previous: p33; next: p39

> </div>

<!-- pedagogy-paragraph: p39 sha256 7bcebc101fc3d68752aaaad0bd35d63537e6c9387555337d9cc1d87510883b8d -->
p39, lines 39-39; prose; priority: unchanged; previous: p37; next: p41

> The activation retains a decaying contribution from earlier spikes, so a spike train and its activation trace are different objects.

<!-- pedagogy-paragraph: p41 sha256 f185d2789a819913e453567a284f7f8ff493b18cb72d9a292c313a6546983289 -->
p41, lines 41-41; prose; priority: unchanged; previous: p39; next: p48

> The rate $r_i$ has units of spikes per second. The summed input and the firing rule are

<!-- pedagogy-paragraph: p48 sha256 28b7f192a0b94f9f7c0c91af7ddec7b2c325c6c71d3465287ff18740d1484137 -->
p48, lines 48-52; prose; priority: unchanged; previous: p41; next: p54

> <!-- vale ai-tells.EmDashUsage = NO --> <!-- vale ai-tells.FormalTransitions = NO --> The fixed weights $W_{ij}$ say how neuron $j$ affects neuron $i$, and $b_i$ is a constant input. [The [**neural transfer function**]{.definition-term custom-style="Definition Term"} $\phi$ converts total input into a nonnegative firing rate.]{.definition-explanation} For example, increasing input might increase firing linearly over some input range, or exponentially. The paper allows general connectivity and transfer functions at first ([Model, Eqs. 7–9, p. 5](../papers/burak-fiete-2012-persistent-activity.pdf#page=5&zoom=125,0,372)).[^p1-model] <!-- vale ai-tells.FormalTransitions = YES --> <!-- vale ai-tells.EmDashUsage = YES -->

<!-- pedagogy-paragraph: p54 sha256 9521cfb65d9dce223117daf19bd92321dce1d8886a492f85540565589eeb5d57 -->
p54, lines 54-56; prose; priority: unchanged; previous: p48; next: p58

> <!-- vale ai-tells.FormalTransitions = NO --> A spike from cell $j$ raises $s_j$ by one and therefore changes the input to cell $i$ by $W_{ij}$. That contribution then decays over time $\tau$. For an increasing transfer function, a positive weight raises the receiving cell's rate and a negative weight lowers it. The resulting new spikes affect other cells in turn. Thus the weights set where a disturbance goes, the transfer function sets the rate response, and $\tau$ sets how long each synaptic contribution lasts. The input $g_i$ is in the model's input units. It is not specified as a measured membrane voltage. <!-- vale ai-tells.FormalTransitions = YES -->

<!-- pedagogy-paragraph: p58 sha256 f45834f1c9bf180a0a2fd7c0c35e87ed046ad06a118c91be07e994baf9857e46 -->
p58, lines 58-60; prose; priority: unchanged; previous: p54; next: p69

> <!-- vale ai-tells.FormalTransitions = NO --> Conditioned on the present rates, spike counts over a short interval $dt$ are independent Poisson variables. Thus <!-- vale ai-tells.FormalTransitions = YES -->

<!-- pedagogy-paragraph: p69 sha256 2d213217d67ac51d540f1da81d08b391967e49cb43712b3d9b80b46c48646890 -->
p69, lines 69-69; prose; priority: unchanged; previous: p58; next: p78

> The symbol $\delta_{ij}$ is one when $i=j$ and zero otherwise. Splitting the count into its mean and fluctuation gives

<!-- pedagogy-paragraph: p78 sha256 3eb9b922aa6f9d35a1c87491f74b1f4d0feee18d5d9823100af8909b2fd60035 -->
p78, lines 78-78; prose; priority: unchanged; previous: p69; next: p86

> This is still a jump process. [In the paper's [**weak fluctuation approximation**]{.definition-term custom-style="Definition Term"}, many individually small spike contributions produce only small changes in each neuron's total input. Their summed fluctuation can then be represented by Gaussian noise with the same leading mean and covariance:]{.definition-explanation}

<!-- pedagogy-paragraph: p86 sha256 c844900bf583de75a9179ccb7c363e44da4f5e4b64d845799e24976092813bcf -->
p86, lines 86-88; prose; priority: unchanged; previous: p78; next: p90

> <!-- vale ai-tells.EmDashUsage = NO --> where the $B_i$ are independent standard Brownian processes. The noise coefficient has units $\mathrm{s}^{-1/2}$, so its product with $dB_i$ is a dimensionless activation increment. The Gaussian approximation is for small fluctuations in total input. It does not require each single neuron's entire spike train to look like a Gaussian process ([SI Eqs. S2–S5, p. 2](../papers/burak-fiete-2012-persistent-activity-si.pdf#page=2&zoom=125,0,128)).[^p1-weak] <!-- vale ai-tells.EmDashUsage = YES -->

<!-- pedagogy-paragraph: p90 sha256 0fd899ed33da83f26442e618a5039413655cbc2e601728cacb87ab2f19ca7ad3 -->
p90, lines 90-92; prose; priority: unchanged; previous: p86; next: p94

> <!-- vale ai-tells.FormalTransitions = NO --> The supplement makes this limit concrete by replacing each population with $n$ equivalent neurons and dividing each connection weight by $n$. A summed input has a mean proportional to $n/n=1$, while its variance is proportional to $n/n^2=1/n$. Increasing population size therefore keeps the mean dynamics fixed and reduces input fluctuations. [For a ring network, a neuron's [**preferred angle**]{.definition-term custom-style="Definition Term"} is an angle where its tuning curve peaks.]{.definition-explanation} Increasing the density of equally spaced preferred angles and scaling weights as $1/N$ serves the same purpose. The paper's formulas give the leading terms in this large population limit, rather than exact finite network identities.[^p1-large] <!-- vale ai-tells.FormalTransitions = YES -->

<!-- pedagogy-paragraph: p94 sha256 4f6cb8f2d857da75dc2cee6f02cc0f1f23c8e6230c7c66e10abc8b7a8b33dd3f -->
p94, lines 94-94; prose; priority: unchanged; previous: p90; next: p103

> Setting noise to zero gives the deterministic rate dynamics $\dot{\mathbf s}=\mathbf F(\mathbf s)$. A continuous attractor is a family of fixed points satisfying

<!-- pedagogy-paragraph: p103 sha256 79c676fc0bbcd965af880e2126de67cb023f9e576a58735cbcf22be8bfd7518c -->
p103, lines 103-103; prose; priority: unchanged; previous: p94; next: p107

> **Interpretation.** In the noise free dynamics, recurrent firing balances synaptic decay at each fixed point. The network must be tuned to possess this family. An arbitrary recurrent network will generally have isolated fixed points rather than a whole line or ring of them.


Claim-bearing content: figure

Claims to check:

- Claim c1, line 35: "Caption: Each spike adds one activation unit, which then decays with a 50 ms time constant. Closely spaced spikes add to the activation left by earlier spikes. The five spike times are an illustrative input, and the activation is calculated exactly from the chapter equation. Alt: Five spike marks..." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c2, line 48: "The paper allows general connectivity and transfer functions at first ([Model, Eqs. 7–9, p. 5](../papers/burak-fiete-2012-persistent-activity.pdf#page=5&zoom=125,0,372)).[^p1-model] <!-- vale ai-tells.FormalTransitions = YES --> <!-- vale ai-tells.EmDashUsage = YES -->" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c3, line 71: "$$ ds_i=\left[-\frac{s_i}{\tau}+\phi(g_i)\right]dt+dM_i, \qquad E[dM_i]=0, \quad E[dM_i dM_j]=\delta_{ij}r_i\,dt. $$" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c4, line 78: "[In the paper's [**weak fluctuation approximation**]{.definition-term custom-style="Definition Term"}, many individually small spike contributions produce only small changes in each neuron's total input." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c5, line 86: "The noise coefficient has units $\mathrm{s}^{-1/2}$, so its product with $dB_i$ is a dimensionless activation increment." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c6, line 86: "The Gaussian approximation is for small fluctuations in total input." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c7, line 86: "S2–S5, p. 2](../papers/burak-fiete-2012-persistent-activity-si.pdf#page=2&zoom=125,0,128)).[^p1-weak] <!-- vale ai-tells.EmDashUsage = YES -->" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c8, line 90: "A summed input has a mean proportional to $n/n=1$, while its variance is proportional to $n/n^2=1/n$." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c9, line 90: "[For a ring network, a neuron's [**preferred angle**]{.definition-term custom-style="Definition Term"} is an angle where its tuning curve peaks.]{.definition-explanation} Increasing the density of equally spaced preferred angles and scaling weights as $1/N$ serves the same purpose." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c10, line 90: "The paper's formulas give the leading terms in this large population limit, rather than exact finite network identities.[^p1-large] <!-- vale ai-tells.FormalTransitions = YES -->" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c11, line 96: "$$ 0=-\frac{\bar s_i(\theta)}{\tau} +\phi[\bar g_i(\theta)], \qquad \bar s_i(\theta)=\tau\bar r_i(\theta). $$" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c12, line 103: "The network must be tuned to possess this family." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]

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

Location: line 105, anchor `sec:MEMORY-LINEARIZATION`

First content kind: `prose`

Opening passage line: 107
Closing passage line: 206

Paragraphs in source order (complete `PARAGRAPH_REVIEW.json`):

<!-- pedagogy-paragraph: p107 sha256 04166ad334077f6cc818e98cfcb98d0b59409ad95842445142dc33e13cbfe4ad -->
p107, lines 107-107; prose; priority: unchanged; previous: p103; next: p109

> **Neural mechanism.** A spike perturbs many aspects of a network's state. Most of those changes decay as the state returns to the attractor. [To calculate memory loss, we need the lasting change: the displacement to a different fixed point. We assume a smooth continuous family with one neutral memory direction, while all other local modes decay. The disturbance must be small enough that the first order response describes the return flow.]{.key-statement}

<!-- pedagogy-paragraph: p109 sha256 e7e596574028784a376666758d80b11535a2d7fbf4db3b526d039a0cc027faff -->
p109, lines 109-109; prose; priority: unchanged; previous: p107; next: p116

> **Mathematical derivation.** [A [**linearization**]{.definition-term custom-style="Definition Term"} keeps the terms proportional to a small perturbation and drops terms quadratic or higher in it.]{.definition-explanation} Here the network activation is $\mathbf s=\bar{\mathbf s}(\theta)+\delta\mathbf s$. Taylor expansion of the transfer function gives

<!-- pedagogy-paragraph: p116 sha256 93d563f6c3a7b382755160168f8f770008007dc071ce6cfb279b509adf2b5d34 -->
p116, lines 116-118; prose; priority: unchanged; previous: p109; next: p127

> <!-- vale ai-tells.FormalTransitions = NO --> The constant terms cancel because $\bar{\mathbf s}$ is a fixed point. Therefore <!-- vale ai-tells.FormalTransitions = YES -->

<!-- pedagogy-paragraph: p127 sha256 d7ebb275e853df3e3325fa2d46b421976ffcb73960bc72a8c240a3dbb1f3083c -->
p127, lines 127-127; prose; priority: unchanged; previous: p116; next: p129

> In this leading local calculation the noise strengths are evaluated at the fixed point. The entries of $K$ have units of inverse time.[^p1-projection]

<!-- pedagogy-paragraph: p129 sha256 82031746f4cc12d27c9b4ef131c6014207f3e9d4434e97fd29ec69d09a893646 -->
p129, lines 129-129; prose; priority: unchanged; previous: p127; next: p131

> The term $-\delta_{ij}/\tau$ removes a disturbance as synaptic activation fades. The term $\phi'(\bar g_i)W_{ij}$ describes recurrent renewal: the connection converts a change in cell $j$'s activation into input to cell $i$, and the local slope of the transfer function converts that input into a rate change. A steeper slope makes this response stronger. [Whether a disturbance decays, persists, or grows depends on the combined feedback through the whole network.]{.key-statement} A stronger connection alone does not establish better memory.

<!-- pedagogy-paragraph: p131 sha256 304dd8dac46d7f3b9e61f07b014d18878e606a90f911a07cc0b6c13fef5d7479 -->
p131, lines 131-131; prose; priority: unchanged; previous: p129; next: p138

> Moving a little along the fixed point family changes the activation by

<!-- pedagogy-paragraph: p138 sha256 94f3ecaae1c4e3b7ccf9f8dbab75022e08dfc595dc1f5a6039b71bf06fa969c5 -->
p138, lines 138-138; prose; priority: unchanged; previous: p131; next: p144

> Differentiate the fixed point equation $\mathbf F[\bar{\mathbf s}(\theta)]=0$. The chain rule gives

<!-- pedagogy-paragraph: p144 sha256 83df2fc5afb00397c2fdd9632bee845b2b41c1b4d8cb385d00561c973adb5424 -->
p144, lines 144-146; prose; priority: unchanged; previous: p138; next: p148

> <!-- vale ai-tells.FormalTransitions = NO --> [Thus $\mathbf u$ is a [**right zero eigenvector**]{.definition-term custom-style="Definition Term"}: a state direction that the linear dynamics neither restores nor amplifies.]{.definition-explanation} It is the tangent to the attractor. The other modes must decay for this local family to be attracting. <!-- vale ai-tells.FormalTransitions = YES -->

<!-- pedagogy-paragraph: p148 sha256 7056f80a1f7f3fb138e9f30730975c61ab17d1c64ba13a50c8d1156acdb36874 -->
p148, lines 148-150; prose; priority: unchanged; previous: p144; next: p157

> <!-- vale ai-tells.NegatedObject = NO --> [We also need a [**left zero eigenvector**]{.definition-term custom-style="Definition Term"}, a vector $\mathbf v$ satisfying]{.definition-explanation} <!-- vale ai-tells.NegatedObject = YES -->

<!-- pedagogy-paragraph: p157 sha256 c965fdaee89b0af4ec01f463b596c3e373caf60fb1cca82e5734731220db6503 -->
p157, lines 157-157; prose; priority: unchanged; previous: p148; next: p163

> Its purpose is to extract the lasting memory displacement from a general perturbation. The normalization makes $\mathbf v^T(\mathbf u\,\delta\theta)=\delta\theta$. If a stable mode $\mathbf z$ satisfies $K\mathbf z=\lambda\mathbf z$ with $\lambda\ne0$, then

<!-- pedagogy-paragraph: p163 sha256 8d5491cf1dae59b39784e70eafd8d0f1d69fca33c4e65d8b98ac91a2b32f16f5 -->
p163, lines 163-167; prose; priority: unchanged; previous: p157; next: p174

> <!-- vale ai-tells.EmDashUsage = NO --> <!-- vale ai-tells.FormalTransitions = NO --> so $\mathbf v^T\mathbf z=0$. The left vector discards every decaying mode ([SI Eqs. S12–S13, p. 3](../papers/burak-fiete-2012-persistent-activity-si.pdf#page=3&zoom=125,0,409)). Consequently the surviving part of a small perturbation is <!-- vale ai-tells.FormalTransitions = YES --> <!-- vale ai-tells.EmDashUsage = YES -->

<!-- pedagogy-paragraph: p174 sha256 71645943edb378cac29603b00c128e0eff8d642f6956a0cb9306ec28aaa5f5c4 -->
p174, lines 174-174; prose; priority: unchanged; previous: p163; next: p176

> **Interpretation.** This generally differs from a perpendicular geometric projection. Decay can be tilted relative to the tangent. Even symmetric synaptic weights do not usually make $K$ symmetric, because $\phi'(\bar g_i)$ multiplies different rows by different amounts.

<!-- pedagogy-paragraph: p176 sha256 8e19185c156210567a045f638d7d3d1269765f40e35d9cff42cebc457898c408 -->
p176, lines 176-176; prose; priority: unchanged; previous: p174; next: p178

> <div class="publisher-worked-calculation publisher-fold-always">

<!-- pedagogy-paragraph: p178 sha256 2210c0e5171fed9aa1a84252a0649f4d9da4e9c34a3d76752952bcd9690682bd -->
p178, lines 178-178; prose; priority: unchanged; previous: p176; next: p180

> **Example: a disturbance that slides while it decays.**

<!-- pedagogy-paragraph: p180 sha256 e532d1502e3bb94fc6a1e885bdcaf05890cd49304b705fe4bebdd95e6175b12e -->
p180, lines 180-180; prose; priority: unchanged; previous: p178; next: p186

> To see the distinction without a neural simulation, consider the local system

<!-- pedagogy-paragraph: p186 sha256 b1514ac4ed7c28962acf3fba4e3240161c5afae143fc7f1e606483895133eb33 -->
p186, lines 186-186; prose; priority: unchanged; previous: p180; next: p192

> Every point with $y=0$ is fixed. Starting from $(x_0,y_0)$ gives $y(t)=y_0e^{-\lambda t}$ and

<!-- pedagogy-paragraph: p192 sha256 f6c0acf2afc898e43ffe406a85cfab15859f44f7a811d2cae00244b9c49d322a -->
p192, lines 192-196; prose; priority: unchanged; previous: p186; next: p198

> <!-- vale ai-tells.AnthropomorphicCognition = NO --> <!-- vale ai-tells.ContrastiveFormulas = NO --> Here $\mathbf u=(1,0)^T$ and $\mathbf v=(1,a/\lambda)^T$. A vertical perturbation changes the final memory whenever $a\ne0$. A perpendicular projection would miss that change. This is a teaching example of the projection geometry, not an additional network used in the paper. <!-- vale ai-tells.ContrastiveFormulas = YES --> <!-- vale ai-tells.AnthropomorphicCognition = YES -->

<!-- pedagogy-paragraph: p198 sha256 2c643bd85d3e8933fd7127e586cd0d302d74dcd69d691fc3921ef217cc019e39 -->
p198, lines 198-198; prose; priority: unchanged; previous: p192; next: p202

> <div class="figure-scroll">

<!-- pedagogy-paragraph: p202 sha256 aac32651b10f567c461b9b4f255d6fb1fa6859b5368d8bd9a51af920ab21cf23 -->
p202, lines 202-202; prose; priority: unchanged; previous: p198; next: p204

> </div>

<!-- pedagogy-paragraph: p204 sha256 383f2a63f88157db03010440a00e7e4f2a17473dd7c56143502d4c59500dbe29 -->
p204, lines 204-204; prose; priority: unchanged; previous: p202; next: p206

> As $y$ decays, $x$ changes by one. The left vector extracts that lasting shift.

<!-- pedagogy-paragraph: p206 sha256 aac32651b10f567c461b9b4f255d6fb1fa6859b5368d8bd9a51af920ab21cf23 -->
p206, lines 206-206; prose; priority: unchanged; previous: p204; next: p210

> </div>


Claim-bearing content: figure

Claims to check:

- Claim c1, line 107: "The disturbance must be small enough that the first order response describes the return flow.]{.key-statement}" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c2, line 109: "**Mathematical derivation.** [A [**linearization**]{.definition-term custom-style="Definition Term"} keeps the terms proportional to a small perturbation and drops terms quadratic or higher in it.]{.definition-explanation} Here the network activation is $\mathbf s=\bar{\mathbf s}(\theta)+\delta\m..." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c3, line 120: "$$ d\delta\mathbf s=K\delta\mathbf s\,dt+R^{1/2}d\mathbf B, \qquad K_{ij}=-\frac{\delta_{ij}}{\tau}+\phi'(\bar g_i)W_{ij}, \qquad R=\operatorname{diag}(\bar r_i). $$" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c4, line 127: "The entries of $K$ have units of inverse time.[^p1-projection]" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c5, line 129: "[Whether a disturbance decays, persists, or grows depends on the combined feedback through the whole network.]{.key-statement} A stronger connection alone does not establish better memory." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c6, line 138: "Differentiate the fixed point equation $\mathbf F[\bar{\mathbf s}(\theta)]=0$." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c7, line 140: "$$ K\mathbf u=0. $$" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c8, line 144: "The other modes must decay for this local family to be attracting. <!-- vale ai-tells.FormalTransitions = YES -->" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c9, line 152: "$$ \mathbf v^T K=0, \qquad \mathbf v^T\mathbf u=1. $$" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c10, line 159: "$$ 0=\mathbf v^T K\mathbf z=\lambda\mathbf v^T\mathbf z, $$" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c11, line 163: "<!-- vale ai-tells.EmDashUsage = NO --> <!-- vale ai-tells.FormalTransitions = NO --> so $\mathbf v^T\mathbf z=0$." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c12, line 163: "The left vector discards every decaying mode ([SI Eqs." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c13, line 163: "S12–S13, p. 3](../papers/burak-fiete-2012-persistent-activity-si.pdf#page=3&zoom=125,0,409))." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c14, line 163: "Consequently the surviving part of a small perturbation is <!-- vale ai-tells.FormalTransitions = YES --> <!-- vale ai-tells.EmDashUsage = YES -->" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c15, line 176: "<div class="publisher-worked-calculation publisher-fold-always">" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c16, line 182: "$$ \dot x=ay,\qquad \dot y=-\lambda y,\quad\lambda>0. $$" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c17, line 186: "Every point with $y=0$ is fixed." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c18, line 188: "$$ x(\infty)=x_0+\frac{a}{\lambda}y_0. $$" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c19, line 200: "Caption: Original guide construction of the tilted decay example, with dimensionless coordinates and $a/\lambda=1/2$. After an imposed jump from $(0,0)$ to $(0,2)$, the state relaxes toward $(1,0)$. Successive time marks crowd toward that endpoint. This illustrates the left and right zero vector..." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]

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

Location: line 208, anchor `sec:MEMORY-DIFFUSION`

First content kind: `prose`

Opening passage line: 210
Closing passage line: 250

Paragraphs in source order (complete `PARAGRAPH_REVIEW.json`):

<!-- pedagogy-paragraph: p210 sha256 b450e50c4d07d13f19e9b687c71cc23cb511b6d2e4d15bf84dbf7b80b0d7e237 -->
p210, lines 210-210; prose; priority: unchanged; previous: p206; next: p212

> **Neural mechanism.** We can now calculate how much random displacement remains after the stable components have relaxed. [Each cell's random spikes disturb its outgoing synaptic activation. The circuit's return flow determines the lasting shift in memory.]{.key-statement} This calculation uses the weak noise and conditional independence assumptions, with rates and return flow evaluated near one fixed point.

<!-- pedagogy-paragraph: p212 sha256 bd3857bc406f559066dc2e47857ee92af3814c68355b3113846d3f2cdb68dd24 -->
p212, lines 212-212; prose; priority: unchanged; previous: p210; next: p219

> **Mathematical derivation.** The variance of a linear combination of independent noise increments is the sum of their variances multiplied by squared weights. Here the weights are the components of $\mathbf v$: multiply the linear stochastic equation by $\mathbf v^T$. Since $\mathbf v^TK=0$,

<!-- pedagogy-paragraph: p219 sha256 5c74a0d27d21c01839a3300d9e65cac53c256ca43472bcd096cb523008ff32ae -->
p219, lines 219-219; prose; priority: unchanged; previous: p212; next: p227

> The independent Brownian increments have covariance $E[dB_i dB_j]=\delta_{ij}dt$, so

<!-- pedagogy-paragraph: p227 sha256 1e983b78439175990263ecbed3945f1f31139d79133898a7f175cd78f96f0376 -->
p227, lines 227-229; prose; priority: unchanged; previous: p219; next: p235

> <!-- vale ai-tells.EmDashUsage = NO --> Matching this to $2D\,dt$ yields the general local result ([SI Eqs. S14–S15, p. 3](../papers/burak-fiete-2012-persistent-activity-si.pdf#page=3&zoom=125,0,576)) <!-- vale ai-tells.EmDashUsage = YES -->

<!-- pedagogy-paragraph: p235 sha256 a7caf8e53d34dfd94c6532d201b7126a46f9ed8d20a8483b3e2e3420977b6887 -->
p235, lines 235-235; prose; priority: unchanged; previous: p227; next: p241

> For several memory coordinates $\theta_\alpha$, choose tangent vectors $u_i^\alpha=\partial\bar s_i/\partial\theta_\alpha$ and left vectors with $\sum_i v_i^\alpha u_i^\beta=\delta_{\alpha\beta}$. The same covariance calculation gives

<!-- pedagogy-paragraph: p241 sha256 3bb92a95bb5e65d41932fbc8e70d7ea05d8bc632f98c6ba5e5e80e715ea725f2 -->
p241, lines 241-241; prose; priority: unchanged; previous: p235; next: p243

> **Interpretation.** For one memory coordinate, each neuron's contribution combines its spike variability, $\bar r_i$, with the squared effect of one activation fluctuation on the final memory, $v_i^2$. The formula does not say that neurons with high rates necessarily damage memory more: changing rates can also change the tuning curves and the projection weights. Those changes must be included in a comparison.[^p1-projection]

<!-- pedagogy-paragraph: p243 sha256 764a8f5ef559dc2fa44b4ef7f7e7c124437ad8b5313cf856a4d135fb1840c8df -->
p243, lines 243-243; prose; priority: unchanged; previous: p241; next: p245

> The result is local in state and leading order in weak noise. The time interval must satisfy two conditions:

<!-- pedagogy-paragraph: p245 sha256 77954ae8f645cf205c0e779e6ca9ff1b99bdc91cd2e81901ebcb3dfde9c777a2 -->
p245, lines 245-245; list_item; priority: unchanged; previous: p243; next: p246

> It must be long enough for the approximation based on many spike contributions to apply.

<!-- pedagogy-paragraph: p246 sha256 9fb7d0fbf782fba16b31d08130811f9a4b7ebc2ca21aa3a8ce164261529b920b -->
p246, lines 246-246; list_item; priority: unchanged; previous: p245; next: p248

> It must be short enough that the coefficients do not change substantially as the memory moves.

<!-- pedagogy-paragraph: p248 sha256 0b1bf57cb6140ce6936014e30fbb946e4836afed2c49014b376ee3d1bf9e959f -->
p248, lines 248-248; prose; priority: unchanged; previous: p246; next: p250

> These conditions justify a local spreading rate. Systematic drift requires a [separate check in the next chapter](ch-memory-long-delays.html#sec-memory-drift-scope).

<!-- pedagogy-paragraph: p250 sha256 b80fba82e48f020a28335b1a7375c875ce983e68187f40d324744dadcc9518d6 -->
p250, lines 250-250; prose; priority: unchanged; previous: p248; next: p254

> [The [**diffusion tensor**]{.definition-term custom-style="Definition Term"} is the matrix of displacement covariances per twice the elapsed time.]{.definition-explanation} Its diagonal entries describe spreading in individual coordinates. Its other entries describe how coordinate displacements vary together. Even independently generated spike-count fluctuations can generate coupled motion of the represented coordinates.[^p1-multid]


Claim-bearing content: none

Claims to check:

- Claim c1, line 210: "**Neural mechanism.** We can now calculate how much random displacement remains after the stable components have relaxed." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c2, line 212: "Since $\mathbf v^TK=0$," -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c3, line 214: "$$ d\theta=\mathbf v^T R^{1/2}d\mathbf B =\sum_i v_i\sqrt{\bar r_i}\,dB_i. $$" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c4, line 227: "S14–S15, p. 3](../papers/burak-fiete-2012-persistent-activity-si.pdf#page=3&zoom=125,0,576)) <!-- vale ai-tells.EmDashUsage = YES -->" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c5, line 241: "Those changes must be included in a comparison.[^p1-projection]" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c6, line 243: "The time interval must satisfy two conditions:" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c7, line 245: "It must be long enough for the approximation based on many spike contributions to apply." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c8, line 246: "It must be short enough that the coefficients do not change substantially as the memory moves." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c9, line 250: "Even independently generated spike-count fluctuations can generate coupled motion of the represented coordinates.[^p1-multid]" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]

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

Location: line 252, anchor `sec:MEMORY-SYMMETRIC`

First content kind: `prose`

Opening passage line: 254
Closing passage line: 374

Paragraphs in source order (complete `PARAGRAPH_REVIEW.json`):

<!-- pedagogy-paragraph: p254 sha256 8eb8a13271fa08565118272c4fbfe1fc3c38647a5fedd790d019c2ec615210bf -->
p254, lines 254-256; prose; priority: unchanged; previous: p250; next: p258

> <!-- vale ai-tells.VerbTricolon = NO --> **Neural mechanism.** The general formula requires the left vector of the network dynamics. [When $W_{ij}=W_{ji}$, can we express it through the tuning curves and neural transfer function?]{.key-statement} Symmetric connections make each cell affect another cell's input with the same weight that it receives in return, while their firing responses can still differ. We retain the common synaptic time constant, a stable continuous family, and the weak noise and conditional independence assumptions. <!-- vale ai-tells.VerbTricolon = YES -->

<!-- pedagogy-paragraph: p258 sha256 362f3bb9b1a17d89055cd1b831bc0fc25d9b40981d35ce2a977c96ba921a5eee -->
p258, lines 258-258; prose; priority: unchanged; previous: p254; next: p265

> **Mathematical derivation.** The chain rule relates the slope of a response curve to the slope of its input curve. Here let $g_i'=d\bar g_i/d\theta$ and $r_i'=d\bar r_i/d\theta$. Differentiating the fixed point identities gives

<!-- pedagogy-paragraph: p265 sha256 3841788895bc44b11ce452bf9b4364ea04bf263d1d50a4730c96be83d8bd5a18 -->
p265, lines 265-265; prose; priority: unchanged; previous: p258; next: p273

> With symmetric $W$, the transpose of the linearized matrix satisfies

<!-- pedagogy-paragraph: p273 sha256 ecb783f3366ce12aa6ce95d0ec7f90fb21e931fda6d62d90982b5e14db3a299f -->
p273, lines 273-275; prose; priority: unchanged; previous: p265; next: p281

> <!-- vale ai-tells.FormalTransitions = NO --> Therefore $\mathbf v$ is proportional to $\mathbf g'$. Its normalization is <!-- vale ai-tells.FormalTransitions = YES -->

<!-- pedagogy-paragraph: p281 sha256 b658ed49add2a1663519c0cbc9486df6e17b978e23730f7b645501991df41fd8 -->
p281, lines 281-281; prose; priority: unchanged; previous: p273; next: p291

> because $u_i=\tau r_i'$. Substituting into the noise projection gives

<!-- pedagogy-paragraph: p291 sha256 9b03c93f3c681f57bf4e1d32ddebc9309c6985b739754dfa9678f07bdbc8e5d5 -->
p291, lines 291-293; prose; priority: unchanged; previous: p281; next: p295

> <!-- vale ai-tells.ContrastiveFormulas = NO --> **Interpretation.** The input slopes $g_i'$ now determine the projection weights, so the diffusion coefficient can be calculated from the tuning curves and transfer function. This follows from [SI Eq. S18, p. 4](../papers/burak-fiete-2012-persistent-activity-si.pdf#page=4&zoom=125,0,239), with $\bar g_i=\phi^{-1}(\bar r_i)$ wherever the transfer function is invertible over the relevant range. The supplied Early Edition [main Eq. 2, p. 2](../papers/burak-fiete-2012-persistent-activity.pdf#page=2&zoom=125,0,88) appears to omit the square on $g_i'$ in the numerator. The projection calculation and SI S18 give the squared expression shown here. This is an independent source check, not an author-confirmed correction. The result requires: <!-- vale ai-tells.ContrastiveFormulas = YES -->

<!-- pedagogy-paragraph: p295 sha256 61d5c495ffbb47efebae3d1fcea3f32b02daa78a7bd73a2f47f6587bc80019f4 -->
p295, lines 295-295; list_item; priority: unchanged; previous: p291; next: p296

> Symmetric weights.

<!-- pedagogy-paragraph: p296 sha256 ee1d0de3359aedb7d10e4aed0c29c1ea3250be9690dd65f5edb1934a53146e98 -->
p296, lines 296-296; list_item; priority: unchanged; previous: p295; next: p297

> A stable continuous family.

<!-- pedagogy-paragraph: p297 sha256 b02e0302e14ee93bad499b9c6ccc96c87e62caa15bf15046f87e2d8c6e8b130f -->
p297, lines 297-297; list_item; priority: unchanged; previous: p296; next: p299

> The noise assumptions already introduced.

<!-- pedagogy-paragraph: p299 sha256 534de71dc4260a8263f71c42a1d12803b1f5cbd9b4444ac77d7d5cd21a25beaa -->
p299, lines 299-299; prose; priority: unchanged; previous: p297; next: p301

> The result does not require [**translation symmetry**]{.definition-term custom-style="Definition Term"}, in which shifting an activity pattern along the represented coordinate leaves the network dynamics unchanged in form.[^p1-symmetric]

<!-- pedagogy-paragraph: p301 sha256 8e19185c156210567a045f638d7d3d1269765f40e35d9cff42cebc457898c408 -->
p301, lines 301-301; prose; priority: unchanged; previous: p299; next: p303

> <div class="publisher-worked-calculation publisher-fold-always">

<!-- pedagogy-paragraph: p303 sha256 63a3ae157ba6d5a81cb7e0ef8e9d2c4b974994ad214ce7a13ef68d48082439d6 -->
p303, lines 303-303; prose; priority: unchanged; previous: p301; next: p305

> **Example: opposite firing changes with constant diffusion.**

<!-- pedagogy-paragraph: p305 sha256 d261b9e7f4181cd1d37f01a96ff6d13d0b60023a89a607cca7af7e3a62f8ea5f -->
p305, lines 305-305; prose; priority: unchanged; previous: p303; next: p312

> Take two mutually inhibiting cells with $W_{12}=W_{21}=-1$, zero self weights, equal biases $b$, and $\phi(g)=g/\tau$ over the positive input range. Its fixed points obey

<!-- pedagogy-paragraph: p312 sha256 727e3daa89322194f5a1d2a0159334c3e5f7c2f860f6cd818c38f6a74e985885 -->
p312, lines 312-312; prose; priority: unchanged; previous: p305; next: p318

> The coordinate is $\theta=s_1-s_2$. The sum $s_1+s_2$ relaxes to $b$, while the difference is neutral. Here $\mathbf u=(1/2,-1/2)^T$, $\mathbf v=(1,-1)^T$, and

<!-- pedagogy-paragraph: p318 sha256 2733c00b7797d5a71297d5f785801ede099bac3530cae1c7152cd8a6e1cc7d91 -->
p318, lines 318-324; prose; priority: unchanged; previous: p312; next: p326

> <!-- vale ai-tells.DefensiveHedges = NO --> <!-- vale ai-tells.EmDashUsage = NO --> <!-- vale ai-tells.FormalTransitions = NO --> Although the two firing rates change with the stored value, their summed spike variability is constant. Therefore this network has constant local diffusion throughout its valid range. Near an endpoint, a negative linear rate would be impossible. A physical implementation must alter the transfer rule, and the interior formula alone does not describe that boundary. This model underlies the mutual inhibition example in [Fig. 2E–G, p. 3](ch-memory-long-delays.html#fig-paper-memory-2).[^p1-two] <!-- vale ai-tells.FormalTransitions = YES --> <!-- vale ai-tells.EmDashUsage = YES --> <!-- vale ai-tells.DefensiveHedges = YES -->

<!-- pedagogy-paragraph: p326 sha256 0118ba3b04a5d2bc07b991fb121d3fb1eb616008aff18a0a0c58de3c6ebeac6c -->
p326, lines 326-326; prose; priority: unchanged; previous: p318; next: p328

> The plot uses $b=20$ activation units and $\tau=0.1\,\mathrm{s}$.

<!-- pedagogy-paragraph: p328 sha256 2c643bd85d3e8933fd7127e586cd0d302d74dcd69d691fc3921ef217cc019e39 -->
p328, lines 328-328; prose; priority: unchanged; previous: p326; next: p332

> <div class="figure-scroll">

<!-- pedagogy-paragraph: p332 sha256 aac32651b10f567c461b9b4f255d6fb1fa6859b5368d8bd9a51af920ab21cf23 -->
p332, lines 332-332; prose; priority: unchanged; previous: p328; next: p334

> </div>

<!-- pedagogy-paragraph: p334 sha256 3a27bfce7fd574d17b10c5f5cac20653061f305ce54eb7ae57c6abd4c34040b6 -->
p334, lines 334-336; prose; priority: unchanged; previous: p332; next: p338

> <!-- vale ai-tells.FigurativeStays = NO --> The dashed rate sum in the upper plot stays fixed, so the lower plot has the same $D$ at every interior value of $\theta$. <!-- vale ai-tells.FigurativeStays = YES -->

<!-- pedagogy-paragraph: p338 sha256 aac32651b10f567c461b9b4f255d6fb1fa6859b5368d8bd9a51af920ab21cf23 -->
p338, lines 338-338; prose; priority: unchanged; previous: p334; next: p340

> </div>

<!-- pedagogy-paragraph: p340 sha256 c434e91454241a31e310a239ac3a093d91ab1fcd15b7ac3b333458ba63f49376 -->
p340, lines 340-340; prose; priority: unchanged; previous: p338; next: p342

> <!-- vale ai-tells.EmDashUsage = NO -->

<!-- pedagogy-paragraph: p342 sha256 6e36e79bce1447ac7eddc2fb19787ace984308e97fbb90fe3fbe309f14b460ff -->
p342, lines 342-342; prose; priority: unchanged; previous: p340; next: p344

> <!-- vale ai-tells.EmDashUsage = YES -->

<!-- pedagogy-paragraph: p344 sha256 5fc4a3efc0a3ac2572db825489d5de978ef64e81809fc8ca8e74c77c4fd5ef5b -->
p344, lines 344-346; prose; priority: unchanged; previous: p342; next: p348

> <!-- vale ai-tells.AnthropomorphicCognition = NO --> <!-- vale ai-tells.EmDashUsage = NO --> <!-- vale ai-tells.SemicolonUsage = NO -->

<!-- pedagogy-paragraph: p348 sha256 b51239384ed0f3f29067599835a50f6b20d9378380abf712dd586714b81360fc -->
p348, lines 348-350; prose; priority: unchanged; previous: p344; next: p352

> <!-- vale ai-tells.SemicolonUsage = YES --> <!-- vale ai-tells.EmDashUsage = YES --> <!-- vale ai-tells.AnthropomorphicCognition = YES -->

<!-- pedagogy-paragraph: p352 sha256 72fb9debbff6b02f5de0f17c603a3aa9b077a0b677b3227f9256736ccfda428a -->
p352, lines 352-353; prose; priority: unchanged; previous: p348; next: p355

> <!-- vale ai-tells.EmDashUsage = NO --> <!-- vale ai-tells.SemicolonUsage = NO -->

<!-- pedagogy-paragraph: p355 sha256 bf506d6f58cf686fa691df4ec9911b976f18e4d4c4e2ebf1dade6fe5b93b6120 -->
p355, lines 355-356; prose; priority: unchanged; previous: p352; next: p358

> <!-- vale ai-tells.SemicolonUsage = YES --> <!-- vale ai-tells.EmDashUsage = YES -->

<!-- pedagogy-paragraph: p358 sha256 c434e91454241a31e310a239ac3a093d91ab1fcd15b7ac3b333458ba63f49376 -->
p358, lines 358-358; prose; priority: unchanged; previous: p355; next: p360

> <!-- vale ai-tells.EmDashUsage = NO -->

<!-- pedagogy-paragraph: p360 sha256 6e36e79bce1447ac7eddc2fb19787ace984308e97fbb90fe3fbe309f14b460ff -->
p360, lines 360-360; prose; priority: unchanged; previous: p358; next: p362

> <!-- vale ai-tells.EmDashUsage = YES -->

<!-- pedagogy-paragraph: p362 sha256 72fb9debbff6b02f5de0f17c603a3aa9b077a0b677b3227f9256736ccfda428a -->
p362, lines 362-363; prose; priority: unchanged; previous: p360; next: p365

> <!-- vale ai-tells.EmDashUsage = NO --> <!-- vale ai-tells.SemicolonUsage = NO -->

<!-- pedagogy-paragraph: p365 sha256 bf506d6f58cf686fa691df4ec9911b976f18e4d4c4e2ebf1dade6fe5b93b6120 -->
p365, lines 365-366; prose; priority: unchanged; previous: p362; next: p368

> <!-- vale ai-tells.SemicolonUsage = YES --> <!-- vale ai-tells.EmDashUsage = YES -->

<!-- pedagogy-paragraph: p368 sha256 c434e91454241a31e310a239ac3a093d91ab1fcd15b7ac3b333458ba63f49376 -->
p368, lines 368-368; prose; priority: unchanged; previous: p365; next: p370

> <!-- vale ai-tells.EmDashUsage = NO -->

<!-- pedagogy-paragraph: p370 sha256 6e36e79bce1447ac7eddc2fb19787ace984308e97fbb90fe3fbe309f14b460ff -->
p370, lines 370-370; prose; priority: unchanged; previous: p368; next: p372

> <!-- vale ai-tells.EmDashUsage = YES -->

<!-- pedagogy-paragraph: p372 sha256 c434e91454241a31e310a239ac3a093d91ab1fcd15b7ac3b333458ba63f49376 -->
p372, lines 372-372; prose; priority: unchanged; previous: p370; next: p374

> <!-- vale ai-tells.EmDashUsage = NO -->

<!-- pedagogy-paragraph: p374 sha256 6e36e79bce1447ac7eddc2fb19787ace984308e97fbb90fe3fbe309f14b460ff -->
p374, lines 374-374; prose; priority: unchanged; previous: p372; next: none

> <!-- vale ai-tells.EmDashUsage = YES -->


Claim-bearing content: figure

Claims to check:

- Claim c1, line 267: "$$ K^T\mathbf g' =-\mathbf g'/\tau+W\operatorname{diag}[\phi'(\bar g_i)]\mathbf g' =-\mathbf g'/\tau+W\mathbf r'=0. $$" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c2, line 291: "S18, p. 4](../papers/burak-fiete-2012-persistent-activity-si.pdf#page=4&zoom=125,0,239), with $\bar g_i=\phi^{-1}(\bar r_i)$ wherever the transfer function is invertible over the relevant range." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c3, line 291: "The supplied Early Edition [main Eq. 2, p. 2](../papers/burak-fiete-2012-persistent-activity.pdf#page=2&zoom=125,0,88) appears to omit the square on $g_i'$ in the numerator." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c4, line 299: "The result does not require [**translation symmetry**]{.definition-term custom-style="Definition Term"}, in which shifting an activity pattern along the represented coordinate leaves the network dynamics unchanged in form.[^p1-symmetric]" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c5, line 301: "<div class="publisher-worked-calculation publisher-fold-always">" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c6, line 305: "Take two mutually inhibiting cells with $W_{12}=W_{21}=-1$, zero self weights, equal biases $b$, and $\phi(g)=g/\tau$ over the positive input range." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c7, line 307: "$$ \bar s_1=\frac{b+\theta}{2},\qquad \bar s_2=\frac{b-\theta}{2},\qquad |\theta|<b. $$" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c8, line 312: "The coordinate is $\theta=s_1-s_2$." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c9, line 312: "The sum $s_1+s_2$ relaxes to $b$, while the difference is neutral." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c10, line 312: "Here $\mathbf u=(1/2,-1/2)^T$, $\mathbf v=(1,-1)^T$, and" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c11, line 314: "$$ 2D=\bar r_1+\bar r_2=b/\tau. $$" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c12, line 318: "A physical implementation must alter the transfer rule, and the interior formula alone does not describe that boundary." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c13, line 318: "This model underlies the mutual inhibition example in [Fig. 2E–G, p. 3](ch-memory-long-delays.html#fig-paper-memory-2).[^p1-two] <!-- vale ai-tells.FormalTransitions = YES --> <!-- vale ai-tells.EmDashUsage = YES --> <!-- vale ai-tells.DefensiveHedges = YES -->" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c14, line 326: "The plot uses $b=20$ activation units and $\tau=0.1\,\mathrm{s}$." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c15, line 330: "Caption: For the chapter’s two mutually inhibiting cells, b = 20 activation units and tau = 0.1 s give opposite changes in the two rates. Their sum remains 200 spikes/s, so local D remains 100 coordinate units squared/s. Open endpoints mark the excluded boundaries. The linear interior model does..." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c16, line 334: "<!-- vale ai-tells.FigurativeStays = NO --> The dashed rate sum in the upper plot stays fixed, so the lower plot has the same $D$ at every interior value of $\theta$. <!-- vale ai-tells.FigurativeStays = YES -->" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]

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

Purpose: In the memory-network model, random changes in a stored angle accumulate over time. This chapter extends the local spreading calculation to longer delays, where boundaries, angular wraparound, and systematic drift can change the size of the memory error.

Prerequisites: ch:MEMORY-DYNAMICS

Sidecar sections: Long delay errors depend on boundaries and local diffusion, A diffusion calculation does not determine systematic drift, Figures distinguish memory motion from readout error and test diffusion

Blocks: 4 figure(s), 0 equation(s), 0 code block(s)

Result labels: No Answer/Conclusion/Feedback label detected

<!-- pedagogy-unit: content/chapters/02b-memory-long-delays.md::ch:MEMORY-LONG-DELAYS -->

### Chapter opening

Location: line 2, anchor `ch:MEMORY-LONG-DELAYS`

First content kind: `prose`

Opening passage line: 3
Closing passage line: 11

Paragraphs in source order (complete `PARAGRAPH_REVIEW.json`):

<!-- pedagogy-paragraph: p3 sha256 796d53109458cfe2fbb392dbaf62bd7aeab805fa9c143e7a79d542a3bf3b6e38 -->
p3, lines 3-3; prose; priority: unchanged; previous: none; next: p5

> <!-- vale ai-tells.NounString = YES -->

<!-- pedagogy-paragraph: p5 sha256 c506d9cf11bdfe7601200ca8f86d5c71fab277e058cf53b90c14b5b454f127a7 -->
p5, lines 5-7; prose; priority: unchanged; previous: p3; next: p9

> <!-- vale ai-tells.VerbTricolon = NO --> [A rate of random spreading measured near one stored value does not yet tell us how memory error behaves after a long wait.]{.key-statement} The value may approach a boundary, wrap around an angular range, or reach a region where the spreading rate differs. A consistent movement of the average value would also change the error without being captured by the rate of random spreading alone. <!-- vale ai-tells.VerbTricolon = YES -->

<!-- pedagogy-paragraph: p9 sha256 24ae9d69eaf437eb15052f9f5211f48baf7c712c4038f6ade6c7b4877ad4c288 -->
p9, lines 9-9; prose; priority: unchanged; previous: p5; next: p11

> We begin by following the distribution of stored values across repeated trials, using the local diffusion coefficient derived in the preceding chapter. This shows why errors can keep growing on a line but level off when angular error is measured within one turn. We then separate random spreading from systematic drift and make the noise assumptions explicit. Finally, the paper's figures show what its network simulations test and distinguish movement of the memory from uncertainty when another circuit reads it. That second uncertainty motivates the information calculation that follows.

<!-- pedagogy-paragraph: p11 sha256 98f61808845505ea0ae7403dd4ee06e82bf061dfa9b33de987306e66b7843126 -->
p11, lines 11-11; prose; priority: unchanged; previous: p9; next: p15

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

Location: line 13, anchor `sec:MEMORY-LONG-TIME`

First content kind: `prose`

Opening passage line: 15
Closing passage line: 124

Paragraphs in source order (complete `PARAGRAPH_REVIEW.json`):

<!-- pedagogy-paragraph: p15 sha256 1487ad3e86f364fc0a2e65446679c6759c2773964dca631d7e16cda2e170af60 -->
p15, lines 15-15; prose; priority: unchanged; previous: p11; next: p17

> **Neural mechanism.** Spike fluctuations keep shifting the stored value after the cue has ended. The local diffusion coefficient describes the variance of those shifts after stable disturbances have relaxed. It does not by itself say that variance grows at the same rate forever: boundaries and variation of $D$ can change the long time behavior. We first keep $D$ constant, so the line and circle differ only in how the memory coordinate is bounded.

<!-- pedagogy-paragraph: p17 sha256 2f3020015003a86f8a21b7b10a1d497375bddc09c572da42023a7f8f3cef3fff -->
p17, lines 17-17; prose; priority: unchanged; previous: p15; next: p21

> **Mathematical derivation.** Let $p(\theta,t)$ be the density of the memory coordinate across repeated trials initialized at $\Theta$. [The [**Itô convention**]{.definition-term custom-style="Definition Term"} evaluates a state-dependent noise coefficient at the beginning of each increment.]{.definition-explanation} A density equation tracks how small random increments redistribute probability. The calculation below first obtains that equation for a general state-dependent $D$. Constant $D$ then gives the line and circle solutions.

<!-- pedagogy-paragraph: p21 sha256 5b07edf8afc9be206828ba0d4eec67174912c4307c53c43a1769c6a2fbe975b7 -->
p21, lines 21-21; prose; priority: unchanged; previous: p17; next: p32

> To pass from random increments to a density equation, choose any smooth function $F(\theta)$. In a short interval $dt$, the zero-drift Itô increment has conditional mean zero and conditional second moment $2D(\theta)dt$. Taylor expansion at the starting coordinate gives

<!-- pedagogy-paragraph: p32 sha256 193f77f82798c9b294a4d81af5c66d6c83afbf3a57d24c46c4b785cafe0b3c6b -->
p32, lines 32-32; prose; priority: unchanged; previous: p21; next: p39

> The higher-order terms vanish faster than $dt$ in this diffusion approximation. Averaging over the starting-coordinate density and dividing by $dt$ gives

<!-- pedagogy-paragraph: p39 sha256 e2cd40d0adba1709c73e5d00e6582f0545148d633be2dad2017853c81533ce25 -->
p39, lines 39-39; prose; priority: unchanged; previous: p32; next: p43

> Take $F$ to vanish outside an interior region, or use boundaries for which the integration terms vanish. Integrating by parts twice moves both derivatives from $F$ onto the product $Dp$. Because the resulting identity holds for every such smooth $F$, it gives the density equation below.

<!-- pedagogy-paragraph: p43 sha256 c501255c330983a7d0a9a35547f2217157059b5916c9079b5bc89e76de2d35e3 -->
p43, lines 43-43; prose; priority: unchanged; previous: p39; next: p51

> [In the zero-drift diffusion approximation, this density evolves according to the [**Fokker Planck equation**]{.definition-term custom-style="Definition Term"}:]{.definition-explanation}

<!-- pedagogy-paragraph: p51 sha256 74a0d4e314a5096621af8b9c8d6010953d7cec92c6b40685839647216bf8dbdc -->
p51, lines 51-51; prose; priority: unchanged; previous: p43; next: p58

> [Here the [**Dirac delta**]{.definition-term custom-style="Definition Term"} denotes a point mass: initially all probability is at $\Theta$.]{.definition-explanation} It differs from the earlier zero-or-one symbol $\delta_{ij}$. For constant $D$ on an unbounded line, the Gaussian solution is

<!-- pedagogy-paragraph: p58 sha256 e3f271c6ee9de04b0fca360dc741b8f536faa992c9f020a4820585e8831eec6f -->
p58, lines 58-58; prose; priority: unchanged; previous: p51; next: p64

> Its variance is $2Dt$. For an angular coordinate, add the densities at all displacements $\theta-\Theta+2\pi k$, $k\in\mathbb Z$, to wrap the Gaussian around the circle. This wrapped sum appears in [SI Eq. S31, p. 7](../papers/burak-fiete-2012-persistent-activity-si.pdf#page=7&zoom=125,0,483). At long times the density approaches $1/(2\pi)$. If angular errors are reported in $[-\pi,\pi)$, their limiting mean squared value is

<!-- pedagogy-paragraph: p64 sha256 1d0edd936da6193d423334a1e3dc696735d8cacccec722a08098fc38fd294647 -->
p64, lines 64-66; prose; priority: unchanged; previous: p58; next: p68

> <!-- vale ai-tells.FormalTransitions = NO --> **Interpretation.** [The flattening of a ring network's error curve can therefore occur while its local noise mechanism remains unchanged. It reflects the bounded way angular error is reported.]{.key-statement}[^p1-fp] <!-- vale ai-tells.FormalTransitions = YES -->

<!-- pedagogy-paragraph: p68 sha256 f1ee245bbd0788846e584cf212e1c61cde231d0e38be1ace3f63043ca2e1a88d -->
p68, lines 68-68; prose; priority: unchanged; previous: p64; next: p70

> For $D=0.5\,\mathrm{rad}^2/\mathrm{s}$, the plots show how the density and squared error change with delay.

<!-- pedagogy-paragraph: p70 sha256 2c643bd85d3e8933fd7127e586cd0d302d74dcd69d691fc3921ef217cc019e39 -->
p70, lines 70-70; prose; priority: unchanged; previous: p68; next: p74

> <div class="figure-scroll">

<!-- pedagogy-paragraph: p74 sha256 aac32651b10f567c461b9b4f255d6fb1fa6859b5368d8bd9a51af920ab21cf23 -->
p74, lines 74-74; prose; priority: unchanged; previous: p70; next: p76

> </div>

<!-- pedagogy-paragraph: p76 sha256 7b72b542cc7656abf57014e2c30073563d1c1bd096bf6daa8438dfb1cc9d4867 -->
p76, lines 76-76; prose; priority: unchanged; previous: p74; next: p78

> As the wrapped density approaches uniform, its mean squared error approaches $\pi^2/3$. The unbounded line error keeps growing.

<!-- pedagogy-paragraph: p78 sha256 1d107df5394a20b8e496cd85eafaf7df439d54295a31267ee99005e55015f576 -->
p78, lines 78-78; prose; priority: unchanged; previous: p76; next: p80

> **Neural mechanism.** The rate of random spreading can change as the stored value changes, because the current firing rates set the spike variability. The supplement illustrates this dependence with mutual excitation, $W_{12}=W_{21}=1$, biases $(b_0,-b_0)$, and the same linear transfer rule. The fixed activation states are $(\theta+b_0/2,\theta-b_0/2)$. Now $\mathbf u=(1,1)^T$, $\mathbf v=(1/2,1/2)^T$.

<!-- pedagogy-paragraph: p80 sha256 861f276b408aacf059d19fe94f7e792bf76755740447fa699de4582144e404c4 -->
p80, lines 80-88; prose; priority: unchanged; previous: p78; next: p90

> <!-- vale ai-tells.ContrastiveFormulas = NO --> <!-- vale ai-tells.FigurativeFires = NO --> <!-- vale ai-tells.FigurativeStays = NO --> <!-- vale ai-tells.FormalTransitions = NO --> Here $\theta$ is an activation coordinate, not an angle, and both steady rates are positive only when $\theta>|b_0|/2$. When both activations rise together, each cell raises the other's firing enough to replace the extra synaptic decay. This common increase persists and changes the stored value. A disturbance in their difference instead decays toward the difference set by the biases. Larger $\theta$ raises both firing rates and hence both Poisson count variances. Because the projection weights stay fixed in this example, more of that variability remains as memory error. <!-- vale ai-tells.FormalTransitions = YES --> <!-- vale ai-tells.FigurativeStays = YES --> <!-- vale ai-tells.FigurativeFires = YES --> <!-- vale ai-tells.ContrastiveFormulas = YES -->

<!-- pedagogy-paragraph: p90 sha256 f0b07be1c5e67043f621eb2a24bb57707ad005df260e77cad6dbbfce6318fb41 -->
p90, lines 90-90; prose; priority: unchanged; previous: p80; next: p98

> **Mathematical derivation.** When $D$ varies with state, the zero drift stochastic equation is $d\theta=\sqrt{2D(\theta)}\,dB$ with the Itô convention. Under conditions that remove boundary terms, the density equation gives

<!-- pedagogy-paragraph: p98 sha256 ec4c9faf4cdb1b7ee5303f61b648b9802df3a33150f8fdcc2ca32bc634ea98d6 -->
p98, lines 98-102; prose; priority: unchanged; previous: p90; next: p109

> <!-- vale ai-tells.ConsequenceParticiple = NO --> <!-- vale ai-tells.FormalTransitions = NO --> To obtain these identities, multiply the density equation by $\theta$ or $(\theta-\Theta)^2$, integrate over $\theta$, and integrate by parts twice. The second derivatives of these functions are respectively zero and two, giving the two identities. A similar calculation for the smooth function $D$ gives $dE[D]/dt=E[DD'']$. Expanding at $t=0$ therefore yields <!-- vale ai-tells.FormalTransitions = YES --> <!-- vale ai-tells.ConsequenceParticiple = YES -->

<!-- pedagogy-paragraph: p109 sha256 97344b5ad00188bf83938cd992ef1cbbaa16c609f29eaf24ad1c400f43720910 -->
p109, lines 109-109; prose; priority: unchanged; previous: p98; next: p116

> This is [SI Eq. S37, p. 8](../papers/burak-fiete-2012-persistent-activity-si.pdf#page=8&zoom=125,0,602).[^p1-variable] For the mutual excitation network, substituting $v_1=v_2=1/2$ into the diffusion formula gives

<!-- pedagogy-paragraph: p116 sha256 e7e825cf4a58ccc94929c3a625f15f0f8819a666b8a025e5bda7cf8fb83671dc -->
p116, lines 116-116; prose; priority: unchanged; previous: p109; next: p118

> **Interpretation.** A state dependent $D$ need not produce a nonlinear increase of variance with time. If $D$ is linear in $\theta$, then $E[D(\theta)]=D(E[\theta])=D(\Theta)$, so the variance remains linear while the process stays within the model's valid domain. The implied variance for this network is $\Theta t/(2\tau)$, agreeing with [SI Eq. S41, p. 9](../papers/burak-fiete-2012-persistent-activity-si.pdf#page=9&zoom=125,0,383) and the slope tested in [Fig. S1, p. 10](ch-memory-long-delays.html#fig-paper-memory-s1). SI Eq. S40 instead prints $D=\theta/(2\tau)$. Under the convention used throughout this guide, that displayed value differs by a factor of two from the direct projection and S41.[^p1-excitation]

<!-- pedagogy-paragraph: p118 sha256 a5aff214ac327ee8b6b161e0daf80bc01ba0c331311eed9ae02e1bec6f8e9858 -->
p118, lines 118-120; prose; priority: unchanged; previous: p116; next: p124

> <details class="publisher-long-content publisher-source-figure"> <summary>Original paper figure: Burak and Fiete (2012), Figure S1</summary> <div class="publisher-fold-body">

<!-- pedagogy-paragraph: p124 sha256 fcd1e43c0c40c2d1dd2932edba0594c38927752553522ce5ed959562b6a78f49 -->
p124, lines 124-125; prose; priority: unchanged; previous: p118; next: p129

> </div> </details>


Claim-bearing content: figure

Claims to check:

- Claim c1, line 15: "We first keep $D$ constant, so the line and circle differ only in how the memory coordinate is bounded." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c2, line 17: "[The [**Itô convention**]{.definition-term custom-style="Definition Term"} evaluates a state-dependent noise coefficient at the beginning of each increment.]{.definition-explanation} A density equation tracks how small random increments redistribute probability." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c3, line 39: "Because the resulting identity holds for every such smooth $F$, it gives the density equation below." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c4, line 58: "For an angular coordinate, add the densities at all displacements $\theta-\Theta+2\pi k$, $k\in\mathbb Z$, to wrap the Gaussian around the circle." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c5, line 58: "S31, p. 7](../papers/burak-fiete-2012-persistent-activity-si.pdf#page=7&zoom=125,0,483)." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c6, line 58: "At long times the density approaches $1/(2\pi)$." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c7, line 64: "<!-- vale ai-tells.FormalTransitions = NO --> **Interpretation.** [The flattening of a ring network's error curve can therefore occur while its local noise mechanism remains unchanged." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c8, line 64: "It reflects the bounded way angular error is reported.]{.key-statement}[^p1-fp] <!-- vale ai-tells.FormalTransitions = YES -->" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c9, line 68: "For $D=0.5\,\mathrm{rad}^2/\mathrm{s}$, the plots show how the density and squared error change with delay." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c10, line 72: "Caption: With the same constant D = 0.5 rad²/s, wrapped Gaussian error densities widen toward 1/(2π). The unbounded line has mean squared error 2Dt. Reporting angular error in $[-\pi,\pi)$ instead gives a mean squared error that approaches π²/3. The flattening comes from the bounded error convent..." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c11, line 76: "As the wrapped density approaches uniform, its mean squared error approaches $\pi^2/3$." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c12, line 78: "The supplement illustrates this dependence with mutual excitation, $W_{12}=W_{21}=1$, biases $(b_0,-b_0)$, and the same linear transfer rule." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c13, line 78: "The fixed activation states are $(\theta+b_0/2,\theta-b_0/2)$." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c14, line 78: "Now $\mathbf u=(1,1)^T$, $\mathbf v=(1/2,1/2)^T$." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c15, line 80: "<!-- vale ai-tells.ContrastiveFormulas = NO --> <!-- vale ai-tells.FigurativeFires = NO --> <!-- vale ai-tells.FigurativeStays = NO --> <!-- vale ai-tells.FormalTransitions = NO --> Here $\theta$ is an activation coordinate, not an angle, and both steady rates are positive only when $\theta>|b_0|..." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c16, line 80: "Because the projection weights stay fixed in this example, more of that variability remains as memory error. <!-- vale ai-tells.FormalTransitions = YES --> <!-- vale ai-tells.FigurativeStays = YES --> <!-- vale ai-tells.FigurativeFires = YES --> <!-- vale ai-tells.ContrastiveFormulas = YES -->" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c17, line 92: "$$ \frac{d}{dt}E[\theta]=0, \qquad \frac{d}{dt}\operatorname{Var}(\theta)=2E[D(\theta)]. $$" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c18, line 98: "Expanding at $t=0$ therefore yields <!-- vale ai-tells.FormalTransitions = YES --> <!-- vale ai-tells.ConsequenceParticiple = YES -->" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c19, line 104: "$$ \operatorname{Var}(\theta) =2D(\Theta)t+D(\Theta)D''(\Theta)t^2+O(t^3). $$" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c20, line 109: "S37, p. 8](../papers/burak-fiete-2012-persistent-activity-si.pdf#page=8&zoom=125,0,602).[^p1-variable] For the mutual excitation network, substituting $v_1=v_2=1/2$ into the diffusion formula gives" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c21, line 111: "$$ 2D=\frac{1}{4}(\bar r_1+\bar r_2)=\frac{\theta}{2\tau}, \qquad D=\frac{\theta}{4\tau}. $$" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c22, line 116: "If $D$ is linear in $\theta$, then $E[D(\theta)]=D(E[\theta])=D(\Theta)$, so the variance remains linear while the process stays within the model's valid domain." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c23, line 116: "S41, p. 9](../papers/burak-fiete-2012-persistent-activity-si.pdf#page=9&zoom=125,0,383) and the slope tested in [Fig." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c24, line 116: "Under the convention used throughout this guide, that displayed value differs by a factor of two from the direct projection and S41.[^p1-excitation]" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c25, line 118: "<details class="publisher-long-content publisher-source-figure"> <summary>Original paper figure: Burak and Fiete (2012), Figure S1</summary> <div class="publisher-fold-body">" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c26, line 122: "Caption: Mutual excitation produces a wandering state and approximately linear variance growth in the plotted simulation. Original Figure S1 from Burak and Fiete (2012), reproduced as an exact artwork excerpt. [PDF page 10](../papers/burak-fiete-2012-persistent-activity-si.pdf#page=10). [Open ima..." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]

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

Location: line 127, anchor `sec:MEMORY-DRIFT-SCOPE`

First content kind: `prose`

Opening passage line: 129
Closing passage line: 145

Paragraphs in source order (complete `PARAGRAPH_REVIEW.json`):

<!-- pedagogy-paragraph: p129 sha256 944d04022ab15d36358aee2060c69d8d8552925d096cbd25371250a27de84638 -->
p129, lines 129-129; prose; priority: unchanged; previous: p124; next: p131

> **Neural mechanism.** [Repeated trials can spread apart even if their average stays at the original value. That random spreading differs from a reproducible movement in one direction.]{.key-statement} Both can occur, and the derivation of $D$ alone does not settle the second question.

<!-- pedagogy-paragraph: p131 sha256 caa215a58983e040952e4f20e3f3b7d40edbe1e72494e68ada19ebd6d1b26930 -->
p131, lines 131-137; prose; priority: unchanged; previous: p129; next: p139

> <!-- vale ai-tells.ConsequenceParticiple = NO --> <!-- vale ai-tells.EmDashUsage = NO --> <!-- vale ai-tells.FormalTransitions = NO --> [The paper assumes that the network is tuned to eliminate systematic drift, meaning a nonzero mean velocity along the attractor.]{.definition-explanation} A deterministic mismatch in weights can create such a velocity. In addition, state dependent noise and curved network dynamics can create a small mean motion even if the noise free model has an exact continuous attractor. The supplement explains that deriving the exact mean motion requires the microscopic jump process, beyond the leading variance calculation ([SI “Systematic drift,” pp. 4–5](../papers/burak-fiete-2012-persistent-activity-si.pdf#page=4&zoom=125,0,362)).[^p1-systematic] <!-- vale ai-tells.FormalTransitions = YES --> <!-- vale ai-tells.EmDashUsage = YES --> <!-- vale ai-tells.ConsequenceParticiple = YES -->

<!-- pedagogy-paragraph: p139 sha256 37a4dab3f86b12b2ee8b107bd95154dbc7698266cdb00db70e79ecdaf4018779 -->
p139, lines 139-139; prose; priority: unchanged; previous: p131; next: p141

> **Mathematical derivation.** For state dependent $D$, where the coefficient is evaluated affects the process. [The [**Stratonovich convention**]{.definition-term custom-style="Definition Term"} uses midpoint evaluation in its limiting increments.]{.definition-explanation} With the same written coefficient and zero written drift, it describes a different process from the Itô equation. Converting the Stratonovich equation into Itô form adds a drift $D'/2$. This follows from the conversion term $bb'/2$ with $b=\sqrt{2D}$ and $bb'=D'$. The supplement uses the difference to estimate a possible scale of noise induced drift, not to identify the exact drift of every neural network.

<!-- pedagogy-paragraph: p141 sha256 30a2a98933048070f2dd040043ac45bc07040e2b76323bb43b36a97ee83d5804 -->
p141, lines 141-141; prose; priority: unchanged; previous: p139; next: p143

> With $D$ of order $1/N$, random displacement over $dt$ is of order $\sqrt{dt/N}$, while such a mean displacement is of order $dt/N$.

<!-- pedagogy-paragraph: p143 sha256 87e9ef0b50577535dfb24322f9e27730d8cf6b29042b8b38824afb679267920a -->
p143, lines 143-143; prose; priority: unchanged; previous: p141; next: p145

> **Interpretation.** The variance calculation captures the leading random term. [Small changes to weights or biases might cancel the mean drift. They cannot remove the random increments by subtracting a known average.]{.key-statement} A known mean drift can in principle be accounted for by a decoder, but any actual implementation must know that drift and respect the domain and boundary conditions.

<!-- pedagogy-paragraph: p145 sha256 2019148d88c7147dd1836ce19071c4c2ced9407e0561820471bcefe5e873276d -->
p145, lines 145-145; prose; priority: unchanged; previous: p143; next: p149

> The independence assumption also has a precise scope. Newly generated spike-count fluctuations are conditionally independent given the present state. Shared recurrent fluctuations can still correlate the observed spike trains over time. An extra source of correlated fluctuations would change the projection formula to $2D=\mathbf v^TQ\mathbf v$, where $Q\,dt$ is their increment covariance. A matching calculation of information would need the probabilities of joint spike patterns. The paper discusses such correlated models as future extensions ([Discussion, p. 5, paragraph beginning “Our spiking model”](../papers/burak-fiete-2012-persistent-activity.pdf#page=5&zoom=125,0,142)). It does not prove that every correlated spiking model obeys its Poisson formulas.[^p1-correlation]


Claim-bearing content: none

Claims to check:

- Claim c1, line 131: "In addition, state dependent noise and curved network dynamics can create a small mean motion even if the noise free model has an exact continuous attractor." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c2, line 131: "The supplement explains that deriving the exact mean motion requires the microscopic jump process, beyond the leading variance calculation ([SI “Systematic drift,” pp. 4–5](../papers/burak-fiete-2012-persistent-activity-si.pdf#page=4&zoom=125,0,362)).[^p1-systematic] <!-- vale ai-tells.FormalTran..." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c3, line 139: "Converting the Stratonovich equation into Itô form adds a drift $D'/2$." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c4, line 139: "This follows from the conversion term $bb'/2$ with $b=\sqrt{2D}$ and $bb'=D'$." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c5, line 139: "The supplement uses the difference to estimate a possible scale of noise induced drift, not to identify the exact drift of every neural network." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c6, line 141: "With $D$ of order $1/N$, random displacement over $dt$ is of order $\sqrt{dt/N}$, while such a mean displacement is of order $dt/N$." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c7, line 143: "[Small changes to weights or biases might cancel the mean drift." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c8, line 143: "They cannot remove the random increments by subtracting a known average.]{.key-statement} A known mean drift can in principle be accounted for by a decoder, but any actual implementation must know that drift and respect the domain and boundary conditions." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c9, line 145: "The paper discusses such correlated models as future extensions ([Discussion, p. 5, paragraph beginning “Our spiking model”](../papers/burak-fiete-2012-persistent-activity.pdf#page=5&zoom=125,0,142))." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c10, line 145: "It does not prove that every correlated spiking model obeys its Poisson formulas.[^p1-correlation]" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]

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

Location: line 147, anchor `sec:MEMORY-FIGURES`

First content kind: `prose`

Opening passage line: 149
Closing passage line: 227

Paragraphs in source order (complete `PARAGRAPH_REVIEW.json`):

<!-- pedagogy-paragraph: p149 sha256 a1e155fcff170fe8b8c2bbf81cb76ab0e1f14518532ed9539e59d23107bbae6a -->
p149, lines 149-149; prose; priority: unchanged; previous: p145; next: p151

> **Neural mechanism in the figures.** [Figure 1A, p. 2](ch-memory-long-delays.html#fig-paper-memory-1) shows the definition of the memory coordinate. Start at a green point off the attractor and follow the noise free flow to the black point on it. This endpoint defines the instantaneous attractor state. After one noisy interval, repeat that flow. The difference between the two endpoints is the retained memory change. The relevant projection follows the flow, as in the [tilted two variable example](ch-memory-dynamics.html#sec-memory-linearization).

<!-- pedagogy-paragraph: p151 sha256 20227211a5e9b281bd19f8b58a00324daf13275c8fed10ef91de67e941a9e2a5 -->
p151, lines 151-153; prose; priority: unchanged; previous: p149; next: p155

> <!-- vale Google.Units = NO --> [In Fig. 1B, an [**activity bump**]{.definition-term custom-style="Definition Term"} is a localized peak of population firing rates across the neurons' preferred angles.]{.definition-explanation} The figure separates two sources of error: <!-- vale Google.Units = YES -->

<!-- pedagogy-paragraph: p155 sha256 58ac67f0029cc968bea6eec6f7c6edb078232a5cb99beadb24a366ea6ce9347b -->
p155, lines 155-155; list_item; priority: unchanged; previous: p151; next: p156

> During storage, the bump's location has moved away from its initial value $\Theta$.

<!-- pedagogy-paragraph: p156 sha256 f805c290d89f946694a301282d1157f350eaf432d85ef18d4e2fb74ca5511874 -->
p156, lines 156-156; list_item; priority: unchanged; previous: p155; next: p158

> At the later time, an observer has additional uncertainty about the bump's current location because it sees only a finite sample of spikes.

<!-- pedagogy-paragraph: p158 sha256 26b0811d88b6550ac1495a4852089802e1653d29d67adb2eb52c5a26113c7b46 -->
p158, lines 158-158; prose; priority: unchanged; previous: p156; next: p160

> The [information calculation](ch-memory-information.html#sec-memory-fi) measures this second uncertainty and relates it to diffusion. The [readout chapter](ch-memory-readout.html) then follows observation of the moving state.[^p1-fig1]

<!-- pedagogy-paragraph: p160 sha256 e79093c88eed092dd4eb6a1860586ee755c34497af472d61ec7d187ae790a2b2 -->
p160, lines 160-162; prose; priority: unchanged; previous: p158; next: p166

> <details class="publisher-long-content publisher-source-figure"> <summary>Original paper figure: Burak and Fiete (2012), Figure 1</summary> <div class="publisher-fold-body">

<!-- pedagogy-paragraph: p166 sha256 fcd1e43c0c40c2d1dd2932edba0594c38927752553522ce5ed959562b6a78f49 -->
p166, lines 166-167; prose; priority: unchanged; previous: p160; next: p169

> </div> </details>

<!-- pedagogy-paragraph: p169 sha256 522968b54c642f9c0afebe1bbe67d3fd29cc40c55f809b88a1233a4abcd2a71b -->
p169, lines 169-169; prose; priority: unchanged; previous: p166; next: p171

> [Figure 2, p. 3](ch-memory-long-delays.html#fig-paper-memory-2) tests the diffusion calculation in two different network designs. Panel A shows a ring with weights determined by differences of preferred angles. This gives rotational symmetry: rotating the activity pattern around the ring leaves its dynamics unchanged in form. In B, compare the firing rate curves and spike marks in the inset before reading the wandering angular trace. The curve describes rates. The marks show individual spikes. The trace shows the represented angle rather than overall activity amplitude.

<!-- pedagogy-paragraph: p171 sha256 ff718a368d9870a00609c9d5c757ef001c401e18f8484d3e3c83a92639c74fcb -->
p171, lines 171-171; prose; priority: unchanged; previous: p169; next: p173

> **Interpretation of the simulation tests.** Panels C and D test different parts of the prediction:

<!-- pedagogy-paragraph: p173 sha256 2544c38702c0595ec4722a0db0e7ecb232295c768ecbf63447bc1426dc1f772f -->
p173, lines 173-173; prose; priority: unchanged; previous: p171; next: p174

> <!-- vale ai-tells.ContrastiveFormulas = NO -->

<!-- pedagogy-paragraph: p174 sha256 d2901040c7662cb3aa9544431dc1be7a4ac186d262516414e7155769c92d3f9c -->
p174, lines 174-175; list_item; priority: unchanged; previous: p173; next: p176

> Panel C compares simulated mean squared angular displacements with the prediction from the tuning curves and transfer function. The gray exponential case and black sigmoidal, or S-shaped, case have different transfer functions. The dashed bound is a lower limit for the sigmoidal case, not a separate fitted trajectory. A model can lie above its information bound while still agreeing with the derived diffusion formula. <!-- vale ai-tells.ContrastiveFormulas = YES -->

<!-- pedagogy-paragraph: p176 sha256 2a55904b08c60036057d786d9b6ff9d2581c6775ee0bb7d216f73c4adaa201ae -->
p176, lines 176-176; list_item; priority: unchanged; previous: p174; next: p178

> Panel D follows angular error to longer intervals. Its flattening uses angular wrapping, not a disappearance of noise. The expected limiting value with the caption's error convention is $\pi^2/3$.

<!-- pedagogy-paragraph: p178 sha256 ea520e3df7556f9c0d470a5779fee9b65c567916596531b044165e9a7ed7a482 -->
p178, lines 178-180; prose; priority: unchanged; previous: p176; next: p182

> <!-- vale ai-tells.CataphoricForecasting = NO --> Panels E to G use mutual inhibition rather than a ring. The two rates in F vary in opposite directions. Their difference represents memory. Panel G compares their displacement statistics with the analytic prediction. This second design matters because the projection argument does not require rotational symmetry. These are simulations checking the model calculation. They are not direct measurements of memory noise in an animal.[^p1-fig2] <!-- vale ai-tells.CataphoricForecasting = YES -->

<!-- pedagogy-paragraph: p182 sha256 478ca7d7faa5d1fb92250c4eab86c64eac3ca6817f398a4b6ff8965ff810ee2a -->
p182, lines 182-184; prose; priority: unchanged; previous: p178; next: p188

> <details class="publisher-long-content publisher-source-figure"> <summary>Original paper figure: Burak and Fiete (2012), Figure 2</summary> <div class="publisher-fold-body">

<!-- pedagogy-paragraph: p188 sha256 fcd1e43c0c40c2d1dd2932edba0594c38927752553522ce5ed959562b6a78f49 -->
p188, lines 188-189; prose; priority: unchanged; previous: p182; next: p191

> </div> </details>

<!-- pedagogy-paragraph: p191 sha256 1f5cf531981995c9079f01236be4d4bca14e74209587f97fbeff10d0f05f3bc2 -->
p191, lines 191-191; prose; priority: unchanged; previous: p188; next: p193

> The derivation has now supplied a dynamical quantity, $D$, from spike variability and the way a network returns to its attractor. We next derive a statistical quantity from the same tuning curves and ask why it puts a lower limit on $D$.

<!-- pedagogy-paragraph: p193 sha256 2139b3f6693ec084037797db2d5af08c75595d3c10e042fc61ad7e76e942f2c1 -->
p193, lines 193-194; prose; priority: unchanged; previous: p191; next: p196

> <!-- vale ai-tells.AnthropomorphicCognition = NO --> <!-- vale ai-tells.EmDashUsage = NO -->

<!-- pedagogy-paragraph: p196 sha256 fb62b1024cd03e292e79a9b6791592f9a6038ef448a6929b919813c2ff2129fe -->
p196, lines 196-197; prose; priority: unchanged; previous: p193; next: p199

> <!-- vale ai-tells.EmDashUsage = YES --> <!-- vale ai-tells.AnthropomorphicCognition = YES -->

<!-- pedagogy-paragraph: p199 sha256 c434e91454241a31e310a239ac3a093d91ab1fcd15b7ac3b333458ba63f49376 -->
p199, lines 199-199; prose; priority: unchanged; previous: p196; next: p201

> <!-- vale ai-tells.EmDashUsage = NO -->

<!-- pedagogy-paragraph: p201 sha256 6e36e79bce1447ac7eddc2fb19787ace984308e97fbb90fe3fbe309f14b460ff -->
p201, lines 201-201; prose; priority: unchanged; previous: p199; next: p203

> <!-- vale ai-tells.EmDashUsage = YES -->

<!-- pedagogy-paragraph: p203 sha256 72fb9debbff6b02f5de0f17c603a3aa9b077a0b677b3227f9256736ccfda428a -->
p203, lines 203-204; prose; priority: unchanged; previous: p201; next: p206

> <!-- vale ai-tells.EmDashUsage = NO --> <!-- vale ai-tells.SemicolonUsage = NO -->

<!-- pedagogy-paragraph: p206 sha256 bf506d6f58cf686fa691df4ec9911b976f18e4d4c4e2ebf1dade6fe5b93b6120 -->
p206, lines 206-207; prose; priority: unchanged; previous: p203; next: p209

> <!-- vale ai-tells.SemicolonUsage = YES --> <!-- vale ai-tells.EmDashUsage = YES -->

<!-- pedagogy-paragraph: p209 sha256 72fb9debbff6b02f5de0f17c603a3aa9b077a0b677b3227f9256736ccfda428a -->
p209, lines 209-210; prose; priority: unchanged; previous: p206; next: p212

> <!-- vale ai-tells.EmDashUsage = NO --> <!-- vale ai-tells.SemicolonUsage = NO -->

<!-- pedagogy-paragraph: p212 sha256 bf506d6f58cf686fa691df4ec9911b976f18e4d4c4e2ebf1dade6fe5b93b6120 -->
p212, lines 212-213; prose; priority: unchanged; previous: p209; next: p215

> <!-- vale ai-tells.SemicolonUsage = YES --> <!-- vale ai-tells.EmDashUsage = YES -->

<!-- pedagogy-paragraph: p215 sha256 1101a39dc4239d053bfdb3a5840e5490073e98b4b75f7ca4b7320ae17703ef70 -->
p215, lines 215-216; prose; priority: unchanged; previous: p212; next: p218

> <!-- vale Microsoft.Quotes = NO --> <!-- vale ai-tells.EmDashUsage = NO -->

<!-- pedagogy-paragraph: p218 sha256 bf27caddc450f798d3fd220d0e0c302006ebe94f131f110677fc750f21204ba1 -->
p218, lines 218-219; prose; priority: unchanged; previous: p215; next: p221

> <!-- vale ai-tells.EmDashUsage = YES --> <!-- vale Microsoft.Quotes = YES -->

<!-- pedagogy-paragraph: p221 sha256 c434e91454241a31e310a239ac3a093d91ab1fcd15b7ac3b333458ba63f49376 -->
p221, lines 221-221; prose; priority: unchanged; previous: p218; next: p223

> <!-- vale ai-tells.EmDashUsage = NO -->

<!-- pedagogy-paragraph: p223 sha256 6e36e79bce1447ac7eddc2fb19787ace984308e97fbb90fe3fbe309f14b460ff -->
p223, lines 223-223; prose; priority: unchanged; previous: p221; next: p225

> <!-- vale ai-tells.EmDashUsage = YES -->

<!-- pedagogy-paragraph: p225 sha256 c434e91454241a31e310a239ac3a093d91ab1fcd15b7ac3b333458ba63f49376 -->
p225, lines 225-225; prose; priority: unchanged; previous: p223; next: p227

> <!-- vale ai-tells.EmDashUsage = NO -->

<!-- pedagogy-paragraph: p227 sha256 6e36e79bce1447ac7eddc2fb19787ace984308e97fbb90fe3fbe309f14b460ff -->
p227, lines 227-227; prose; priority: unchanged; previous: p225; next: none

> <!-- vale ai-tells.EmDashUsage = YES -->


Claim-bearing content: figure

Claims to check:

- Claim c1, line 149: "**Neural mechanism in the figures.** [Figure 1A, p. 2](ch-memory-long-delays.html#fig-paper-memory-1) shows the definition of the memory coordinate." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c2, line 156: "At the later time, an observer has additional uncertainty about the bump's current location because it sees only a finite sample of spikes." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c3, line 158: "The [readout chapter](ch-memory-readout.html) then follows observation of the moving state.[^p1-fig1]" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c4, line 160: "<details class="publisher-long-content publisher-source-figure"> <summary>Original paper figure: Burak and Fiete (2012), Figure 1</summary> <div class="publisher-fold-body">" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c5, line 164: "Caption: Noise-free return flow defines the memory coordinate. The second panel separates movement of that coordinate from uncertainty when reading it. Original Figure 1 from Burak and Fiete (2012), reproduced as an exact artwork excerpt. [PDF page 2](../papers/burak-fiete-2012-persistent-activit..." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c6, line 169: "[Figure 2, p. 3](ch-memory-long-delays.html#fig-paper-memory-2) tests the diffusion calculation in two different network designs." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c7, line 176: "The expected limiting value with the caption's error convention is $\pi^2/3$." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c8, line 178: "They are not direct measurements of memory noise in an animal.[^p1-fig2] <!-- vale ai-tells.CataphoricForecasting = YES -->" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c9, line 182: "<details class="publisher-long-content publisher-source-figure"> <summary>Original paper figure: Burak and Fiete (2012), Figure 2</summary> <div class="publisher-fold-body">" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c10, line 186: "Caption: The ring and mutual-inhibition simulations compare measured displacement statistics with the predicted diffusion. Original Figure 2 from Burak and Fiete (2012), reproduced as an exact artwork excerpt. [PDF page 3](../papers/burak-fiete-2012-persistent-activity.pdf#page=3). [Open image at..." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]

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

Purpose: A neuron receiving spikes from a memory circuit has access to information about the stored value. This chapter sets a bound on estimation error under the model’s assumptions and derives the constraint that spike information places on the circuit’s memory stability.

Prerequisites: ch:MEMORY-DYNAMICS, ch:MEMORY-LONG-DELAYS

Sidecar sections: Rate slopes and spike variability determine local information, Spike information sets a lower bound on memory diffusion, Improving persistence depends on what a comparison holds fixed

Blocks: 2 figure(s), 0 equation(s), 0 code block(s)

Result labels: No Answer/Conclusion/Feedback label detected

<!-- pedagogy-unit: content/chapters/03-memory-information.md::ch:MEMORY-INFORMATION -->

### Chapter opening

Location: line 2, anchor `ch:MEMORY-INFORMATION`

First content kind: `prose`

Opening passage line: 3
Closing passage line: 13

Paragraphs in source order (complete `PARAGRAPH_REVIEW.json`):

<!-- pedagogy-paragraph: p3 sha256 796d53109458cfe2fbb392dbaf62bd7aeab805fa9c143e7a79d542a3bf3b6e38 -->
p3, lines 3-3; prose; priority: unchanged; previous: none; next: p5

> <!-- vale ai-tells.NounString = YES -->

<!-- pedagogy-paragraph: p5 sha256 0b905a3bf51188d1cef0f40a1c669043e9eba1ee6a48a2c72df68847c92aa6b7 -->
p5, lines 5-5; prose; priority: unchanged; previous: p3; next: p7

> A neuron that receives spikes from a memory circuit can use them to estimate the value stored by that circuit. [Collecting more spikes helps distinguish nearby activity patterns, but during collection the pattern itself keeps moving.]{.key-statement} The same variability that limits readout also perturbs the recurrent network. Burak and Fiete connect these two effects by deriving a lower bound on memory diffusion from the information in the spikes.[^p1-info-main]

<!-- pedagogy-paragraph: p7 sha256 ca70cb8e0d9784411f7fb03be22e2968d0e65d5fc17702b94c3c8cf49e3ce359 -->
p7, lines 7-11; prose; priority: unchanged; previous: p5; next: p13

> <!-- vale ai-tells.EmptyPadding = NO --> <!-- vale ai-tells.FigurativeStays = NO --> The useful quantity is how clearly a short spike sample distinguishes nearby memory values. Comparing that quantity with the random motion already derived gives a minimum rate of memory spreading. This is a limit for a particular network, so using it to compare different networks also requires keeping track of what changes and what stays fixed. More information can permit better stability without ensuring that a particular circuit achieves it. <!-- vale ai-tells.FigurativeStays = YES --> <!-- vale ai-tells.EmptyPadding = YES -->

<!-- pedagogy-paragraph: p13 sha256 eb385308e8e79422f09da8e48b70750ff8173daf1a9ad2a3a5185ae2dd5c9675 -->
p13, lines 13-13; prose; priority: unchanged; previous: p7; next: p17

> We retain the memory coordinate $\theta$, initial value $\Theta$, firing rate $\bar r_i(\theta)$, synaptic time constant $\tau$, and diffusion convention $\operatorname{Var}(\Delta\theta)=2D\Delta t$. The [network projection](ch-memory-dynamics.html#sec-memory-linearization) determines which activity changes remain as changes in the stored value.


Claim-bearing content: none

Claims to check:

- Claim c1, line 5: "Burak and Fiete connect these two effects by deriving a lower bound on memory diffusion from the information in the spikes.[^p1-info-main]" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c2, line 7: "More information can permit better stability without ensuring that a particular circuit achieves it. <!-- vale ai-tells.FigurativeStays = YES --> <!-- vale ai-tells.EmptyPadding = YES -->" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c3, line 13: "We retain the memory coordinate $\theta$, initial value $\Theta$, firing rate $\bar r_i(\theta)$, synaptic time constant $\tau$, and diffusion convention $\operatorname{Var}(\Delta\theta)=2D\Delta t$." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c4, line 13: "The [network projection](ch-memory-dynamics.html#sec-memory-linearization) determines which activity changes remain as changes in the stored value." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]

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

Location: line 15, anchor `sec:MEMORY-FI`

First content kind: `prose`

Opening passage line: 17
Closing passage line: 88

Paragraphs in source order (complete `PARAGRAPH_REVIEW.json`):

<!-- pedagogy-paragraph: p17 sha256 396870d2eb9aa341f5f44febefd34ff751c34ed83a193ed1de86b7e0893c01a7 -->
p17, lines 17-17; prose; priority: unchanged; previous: p13; next: p19

> **Neural mechanism.** Suppose two nearby memory values produce almost identical rates. A short spike sample cannot reliably tell them apart. If a small change in memory instead produces a large rate change relative to spike variability, that sample is more useful. We need a quantity that measures this local distinction.

<!-- pedagogy-paragraph: p19 sha256 164aa6885f6622cb2cbbee140073ff00405de4dd46f02f705a758fdfb0fd1e5d -->
p19, lines 19-19; prose; priority: unchanged; previous: p17; next: p21

> In a short interval $h$, let $n_i$ be neuron $i$'s count. Treat the memory state as locally constant and use the conditionally independent Poisson approximation from the neural model. The calculation below uses positive rates.

<!-- pedagogy-paragraph: p21 sha256 61d41dd5d2f8ab9ca1175564d7d110d1095245da9d3936cb5ecc268aab032f3c -->
p21, lines 21-21; prose; priority: unchanged; previous: p19; next: p28

> **Mathematical derivation.** [A [**likelihood**]{.definition-term custom-style="Definition Term"} is the probability of observed data as a function of a proposed parameter value.]{.definition-explanation} For the neural model,

<!-- pedagogy-paragraph: p28 sha256 8675fc7625752639bc4e701e8586b1c0c3c753143fcc06891f0dce5c927e29c3 -->
p28, lines 28-28; prose; priority: unchanged; previous: p21; next: p40

> Taking the logarithm turns the product into a sum. With $r_i'=d\bar r_i/d\theta$,

<!-- pedagogy-paragraph: p40 sha256 bd47a545f421759d651532c0d9ae427e1a3c1d664ecfd783d164e3d0c660fcaa -->
p40, lines 40-40; prose; priority: unchanged; previous: p28; next: p48

> [The [**score**]{.definition-term custom-style="Definition Term"} $S$ measures how the log likelihood changes when the proposed memory value changes.]{.definition-explanation} Its mean is zero because $E[n_i]=\bar r_i h$. Its mean square is

<!-- pedagogy-paragraph: p48 sha256 bd475765cd52d13ba882a8258a31c7e0038746f59c12e9650fb21b405331004f -->
p48, lines 48-48; prose; priority: unchanged; previous: p40; next: p54

> The cross terms vanish by conditional independence, and Poisson variance supplies $\operatorname{Var}(n_i)=\bar r_i h$. [[**Fisher information**]{.definition-term custom-style="Definition Term"} is this expected squared score. The paper divides it by observation duration and calls the result the [**internal Fisher information rate**]{.definition-term custom-style="Definition Term"}:]{.definition-explanation}

<!-- pedagogy-paragraph: p54 sha256 87e588fbb60f059698ae27bf1c53268b6898be6aa9c681cc1b65714814ea4271 -->
p54, lines 54-54; prose; priority: unchanged; previous: p48; next: p62

> [To understand why inverse information is an error scale, let $\hat\theta(\mathbf n)$ be an estimator whose mean equals $\theta$ locally. Such an estimator is [**unbiased**]{.definition-term custom-style="Definition Term"}.]{.definition-explanation} Differentiate $E_\theta[\hat\theta]=\theta$ with respect to $\theta$. Under the usual conditions allowing differentiation through the sum over data,

<!-- pedagogy-paragraph: p62 sha256 182b9d66412774e0d5a6ed8f029abc79d7aed0042a49fe1ff6dd1f7d2c2ed080 -->
p62, lines 62-62; prose; priority: unchanged; previous: p54; next: p70

> The last equality uses $E[S]=0$. Cauchy Schwarz now gives

<!-- pedagogy-paragraph: p70 sha256 c2b4203d2ed9bd13af062743ad4b6a59df6a117da196b57353e58c884644f9ca -->
p70, lines 70-70; prose; priority: unchanged; previous: p62; next: p72

> **Interpretation.** [This is the [**Cramér Rao bound**]{.definition-term custom-style="Definition Term"}. It is a local bound for regular unbiased estimation.]{.definition-explanation} It does not guarantee that every finite spike sample admits an estimator attaining it. The paper works in a weak noise, informative sample regime where local likelihoods can be approximated as Gaussian and a suitable estimator can approach the bound. [A [**prior distribution**]{.definition-term custom-style="Definition Term"} represents knowledge about likely parameter values before observing the spikes.]{.definition-explanation} A strong prior, bias, boundaries, or globally ambiguous tuning changes the estimation problem.[^p1-cr]

<!-- pedagogy-paragraph: p72 sha256 e204358e0bd77b4f1712083188f2fd4c07bc43b28faa737663302c7fdde3a61a -->
p72, lines 72-72; prose; priority: unchanged; previous: p70; next: p74

> If the coordinate is an angle in radians, $J$ has units $\mathrm{rad}^{-2}\mathrm{s}^{-1}$. The information in a locally stationary interval of duration $h$ is $Jh$, not $J$.[^p1-fi-source] A vanishing rate requires a suitable limit and regularity of the likelihood.

<!-- pedagogy-paragraph: p74 sha256 113206da8286747546c8ee56b371b2c07d467f7ceea4968da233383178117082 -->
p74, lines 74-76; prose; priority: unchanged; previous: p72; next: p78

> <!-- vale ai-tells.ParallelStaccato = NO --> Each cell contributes squared slope divided by its count variance per unit time. High rates with zero slope do not distinguish neighboring values, so they contribute no local information. A sharply changing rate can be informative even if it is smaller than another cell's peak rate. The coordinate here describes the network's present internal state. It need not be a currently visible external stimulus. Sensory Fisher information has the same Poisson formula only when the stimulus dependent tuning curves are the relevant rates. <!-- vale ai-tells.ParallelStaccato = YES -->

<!-- pedagogy-paragraph: p78 sha256 6f51450cb2a27e927f068e2fc8cfadc077bb37d1dafda9071c05c9fdef2c3cde -->
p78, lines 78-80; prose; priority: unchanged; previous: p74; next: p82

> <!-- vale ai-tells.CataphoricForecasting = NO --> Two positive tuning curves with the same changing part isolate the effect of extra baseline firing. <!-- vale ai-tells.CataphoricForecasting = YES -->

<!-- pedagogy-paragraph: p82 sha256 2c643bd85d3e8933fd7127e586cd0d302d74dcd69d691fc3921ef217cc019e39 -->
p82, lines 82-82; prose; priority: unchanged; previous: p78; next: p86

> <div class="figure-scroll">

<!-- pedagogy-paragraph: p86 sha256 aac32651b10f567c461b9b4f255d6fb1fa6859b5368d8bd9a51af920ab21cf23 -->
p86, lines 86-86; prose; priority: unchanged; previous: p82; next: p88

> </div>

<!-- pedagogy-paragraph: p88 sha256 12b8515ac2dd1bfafa84bbd6fd8f06aeee05e2d705481e258766d410578b6be0 -->
p88, lines 88-88; prose; priority: unchanged; previous: p86; next: p92

> The rate peak has zero local slope, so it contributes no local information at that point. Extra spikes from a constant baseline increase Poisson variability without making nearby values easier to distinguish. See [Internal Fisher information, Eq. 3, p. 2](../papers/burak-fiete-2012-persistent-activity.pdf#page=2).


Claim-bearing content: figure

Claims to check:

- Claim c1, line 17: "A short spike sample cannot reliably tell them apart." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c2, line 17: "If a small change in memory instead produces a large rate change relative to spike variability, that sample is more useful." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c3, line 56: "$$ 1=\sum_{\mathbf n}\hat\theta(\mathbf n)\partial_\theta p(\mathbf n\mid\theta) =E[\hat\theta S] =E[(\hat\theta-\theta)S]. $$" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c4, line 62: "The last equality uses $E[S]=0$." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c5, line 70: "It is a local bound for regular unbiased estimation.]{.definition-explanation} It does not guarantee that every finite spike sample admits an estimator attaining it." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c6, line 70: "[A [**prior distribution**]{.definition-term custom-style="Definition Term"} represents knowledge about likely parameter values before observing the spikes.]{.definition-explanation} A strong prior, bias, boundaries, or globally ambiguous tuning changes the estimation problem.[^p1-cr]" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c7, line 72: "If the coordinate is an angle in radians, $J$ has units $\mathrm{rad}^{-2}\mathrm{s}^{-1}$." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c8, line 72: "The information in a locally stationary interval of duration $h$ is $Jh$, not $J$.[^p1-fi-source] A vanishing rate requires a suitable limit and regularity of the likelihood." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c9, line 74: "Sensory Fisher information has the same Poisson formula only when the stimulus dependent tuning curves are the relevant rates. <!-- vale ai-tells.ParallelStaccato = YES -->" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c10, line 78: "<!-- vale ai-tells.CataphoricForecasting = NO --> Two positive tuning curves with the same changing part isolate the effect of extra baseline firing. <!-- vale ai-tells.CataphoricForecasting = YES -->" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c11, line 84: "Caption: Analytic teaching curves $r_A(\theta)=5+35e^{-\theta^2/(2w^2)}$ and $r_B(\theta)=r_A(\theta)+20$, in spikes per second, with chosen width $w=0.6$ rad. The rates have the same derivative. Their individual Poisson information contributions $(r_i^{\prime})^2/r_i$ vanish at the rate peak, wh..." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c12, line 88: "See [Internal Fisher information, Eq. 3, p. 2](../papers/burak-fiete-2012-persistent-activity.pdf#page=2)." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]

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

Location: line 90, anchor `sec:MEMORY-BOUND`

First content kind: `prose`

Opening passage line: 92
Closing passage line: 240

Paragraphs in source order (complete `PARAGRAPH_REVIEW.json`):

<!-- pedagogy-paragraph: p92 sha256 0afe45d5fd2e53d7335d6adc79f7b9c685bca6550aadf2e1d1d547926b6d1584 -->
p92, lines 92-92; prose; priority: unchanged; previous: p88; next: p94

> **Neural mechanism.** The network has no access to its exact firing rates as noiseless numbers. Its recurrent input is built from the same random spikes that an external observer sees. The lower bound on diffusion follows directly by comparing the state sensitivity of the network with the spike information.

<!-- pedagogy-paragraph: p94 sha256 429fbad1da9f7bd925f64183f9b79ff20c137064d35f2acdccb605e0fe3691cc -->
p94, lines 94-94; prose; priority: unchanged; previous: p92; next: p104

> **Mathematical derivation.** Cauchy Schwarz bounds a dot product by the product of the two vector lengths. Here the normalization of the memory projection fixes that dot product, while the two lengths measure diffusion and information. From the [projection and diffusion calculation](ch-memory-dynamics.html#sec-memory-diffusion),

<!-- pedagogy-paragraph: p104 sha256 dbab6cd1e6f5b341d1032b319082425b63326bce59172c62dbc1ca1c51c5d08d -->
p104, lines 104-104; prose; priority: unchanged; previous: p94; next: p110

> Define two vectors $a_i=v_i\sqrt{\bar r_i}$ and $b_i=r_i'/\sqrt{\bar r_i}$. Their dot product is

<!-- pedagogy-paragraph: p110 sha256 320633a08f1866acf1d82d25a43664ec941753186bc3556b5d5378c91c1ca72d -->
p110, lines 110-112; prose; priority: unchanged; previous: p104; next: p119

> <!-- vale ai-tells.FormalTransitions = NO --> Their squared lengths are $\sum_i a_i^2=2D$ and $\sum_i b_i^2=J$. Cauchy Schwarz therefore gives <!-- vale ai-tells.FormalTransitions = YES -->

<!-- pedagogy-paragraph: p119 sha256 7175517a370b5cd2e664e3fd29c4ea9db5ce17058eb9772fe090a5485e49dad6 -->
p119, lines 119-119; prose; priority: unchanged; previous: p110; next: p125

> or

<!-- pedagogy-paragraph: p125 sha256 1e3ec3997f61151638ec6d2b7548e178d1a585cfdeddfbb099b4e1584737dced -->
p125, lines 125-127; prose; priority: unchanged; previous: p119; next: p129

> <!-- vale ai-tells.AnthropomorphicCognition = NO --> **Interpretation.** This proof uses the general left vector formula, so symmetric weights are unnecessary. It is a shorter teaching reconstruction of the scalar proof in SI Section V. Its assumptions are those used to derive $D$ and $J$. It is not a general statement about all possible noisy memory systems.[^p1-bound-source] <!-- vale ai-tells.AnthropomorphicCognition = YES -->

<!-- pedagogy-paragraph: p129 sha256 62f561543b8a56b1087298fe25a5c8ac16445d3cddd2f77be04de9319a20221c -->
p129, lines 129-129; prose; priority: unchanged; previous: p125; next: p131

> The units agree: $\tau^2J$ has units of time per coordinate squared, so its reciprocal has the units of diffusion. [Small internal information forces a large minimum diffusion coefficient. Large information allows small diffusion, but does not guarantee it.]{.key-statement}

<!-- pedagogy-paragraph: p131 sha256 7c868d66ce5d3eb8b3bd782a68271dc11f9fc45be31d5fccea9f632f5e4c0fc3 -->
p131, lines 131-131; prose; priority: unchanged; previous: p129; next: p133

> **Neural mechanism.** [Reaching the bound requires the network's retained response to each cell's spike noise to match that cell's information about memory.]{.key-statement} A cell that adds retained noise without helping distinguish nearby values prevents equality.

<!-- pedagogy-paragraph: p133 sha256 7fd575167caffa0d7f2e69b1570f69bffab9389578ebcbd8c7a51ef321571e8f -->
p133, lines 133-133; prose; priority: unchanged; previous: p131; next: p141

> **Mathematical derivation.** Equality requires the two vectors in the proof to be proportional:

<!-- pedagogy-paragraph: p141 sha256 a175cba48be2011c9ab3a2432309b41871368ad29204d99db44b442ce0c4abe2 -->
p141, lines 141-143; prose; priority: unchanged; previous: p133; next: p149

> <!-- vale ai-tells.FormalTransitions = NO --> Cells with zero tuning slope cannot contribute extra projected noise if equality is to hold. In a symmetric network, $v_i$ is proportional to $g_i'$, and $r_i'=\phi'(\bar g_i)g_i'$. At each state, the participating cells therefore need a common value of $\phi'(\bar g_i)/\phi(\bar g_i)$. A sufficient way to satisfy this at all states is to choose that ratio equal to the same constant $k$ throughout the relevant input range. Solving <!-- vale ai-tells.FormalTransitions = YES -->

<!-- pedagogy-paragraph: p149 sha256 078c6f7683f3682d617b14c66ce0ef14e43fc1209a75ce78d87a97ba33ffc088 -->
p149, lines 149-149; prose; priority: unchanged; previous: p141; next: p151

> gives $\phi(g)=A e^{kg}$.

<!-- pedagogy-paragraph: p151 sha256 0f8fc6683738cfa28a94765e906e401f28cf5b8a01fd71cc5b002375abfb3ab0 -->
p151, lines 151-151; prose; priority: unchanged; previous: p149; next: p155

> **Interpretation.** This exponential family attains equality for symmetric weights with Poisson noise, under the other model assumptions. It is a sufficient condition, rather than a general necessity: the common ratio may depend on the current memory state.[^p1-equality]

<!-- pedagogy-paragraph: p155 sha256 941e5fcd09fd12a78e118796e07f4ba9e80fad3587b6f9c304d358b1c4b0bbf7 -->
p155, lines 155-157; prose; priority: unchanged; previous: p151; next: p165

> <!-- vale ai-tells.FormalTransitions = NO --> The [mutual-excitation example](ch-memory-long-delays.html#sec-memory-long-time) shows why equality does not require an exponential transfer rule. Set its bias $b_0=0$ and use the linear rule $\phi(g)=g/\tau$ on positive inputs. Its fixed states are $s_1=s_2=\theta>0$, with $\mathbf u=(1,1)^T$ and $\mathbf v=(1/2,1/2)^T$. Both rates are $\theta/\tau$, and both rate derivatives are $1/\tau$. Therefore <!-- vale ai-tells.FormalTransitions = YES -->

<!-- pedagogy-paragraph: p165 sha256 b4927e28a3ce11d61aa9c6c3cc25cb778dd70b175ab749a6c074ec041ae20344 -->
p165, lines 165-169; prose; priority: unchanged; previous: p155; next: p173

> <!-- vale ai-tells.ConclusionMarkers = NO --> <!-- vale ai-tells.EmDashUsage = NO --> Equality holds throughout this family even though its transfer rule is linear. At each state both cells receive the same input, and the ratio $\phi'/\phi=1/\theta$ changes between states. To conclude that equality forces an exponential rule, we need additional restrictions linking the participating input values across cells and states. Continuous variation of the represented value alone does not supply them. This qualification concerns the source's claim that equality requires an exponential rule. The information–diffusion inequality remains unchanged. <!-- vale ai-tells.EmDashUsage = YES --> <!-- vale ai-tells.ConclusionMarkers = YES -->

<!-- pedagogy-paragraph: p173 sha256 8e19185c156210567a045f638d7d3d1269765f40e35d9cff42cebc457898c408 -->
p173, lines 173-173; prose; priority: unchanged; previous: p165; next: p175

> <div class="publisher-worked-calculation publisher-fold-always">

<!-- pedagogy-paragraph: p175 sha256 41c512056921db305b60b53437148507b969cfe96255bd4bb8ce680342837dab -->
p175, lines 175-175; prose; priority: unchanged; previous: p173; next: p177

> **Example: the same diffusion with a looser information bound.**

<!-- pedagogy-paragraph: p177 sha256 4dddb2cbf2578967d1fb6de7b46cf7444343cdd90807aa3b19fe87b1e832bcbf -->
p177, lines 177-181; prose; priority: unchanged; previous: p175; next: p188

> <!-- vale ai-tells.ContrastiveFormulas = NO --> <!-- vale ai-tells.FormalTransitions = NO --> In the two cell mutual inhibition model, use $b=200$ activation units and $\tau=0.1\,\mathrm{s}$. The memory coordinate is an activation difference, not an angle. At $\theta=0$ both rates are $1000\,\mathrm{s}^{-1}$ and their slopes are $\pm5\,\mathrm{s}^{-1}$ per activation unit. Thus <!-- vale ai-tells.FormalTransitions = YES --> <!-- vale ai-tells.ContrastiveFormulas = YES -->

<!-- pedagogy-paragraph: p188 sha256 940604609743e6367eadb6b3c496c3eaa2e792df6f81dc2a06c57ddf863f78dc -->
p188, lines 188-188; prose; priority: unchanged; previous: p177; next: p195

> Here $J$ has units of inverse activation unit squared per second, and $D$ has activation unit squared per second. The bound is $1/(2\tau^2J)=1000$, so equality holds at this balanced state. At $\theta=100$, the rates become $1500$ and $500\,\mathrm{s}^{-1}$, while their slopes stay $\pm5$. Now

<!-- pedagogy-paragraph: p195 sha256 78ebd202d0a70719c29bf03421c45bbf2659f344fe50b14b8bc5eb8d76a4d740 -->
p195, lines 195-195; prose; priority: unchanged; previous: p188; next: p199

> The actual diffusion remains $1000$. The inequality is strict because these two unequal rates no longer align the network's projection weights with the information optimal weights. This also shows why equality at a special state does not force the transfer function to be exponential on its whole domain. A constant lower bound attained everywhere and an accidental equality at one state are different claims.

<!-- pedagogy-paragraph: p199 sha256 2c643bd85d3e8933fd7127e586cd0d302d74dcd69d691fc3921ef217cc019e39 -->
p199, lines 199-199; prose; priority: unchanged; previous: p195; next: p203

> <div class="figure-scroll">

<!-- pedagogy-paragraph: p203 sha256 aac32651b10f567c461b9b4f255d6fb1fa6859b5368d8bd9a51af920ab21cf23 -->
p203, lines 203-203; prose; priority: unchanged; previous: p199; next: p205

> </div>

<!-- pedagogy-paragraph: p205 sha256 998c132a3d415d042cc86eea6027aba1f5cc9b69dfdafe2c6e97443e96a26239 -->
p205, lines 205-205; prose; priority: unchanged; previous: p203; next: p207

> The gap at $\theta=100$ shows why a lower minimum allowed by the inequality is not a reduction in the network’s actual diffusion. See [Diffusion bound, Eq. 4, p. 3](../papers/burak-fiete-2012-persistent-activity.pdf#page=3).

<!-- pedagogy-paragraph: p207 sha256 aac32651b10f567c461b9b4f255d6fb1fa6859b5368d8bd9a51af920ab21cf23 -->
p207, lines 207-207; prose; priority: unchanged; previous: p205; next: p209

> </div>

<!-- pedagogy-paragraph: p209 sha256 085144698a6e8172183e916aa7e94407c84caf1728549cb5345a0c7492b6d519 -->
p209, lines 209-211; prose; priority: unchanged; previous: p207; next: p213

> <!-- vale ai-tells.FormalTransitions = NO --> **Neural mechanism.** When a circuit stores several coordinates, a spike can shift more than one of them. Comparing each coordinate separately would miss combinations of shifts. The information and diffusion must therefore describe these shared directions. <!-- vale ai-tells.FormalTransitions = YES -->

<!-- pedagogy-paragraph: p213 sha256 fceec106a7e0f25d5b59aac998cca0a71174e77422d3012f014b69ed70d80533 -->
p213, lines 213-213; prose; priority: unchanged; previous: p209; next: p221

> **Mathematical derivation.** For $m$ memory coordinates the information is a matrix,

<!-- pedagogy-paragraph: p221 sha256 0c6684840dd06316c71d8749cc327a35585fb933353edcb9b10fa6b7584a85b3 -->
p221, lines 221-221; prose; priority: unchanged; previous: p213; next: p229

> The matrix calculation assumes that every independent small coordinate change can be distinguished through a change in rates, so $J$ is invertible. The matrix bound $2D\succeq\tau^{-2}J^{-1}$ means that every linear combination of coordinate displacements obeys the corresponding variance lower bound. Here $A\succeq B$ means $\mathbf z^T(A-B)\mathbf z\ge0$ for every real vector $\mathbf z$. To derive it, form $N\times m$ matrices $U_{i\alpha}=u_i^\alpha/\sqrt{\bar r_i}$ and $V_{i\alpha}=v_i^\alpha\sqrt{\bar r_i}$. Then

<!-- pedagogy-paragraph: p229 sha256 3ebe84417bb4edca036016b413a1e0ee2b9de9642f60067fe5349d0c07c669dc -->
p229, lines 229-229; prose; priority: unchanged; previous: p221; next: p238

> Set $Q=V-U(U^TU)^{-1}$. Expanding $Q^TQ$ and using $U^TV=I$ gives

<!-- pedagogy-paragraph: p238 sha256 1e87dbbf2dd52cc0e555cb60ae4b3b99285b3af3cf2ef19562216863a8427e82 -->
p238, lines 238-238; prose; priority: unchanged; previous: p229; next: p240

> **Interpretation.** The bound controls every combination of stored coordinates, including coupled directions that separate scalar bounds would miss. If $J$ is singular, this ordinary inverse formula cannot be used.[^p1-matrix]

<!-- pedagogy-paragraph: p240 sha256 c2316ffd5a6eb7c065f07757406f4f87a1ca5abadac61a703068036a50a6d8f5 -->
p240, lines 240-242; prose; priority: unchanged; previous: p238; next: p244

> <!-- vale ai-tells.BareHolds = NO --> <!-- vale ai-tells.ExplainerHeadings = NO --> <!-- vale ai-tells.FigurativeHolds = NO -->


Claim-bearing content: figure

Claims to check:

- Claim c1, line 96: "$$ 2D=\sum_i v_i^2\bar r_i, \qquad u_i=\tau r_i', \qquad \sum_i v_i u_i=1. $$" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c2, line 110: "<!-- vale ai-tells.FormalTransitions = NO --> Their squared lengths are $\sum_i a_i^2=2D$ and $\sum_i b_i^2=J$." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c3, line 114: "$$ \left(\frac1\tau\right)^2 \le\left(\sum_i a_i^2\right)\left(\sum_i b_i^2\right)=2DJ, $$" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c4, line 125: "It is a shorter teaching reconstruction of the scalar proof in SI Section V." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c5, line 125: "It is not a general statement about all possible noisy memory systems.[^p1-bound-source] <!-- vale ai-tells.AnthropomorphicCognition = YES -->" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c6, line 129: "[Small internal information forces a large minimum diffusion coefficient." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c7, line 129: "Large information allows small diffusion, but does not guarantee it.]{.key-statement}" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c8, line 131: "**Neural mechanism.** [Reaching the bound requires the network's retained response to each cell's spike noise to match that cell's information about memory.]{.key-statement} A cell that adds retained noise without helping distinguish nearby values prevents equality." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c9, line 135: "$$ v_i=c\frac{r_i'}{\bar r_i} \quad\text{for every contributing cell}, \qquad c=\frac{1}{\tau J}. $$" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c10, line 141: "<!-- vale ai-tells.FormalTransitions = NO --> Cells with zero tuning slope cannot contribute extra projected noise if equality is to hold." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c11, line 151: "It is a sufficient condition, rather than a general necessity: the common ratio may depend on the current memory state.[^p1-equality]" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c12, line 155: "Set its bias $b_0=0$ and use the linear rule $\phi(g)=g/\tau$ on positive inputs." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c13, line 155: "Its fixed states are $s_1=s_2=\theta>0$, with $\mathbf u=(1,1)^T$ and $\mathbf v=(1/2,1/2)^T$." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c14, line 155: "Both rates are $\theta/\tau$, and both rate derivatives are $1/\tau$." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c15, line 165: "At each state both cells receive the same input, and the ratio $\phi'/\phi=1/\theta$ changes between states." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c16, line 165: "The information–diffusion inequality remains unchanged. <!-- vale ai-tells.EmDashUsage = YES --> <!-- vale ai-tells.ConclusionMarkers = YES -->" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c17, line 173: "<div class="publisher-worked-calculation publisher-fold-always">" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c18, line 177: "<!-- vale ai-tells.ContrastiveFormulas = NO --> <!-- vale ai-tells.FormalTransitions = NO --> In the two cell mutual inhibition model, use $b=200$ activation units and $\tau=0.1\,\mathrm{s}$." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c19, line 177: "At $\theta=0$ both rates are $1000\,\mathrm{s}^{-1}$ and their slopes are $\pm5\,\mathrm{s}^{-1}$ per activation unit." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c20, line 183: "$$ J=\frac{25}{1000}+\frac{25}{1000}=0.05, \qquad D=\frac{b}{2\tau}=1000. $$" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c21, line 188: "The bound is $1/(2\tau^2J)=1000$, so equality holds at this balanced state." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c22, line 188: "At $\theta=100$, the rates become $1500$ and $500\,\mathrm{s}^{-1}$, while their slopes stay $\pm5$." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c23, line 190: "$$ J=\frac{25}{1500}+\frac{25}{500}=\frac1{15}\simeq0.06667, \qquad \frac1{2\tau^2J}=750. $$" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c24, line 195: "The actual diffusion remains $1000$." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c25, line 201: "Caption: Analytic teaching calculation for the chapter’s mutual inhibition example, with $b=200$ activation units and $\tau=0.1$ s. The coordinate $\theta$ is an activation difference. For positive rates $r_{1,2}=(b\pm\theta)/(2\tau)$, $J=2000/(40000-\theta^2)$ while $D=1000$ activation units squ..." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c26, line 205: "The gap at $\theta=100$ shows why a lower minimum allowed by the inequality is not a reduction in the network’s actual diffusion." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c27, line 205: "See [Diffusion bound, Eq. 4, p. 3](../papers/burak-fiete-2012-persistent-activity.pdf#page=3)." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c28, line 209: "The information and diffusion must therefore describe these shared directions. <!-- vale ai-tells.FormalTransitions = YES -->" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c29, line 221: "The matrix calculation assumes that every independent small coordinate change can be distinguished through a change in rates, so $J$ is invertible." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c30, line 221: "The matrix bound $2D\succeq\tau^{-2}J^{-1}$ means that every linear combination of coordinate displacements obeys the corresponding variance lower bound." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c31, line 221: "Here $A\succeq B$ means $\mathbf z^T(A-B)\mathbf z\ge0$ for every real vector $\mathbf z$." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c32, line 223: "$$ U^TV=I,\qquad U^TU=\tau^2J,\qquad V^TV=2D. $$" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c33, line 229: "Set $Q=V-U(U^TU)^{-1}$." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c34, line 231: "$$ Q^TQ=V^TV-(U^TU)^{-1} =2D-\tau^{-2}J^{-1}\succeq0. $$" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c35, line 238: "**Interpretation.** The bound controls every combination of stored coordinates, including coupled directions that separate scalar bounds would miss." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c36, line 238: "If $J$ is singular, this ordinary inverse formula cannot be used.[^p1-matrix]" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]

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

Location: line 243, anchor `sec:MEMORY-COMPARISONS`

First content kind: `prose`

Opening passage line: 244
Closing passage line: 373

Paragraphs in source order (complete `PARAGRAPH_REVIEW.json`):

<!-- pedagogy-paragraph: p244 sha256 e5313e0692592591abd1819045b739104a24c94bdbe7774dda18c3202d698798 -->
p244, lines 244-246; prose; priority: unchanged; previous: p240; next: p248

> <!-- vale ai-tells.FigurativeHolds = YES --> <!-- vale ai-tells.ExplainerHeadings = YES --> <!-- vale ai-tells.BareHolds = YES -->

<!-- pedagogy-paragraph: p248 sha256 10b1e44529cf15d3c1594bd1f3f169a60b76f9dd6dc29e5a0c9bb2853ead93df -->
p248, lines 248-252; prose; priority: unchanged; previous: p244; next: p254

> <!-- vale ai-tells.FigurativeStays = NO --> <!-- vale ai-tells.HedgingPhrases = NO --> **Neural mechanism.** [The inequality compares diffusion and information for the same network. To compare different networks, we must say what stays fixed.]{.key-statement} Otherwise an apparent benefit of a parameter change may come from changing another property at the same time. The comparisons below control how added neurons, altered firing rates, or slower synaptic decay affect the tuning curves and recurrent input. <!-- vale ai-tells.HedgingPhrases = YES --> <!-- vale ai-tells.FigurativeStays = YES -->

<!-- pedagogy-paragraph: p254 sha256 87b69d067f665bd12ea4db31917eec5cc41a4df195dc18ae2f19666f7676517c -->
p254, lines 254-258; prose; priority: unchanged; previous: p248; next: p260

> <!-- vale ai-tells.ContrastiveFormulas = NO --> <!-- vale ai-tells.FormalTransitions = NO --> **Mathematical derivation.** Increasing $N$ while retaining the same distribution of tuning curves and scaling weights as $1/N$ keeps individual inputs and rates fixed. The sums in the symmetric formula scale as $N$ in the numerator and $N^2$ in the denominator. Consequently $D\propto1/N$, while $J\propto N$. This is a controlled density or population replication comparison, not a promise about adding arbitrary neurons. <!-- vale ai-tells.FormalTransitions = YES --> <!-- vale ai-tells.ContrastiveFormulas = YES -->

<!-- pedagogy-paragraph: p260 sha256 1321b00b920330fee1ccaeed4ef60a07818b3266fea1fece4a7328e8b3332312 -->
p260, lines 260-260; prose; priority: unchanged; previous: p254; next: p262

> If all tuning rates are multiplied by a factor $a$, their slopes are also multiplied by $a$, so $J\mapsto aJ$. For equality achieving exponential networks, $D\mapsto D/a$ immediately follows. The same scaling follows from the symmetric diffusion formula when the change preserves $g_i'$ up to a common scale and preserves the tuning geometry. For a general fixed nonlinear transfer rule, multiplying rates need not preserve those quantities or even the attractor. The paper's rate comparison is made with the tuning shapes and appropriate network scaling held under control.[^p1-scaling]

<!-- pedagogy-paragraph: p262 sha256 4f4c961abbf14ae086d79e86da928ac1e337a84592d5eb20ae6a5dc1e2e902c8 -->
p262, lines 262-262; prose; priority: unchanged; previous: p260; next: p264

> Changing $\tau$ while holding the rate tuning curves and their input relation fixed gives $D\propto\tau^{-2}$ in the symmetric formula. Maintaining those curves requires retuning the network, because $\bar s=\tau\bar r$.

<!-- pedagogy-paragraph: p264 sha256 ff6a98f6994fcfd8376988b2675a2bbfbceb76b5469f2f74a251abc9369b174c -->
p264, lines 264-268; prose; priority: unchanged; previous: p262; next: p270

> <!-- vale ai-tells.FigurativeStays = NO --> <!-- vale ai-tells.FormalTransitions = NO --> At fixed rates, longer-lasting spike effects give larger mean activations. The activation difference between two nearby stored values also grows in proportion to $\tau$. In this symmetric comparison, one spike's unit activation change therefore produces a smaller displacement of the stored value: the projection weights scale as $1/\tau$. The spike variance per unit time stays fixed, so the retained variance scales as $1/\tau^2$. <!-- vale ai-tells.FormalTransitions = YES --> <!-- vale ai-tells.FigurativeStays = YES -->

<!-- pedagogy-paragraph: p270 sha256 fa1e0ed31be98d15306a0ab7fb9e51abe114abe1a98e429fdb431467c89e58e0 -->
p270, lines 270-272; prose; priority: unchanged; previous: p264; next: p274

> <!-- vale ai-tells.FormalTransitions = NO --> In contrast, holding activation curves and dimensionless weights fixed in the linear two cell example makes rates scale as $1/\tau$, so $D=b/(2\tau)\propto\tau^{-1}$. <!-- vale ai-tells.FormalTransitions = YES -->

<!-- pedagogy-paragraph: p274 sha256 541c662e707758052e1f2ef1bc3a3af766c192797163510bed81a5e96185e242 -->
p274, lines 274-274; prose; priority: unchanged; previous: p270; next: p276

> **Interpretation.** These two statements concern different controlled comparisons. A larger cellular time constant can improve memory stability while the exponent of its effect depends on what the experiment keeps fixed.

<!-- pedagogy-paragraph: p276 sha256 33536c5cc6e06bb21737ca94caf916f5bc9f5b8f77170fa92ed5b46e53c61c30 -->
p276, lines 276-280; prose; priority: unchanged; previous: p274; next: p282

> <!-- vale ai-tells.AnthropomorphicCognition = NO --> <!-- vale ai-tells.StrawmanContrast = NO --> **Neural mechanism.** The paper also links tuning width to memory persistence. The reason for its opposite predictions in one and three dimensions can be derived from the number of active cells and their slopes. This derivation is a teaching reconstruction of the tuning width argument cited in the main text, rather than a proof that every tuning family follows one power law.[^p1-width] <!-- vale ai-tells.StrawmanContrast = YES --> <!-- vale ai-tells.AnthropomorphicCognition = YES -->

<!-- pedagogy-paragraph: p282 sha256 4ec9786980965a1ab2cbe0f2dabf4b275835f6ac725ca92d14d00201ce370f5d -->
p282, lines 282-282; prose; priority: unchanged; previous: p276; next: p289

> Assume preferred positions $\mathbf c$ have uniform density $\rho$ in a $d$ dimensional stimulus or memory space. Away from boundaries, let identical tuning curves have fixed peak rate $a$ and a common shape $f$:

<!-- pedagogy-paragraph: p289 sha256 b83b728067569418eb10647f858460bb3183d7c2d0d5c8dba7be6140b515e538 -->
p289, lines 289-289; prose; priority: unchanged; previous: p282; next: p291

> The width $w$ is varied while $a$, $\rho$, and the shape $f$ are fixed.

<!-- pedagogy-paragraph: p291 sha256 3d9c0c2398aec08799aa8ada6738de57516cd5f1fddb71d6d359743dd0e95c47 -->
p291, lines 291-291; prose; priority: unchanged; previous: p289; next: p301

> **Mathematical derivation.** For one coordinate direction $\alpha$, replace the population sum by an integral and substitute $\mathbf z=(\boldsymbol\theta-\mathbf c)/w$:

<!-- pedagogy-paragraph: p301 sha256 4fcd335e5ea5e5b5e4d6de098c25ab9b7b5dadc6b97f0b59862278409cfc4b7c -->
p301, lines 301-303; prose; priority: unchanged; previous: p291; next: p305

> <!-- vale ai-tells.CataphoricForecasting = NO --> Two factors determine how information changes with tuning width: <!-- vale ai-tells.CataphoricForecasting = YES -->

<!-- pedagogy-paragraph: p305 sha256 a6d7c88d5dcfaf936b3c4f4528da08eeea73202aa54dcfb98d0bbf872f6c339e -->
p305, lines 305-305; list_item; priority: unchanged; previous: p301; next: p306

> The volume element contributes $w^d$ because broader fields recruit more neurons.

<!-- pedagogy-paragraph: p306 sha256 ab0b63ce72cafdb9fc8796cf4e226baf8dd46ad9ea8659f5be81aef6f2ed3621 -->
p306, lines 306-306; list_item; priority: unchanged; previous: p305; next: p308

> The squared slope contributes $w^{-2}$ because broader curves change more slowly.

<!-- pedagogy-paragraph: p308 sha256 330ea61cde1f5620b86a95949380dd56c27b7bf9120064166b6365020d4df1ae -->
p308, lines 308-310; prose; priority: unchanged; previous: p306; next: p312

> <!-- vale ai-tells.FormalTransitions = NO --> Each diagonal entry therefore scales as $J_{\alpha\alpha}\propto w^{d-2}$. Now restrict the tuning shape $f$ to depend only on distance from its center. Uniformly distributing those centers makes every coordinate direction equivalent: off-diagonal information terms vanish, and all diagonal entries are equal. For an exponential network that attains the matrix bound, $D_{\alpha\alpha}=1/(2\tau^2J_{\alpha\alpha})\propto w^{2-d}$. <!-- vale ai-tells.FormalTransitions = YES -->

<!-- pedagogy-paragraph: p312 sha256 8eea96df128371006e6cb6706f0c036aa3cc07fb79da7b0546bda90cbe3b7b10 -->
p312, lines 312-312; prose; priority: unchanged; previous: p308; next: p314

> **Interpretation.** The resulting comparisons are:

<!-- pedagogy-paragraph: p314 sha256 84ef728d20e64e01bb1f04ffb6ff45fbfaca3a0c072f45f3dde4389d1dd7a179 -->
p314, lines 314-314; list_item; priority: unchanged; previous: p312; next: p315

> Narrower curves help in $d=1$.

<!-- pedagogy-paragraph: p315 sha256 df3c4bfa25c1b3d2285ae09eca3f69a0dae5c185411a8f1041d476cb67126801 -->
p315, lines 315-315; list_item; priority: unchanged; previous: p314; next: p316

> Width has no leading effect in $d=2$.

<!-- pedagogy-paragraph: p316 sha256 abe1badbcc8962e249e45920a9b75890735b8a4d0a67a4880dc1c49174d2ed00 -->
p316, lines 316-316; list_item; priority: unchanged; previous: p315; next: p318

> Broader curves help in $d=3$.

<!-- pedagogy-paragraph: p318 sha256 3abe9786133dc3fce6afecec77445cf0eaabb80f6bd7332edc71f3078924c23b -->
p318, lines 318-320; prose; priority: unchanged; previous: p316; next: p322

> <!-- vale ai-tells.BareReaches = NO --> [These conclusions change under another resource constraint. Fixing the total population spike rate instead of peak rate makes $a\propto w^{-d}$, giving $J\propto w^{-2}$ in every dimension.]{.key-statement} Sparse coverage, a large baseline rate, finite boundaries, correlated noise, or a width too small for the population integral can also change the comparison. Attaining equality means the network reaches the diffusion lower bound for its information rate and synaptic time constant. Minimizing diffusion still requires deciding how much information the allowed architecture and firing budget can supply. <!-- vale ai-tells.BareReaches = YES -->

<!-- pedagogy-paragraph: p322 sha256 b40fb08d5b3b6c94414213cea91c17ebc16076bc0a2c652aac56b5d81b3192a3 -->
p322, lines 322-330; prose; priority: unchanged; previous: p318; next: p332

> <!-- vale ai-tells.EmptyPadding = NO --> <!-- vale ai-tells.ExplainerLeads = NO --> <!-- vale ai-tells.FormalTransitions = NO --> <!-- vale ai-tells.ParallelStaccato = NO --> If an external stimulus produces the same tuning curves as the network's input free memory states, the sensory and internal Fisher information are equal. In a symmetric exponential network, maximizing this information then improves sensory estimation and minimizes memory diffusion together. This is why the paper suggests that one circuit could support both sensory estimation and memory storage. The mathematical compatibility does not establish where a particular animal stores a memory, and the equality of tuning curves must be checked rather than inferred from the shared formula.[^p1-colocation] <!-- vale ai-tells.ParallelStaccato = YES --> <!-- vale ai-tells.FormalTransitions = YES --> <!-- vale ai-tells.ExplainerLeads = YES --> <!-- vale ai-tells.EmptyPadding = YES -->

<!-- pedagogy-paragraph: p332 sha256 c434e91454241a31e310a239ac3a093d91ab1fcd15b7ac3b333458ba63f49376 -->
p332, lines 332-332; prose; priority: unchanged; previous: p322; next: p334

> <!-- vale ai-tells.EmDashUsage = NO -->

<!-- pedagogy-paragraph: p334 sha256 6e36e79bce1447ac7eddc2fb19787ace984308e97fbb90fe3fbe309f14b460ff -->
p334, lines 334-334; prose; priority: unchanged; previous: p332; next: p336

> <!-- vale ai-tells.EmDashUsage = YES -->

<!-- pedagogy-paragraph: p336 sha256 c434e91454241a31e310a239ac3a093d91ab1fcd15b7ac3b333458ba63f49376 -->
p336, lines 336-336; prose; priority: unchanged; previous: p334; next: p338

> <!-- vale ai-tells.EmDashUsage = NO -->

<!-- pedagogy-paragraph: p338 sha256 6e36e79bce1447ac7eddc2fb19787ace984308e97fbb90fe3fbe309f14b460ff -->
p338, lines 338-338; prose; priority: unchanged; previous: p336; next: p340

> <!-- vale ai-tells.EmDashUsage = YES -->

<!-- pedagogy-paragraph: p340 sha256 a68eb38b79889b460002793b1ff6a14f5133e7f51c1c8e5f424c4a668a7bf4c7 -->
p340, lines 340-340; prose; priority: unchanged; previous: p338; next: p342

> <!-- vale ai-tells.AnthropomorphicCognition = NO -->

<!-- pedagogy-paragraph: p342 sha256 07d5c635bbd45ea7a4d2841a27ffd89a0a0bd304c283ec3e8d617fdc3e778cc4 -->
p342, lines 342-342; prose; priority: unchanged; previous: p340; next: p344

> <!-- vale ai-tells.AnthropomorphicCognition = YES -->

<!-- pedagogy-paragraph: p344 sha256 c434e91454241a31e310a239ac3a093d91ab1fcd15b7ac3b333458ba63f49376 -->
p344, lines 344-344; prose; priority: unchanged; previous: p342; next: p346

> <!-- vale ai-tells.EmDashUsage = NO -->

<!-- pedagogy-paragraph: p346 sha256 6e36e79bce1447ac7eddc2fb19787ace984308e97fbb90fe3fbe309f14b460ff -->
p346, lines 346-346; prose; priority: unchanged; previous: p344; next: p348

> <!-- vale ai-tells.EmDashUsage = YES -->

<!-- pedagogy-paragraph: p348 sha256 c434e91454241a31e310a239ac3a093d91ab1fcd15b7ac3b333458ba63f49376 -->
p348, lines 348-348; prose; priority: unchanged; previous: p346; next: p350

> <!-- vale ai-tells.EmDashUsage = NO -->

<!-- pedagogy-paragraph: p350 sha256 6e36e79bce1447ac7eddc2fb19787ace984308e97fbb90fe3fbe309f14b460ff -->
p350, lines 350-350; prose; priority: unchanged; previous: p348; next: p352

> <!-- vale ai-tells.EmDashUsage = YES -->

<!-- pedagogy-paragraph: p352 sha256 2139b3f6693ec084037797db2d5af08c75595d3c10e042fc61ad7e76e942f2c1 -->
p352, lines 352-353; prose; priority: unchanged; previous: p350; next: p355

> <!-- vale ai-tells.AnthropomorphicCognition = NO --> <!-- vale ai-tells.EmDashUsage = NO -->

<!-- pedagogy-paragraph: p355 sha256 fb62b1024cd03e292e79a9b6791592f9a6038ef448a6929b919813c2ff2129fe -->
p355, lines 355-356; prose; priority: unchanged; previous: p352; next: p358

> <!-- vale ai-tells.EmDashUsage = YES --> <!-- vale ai-tells.AnthropomorphicCognition = YES -->

<!-- pedagogy-paragraph: p358 sha256 72fb9debbff6b02f5de0f17c603a3aa9b077a0b677b3227f9256736ccfda428a -->
p358, lines 358-359; prose; priority: unchanged; previous: p355; next: p361

> <!-- vale ai-tells.EmDashUsage = NO --> <!-- vale ai-tells.SemicolonUsage = NO -->

<!-- pedagogy-paragraph: p361 sha256 bf506d6f58cf686fa691df4ec9911b976f18e4d4c4e2ebf1dade6fe5b93b6120 -->
p361, lines 361-362; prose; priority: unchanged; previous: p358; next: p364

> <!-- vale ai-tells.SemicolonUsage = YES --> <!-- vale ai-tells.EmDashUsage = YES -->

<!-- pedagogy-paragraph: p364 sha256 2139b3f6693ec084037797db2d5af08c75595d3c10e042fc61ad7e76e942f2c1 -->
p364, lines 364-365; prose; priority: unchanged; previous: p361; next: p367

> <!-- vale ai-tells.AnthropomorphicCognition = NO --> <!-- vale ai-tells.EmDashUsage = NO -->

<!-- pedagogy-paragraph: p367 sha256 fb62b1024cd03e292e79a9b6791592f9a6038ef448a6929b919813c2ff2129fe -->
p367, lines 367-368; prose; priority: unchanged; previous: p364; next: p370

> <!-- vale ai-tells.EmDashUsage = YES --> <!-- vale ai-tells.AnthropomorphicCognition = YES -->

<!-- pedagogy-paragraph: p370 sha256 72fb9debbff6b02f5de0f17c603a3aa9b077a0b677b3227f9256736ccfda428a -->
p370, lines 370-371; prose; priority: unchanged; previous: p367; next: p373

> <!-- vale ai-tells.EmDashUsage = NO --> <!-- vale ai-tells.SemicolonUsage = NO -->

<!-- pedagogy-paragraph: p373 sha256 bf506d6f58cf686fa691df4ec9911b976f18e4d4c4e2ebf1dade6fe5b93b6120 -->
p373, lines 373-374; prose; priority: unchanged; previous: p370; next: none

> <!-- vale ai-tells.SemicolonUsage = YES --> <!-- vale ai-tells.EmDashUsage = YES -->


Claim-bearing content: none

Claims to check:

- Claim c1, line 248: "To compare different networks, we must say what stays fixed.]{.key-statement} Otherwise an apparent benefit of a parameter change may come from changing another property at the same time." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c2, line 254: "<!-- vale ai-tells.ContrastiveFormulas = NO --> <!-- vale ai-tells.FormalTransitions = NO --> **Mathematical derivation.** Increasing $N$ while retaining the same distribution of tuning curves and scaling weights as $1/N$ keeps individual inputs and rates fixed." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c3, line 254: "Consequently $D\propto1/N$, while $J\propto N$." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c4, line 260: "The paper's rate comparison is made with the tuning shapes and appropriate network scaling held under control.[^p1-scaling]" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c5, line 262: "Changing $\tau$ while holding the rate tuning curves and their input relation fixed gives $D\propto\tau^{-2}$ in the symmetric formula." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c6, line 264: "In this symmetric comparison, one spike's unit activation change therefore produces a smaller displacement of the stored value: the projection weights scale as $1/\tau$." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c7, line 264: "The spike variance per unit time stays fixed, so the retained variance scales as $1/\tau^2$. <!-- vale ai-tells.FormalTransitions = YES --> <!-- vale ai-tells.FigurativeStays = YES -->" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c8, line 270: "<!-- vale ai-tells.FormalTransitions = NO --> In contrast, holding activation curves and dimensionless weights fixed in the linear two cell example makes rates scale as $1/\tau$, so $D=b/(2\tau)\propto\tau^{-1}$. <!-- vale ai-tells.FormalTransitions = YES -->" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c9, line 276: "This derivation is a teaching reconstruction of the tuning width argument cited in the main text, rather than a proof that every tuning family follows one power law.[^p1-width] <!-- vale ai-tells.StrawmanContrast = YES --> <!-- vale ai-tells.AnthropomorphicCognition = YES -->" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c10, line 293: "$$ J_{\alpha\alpha} \simeq\rho\int d^d c\, \frac{a^2w^{-2}(\partial_\alpha f)^2}{af} =\rho a w^{d-2} \int d^d z\,\frac{(\partial_\alpha f)^2}{f}. $$" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c11, line 306: "The squared slope contributes $w^{-2}$ because broader curves change more slowly." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c12, line 308: "<!-- vale ai-tells.FormalTransitions = NO --> Each diagonal entry therefore scales as $J_{\alpha\alpha}\propto w^{d-2}$." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c13, line 308: "Now restrict the tuning shape $f$ to depend only on distance from its center." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c14, line 308: "Uniformly distributing those centers makes every coordinate direction equivalent: off-diagonal information terms vanish, and all diagonal entries are equal." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c15, line 308: "For an exponential network that attains the matrix bound, $D_{\alpha\alpha}=1/(2\tau^2J_{\alpha\alpha})\propto w^{2-d}$. <!-- vale ai-tells.FormalTransitions = YES -->" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c16, line 314: "Narrower curves help in $d=1$." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c17, line 315: "Width has no leading effect in $d=2$." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c18, line 316: "Broader curves help in $d=3$." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c19, line 318: "Fixing the total population spike rate instead of peak rate makes $a\propto w^{-d}$, giving $J\propto w^{-2}$ in every dimension.]{.key-statement} Sparse coverage, a large baseline rate, finite boundaries, correlated noise, or a width too small for the population integral can also change the comp..." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c20, line 322: "The mathematical compatibility does not establish where a particular animal stores a memory, and the equality of tuning curves must be checked rather than inferred from the shared formula.[^p1-colocation] <!-- vale ai-tells.ParallelStaccato = YES --> <!-- vale ai-tells.FormalTransitions = YES -->..." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]

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

Purpose: Reading spikes from a memory circuit takes time, during which its stored value can keep changing. This chapter calculates how much longer observation can help recover the value present at a recall cue, and explains why it cannot recover every earlier random displacement.

Prerequisites: ch:MEMORY-INFORMATION

Sidecar sections: Storage loss and readout error add under specific assumptions, Equal weighting becomes harmful when observation lasts too long, Accounting for diffusion makes readout improve toward a limit, Limited access can make observation slower, Time scales and noise laws change the bound and its equality condition, Readout saturates, and one printed error bound needs qualification

Blocks: 4 figure(s), 0 equation(s), 0 code block(s)

Result labels: No Answer/Conclusion/Feedback label detected

<!-- pedagogy-unit: content/chapters/03b-memory-readout.md::ch:MEMORY-READOUT -->

### Chapter opening

Location: line 2, anchor `ch:MEMORY-READOUT`

First content kind: `prose`

Opening passage line: 3
Closing passage line: 11

Paragraphs in source order (complete `PARAGRAPH_REVIEW.json`):

<!-- pedagogy-paragraph: p3 sha256 a319bcf28c3fe4f18362415d6e8781649da362a187d570c6d533a56c6ede8760 -->
p3, lines 3-3; prose; priority: unchanged; previous: none; next: p5

> <!-- vale ai-tells.ExplainerHeadings = YES -->

<!-- pedagogy-paragraph: p5 sha256 f876f5f727108c327c5531b014552719ec32bbed9d4ebbf7f32fbd82e70bc567 -->
p5, lines 5-7; prose; priority: unchanged; previous: p3; next: p9

> <!-- vale ai-tells.EmptyPadding = NO --> When a recall cue arrives, the stored value has already moved. Later spikes can help estimate the value present at that cue, but they cannot reveal the particular random displacements that occurred before it. Waiting for more spikes also allows the network to move further. [The question is how much observation helps when the value being read keeps changing.]{.key-statement} <!-- vale ai-tells.EmptyPadding = YES -->

<!-- pedagogy-paragraph: p9 sha256 59030693eab1d4fc53491ddaaa84a0bf675d55f53f102f144e8a6341d38ef568 -->
p9, lines 9-9; prose; priority: unchanged; previous: p5; next: p11

> Separating the error accumulated during storage from the error of reading the cue state makes that question precise. Equal weighting of later observations shows why waiting can become harmful. Allowing for the state's motion then shows how observation can keep helping toward a limit, and how access to only some spikes changes the useful duration. The time constants and noise assumptions also need checking before the resulting limits can be compared with the paper's final error claim.

<!-- pedagogy-paragraph: p11 sha256 824f27b9cecc2ed6c660bb1a9a12080f495821617c9abf39dbd5f56fb6be2336 -->
p11, lines 11-13; prose; priority: unchanged; previous: p9; next: p17

> <!-- vale ai-tells.VerbTricolon = NO --> As before, the memory coordinate is $\theta$, its initial value is $\Theta$, and its displacement variance is $2Dt$ for constant diffusion coefficient $D$ without boundaries or systematic drift. The storage delay $T$ ends at the recall cue. The observation interval $L$ begins there. The [spike information rate $J$](ch-memory-information.html#sec-memory-fi) measures how clearly nearby present states can be distinguished, and $\tau$ is the basic model's common synaptic time constant. <!-- vale ai-tells.VerbTricolon = YES -->


Claim-bearing content: none

Claims to check:

- Claim c1, line 5: "Later spikes can help estimate the value present at that cue, but they cannot reveal the particular random displacements that occurred before it." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c2, line 9: "Allowing for the state's motion then shows how observation can keep helping toward a limit, and how access to only some spikes changes the useful duration." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]

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

Location: line 15, anchor `sec:MEMORY-READOUT-SETUP`

First content kind: `prose`

Opening passage line: 17
Closing passage line: 66

Paragraphs in source order (complete `PARAGRAPH_REVIEW.json`):

<!-- pedagogy-paragraph: p17 sha256 c5fc72d7fe50832c991e9d5da76d32d7db5db3670921f99ea02b5f4b4cb8c9a7 -->
p17, lines 17-17; prose; priority: unchanged; previous: p11; next: p19

> **Neural question and model.** At time $T$, a recall cue arrives. The observer must estimate the original value $\Theta$, but only has access to future spikes. The network has already diffused during storage.

<!-- pedagogy-paragraph: p19 sha256 a6962fd89ad1dcf8aedd7ac91b2ae530ff009fbf83e24c96b9926645672cbca3 -->
p19, lines 19-19; prose; priority: unchanged; previous: p17; next: p31

> To solve the readout problem, the supplement approximates the likelihood from each short bin of duration $h$ as Gaussian. Let $x=\theta(T)$ and index subsequent bins by $k$. The equivalent observation model is

<!-- pedagogy-paragraph: p31 sha256 1bad34a9d5290788c15d8e6e47b94916e94260fc3c7fe40f89c3990ae6fc52aa -->
p31, lines 31-33; prose; priority: unchanged; previous: p19; next: p35

> <!-- vale ai-tells.ParallelStaccato = NO --> The Gaussian increments and observation errors are independent in this approximation. The value $y_k$ summarizes information about the state from that bin's population spikes. It is not an additional directly measured physical coordinate. The continuous limit is a convenient mathematical description of the many spike, weak fluctuation regime. It does not assert that an arbitrarily short physical bin already contains enough spikes for a Gaussian fit. The derivations below are exact within this local Gaussian readout model.[^p1-read-gaussian] <!-- vale ai-tells.ParallelStaccato = YES -->

<!-- pedagogy-paragraph: p35 sha256 92d81c9e8abca464c240e056f3b2b60d41b2d9ddc1baead7bcb8fa6653621cb9 -->
p35, lines 35-35; prose; priority: unchanged; previous: p31; next: p43

> **Mathematical derivation.** For an unbounded coordinate with constant $D$ and no drift, let $x=\theta(T)$ and let $\widehat x$ estimate that state from later spikes. Write the storage displacement as $s=x-\Theta$ and the readout error as $e=\widehat x-x$. The total recall error is their sum:

<!-- pedagogy-paragraph: p43 sha256 0fe5e3f62da80211dd86be8624946df328f0b50a9b747022e365f3fa8ab235b2 -->
p43, lines 43-45; prose; priority: unchanged; previous: p35; next: p51

> <!-- vale ai-tells.FormalTransitions = NO --> Assume the readout is locally unbiased at every possible $x$ and the future noise is independent of the storage history. Conditional on that history, the readout error then has mean zero. Since $s$ is fixed by the history, $\mathbb E[se]=\mathbb E[s\,\mathbb E(e\mid\text{storage history})]=0$. Both errors have zero mean, so their covariance vanishes. [In this readout model, [**translation invariance**]{.definition-term custom-style="Definition Term"} means that shifting the represented value does not change the statistics of the readout error.]{.definition-explanation} Its variance is therefore the same at every $x$. Denote it by $V_{\mathrm{read}}(L)$. Using $\operatorname{Var}(s)=2DT$ gives <!-- vale ai-tells.FormalTransitions = YES -->

<!-- pedagogy-paragraph: p51 sha256 58e79d7af25b13212b534fac88ddf1990ea08fa56fad5aa6c205e32b3676265b -->
p51, lines 51-53; prose; priority: unchanged; previous: p43; next: p55

> <!-- vale ai-tells.CataphoricForecasting = NO --> **Interpretation.** The two terms describe different sources of error: <!-- vale ai-tells.CataphoricForecasting = YES -->

<!-- pedagogy-paragraph: p55 sha256 f459ad3a1a021b515af4f91f5dff132162c846c5d21b84e8626f271c44907a51 -->
p55, lines 55-55; list_item; priority: unchanged; previous: p51; next: p56

> $2DT$ comes from storage.

<!-- pedagogy-paragraph: p56 sha256 9dfb364848af2b364e5fc77e7e24766b7b8180c5a7d217ea21f8d8f5cece73c6 -->
p56, lines 56-56; list_item; priority: unchanged; previous: p55; next: p58

> $V_{\mathrm{read}}(L)$ concerns estimation of $\theta(T)$ from spikes after $T$.

<!-- pedagogy-paragraph: p58 sha256 daa47dcb132fbaf93a91740628bd6cbd80cc7057cb4018e82d51a2f27d9a7903 -->
p58, lines 58-58; prose; priority: unchanged; previous: p56; next: p60

> The supplement derives this decomposition for a locally translation invariant diffusion and readout model. State dependence, boundaries, informative priors, or uncertain initial encoding require corresponding changes.[^p1-read-setup]

<!-- pedagogy-paragraph: p60 sha256 4b36a2489b8b6a1ef4f20f37dd473a54057747f5babbcc9b1d88122fc98a08b2 -->
p60, lines 60-60; prose; priority: unchanged; previous: p58; next: p62

> A timeline separates the displacement accumulated before the cue from the error in estimating the cue state afterward.

<!-- pedagogy-paragraph: p62 sha256 2c643bd85d3e8933fd7127e586cd0d302d74dcd69d691fc3921ef217cc019e39 -->
p62, lines 62-62; prose; priority: unchanged; previous: p60; next: p66

> <div class="figure-scroll">

<!-- pedagogy-paragraph: p66 sha256 aac32651b10f567c461b9b4f255d6fb1fa6859b5368d8bd9a51af920ab21cf23 -->
p66, lines 66-66; prose; priority: unchanged; previous: p62; next: p72

> </div>


Claim-bearing content: figure

Claims to check:

- Claim c1, line 17: "The observer must estimate the original value $\Theta$, but only has access to future spikes." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c2, line 21: "$$ \theta_{k+1}=\theta_k+\eta_k, \qquad y_k=\theta_k+\epsilon_k, $$" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c3, line 26: "$$ \operatorname{Var}(\eta_k)=2Dh, \qquad \operatorname{Var}(\epsilon_k)=\frac1{Jh}. $$" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c4, line 31: "The derivations below are exact within this local Gaussian readout model.[^p1-read-gaussian] <!-- vale ai-tells.ParallelStaccato = YES -->" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c5, line 37: "$$ \widehat x-\Theta=s+e,\qquad \operatorname{Var}(s+e)=\operatorname{Var}(s)+\operatorname{Var}(e) +2\operatorname{Cov}(s,e). $$" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c6, line 43: "<!-- vale ai-tells.FormalTransitions = NO --> Assume the readout is locally unbiased at every possible $x$ and the future noise is independent of the storage history." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c7, line 43: "Since $s$ is fixed by the history, $\mathbb E[se]=\mathbb E[s\,\mathbb E(e\mid\text{storage history})]=0$." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c8, line 43: "[In this readout model, [**translation invariance**]{.definition-term custom-style="Definition Term"} means that shifting the represented value does not change the statistics of the readout error.]{.definition-explanation} Its variance is therefore the same at every $x$." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c9, line 43: "Using $\operatorname{Var}(s)=2DT$ gives <!-- vale ai-tells.FormalTransitions = YES -->" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c10, line 47: "$$ V_{\mathrm{total}}(T,L)=2DT+V_{\mathrm{read}}(L). $$" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c11, line 58: "State dependence, boundaries, informative priors, or uncertain initial encoding require corresponding changes.[^p1-read-setup]" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c12, line 64: "Caption: Original guide construction of storage and cue state readout, based on Burak and Fiete (2012), Supporting Text, p. 12, Eq. S57. The illustrated path is one possible construction, and the orange estimate concerns the state at the cue rather than the state at the end of observation. With t..." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]

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

Location: line 70, anchor `sec:MEMORY-NAIVE`

First content kind: `prose`

Opening passage line: 72
Closing passage line: 125

Paragraphs in source order (complete `PARAGRAPH_REVIEW.json`):

<!-- pedagogy-paragraph: p72 sha256 3ec9e8294969d19195d8bfa74a0b3216c738d6694e15655750d47a2c72d858e9 -->
p72, lines 72-72; prose; priority: unchanged; previous: p66; next: p74

> **Neural question and model.** A decoder designed for a stationary state averages its observations with equal weight. That reduces independent observation noise, but late observations reflect a state that has moved further from $x$.

<!-- pedagogy-paragraph: p74 sha256 f24d141e7fbe8272f6738a633e91ffb2507747a7da6c05e2f2a9495c8d060b2d -->
p74, lines 74-74; prose; priority: unchanged; previous: p72; next: p80

> **Mathematical derivation.** Write $\theta(T+t)=x+B_D(t)$, where $B_D$ has Brownian covariance

<!-- pedagogy-paragraph: p80 sha256 621aeaafc66d672886b5101b551c746c026f13ee783cb41ec29148e47d490899 -->
p80, lines 80-80; prose; priority: unchanged; previous: p74; next: p86

> The covariance arises because the two values share increments up to the earlier time. Their later increments are independent. The continuous average is

<!-- pedagogy-paragraph: p86 sha256 275eb9fc796445fb7a0be35d4ca97785c2be69f0d7ee9ba355e24e26e367eb68 -->
p86, lines 86-86; prose; priority: unchanged; previous: p80; next: p92

> Count noise contributes $1/(JL)$: $n=L/h$ bins, each of variance $1/(Jh)$, give average variance $[n/(Jh)]/n^2=1/(JL)$. The motion contribution is

<!-- pedagogy-paragraph: p92 sha256 ac49cc7b5c1440cf04c5ba1b746799cdb3838d03ddf8919ecd663c13ed7b6868 -->
p92, lines 92-94; prose; priority: unchanged; previous: p86; next: p102

> <!-- vale ai-tells.FormalTransitions = NO --> Split the square into its two equal triangles. On the triangle $0\le s\le t\le L$, the minimum is $s$. Therefore <!-- vale ai-tells.FormalTransitions = YES -->

<!-- pedagogy-paragraph: p102 sha256 ba69c22f467e0337d40fed4f0dc8d8e1ebc46d11e38828df6b4efe7e734affcd -->
p102, lines 102-102; prose; priority: unchanged; previous: p92; next: p108

> Combining the terms gives

<!-- pedagogy-paragraph: p108 sha256 4030934ba86d700fa34ecb5d2b4467d4808d8c574748d4351695872c9e125f21 -->
p108, lines 108-110; prose; priority: unchanged; previous: p102; next: p118

> <!-- vale ai-tells.CataphoricForecasting = NO --> The two contributions have opposite dependence on $L$. Differentiating, <!-- vale ai-tells.CataphoricForecasting = YES -->

<!-- pedagogy-paragraph: p118 sha256 0745849b93458f3c978bafcc6900eb5228e0b7a4d9d772df43a0ec943ac2aca9 -->
p118, lines 118-118; prose; priority: unchanged; previous: p108; next: p125

> At that duration the two error terms are equal, and

<!-- pedagogy-paragraph: p125 sha256 de53411e75a1f78addf0c49f319aa80349e359b0451a72ea06076083bf1fd70e -->
p125, lines 125-125; prose; priority: unchanged; previous: p118; next: p129

> **Interpretation.** [Waiting longer eventually increases error, even with more spikes available. The problem is their equal weighting for a moving state.]{.key-statement}[^p1-naive]


Claim-bearing content: none

Claims to check:

- Claim c1, line 76: "$$ E[B_D(t)B_D(s)]=2D\min(t,s). $$" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c2, line 86: "Count noise contributes $1/(JL)$: $n=L/h$ bins, each of variance $1/(Jh)$, give average variance $[n/(Jh)]/n^2=1/(JL)$." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c3, line 96: "$$ \int_0^L\int_0^L\min(t,s)\,dt\,ds =2\int_0^L\!dt\int_0^t\!s\,ds =\int_0^L t^2dt=\frac{L^3}{3}. $$" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c4, line 112: "$$ \frac{dV_{\mathrm{naive}}}{dL}=\frac{2D}{3}-\frac1{JL^2}=0 \quad\Longrightarrow\quad L_{\mathrm{naive}}^*=\sqrt{\frac3{2DJ}}. $$" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c5, line 125: "The problem is their equal weighting for a moving state.]{.key-statement}[^p1-naive]" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]

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

Location: line 127, anchor `sec:MEMORY-IDEAL`

First content kind: `prose`

Opening passage line: 129
Closing passage line: 227

Paragraphs in source order (complete `PARAGRAPH_REVIEW.json`):

<!-- pedagogy-paragraph: p129 sha256 deef15bb0c9033c2b342765054646b2239258a366d1587600efce32eb0a9ec88 -->
p129, lines 129-131; prose; priority: unchanged; previous: p125; next: p133

> <!-- vale ai-tells.ParallelStaccato = NO --> **Neural question and model.** An observer that accounts for diffusion can use later observations without confusing them with direct measurements of $x$. Their value is limited by the motion separating them from $x$. This is an ideal inference rule for an observer. The readout calculation does not demonstrate a neural circuit implementing it. Its error can be derived by combining information backward from the end of the observation interval. <!-- vale ai-tells.ParallelStaccato = YES -->

<!-- pedagogy-paragraph: p133 sha256 621d04ffdffc710c0f9c4f94c7c79cbb0caf43228e56aa684fc6f617f3dc79e8 -->
p133, lines 133-133; prose; priority: unchanged; previous: p129; next: p135

> **Mathematical derivation.** [The [**precision**]{.definition-term custom-style="Definition Term"} of a scalar Gaussian estimate is the reciprocal of its variance.]{.definition-explanation} Independent Gaussian measurements of one value add precisions. To verify this, multiply likelihoods proportional to $\exp[-(x-a)^2/(2V_a)]$ and $\exp[-(x-b)^2/(2V_b)]$: the coefficient of $x^2/2$ becomes $1/V_a+1/V_b$.

<!-- pedagogy-paragraph: p135 sha256 210394cbe30fd28e9b1a286d2192dc19db475af862a86866f28d881cd0dce8c4 -->
p135, lines 135-137; prose; priority: unchanged; previous: p133; next: p143

> <!-- vale ai-tells.FormalTransitions = NO --> Let $P(L)$ be the precision about the state at the beginning of an interval of length $L$, using all observations in that interval and no informative prior. Suppose we have already compressed the later part into a likelihood about the next bin's state with variance $1/P$. Bringing that likelihood one step backward adds transition variance $q=2Dh$, since the next state equals the earlier state plus an independent Gaussian increment. Its precision about the earlier state is therefore <!-- vale ai-tells.FormalTransitions = YES -->

<!-- pedagogy-paragraph: p143 sha256 6f2c5e969e6a93de3c5012717a12d884def914ec816bc7ed5520a7fd33b495f0 -->
p143, lines 143-145; prose; priority: unchanged; previous: p135; next: p151

> <!-- vale ai-tells.FormalTransitions = NO --> The new earliest observation adds precision $Jh$. Thus, up to bin endpoint conventions that disappear as $h\to0$, <!-- vale ai-tells.FormalTransitions = YES -->

<!-- pedagogy-paragraph: p151 sha256 6b371bf4c033c420669b6bec309fc0de452748eaf6d787ea16edb0b5359c8916 -->
p151, lines 151-151; prose; priority: unchanged; previous: p143; next: p157

> Expand the denominator for small $h$:

<!-- pedagogy-paragraph: p157 sha256 199651e26a065c615ceed7e00e1e83d367a4155c3c429622728d1704be6dc038 -->
p157, lines 157-157; prose; priority: unchanged; previous: p151; next: p164

> The continuous equation and starting condition are

<!-- pedagogy-paragraph: p164 sha256 af738702548c3f815b27c57154615cc84ddcb549604c20b5afe64836bed32e1f -->
p164, lines 164-164; prose; priority: unchanged; previous: p157; next: p168

> With no observations, precision starts at zero. The term $J$ adds information from new observations. The term $2DP^2$ reduces that gain because later observations are separated from the cue state by diffusion.

<!-- pedagogy-paragraph: p168 sha256 b3423f83eaeffadf8f5855175c60bc3ac3686272bbb67a45b948decb051bba44 -->
p168, lines 168-168; prose; priority: unchanged; previous: p164; next: p176

> [The [**hyperbolic tangent**]{.definition-term custom-style="Definition Term"} is $\tanh z=(e^z-e^{-z})/(e^z+e^{-z})$.]{.definition-explanation} [Its [**inverse hyperbolic tangent**]{.definition-term custom-style="Definition Term"} on $(-1,1)$ is $\operatorname{artanh}z=\tfrac12\log[(1+z)/(1-z)]$, whose derivative is $1/(1-z^2)$.]{.definition-explanation} Set $a=\sqrt{J/(2D)}$ and $k=\sqrt{2DJ}$. Separating variables gives

<!-- pedagogy-paragraph: p176 sha256 88c9a085af48fa59a242107a3cf6ffe864f536f0695a8e290f7a0c647be912d4 -->
p176, lines 176-176; prose; priority: unchanged; previous: p168; next: p187

> Taking the inverse function and then the reciprocal yields

<!-- pedagogy-paragraph: p187 sha256 388160e6ae95ae49c9d41a75971e09a3d9f20418acd84738f5c5b3f169da6261 -->
p187, lines 187-191; prose; priority: unchanged; previous: p176; next: p193

> <!-- vale ai-tells.AnthropomorphicCognition = NO --> <!-- vale ai-tells.EmDashUsage = NO --> [The [**hyperbolic cotangent**]{.definition-term custom-style="Definition Term"} is $\coth z=1/\tanh z$.]{.definition-explanation} This backward precision derivation is a teaching reconstruction equivalent to the Gaussian covariance calculation in SI Eqs. S58–S75. It makes explicit how diffusion limits the value of later observations.[^p1-ideal] <!-- vale ai-tells.EmDashUsage = YES --> <!-- vale ai-tells.AnthropomorphicCognition = YES -->

<!-- pedagogy-paragraph: p193 sha256 04b96a48bb82516937ab34cc134d3bf14892fe53c4edde59fd013a72a30b5861 -->
p193, lines 193-193; prose; priority: unchanged; previous: p187; next: p199

> For short intervals, $\coth z=1/z+z/3+O(z^3)$, so

<!-- pedagogy-paragraph: p199 sha256 eec83294fff29ebf67842caf84c8eaa94e7db64d3a5f6f499beff1200051dc4e -->
p199, lines 199-201; prose; priority: unchanged; previous: p193; next: p205

> <!-- vale ai-tells.FormalTransitions = NO --> The naive and ideal estimators therefore agree through the displayed terms. <!-- vale ai-tells.FormalTransitions = YES -->

<!-- pedagogy-paragraph: p205 sha256 8b36520f8b870d530a45595b00e126e0f03424db00c07cf23eaaaf30025f53a8 -->
p205, lines 205-205; prose; priority: unchanged; previous: p199; next: p212

> For long intervals,

<!-- pedagogy-paragraph: p212 sha256 dc7b06cef80bda6d7f90a4ae57024b71f3015a3d6dbe8600f150d0be6c6245a6 -->
p212, lines 212-212; prose; priority: unchanged; previous: p205; next: p214

> **Interpretation.** The ideal observer keeps improving, but the improvement becomes small. Its variance relative to the limiting variance is:

<!-- pedagogy-paragraph: p214 sha256 e4518d8f37792c677e25743c7ca92aebcdba98e7b1a65d6e4aaa94739976b60c -->
p214, lines 214-214; list_item; priority: unchanged; previous: p212; next: p215

> $1.313$ at $L=L^*$.

<!-- pedagogy-paragraph: p215 sha256 e44a0e36cfd4d34eabe8a5b02a93321cf96645429988b772a73346f5179a32ef -->
p215, lines 215-215; list_item; priority: unchanged; previous: p214; next: p216

> $1.037$ at $2L^*$.

<!-- pedagogy-paragraph: p216 sha256 10f30326a0eafaaa0388bd5091f588f3d944d1a60cbef10f6ce86bbc47213a11 -->
p216, lines 216-216; list_item; priority: unchanged; previous: p215; next: p218

> $1.005$ at $3L^*$.

<!-- pedagogy-paragraph: p218 sha256 0dff0718a81fde19361b16b23543d677cf9c646cffbf4362cba21abb09179116 -->
p218, lines 218-218; prose; priority: unchanged; previous: p216; next: p220

> These are variances, so their ratios are not ratios of standard deviations.

<!-- pedagogy-paragraph: p220 sha256 d6d2e932ebc11c3a2bffb2b58633c8d9c85e4bfc99b0e7ed60095ac25c710495 -->
p220, lines 220-220; prose; priority: unchanged; previous: p218; next: p227

> Using $2DJ\ge\tau^{-2}$ gives

<!-- pedagogy-paragraph: p227 sha256 57956f69bc4c0890403adabe5b8ae3ae019ceeb48df51c740a60824c9387d58d -->
p227, lines 227-229; prose; priority: unchanged; previous: p220; next: p233

> <!-- vale ai-tells.FormalTransitions = NO --> [Thus the paper's statement about readout within a cellular time constant concerns a characteristic saturation time under full spike access. It does not mean all benefit ends abruptly at $\tau$.]{.key-statement} The naive observer's best variance is only $2/\sqrt3\simeq1.155$ times the ideal observer's asymptotic variance. Its best standard deviation is about $1.075$ times as large.[^p1-time] <!-- vale ai-tells.FormalTransitions = YES -->


Claim-bearing content: none

Claims to check:

- Claim c1, line 133: "To verify this, multiply likelihoods proportional to $\exp[-(x-a)^2/(2V_a)]$ and $\exp[-(x-b)^2/(2V_b)]$: the coefficient of $x^2/2$ becomes $1/V_a+1/V_b$." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c2, line 135: "Suppose we have already compressed the later part into a likelihood about the next bin's state with variance $1/P$." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c3, line 135: "Bringing that likelihood one step backward adds transition variance $q=2Dh$, since the next state equals the earlier state plus an independent Gaussian increment." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c4, line 139: "$$ \frac{1}{1/P+q}=\frac{P}{1+2DhP}. $$" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c5, line 147: "$$ P(L+h)=Jh+\frac{P(L)}{1+2DhP(L)}. $$" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c6, line 151: "Expand the denominator for small $h$:" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c7, line 153: "$$ P(L+h)=P(L)+[J-2DP(L)^2]h+O(h^2). $$" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c8, line 159: "$$ \frac{dP}{dL}=J-2DP^2, \qquad P(0)=0. $$" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c9, line 168: "[The [**hyperbolic tangent**]{.definition-term custom-style="Definition Term"} is $\tanh z=(e^z-e^{-z})/(e^z+e^{-z})$.]{.definition-explanation} [Its [**inverse hyperbolic tangent**]{.definition-term custom-style="Definition Term"} on $(-1,1)$ is $\operatorname{artanh}z=\tfrac12\log[(1+z)/(1-z)]$..." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c10, line 170: "$$ \int_0^{P/a}\frac{dz}{1-z^2}=kL, \qquad \operatorname{artanh}(P/a)=kL. $$" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c11, line 187: "<!-- vale ai-tells.AnthropomorphicCognition = NO --> <!-- vale ai-tells.EmDashUsage = NO --> [The [**hyperbolic cotangent**]{.definition-term custom-style="Definition Term"} is $\coth z=1/\tanh z$.]{.definition-explanation} This backward precision derivation is a teaching reconstruction equivalen..." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c12, line 187: "It makes explicit how diffusion limits the value of later observations.[^p1-ideal] <!-- vale ai-tells.EmDashUsage = YES --> <!-- vale ai-tells.AnthropomorphicCognition = YES -->" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c13, line 193: "For short intervals, $\coth z=1/z+z/3+O(z^3)$, so" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c14, line 212: "**Interpretation.** The ideal observer keeps improving, but the improvement becomes small." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c15, line 214: "$1.313$ at $L=L^*$." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c16, line 215: "$1.037$ at $2L^*$." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c17, line 216: "$1.005$ at $3L^*$." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c18, line 220: "Using $2DJ\ge\tau^{-2}$ gives" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c19, line 227: "It does not mean all benefit ends abruptly at $\tau$.]{.key-statement} The naive observer's best variance is only $2/\sqrt3\simeq1.155$ times the ideal observer's asymptotic variance." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c20, line 227: "Its best standard deviation is about $1.075$ times as large.[^p1-time] <!-- vale ai-tells.FormalTransitions = YES -->" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]

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

Location: line 231, anchor `sec:MEMORY-PARTIAL`

First content kind: `prose`

Opening passage line: 233
Closing passage line: 262

Paragraphs in source order (complete `PARAGRAPH_REVIEW.json`):

<!-- pedagogy-paragraph: p233 sha256 63ae8fb4e0001ae279bc7d1a09d996b9507eebab124d05f8415c762ace31fa37 -->
p233, lines 233-233; prose; priority: unchanged; previous: p227; next: p235

> **Neural mechanism.** [A downstream area may receive only some of the memory network's spikes. That reduces its information without reducing the fluctuations that already move the full memory network.]{.key-statement}

<!-- pedagogy-paragraph: p235 sha256 2959bfe0a07aa77a411ea8a68c09ff7c3fea710d35f51b8ec7e9eba099c7aa28 -->
p235, lines 235-235; prose; priority: unchanged; previous: p233; next: p241

> **Mathematical derivation.** If every spike is independently retained with probability $\alpha$, the observed rates and their slopes both scale by $\alpha$. Substitution in the Poisson information formula gives

<!-- pedagogy-paragraph: p241 sha256 290a64931baab10dd302cea4d33fbf01c6095eb8cad66ae0c4efebd50c59db0c -->
p241, lines 241-243; prose; priority: unchanged; previous: p235; next: p252

> <!-- vale ai-tells.FormalTransitions = NO --> The network diffusion coefficient stays $D$. Hence <!-- vale ai-tells.FormalTransitions = YES -->

<!-- pedagogy-paragraph: p252 sha256 9646551769274865ce09653d0192c4baa9cf482393bc687faaf1bc2803490279 -->
p252, lines 252-252; prose; priority: unchanged; previous: p241; next: p254

> **Interpretation.** The same factor $1/\sqrt\alpha$ multiplies the naive optimal interval and its minimum variance. The information bound implies $L_{\mathrm{obs}}^*\le\tau/\sqrt\alpha$, which can exceed $\tau$. A selected subset of neurons has exactly $\alpha J$ only when it carries that fraction of the information. A fraction of neurons or spikes chosen by a biased rule need not do so.[^p1-partial]

<!-- pedagogy-paragraph: p254 sha256 8e19185c156210567a045f638d7d3d1269765f40e35d9cff42cebc457898c408 -->
p254, lines 254-254; prose; priority: unchanged; previous: p252; next: p256

> <div class="publisher-worked-calculation publisher-fold-always">

<!-- pedagogy-paragraph: p256 sha256 f8b62ac81092705b67108e23deebbd279e3c0c6130ea357e52f50e1e38d7a35a -->
p256, lines 256-256; prose; priority: unchanged; previous: p254; next: p258

> **Example: limited spike access changes the useful interval.**

<!-- pedagogy-paragraph: p258 sha256 dd9c02d346e153ad3318876218ed39d1818b4e917d8f6e1b161ae98e106b8dba -->
p258, lines 258-258; prose; priority: unchanged; previous: p256; next: p260

> Take $\tau=0.1\,\mathrm{s}$, $J=10{,}000\,\mathrm{rad}^{-2}\mathrm{s}^{-1}$, and $D=0.005\,\mathrm{rad}^2/\mathrm{s}$. These values attain the information bound. Full access gives $L^*=0.1\,\mathrm{s}$ and limiting readout variance $0.001\,\mathrm{rad}^2$. The naive optimum is $0.1732\,\mathrm{s}$ with variance $0.001155\,\mathrm{rad}^2$.

<!-- pedagogy-paragraph: p260 sha256 c11437703c5c7d3033b63544399b1acc15efd38675eeb3aab8664c0a05ef2762 -->
p260, lines 260-260; prose; priority: unchanged; previous: p258; next: p262

> If $\alpha=0.1$, then $J_{\mathrm{obs}}=1000\,\mathrm{rad}^{-2}\mathrm{s}^{-1}$. The ideal characteristic interval becomes $0.3162\,\mathrm{s}$ and its limiting variance becomes $0.003162\,\mathrm{rad}^2$. The naive optimum becomes $0.5477\,\mathrm{s}$. A two second storage delay contributes $2DT=0.020\,\mathrm{rad}^2$ in both cases, giving total ideal asymptotic variances $0.021$ and $0.023162\,\mathrm{rad}^2$. Limited access leaves the storage error unchanged but increases the time and uncertainty involved in reading the cue state.

<!-- pedagogy-paragraph: p262 sha256 aac32651b10f567c461b9b4f255d6fb1fa6859b5368d8bd9a51af920ab21cf23 -->
p262, lines 262-262; prose; priority: unchanged; previous: p260; next: p266

> </div>


Claim-bearing content: none

Claims to check:

- Claim c1, line 233: "**Neural mechanism.** [A downstream area may receive only some of the memory network's spikes." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c2, line 235: "**Mathematical derivation.** If every spike is independently retained with probability $\alpha$, the observed rates and their slopes both scale by $\alpha$." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c3, line 252: "**Interpretation.** The same factor $1/\sqrt\alpha$ multiplies the naive optimal interval and its minimum variance." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c4, line 252: "A selected subset of neurons has exactly $\alpha J$ only when it carries that fraction of the information." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c5, line 252: "A fraction of neurons or spikes chosen by a biased rule need not do so.[^p1-partial]" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c6, line 254: "<div class="publisher-worked-calculation publisher-fold-always">" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c7, line 258: "Take $\tau=0.1\,\mathrm{s}$, $J=10{,}000\,\mathrm{rad}^{-2}\mathrm{s}^{-1}$, and $D=0.005\,\mathrm{rad}^2/\mathrm{s}$." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c8, line 258: "Full access gives $L^*=0.1\,\mathrm{s}$ and limiting readout variance $0.001\,\mathrm{rad}^2$." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c9, line 258: "The naive optimum is $0.1732\,\mathrm{s}$ with variance $0.001155\,\mathrm{rad}^2$." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c10, line 260: "If $\alpha=0.1$, then $J_{\mathrm{obs}}=1000\,\mathrm{rad}^{-2}\mathrm{s}^{-1}$." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c11, line 260: "The ideal characteristic interval becomes $0.3162\,\mathrm{s}$ and its limiting variance becomes $0.003162\,\mathrm{rad}^2$." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c12, line 260: "The naive optimum becomes $0.5477\,\mathrm{s}$." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c13, line 260: "A two second storage delay contributes $2DT=0.020\,\mathrm{rad}^2$ in both cases, giving total ideal asymptotic variances $0.021$ and $0.023162\,\mathrm{rad}^2$." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]

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

Location: line 264, anchor `sec:MEMORY-EXTENSIONS`

First content kind: `prose`

Opening passage line: 266
Closing passage line: 322

Paragraphs in source order (complete `PARAGRAPH_REVIEW.json`):

<!-- pedagogy-paragraph: p266 sha256 a05672e504f7a71ce4f29c48d901d9cc448b1240c67e21df5f685e9aa4d88be0 -->
p266, lines 266-268; prose; priority: unchanged; previous: p262; next: p270

> <!-- vale ai-tells.FigurativeCarries = NO --> **Neural mechanism.** The time constant in the inequality comes from the dynamics that carry an activation fluctuation into a lasting memory change. If both synaptic activation and firing rate adjust gradually, which time constant matters? <!-- vale ai-tells.FigurativeCarries = YES -->

<!-- pedagogy-paragraph: p270 sha256 cd1bdfb103a7c85bc2bcbec879aa10b42fb7efce973526d85d5bbdb3a793bd85 -->
p270, lines 270-270; prose; priority: unchanged; previous: p266; next: p278

> In the basic model, the firing rate changes immediately when the summed input changes. Assume symmetric weights. The extension instead lets $r_i$ approach $\phi(g_i)$ gradually, with time constant $\tau_m$, while synaptic activation still decays with time constant $\tau$:

<!-- pedagogy-paragraph: p278 sha256 5d2b1f407a006bc64605e91aa2d6ad24fb0684e29423f1d47adb6a1e55c1548b -->
p278, lines 278-278; prose; priority: unchanged; previous: p270; next: p280

> Here $\xi_i$ is the zero mean noise from variable spike generation, with the same Poisson strength as in the basic model.

<!-- pedagogy-paragraph: p280 sha256 bede15d60ad846453f2271f455f6d213f43f648dfb13ce26fff3e580cb4a7454 -->
p280, lines 280-280; prose; priority: unchanged; previous: p278; next: p289

> **Mathematical derivation.** In this symmetric weight extension, the linear state is $(\delta\mathbf s,\delta\mathbf r)$ and its deterministic matrix is

<!-- pedagogy-paragraph: p289 sha256 3b9c11c54c3939ce8d78f0242f5ed549086eab522984df3ffcb34dd5fadcb2e2 -->
p289, lines 289-291; prose; priority: unchanged; previous: p280; next: p297

> <!-- vale ai-tells.NegatedObject = NO --> The right tangent is $(\tau\mathbf r',\mathbf r')$. Write the left zero vector as $(\mathbf a,\mathbf b)$. The second block of $(\mathbf a^T,\mathbf b^T)A=0$ gives $\mathbf b=\tau_m\mathbf a$. The first then gives $W^T\operatorname{diag}(\phi')\mathbf a=\mathbf a/\tau$, so symmetry again permits $\mathbf a\propto\mathbf g'$. Normalizing its dot product with the right tangent yields <!-- vale ai-tells.NegatedObject = YES -->

<!-- pedagogy-paragraph: p297 sha256 7c8327743dc6a729dc0dcd745f16864fb06c02d11cc4949c18928a7ea0239ccb -->
p297, lines 297-299; prose; priority: unchanged; previous: p289; next: p308

> <!-- vale ai-tells.FormalTransitions = NO --> Only the $s$ block receives the modeled spike noise, so $2D=\sum_i a_i^2\bar r_i$. The symmetric formula consequently becomes <!-- vale ai-tells.FormalTransitions = YES -->

<!-- pedagogy-paragraph: p308 sha256 67aeb6fe58a62301c9262f232684921660b8bfe3e6682889a7ef4fc44a71943a -->
p308, lines 308-310; prose; priority: unchanged; previous: p297; next: p312

> <!-- vale ai-tells.ParallelStaccato = NO --> **Interpretation.** The sum of the two time constants replaces $\tau$. When one time constant is much larger, it supplies most of that sum. This result belongs to the two stage model and noise placement just described. The paper does not prove that arbitrary collections of biological time constants can always be added.[^p1-two-times] <!-- vale ai-tells.ParallelStaccato = YES -->

<!-- pedagogy-paragraph: p312 sha256 58c4e8bfcf7f7725747145584f1f7096cd24683a667412ecd59441ff128662ca -->
p312, lines 312-312; prose; priority: unchanged; previous: p308; next: p318

> **Neural question and model.** The equality condition also depends on the noise law. To see why, replace Poisson spike-count fluctuations with independent additive Gaussian noise of constant strength $q>0$:

<!-- pedagogy-paragraph: p318 sha256 c44b2141588388301a1a612f77dfe3ca2c9ad8654e1c7b00bc96cf82df2fbc08 -->
p318, lines 318-318; prose; priority: unchanged; previous: p312; next: p320

> **Mathematical derivation.** The short interval observation of the mean rate is now Gaussian with variance $q/h$. Repeating the score calculation gives $J=\sum_i(r_i')^2/q$, while projection gives $2D=q\sum_i v_i^2$. The same Cauchy Schwarz proof yields $2DJ\ge\tau^{-2}$. Equality requires $v_i\propto r_i'$ because all cells have the same noise strength. In a symmetric network $v_i\propto g_i'$, so a linear transfer rule supplies the condition by keeping $\phi'(g)$ constant across participating inputs.

<!-- pedagogy-paragraph: p320 sha256 e3951bffdb2534562b07faee823ac045393f45bac3ac8d0303296da5592de892 -->
p320, lines 320-320; prose; priority: unchanged; previous: p318; next: p322

> **Interpretation.** In the Poisson case, variance grows with rate and an exponential rule is a sufficient way to attain equality. The pointwise projection condition remains the general criterion, including the [linear-family counterexample](ch-memory-information.html#sec-memory-bound) already derived. The difference between these sufficient classes follows from the noise weighting, not from linearity being universally preferable.[^p1-gaussian]

<!-- pedagogy-paragraph: p322 sha256 79adff55f80e61d382109a540177dd662421a7ca83dade6a45f619fa2dec1757 -->
p322, lines 322-326; prose; priority: unchanged; previous: p320; next: p330

> <!-- vale ai-tells.AnthropomorphicCognition = NO --> <!-- vale ai-tells.EmDashUsage = NO --> This explicit $q$ formulation is a teaching reconstruction that keeps dimensions and the noise normalization visible. The supplement's Gaussian subsection establishes the change in equality condition. Here the matched noise and likelihood derivation supplies all factors of $q$ and $\tau$ without requiring the reader to infer a normalization from SI Eqs. S94–S95. <!-- vale ai-tells.EmDashUsage = YES --> <!-- vale ai-tells.AnthropomorphicCognition = YES -->


Claim-bearing content: none

Claims to check:

- Claim c1, line 289: "The second block of $(\mathbf a^T,\mathbf b^T)A=0$ gives $\mathbf b=\tau_m\mathbf a$." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c2, line 297: "<!-- vale ai-tells.FormalTransitions = NO --> Only the $s$ block receives the modeled spike noise, so $2D=\sum_i a_i^2\bar r_i$." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c3, line 301: "$$ 2D=\frac{\sum_i\bar r_i(g_i')^2} {(\tau+\tau_m)^2[\sum_i g_i'r_i']^2}, \qquad 2D\ge\frac{J^{-1}}{(\tau+\tau_m)^2}. $$" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c4, line 308: "The paper does not prove that arbitrary collections of biological time constants can always be added.[^p1-two-times] <!-- vale ai-tells.ParallelStaccato = YES -->" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c5, line 312: "To see why, replace Poisson spike-count fluctuations with independent additive Gaussian noise of constant strength $q>0$:" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c6, line 318: "Repeating the score calculation gives $J=\sum_i(r_i')^2/q$, while projection gives $2D=q\sum_i v_i^2$." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c7, line 318: "The same Cauchy Schwarz proof yields $2DJ\ge\tau^{-2}$." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c8, line 320: "The pointwise projection condition remains the general criterion, including the [linear-family counterexample](ch-memory-information.html#sec-memory-bound) already derived." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c9, line 320: "The difference between these sufficient classes follows from the noise weighting, not from linearity being universally preferable.[^p1-gaussian]" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]

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

Location: line 328, anchor `sec:MEMORY-FIG3-AND-CAUTION`

First content kind: `prose`

Opening passage line: 330
Closing passage line: 431

Paragraphs in source order (complete `PARAGRAPH_REVIEW.json`):

<!-- pedagogy-paragraph: p330 sha256 5c370e45e4c2b98aef994308da3cc023a6557af5bb9e117d3f4860abea460400 -->
p330, lines 330-330; prose; priority: unchanged; previous: p322; next: p332

> Figure 3 isolates readout uncertainty, rescaling variance by $\sqrt{2D/J}$ and duration by $L^*$. In these axes the ideal curve is $\coth z$ and the naive curve is $z/3+1/z$. Both diverge like $1/z$ at short durations because too few spikes are available. The plotted features are:

<!-- pedagogy-paragraph: p332 sha256 b0bee7594f35653136bcc64e084439579779f652c2b628b2d19624f18d377633 -->
p332, lines 332-332; list_item; priority: unchanged; previous: p330; next: p333

> The ideal solid curve approaches one.

<!-- pedagogy-paragraph: p333 sha256 6f4fd36218daab805fef5f0fb2c6d311005cf36dde97ea3bd6d6cfb33ccd7038 -->
p333, lines 333-333; list_item; priority: unchanged; previous: p332; next: p334

> The naive dashed curve reaches $2/\sqrt3$ at $z=\sqrt3$, then rises because its equal weighting gives increasing importance to displaced states.

<!-- pedagogy-paragraph: p334 sha256 63dbf6ae7b3b7e53911b65edd8d5cf3e5391a28283b9ce55239d4499d66145a1 -->
p334, lines 334-334; list_item; priority: unchanged; previous: p333; next: p336

> The dotted vertical line marks that naive optimum.

<!-- pedagogy-paragraph: p336 sha256 4517d8077c663f27683bd28143ef451df6fb956a97c8394631a8c7e6deee50b9 -->
p336, lines 336-336; prose; priority: unchanged; previous: p334; next: p338

> The storage delay contribution $2DT$ is not part of these rescaled curves. Figure S2 repeats the comparison for partial access, showing the rightward and upward shifts when $\alpha=0.1$.[^p1-fig3]

<!-- pedagogy-paragraph: p338 sha256 e4ff6a420999fe40ed862d6ac4dc230bea0205cf21e040d7c9d9b49dcc8a445a -->
p338, lines 338-340; prose; priority: unchanged; previous: p336; next: p344

> <details class="publisher-long-content publisher-source-figure"> <summary>Original paper figure: Burak and Fiete (2012), Figure 3</summary> <div class="publisher-fold-body">

<!-- pedagogy-paragraph: p344 sha256 fcd1e43c0c40c2d1dd2932edba0594c38927752553522ce5ed959562b6a78f49 -->
p344, lines 344-345; prose; priority: unchanged; previous: p338; next: p347

> </div> </details>

<!-- pedagogy-paragraph: p347 sha256 2e61a70b137bef1ccaa201377d4957e19bd724a972ec3e9c6c10048e07a9bd4d -->
p347, lines 347-349; prose; priority: unchanged; previous: p344; next: p353

> <details class="publisher-long-content publisher-source-figure"> <summary>Original paper figure: Burak and Fiete (2012), Figure S2</summary> <div class="publisher-fold-body">

<!-- pedagogy-paragraph: p353 sha256 fcd1e43c0c40c2d1dd2932edba0594c38927752553522ce5ed959562b6a78f49 -->
p353, lines 353-354; prose; priority: unchanged; previous: p347; next: p356

> </div> </details>

<!-- pedagogy-paragraph: p356 sha256 2c643bd85d3e8933fd7127e586cd0d302d74dcd69d691fc3921ef217cc019e39 -->
p356, lines 356-356; prose; priority: unchanged; previous: p353; next: p360

> <div class="figure-scroll">

<!-- pedagogy-paragraph: p360 sha256 aac32651b10f567c461b9b4f255d6fb1fa6859b5368d8bd9a51af920ab21cf23 -->
p360, lines 360-360; prose; priority: unchanged; previous: p356; next: p362

> </div>

<!-- pedagogy-paragraph: p362 sha256 03a4d49f4c862c7602aee33b8190a77c04e08a78e753d54c1e1d13ae7b2b318f -->
p362, lines 362-362; prose; priority: unchanged; previous: p360; next: p364

> More observation keeps helping the ideal reader, with diminishing benefit, while equal weighting eventually gives too much influence to a state that has moved.

<!-- pedagogy-paragraph: p364 sha256 49a0da51f37adca414ae261335e6720cd6ed7ff124429d0ca03d7e70fb102e0c -->
p364, lines 364-364; prose; priority: unchanged; previous: p362; next: p374

> One printed inequality deserves special care. Main Eq. 6 says that total error is at least $2D(T+\tau)$. SI Eq. S83 uses a lower bound with readout term $2D\tau/\sqrt\alpha$. But the paper's other derived results imply

<!-- pedagogy-paragraph: p374 sha256 13eb9ea77fdaa32a33b02db8f61fcd9950af167706f66fe53262f9f9859fcb7e -->
p374, lines 374-376; prose; priority: unchanged; previous: p364; next: p383

> <!-- vale ai-tells.FormalTransitions = NO --> Thus the ideal asymptotic readout term is at most $2D\tau$, with equality when the information diffusion inequality is saturated. Substituting an upper bound for this term cannot establish the printed universal lower bound on total error. Within the local Gaussian model, the defensible statement is <!-- vale ai-tells.FormalTransitions = YES -->

<!-- pedagogy-paragraph: p383 sha256 43d292731d7eadbad6393b23c08685830afe1cf58e3635049815f74f24a01d6e -->
p383, lines 383-383; prose; priority: unchanged; previous: p374; next: p385

> with equality approached as $L\to\infty$ for the ideal observer. At saturation this asymptotic expression becomes $2D(T+\tau)$. For partial access the same issue occurs with the factor $1/\sqrt\alpha$. This is an apparent inconsistency between printed formulas, identified by algebra using the supplied sources. It is not a claim that the authors issued a correction.[^p1-printed]

<!-- pedagogy-paragraph: p385 sha256 019a560ae5696ac844dffa19563786e5949882d9a541fb68c94f4912154f86f5 -->
p385, lines 385-385; prose; priority: unchanged; previous: p383; next: p387

> For a concrete strict inequality case, keep $\tau=0.1\,\mathrm{s}$ and $D=0.005\,\mathrm{rad}^2/\mathrm{s}$ but set $J=40{,}000\,\mathrm{rad}^{-2}\mathrm{s}^{-1}$. Then $2DJ=400\,\mathrm{s}^{-2}$ exceeds $\tau^{-2}=100\,\mathrm{s}^{-2}$. The limiting readout variance is $0.0005\,\mathrm{rad}^2$, whereas $2D\tau=0.001\,\mathrm{rad}^2$. At $T=2\,\mathrm{s}$, the Gaussian ideal total limit is $0.0205\,\mathrm{rad}^2$, below $2D(T+\tau)=0.021\,\mathrm{rad}^2$. These values expose the algebraic problem without assuming the bound is saturated.

<!-- pedagogy-paragraph: p387 sha256 61b00a6f58797bb5b45a8e0e4b9f2f7d09e9bd08a3aa8c055a0ad116981d282f -->
p387, lines 387-391; prose; priority: unchanged; previous: p385; next: p395

> <!-- vale ai-tells.EmptyPadding = NO --> <!-- vale ai-tells.ParallelStaccato = NO --> When a continuous attractor circuit is used to accumulate an incoming signal over time, its stored value represents the integral of that signal. The short useful readout interval does not imply a short lifetime for this accumulated value. A tuned circuit can continue to represent the mean of accumulated inputs while its variance grows. A leak would instead pull its mean toward a particular value. [Diffusion limits the accuracy of the integral and the usefulness of long observation. It does not by itself introduce that restoring pull.]{.key-statement} Applying these predictions to an animal also requires checking its spike statistics, tuning, drift, access to spikes, and other sources of movement noise.[^p1-integrator] <!-- vale ai-tells.ParallelStaccato = YES --> <!-- vale ai-tells.EmptyPadding = YES -->

<!-- pedagogy-paragraph: p395 sha256 c434e91454241a31e310a239ac3a093d91ab1fcd15b7ac3b333458ba63f49376 -->
p395, lines 395-395; prose; priority: unchanged; previous: p387; next: p397

> <!-- vale ai-tells.EmDashUsage = NO -->

<!-- pedagogy-paragraph: p397 sha256 6e36e79bce1447ac7eddc2fb19787ace984308e97fbb90fe3fbe309f14b460ff -->
p397, lines 397-397; prose; priority: unchanged; previous: p395; next: p399

> <!-- vale ai-tells.EmDashUsage = YES -->

<!-- pedagogy-paragraph: p399 sha256 c434e91454241a31e310a239ac3a093d91ab1fcd15b7ac3b333458ba63f49376 -->
p399, lines 399-399; prose; priority: unchanged; previous: p397; next: p401

> <!-- vale ai-tells.EmDashUsage = NO -->

<!-- pedagogy-paragraph: p401 sha256 6e36e79bce1447ac7eddc2fb19787ace984308e97fbb90fe3fbe309f14b460ff -->
p401, lines 401-401; prose; priority: unchanged; previous: p399; next: p403

> <!-- vale ai-tells.EmDashUsage = YES -->

<!-- pedagogy-paragraph: p403 sha256 c434e91454241a31e310a239ac3a093d91ab1fcd15b7ac3b333458ba63f49376 -->
p403, lines 403-403; prose; priority: unchanged; previous: p401; next: p405

> <!-- vale ai-tells.EmDashUsage = NO -->

<!-- pedagogy-paragraph: p405 sha256 6e36e79bce1447ac7eddc2fb19787ace984308e97fbb90fe3fbe309f14b460ff -->
p405, lines 405-405; prose; priority: unchanged; previous: p403; next: p407

> <!-- vale ai-tells.EmDashUsage = YES -->

<!-- pedagogy-paragraph: p407 sha256 c434e91454241a31e310a239ac3a093d91ab1fcd15b7ac3b333458ba63f49376 -->
p407, lines 407-407; prose; priority: unchanged; previous: p405; next: p409

> <!-- vale ai-tells.EmDashUsage = NO -->

<!-- pedagogy-paragraph: p409 sha256 6e36e79bce1447ac7eddc2fb19787ace984308e97fbb90fe3fbe309f14b460ff -->
p409, lines 409-409; prose; priority: unchanged; previous: p407; next: p413

> <!-- vale ai-tells.EmDashUsage = YES -->

<!-- pedagogy-paragraph: p413 sha256 c434e91454241a31e310a239ac3a093d91ab1fcd15b7ac3b333458ba63f49376 -->
p413, lines 413-413; prose; priority: unchanged; previous: p409; next: p415

> <!-- vale ai-tells.EmDashUsage = NO -->

<!-- pedagogy-paragraph: p415 sha256 6e36e79bce1447ac7eddc2fb19787ace984308e97fbb90fe3fbe309f14b460ff -->
p415, lines 415-415; prose; priority: unchanged; previous: p413; next: p417

> <!-- vale ai-tells.EmDashUsage = YES -->

<!-- pedagogy-paragraph: p417 sha256 c434e91454241a31e310a239ac3a093d91ab1fcd15b7ac3b333458ba63f49376 -->
p417, lines 417-417; prose; priority: unchanged; previous: p415; next: p419

> <!-- vale ai-tells.EmDashUsage = NO -->

<!-- pedagogy-paragraph: p419 sha256 6e36e79bce1447ac7eddc2fb19787ace984308e97fbb90fe3fbe309f14b460ff -->
p419, lines 419-419; prose; priority: unchanged; previous: p417; next: p421

> <!-- vale ai-tells.EmDashUsage = YES -->

<!-- pedagogy-paragraph: p421 sha256 c434e91454241a31e310a239ac3a093d91ab1fcd15b7ac3b333458ba63f49376 -->
p421, lines 421-421; prose; priority: unchanged; previous: p419; next: p423

> <!-- vale ai-tells.EmDashUsage = NO -->

<!-- pedagogy-paragraph: p423 sha256 6e36e79bce1447ac7eddc2fb19787ace984308e97fbb90fe3fbe309f14b460ff -->
p423, lines 423-423; prose; priority: unchanged; previous: p421; next: p425

> <!-- vale ai-tells.EmDashUsage = YES -->

<!-- pedagogy-paragraph: p425 sha256 c434e91454241a31e310a239ac3a093d91ab1fcd15b7ac3b333458ba63f49376 -->
p425, lines 425-425; prose; priority: unchanged; previous: p423; next: p427

> <!-- vale ai-tells.EmDashUsage = NO -->

<!-- pedagogy-paragraph: p427 sha256 6e36e79bce1447ac7eddc2fb19787ace984308e97fbb90fe3fbe309f14b460ff -->
p427, lines 427-427; prose; priority: unchanged; previous: p425; next: p429

> <!-- vale ai-tells.EmDashUsage = YES -->

<!-- pedagogy-paragraph: p429 sha256 c434e91454241a31e310a239ac3a093d91ab1fcd15b7ac3b333458ba63f49376 -->
p429, lines 429-429; prose; priority: unchanged; previous: p427; next: p431

> <!-- vale ai-tells.EmDashUsage = NO -->

<!-- pedagogy-paragraph: p431 sha256 6e36e79bce1447ac7eddc2fb19787ace984308e97fbb90fe3fbe309f14b460ff -->
p431, lines 431-431; prose; priority: unchanged; previous: p429; next: none

> <!-- vale ai-tells.EmDashUsage = YES -->


Claim-bearing content: figure

Claims to check:

- Claim c1, line 330: "Figure 3 isolates readout uncertainty, rescaling variance by $\sqrt{2D/J}$ and duration by $L^*$." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c2, line 330: "In these axes the ideal curve is $\coth z$ and the naive curve is $z/3+1/z$." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c3, line 330: "Both diverge like $1/z$ at short durations because too few spikes are available." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c4, line 333: "The naive dashed curve reaches $2/\sqrt3$ at $z=\sqrt3$, then rises because its equal weighting gives increasing importance to displaced states." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c5, line 336: "Figure S2 repeats the comparison for partial access, showing the rightward and upward shifts when $\alpha=0.1$.[^p1-fig3]" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c6, line 338: "<details class="publisher-long-content publisher-source-figure"> <summary>Original paper figure: Burak and Fiete (2012), Figure 3</summary> <div class="publisher-fold-body">" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c7, line 342: "Caption: The ideal readout error approaches a limit, while the error of equal weighting rises after its minimum. Original Figure 3 from Burak and Fiete (2012), reproduced as an exact artwork excerpt. [PDF page 4](../papers/burak-fiete-2012-persistent-activity.pdf#page=4). [Open image at full size..." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c8, line 347: "<details class="publisher-long-content publisher-source-figure"> <summary>Original paper figure: Burak and Fiete (2012), Figure S2</summary> <div class="publisher-fold-body">" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c9, line 351: "Caption: Access to a tenth of the spikes shifts the useful observation time and the readout error upward. Original Figure S2 from Burak and Fiete (2012), reproduced as an exact artwork excerpt. [PDF page 16](../papers/burak-fiete-2012-persistent-activity-si.pdf#page=16). [Open image at full size]..." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c10, line 358: "Caption: Original guide construction from the analytic readout formulas in Burak and Fiete (2012), Fig. 3 and Supporting Text, Eqs. S75 and S79–S81, rather than digitized data. Ideal readout approaches a normalized variance of one. Simple averaging reaches $2/\sqrt3$ at $z=\sqrt3$ and then worsen..." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c11, line 366: "$$ 2DJ\ge\tau^{-2} \quad\Longrightarrow\quad J\ge\frac1{2D\tau^2} \quad\Longrightarrow\quad \sqrt{\frac{2D}{J}}\le2D\tau. $$" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c12, line 374: "Substituting an upper bound for this term cannot establish the printed universal lower bound on total error." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c13, line 383: "For partial access the same issue occurs with the factor $1/\sqrt\alpha$." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c14, line 383: "It is not a claim that the authors issued a correction.[^p1-printed]" -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c15, line 385: "For a concrete strict inequality case, keep $\tau=0.1\,\mathrm{s}$ and $D=0.005\,\mathrm{rad}^2/\mathrm{s}$ but set $J=40{,}000\,\mathrm{rad}^{-2}\mathrm{s}^{-1}$." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c16, line 385: "Then $2DJ=400\,\mathrm{s}^{-2}$ exceeds $\tau^{-2}=100\,\mathrm{s}^{-2}$." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c17, line 385: "The limiting readout variance is $0.0005\,\mathrm{rad}^2$, whereas $2D\tau=0.001\,\mathrm{rad}^2$." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c18, line 385: "At $T=2\,\mathrm{s}$, the Gaussian ideal total limit is $0.0205\,\mathrm{rad}^2$, below $2D(T+\tau)=0.021\,\mathrm{rad}^2$." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]
- Claim c19, line 387: "It does not by itself introduce that restoring pull.]{.key-statement} Applying these predictions to an animal also requires checking its spike statistics, tuning, drift, access to spikes, and other sources of movement noise.[^p1-integrator] <!-- vale ai-tells.ParallelStaccato = YES --> <!-- vale..." -> [verdict: true as written, condition stated, fixed, or not a claim; checked: how]

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
