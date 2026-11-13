# Teaching and language

Read these five groups in order when drafting or reviewing teaching text. The short checklist remains in `SKILL.md`; this reference contains the detailed rules.

1. Audience and teaching priorities.
2. What an explanation must teach.
3. Accurate, necessary, plain wording.
4. Paragraph flow and presentation.
5. Writing, review, repair, and recheck.

## Audience and teaching priorities

### Reader benefit governs flexibility

Interpret flexibility in these instructions solely to improve the reader's understanding. Permission to change presentation does not waive the underlying teaching requirement.

A different explanation order must preserve motivation and prerequisite order. Removing a repeated opening template must preserve continuity. Shortening an explanation must preserve the definitions, mechanisms, examples, and qualifications needed to understand and apply it.

Begin with a question, problem, observation, or limitation the reader can understand. Keep its relevance apparent as the explanation develops. Introduce unfamiliar concepts before reasoning depends on them, and use each result to motivate the next necessary step.

For prerequisite review, distinguish a passage that adequately teaches a concept from a preview, reference, label, glossary entry, or mention. Judge whether the intended reader can use the concept for the specific later reasoning, allowing several passages to teach it together. A needed concept may come from the recorded audience baseline. Cite the actual teaching and dependent-use passages in reading order, including within a section or paragraph. A concept-order index organizes these judgments and checks order; extraction and hashes do not decide adequacy, and a concept relation is not automatically a whole-chapter prerequisite. Review transitions separately from graph/order checks.

Do not justify reduced teaching coverage or verification by citing authoring convenience, time, token use, or context limits. When two approaches serve the reader equally well, prefer the simpler and more efficient approach.

A requirement may be inapplicable to a particular subject. Establish that from the subject and the reader's needs, rather than treating flexible wording as permission to omit it.

Quality checks set a minimum; they do not define everything an explanation needs. Writers and reviewers must identify essential missing premises, definitions, relationships, steps, evidence, and qualifications even when no checklist item, lint rule, or automated gate tests them. Do not omit necessary teaching because a gate will not notice, or accept a passage because the available checks passed. Trace what the reader needs to understand the passage's actual claim or task, supply those dependencies, and record unresolved gaps as findings. A focused scope may exclude unrelated material; it cannot exclude a prerequisite on which the included explanation depends.

### Establish the audience baseline

Before drafting or reviewing, record the intended audience, assumed knowledge, and concepts the guide must teach in the guide's project records. Reuse that baseline for local revisions. If it is missing, state a provisional baseline from the course context and ask for clarification when a different assumption would materially change the explanation. Do not silently alternate between beginner and specialist expectations.

Use the baseline to decide what needs explanation. Explain subject-specific meanings of familiar words, such as risk in statistical learning, even when their everyday meanings are familiar. Conversely, do not interrupt the reasoning to reteach assumed knowledge unless the passage uses it in an unfamiliar way. Cite the baseline and relevant passages when judging whether an explanation is missing or unnecessary.

## What an explanation must teach

### Start from the reader's problem

For every core concept and substantial instructional section, begin with an observable situation, question, or limitation that the reader can reason about. State the goal that the current state blocks, makes costly, or leaves uncertain. Where the subject involves a real engineering choice, state the choice and the criterion that governs it before introducing the method.

Use these logical moves where they apply:

1. The pressing problem, production failure, or observable limitation.
2. Its place in the system, data flow, or mathematical setting.
3. The core concept, formal definition, and necessary prerequisites.
4. The mechanism, calculation, or state change.
5. Operational costs and trade-offs.
6. When to choose it and the relevant selection criteria.
7. Limits, failure modes, and boundary conditions.
8. A concrete trace with inputs, intermediate state, result, and conclusion.

These are explanation moves, not eight compulsory paragraphs. Do not invent a production incident or a false choice. A mathematical uncertainty, data-shape constraint, performance cost, or safety boundary can provide the necessary pressure.

Do not open with an imperative, bare definition, taxonomy, formula, code block, table, or visual when the reader has not yet been given the question it answers. A short reference entry may use a shorter form only after its linked teaching location has established the underlying decision. Its review record must explain how that shorter form helps the reader.

Openings need a lower vocabulary burden than the detailed explanation that follows. State the concrete reader problem in familiar words before combining technical terms or abstract noun phrases. A term's earlier definition does not by itself make that term the clearest choice in a later opening. When continuity requires the term, add a short plain reminder or give the plain description first. Use the exact technical term once the explanation depends on its precision. Technical experience does not remove the need to state how the objects in the sentence relate.

When the subject uses the same term for different objects, distinguish the meanings where each one appears. For example, in model-based systems, a model checkpoint is a saved model version, while a workflow checkpoint is saved execution state. Where the exact term is unnecessary, name the concrete object instead. Treat this as a meaning check, not as a rule to replace established technical vocabulary throughout the guide.

### System setup and method choices

Before explaining a multi-component process, establish the setting, goal, component roles, objects exchanged or changed, and relevant trust or access assumptions. Explain one complete cycle or transformation in plain language before equations or cases depend on its moving parts. Map terms that refer to the same role in the example, and distinguish roles that differ. A diagram or trace appearing after the mechanism cannot supply an earlier missing prerequisite. Use only as much setup as the subject needs; a single mathematical object does not require an invented system.

Place an unfamiliar technical name within its family at first substantial use: for example, a training arrangement, a particular algorithm, one aggregation step, a privacy protocol, an attack, or a metric. Define its purpose and the object it acts on before detailing how it works. Mark it as described in "First-definition emphasis". Capitalization, a citation, or an unexplained name is not a definition.

Where several established approaches address the same problem, identify the relevant alternatives and compare them on shared criteria before the reader must interpret the chosen approach. Explain the example's selection and scope. Distinguish alternatives at the same level from complementary protections, prerequisites, attacks, and replaceable steps within a larger method. A shorter treatment may point to a suitable comparison elsewhere in the reading path, but must state the distinction needed here. Do not force a comparison or an exhaustive survey when it would not help the reader; record the reason in the review.

Keep differences in assumptions, input objects, and guarantees visible when moving between methods. A result for one kind of update, data distribution, or operating mode does not automatically apply to another. State the simplification before a worked example uses it, and explain which properties the example cannot illustrate. Use a compact table when the alternatives and criteria are easier to compare that way, after establishing the common problem.

Distinguish steps required by the method from optional choices in an example or implementation. Check whether the wording could make one possible approach seem necessary, universal, or standard without support. State its scope and relevant cost where the reader needs them. Do not imply that understanding or using a concept requires an expensive optional procedure. This check does not require a survey of alternatives when a brief qualification explains the distinction.

### Complete explanations, natural order

At the first substantial treatment of a concept, give the reader a concrete question, observation, or limitation they can understand. An engineering failure can motivate a method, but mathematics and science do not require an invented production problem.

Cover the following where relevant, in the order that makes the explanation easiest to follow:

- the object or method, its purpose, definition, and necessary prerequisites;
- how it works, including the derivation, proof, or changes to data and state;
- a worked example with observable inputs, intermediate steps, and results;
- assumptions, units/shapes, important limits, counterexamples, or failure cases;
- interpretation, measurement, costs, and when the method is useful.

This is a coverage requirement, not a fixed paragraph template. A source transcript, table, formula, or polished summary alone does not teach the method. Small examples are valuable when they isolate a difficult point; add realistic constraints when those affect the conclusion.

Check the additional concepts an example requires beyond its teaching purpose. Keep each only when it helps explain the main concept or preserves a necessary property. Otherwise choose an example with fewer extra prerequisites. Mathematical correctness alone does not make an example suitable: units, terminology, and context must let the intended reader interpret the result. Preserve any displaced teaching through the guide's change and coverage records.

At a concept's first reasoning-dependent use, give its definition, purpose, and first teaching location in the current reading path. The meaning may come from the introducing sentence itself rather than a separate formal definition; see "First-definition emphasis". If the subject uses code, identify a software library, class, function, or literal identifier by its role and format the literal name as code. If the subject uses notation, explain what an index, symbol, or dimension refers to before a calculation depends on it. A later glossary entry or a casual first mention does not satisfy this requirement.

### Establish operating modes before mode-specific details

When an object has different roles in different operating modes, establish those modes at the Part opening or the object's first teaching location before later sections rely on the distinction. For every relevant mode, state the input, output, reference or target when one is required, measurement, and whether it changes parameters or external state. Do not use a figure as the first explanation of those roles.

For model-based systems, distinguish inference, training, and evaluation before later chapters rely on their different inputs and results. Inference turns an input into an output using fixed parameters. Training compares an input-output prediction with a target and uses the resulting objective to update parameters. Evaluation compares predictions with held-out targets but does not update parameters. Use the corresponding modes in other subjects rather than forcing this terminology where it does not fit.

### Bridge real objects and computational representations

When an explanation converts a real-world or flexible software object into a computational representation, state what the original form permits or costs, the constraint or speed opportunity in the computation system, the conversion decision, and the resulting gain and cost. Do not introduce a shape, encoding, or shared dimension as a self-explanatory fact.

For example, an unequal-length collection may be convenient in ordinary application code, while a dense batch needs one rectangular shape to run a shared operation efficiently. Explain the transformation that creates that shape, the control information that preserves the original meaning, and the wasted work or other cost it introduces. The illustration is not a fixed template; use the same bridge for other representation changes.

## Accurate, necessary, plain wording

### Every statement is a claim

Check the strength and support of every statement in the guide, not only in openings. A statement is any sentence, table cell, callout title, reader-visible code comment or string, caption, alt text, figure label, or arrow. None is exempt because it is short, inherited, illustrative, or already reviewed.

- For a possible effect, state the action and qualify its consequence: "Altering training records can change a model's learned behavior." Do not imply that every alteration produces the effect. Established definitions and effects that follow under explicit assumptions can use direct present-tense statements.
- Introduce an invented situation with a natural premise such as "Suppose an employee asks an application to pay an invoice." Present tense is natural after that premise. Establish it once; do not repeat "suppose" or "hypothetical" throughout the passage, or require a scenario when a direct explanation would work better.
- Attribute an observed incident or published research demonstration to its source and keep the conditions that matter to the opening claim. A documented demonstration can motivate the problem without being presented as an incident affecting customers. Do not turn an assumed situation into a reported event.

Match the actor and verb to the actual step. For example, a model may generate a tool call, the application may submit the request and attempt the operation, and the receiving service may execute or reject it. "Proposes" fits advice awaiting action; it understates a request already submitted for execution. Use the components in the system being explained rather than imposing this example's sequence on every architecture. An attempted operation does not imply successful execution.

Attach a requirement to the person, component, or activity that has it. "Investigating this behavior requires training records" explains the purpose of the evidence. "The model requires evidence" assigns that purpose to the wrong subject when the records are needed for investigation. A model can still require a particular input format when that is the actual technical requirement.

Keep capability, required behavior, and observed behavior distinct. "The receiving service can reject the request" describes capability. "The receiving service should reject the request" states expected behavior. "The receiving service rejects the request" describes behavior established for the system or assumed setup. Use "must" when the specified contract or governing rule makes the requirement mandatory. A design requirement can be stated before implementation. A recommendation can follow from an explained mechanism without a published experiment; do not present either as measured evidence that the control works. Neutral teaching prose can state what a system should do; avoiding unnecessary commands to the reader does not justify weakening a requirement to "can."

Check each statement according to its kind:

- About code, a figure, a table, or another section: read that object. Run code as the math, code, and case contract describes.
- Arithmetic: recompute it.
- A research finding: the cited source reports it, under the conditions the sentence keeps.
- The behavior of a library, API, or product: its official documentation for the version the guide uses.
- How a named algorithm or method works: its original paper or official documentation. A familiar summary is not a source.
- A definition: consistent with established use and with every later use in the guide.
- An invented example or number: presented as illustrative, never as a measurement.
- A recommendation: states the condition it depends on.

Words that promise a property need their own verdict: "always", "never", "every", "only", "once", "cannot", "must", "necessary", "ensures", "guarantees", "prevents", "isolates", "remains", "small", and comparisons such as "more precise" or "better". Decide whether the statement is true as written, true only under a condition the sentence must then state, or false. For example, "overlap copies boundary text into adjacent chunks, so a claim crossing the split remains recoverable" promises recovery of every crossing claim. It holds only when the copied text covers the whole claim and the context it needs. The rules on possible effects in this section, and on guarantees and required versus optional steps in "System setup and method choices", supply the usual repairs.

A diagnostic sequence claims that it misses no stage. When the text says that a symptom means one stage failed, check that no earlier stage could produce the same symptom. "The passage is in the source but was never retrieved, so search failed" skips parsing, chunking, and indexing, each of which can lose the passage first.

Check claims before wording. A plain sentence that is false is still a correctness error. The wording rules in "Plain words and precise terms" and "Wording passes across a guide" apply once the claim holds. When a unit contains code, a table, an equation, or a named method, its strongest objection addresses what the unit claims, not only how it is worded.

Check the literal statement before polishing it. Does the subject actually do what the verb says? Does the code, table, or source support the claimed result? Does an optional feature sound mandatory? For example, chapters can explain request preparation; the application prepares a request. Likewise, a trace that saves page IDs cannot identify an excluded chunk on the same page without a chunk identifier. These examples illustrate the test, not phrases to ban.

### Concrete wording and sentence contribution

Every sentence in explanatory prose should give the reader a useful piece of the reasoning: a prerequisite, a definition, a mechanism, a consequence, a decision criterion, a limit, or an example. Delete or combine a sentence that only restates a heading, announces that the chapter will discuss a topic, or substitutes a broad claim for the detail the reader needs.

When a sentence makes a claim about an organization, person, software component, model, dataset, or record, identify the relevant object and what happens to it. State the actor when it matters, the action or state change, the condition that limits it, and the practical consequence. For example, replace “one approval cannot safely stand for every copy” with a statement of what approval covers, which copy or data use is at issue, and why that scope fails to cover a later use.

Treat a word as a review candidate when it conceals the object or action, even when it is grammatical. Examples include “artifact” when “trained model file” or “model output” is meant, “normal application data handling” when the reader needs the specific input, storage, transmission, or answer path, and “compatible terms” when the reader needs the actual permission, restriction, or purpose. Keep an established technical term when it is the most precise name and explain it at first use.

Prefer familiar words unless a less common word provides necessary precision. Review words such as “facilitate,” “functionality,” “implementation,” “methodology,” “optimization,” “utilization,” “utilize,” and “leveraging” for a direct replacement. This is not a ban or a demand for synonyms: retain a word when it is the accurate technical term and the surrounding sentence makes its meaning clear.

### Plain words and precise terms

Apply the language rules to all reader-facing text in the requested scope, including existing titles, captions, and diagram labels. Prefer the simplest familiar wording that preserves the meaning. A technical term being correct is not enough reason to prefer it when its precision is unnecessary. Existing wording, consistency with other material, and editing convenience do not exempt a passage. For an exception, record the original phrase, a simpler candidate, and the meaning or precision the simpler form would lose. If none would be lost, use the simpler form. Record any matching diagram update separately; do not preserve unclear text to avoid changing a diagram.

Name the concrete object, the component acting on it, what changes, and the consequence. Prefer “the application checks the returned fields” to an abstract chain of nouns. Do not add an actor such as “the development team” when the software performs the step.

Use everyday wording unless a more difficult word supplies necessary precision. “Whether the method will work” often serves better than “the feasibility of the method.” Keep “interpolation” when teaching that mathematical operation, but define it before relying on it. Do not replace established terms with strained synonyms or remove equations, proofs, parameters, or failure analysis to simplify the reading.

Some words carry a precise meaning in one sentence and none in the next. None of the words below is banned, and several are the correct technical name in their own subject. They are listed because they are the ones most often reached for when a sentence has not decided what it is about. Apply one test at each occurrence: **can the reader point at the thing the word names, and does the sentence still work if you name that thing instead?** When it does, name it. When the word is the established term for the object being taught, keep it and define it at first use.

| Word | Keep it when | Rewrite it when |
| --- | --- | --- |
| **boundary** | a real edge exists: a page, chunk, or token boundary; or it is the established term, such as a trust boundary, or a decision boundary in classification | it stands for a system that has no edge. “The application boundary” and “the product boundary” name nothing a reader recognizes; say which code validates the input, or which check runs at the crossing |
| **scope** | it is the defined extent of something specific: the cases in scope for a benchmark, the records a token is scoped to | it stands for the subject in general, as in “the scope of the system.” Say what is included and what is not |
| **framework** | it is the actual name of a published framework, such as the NIST AI RMF or an ISO standard | it is used for a library, a method, or a way of thinking. Name the library, or state the method |
| **shape** | it is an array or tensor dimension, where it is the standard name | it stands for structure in general. State the fields, the output format, the schema, or what the choice determines |
| **layer** | it is a real layer: a transformer layer, or a named tier of an architecture being taught | it means “everywhere,” as in “at every layer.” Name the places |
| **space** | it is a mathematical space being taught, such as a vector space | it means a set of possibilities, as in “the output space.” Say “the possible outputs” |
| **surface** | it is a mathematical surface, such as a loss surface | it means extent of exposure, as in “attack surface.” List the inputs an attacker can reach |
| **posture, landscape, perimeter, envelope, footprint** | a specific measured quantity is defined under that name in the subject | otherwise. Each names a feeling of extent rather than anything checkable. State the controls in place, the systems affected, or the limit |
| **lifecycle** | the stages are taught and the reader needs them as a set, as in a memory lifecycle | it is a gesture at duration, as in “the system lifecycle.” Name the stage that matters here |
| **component, mechanism, pipeline** | the reader already knows which one, and the general word avoids pointless repetition | the specific name would be clearer. Say the retriever, the judge, the evaluation pipeline |
| **named** | something is actually given a name, as in a variable named `limit` | it means “the” or “a specific.” Drop it |
| **bounded** | the bound itself is the subject, as in a bounded loss | the limit can be stated: “capped at eight steps,” “no more than two retries” |
| **therefore, thus, hence** | the conclusion would otherwise read as a new claim | the stated sequence already carries the link |
| **abbreviated, leverage, utilize, merely, approximately, subsequent, corresponding, primarily, frequently** | the precise sense is needed, as with an approximate result | a plainer word says the same: shortened, use, use, just, about, later, matching, mainly, often |

A word appearing in this table is a reason to read the sentence, never a reason to edit it. Replacing every occurrence of one of these words is the failure mode described under “Wording passes across a guide,” not compliance with this rule.

Keep these distinctions intact:

- An API is an exposed interface; a protocol specifies message exchange; a schema specifies message structure.
- Faithfulness and source attribution describe different properties. Preserve the metric or method's actual name.
- A trust boundary, an interface, and a limit are not interchangeable. Say which property matters.
- Agent memory and model reasoning are acceptable terms when their implementation is clear. Avoid implying permissions or human intentions that a component does not have.

Explain unfamiliar names and abbreviations at first use. Avoid unusual uses of ordinary words such as “ownership” when a direct statement of which component stores, checks, or executes something is clearer. Keep publishing terms such as “teaching locus,” “disposition,” and “artifact freshness” in project records unless the subject itself requires them.

### Neutral teaching voice and clear actors

Write adult-to-adult. Explain the evidence, mechanism, choice, and consequence without moralizing, scolding, praising the reader, or implying that a difficult idea is obvious or easy. Avoid dismissive phrases such as “simply,” “of course,” and “as you already know” when they hide a reasoning step. Do not tell the reader what to think, feel, remember, or appreciate. State the relevant fact and why it matters. Direct instructions are appropriate for a procedure, exercise, safety step, or genuine requirement. Otherwise, describe what the system does and how the conclusion follows. This rule does not weaken technical, legal, or safety requirements.

Prefer active voice when the actor performs a meaningful action or affects the reader's interpretation: “The application validates the returned fields.” Passive voice is appropriate when the actor is unknown, irrelevant, or less important than the object or result: “The samples were heated to 80°C.” Do not use passive voice to hide responsibility or leave a mechanism unclear. Identify the actor when it affects the explanation, but do not force active voice by inventing “we,” “the team,” or “developers.” Judge the sentence by whether the reader can tell what happened, what acted when that matters, what was affected, and why the result follows.

### Concision

#### Occam principle for explanations

Use the shortest natural explanation that fully teaches the point. Start from the most direct reason or problem, and choose the most straightforward example that demonstrates it. Each extra actor, scenario, concept, or step must help understanding or preserve a property the explanation depends on. If a simpler explanation or example teaches the same point accurately, use it. For instance, tokenization is introduced because a model processes numeric representations of text; evaluation needs are a later consequence, not the reason text must be encoded.

Shortest means sufficient, not compressed: keep necessary definitions, causal steps, assumptions, limits, and interpretation. Concision must not make the reader reconstruct missing reasoning. A brief direct explanation can establish the question without an invented incident; a longer example is justified when its added detail affects the conclusion.

#### Deletion test before wording repairs

Before improving a sentence, decide whether it belongs in the current explanation:

1. Read the paragraph and the next connected passage with the sentence temporarily removed. Include any linked prerequisite or intervening object needed to judge the connection.
2. Name what becomes incorrect, harder to understand, or disconnected: a missing definition, reasoning step, condition, useful example, or connection. A fact disappearing is not by itself a teaching loss.
3. If information is lost, explain why the reader needs it here. Retain necessary content; move useful content that belongs elsewhere; remove a sentence when no needed understanding or connection is lost.

Record the lost contribution and its local need, or why removal loses neither. Check a proposed group of deletions together as well as individually; individually redundant sentences may contain the only remaining explanation when removed together. This test proposes edits, not permission to make them. A true sentence can still be unnecessary. Check the accuracy of retained claims; removing an unnecessary false claim needs no polished replacement. The test does not require inventing a transition for a self-contained reference entry.

Say each point once, positively, and plainly. Apply these checks when drafting and when reviewing:

1. **State what a thing is or does.** Use a negative such as “not X” or “does not Y” only to correct a misconception the reader is likely to hold at that point. Correct each misconception once per chapter, in the place where it arises.
2. **Remove restatement.** Cut a sentence that repeats the previous sentence, paragraph, figure caption, callout, or table. When two passages teach the same point, keep the one in the better place and point to it. A closing summary may restate only what the reader needs for the next step.
3. **Earn every modifier.** Cut adjectives and adverbs that add no checkable meaning, such as clear, specific, explicit, important, actually, simply, robust, or comprehensive. Keep modifiers that change the claim, such as approximate, optional, per-request, or at most.
4. **Use the shortest exact form.** Replace inflated constructions: “is responsible for deciding” becomes “decides”, “in order to” becomes “to”, and “for a consolidated reference of every formula, see Appendix C” becomes “Appendix C collects the formulas.”
5. **Keep every teaching contribution.** A shorter passage that drops a premise, qualifier, step, limit, or example is a defect. Merge the unique part of a redundant sentence before deleting the rest.

Concision never overrides the teaching requirements in this reference. When exact repetition of a term, a parallel rule, or a needed qualification makes a passage longer, keep it.

### Repetition and sentence weight

Normally avoid repeating a substantive word in the same sentence or nearby sentences. Review adjacent sentences and the surrounding paragraph. Merge redundant statements, use a clear pronoun, or recast the sentence before reaching for a synonym. Remove duplicated labels such as “Example: example” and repeated heading/caption wording.

Necessary repetition is allowed: common connecting words, articles, exact technical names, quotations, code or notation, explicit contrasts, and parallel enumerated rules where repeated wording makes the rule easier to compare. Repeating a precise term is better than changing its meaning. A lint warning identifies a passage to inspect, not a requirement to vary every noun. Record exceptions only when needed for an automated check; do not burden the reader with explanations of editorial choices.

Favor short sentences with one main claim, but judge comprehension rather than a rigid word count. Split a sentence when clauses conceal who acts or how one result follows from another. Avoid inflated phrasing, gratuitous negation, self-praise, and commentary about how the guide was written. Keep a natural causal connector when it helps; neither three-item lists nor ordinary punctuation prove poor writing.

Keep semicolons rare, preserving the agreed move toward simpler sentences. Prefer a full stop or a clearer rewrite. Retain a semicolon only when the close relationship between its clauses benefits the reader; respect any stricter rule explicitly configured for the project. Do not reintroduce them merely to vary punctuation.

Read difficult passages aloud. If a learner cannot say what happened and why, rewrite the passage. Delete a sentence when it adds no prerequisite, explanation, consequence, decision, or useful example. Preserve a meaningful distinction instead of turning “not X but Y” into a habitual sentence shape.

## Paragraph flow and presentation

### Chapter openings

A chapter's opening and any purpose line beneath its title should express complete thoughts. Establish the problem in the subject itself, without announcing what the chapter will cover. Choose wording that tells the reader whether the opening describes a general possibility, an assumed situation, or an observed result.

Read the opening as a connected explanation: what can happen, who acts on what, why it matters, and which response is expected or observed. These are meaning checks, not a fixed paragraph template or a requirement to include every distinction in every opening.

### Connected narration

Introduce a Part's central question, what its chapters establish, and why they follow in that order. Use as much prose as needed, not a fixed paragraph count. Front-matter content requirements belong in `source-planning-contract.md`.

Start each instructional section with enough prose to establish its subject and necessary terms before a visual, equation, table, or code block. Use the preceding result to make the next question clear. Do not repeat a recall/need/preview template at every heading, or introduce unfamiliar terms merely to preview them.

After a calculation, concrete trace, or visual, explain what the result means. An example must establish its operating mode, task, inputs, target or reference when relevant, and intended decision before the trace begins. End it with what the trace demonstrated and the consequence for the reader's next decision. Use labels that match the learner action, such as Conclusion after examples and Answer after checkpoints. Avoid generic Feedback when the passage is really giving a result or solution. Reference entries and short subsections need no artificial closing paragraph.

For a chapter revision, reading its opening and section handoffs in sequence gives a first view of the flow. It does not replace reviewing the intervening paragraphs. Apply the claim checks throughout: the premise, actor, action, and claim strength must hold wherever they appear. Moving a section also requires reviewing the surrounding transitions and any prerequisites it supplies elsewhere.

Teach a full method once, then link back when later chapters extend it. A brief recap is appropriate when needed to interpret a new example; avoid copying a complete pipeline without a teaching reason. End-of-chapter questions, when included, should exercise the objectives taught there, with answers or feedback. Explain deliberately cumulative questions rather than treating all earlier knowledge as topic leakage.

When a paragraph seems out of place, identify the question it answers and where that question arises. A bridge uses the established result to raise the next question; it must not import an unrelated evaluation, cost, or deployment argument to force continuity. After an edit, reread the affected paragraphs and their connections. Keep unresolved findings visible, even if every record is filled and every automated check passes.

### Descriptive titles

Titles identify the subject, process, or useful relationship; they do not tell the reader what to do. Prefer “Model alignment” to “Train a model to respond to users,” and “Generating an answer one token at a time” to “Generate an answer one token at a time.” A clear declarative title can use a verb: “General language models can perform different text tasks.”

Use familiar technical names when they are the right subject. Avoid vague capability wording, unexplained acronyms, marketing phrases, and repetitive “Why this chapter matters” headings. Keep capitalization consistent. Prefer a colon for a useful subtitle; do not repeat the same title in the heading, image, and caption.

Renaming a Part, chapter, or section title changes the outline the author approved. Propose the new title with its reason, and apply it only after the author approves. The section ID stays the same, and the structure lock records the change.

### First-definition emphasis

A term's first teaching occurrence in the book is shown in blue. Mark it with the definition span, bold inside the span: `[**term**]{.definition-term custom-style="Definition Term"}`. The publisher renders this span in bold dark blue (#1F4E79) in HTML and Word, and readers use that color to spot a newly introduced term. Mark each term once per book; later uses are plain text. Glossary items use the same span in list form: `- [**Term:**]{.definition-term custom-style="Definition Term"} Definition.`

A formal "X is Y" sentence is optional. Omit it when the sentence that introduces the term already makes the meaning clear, for example "Each piece is called a [**token**]{...}." Write the formal definition when the meaning, purpose, or object the term acts on would otherwise be unclear. The color never replaces meaning: from the marked passage alone, the reader must be able to say what the term refers to. The Glossary carries the formal definition for every marked term, with the same spelling. Where the sentence allows, mark the singular base form so that the Glossary entry matches.

Do not introduce terms with plain bold or italics. Italics mark titles of works. Plain bold marks list labels (`**Label:** text`) and callout titles. Code identifiers use code formatting, not term marking.

### Tables and lists

Use tables for comparisons, reference mappings, and measured results whose relationships are easier to inspect in rows and columns. Give headers visible emphasis and keep unrelated statements outside the table. Do not flatten a narrative into cells.

Use numbered lists for procedures and traces when their order matters. Use bullets for independently useful items. Explain the causal links around a list when the steps alone do not make the reasoning clear; do not force every list into prose.

### Accessible links and location references

Write link text that states the destination or action and still makes sense when read without the surrounding sentence. Do not use bare link text such as "here," "click here," or "read more," and do not use a raw URL when a short descriptive label is available. State when following a link downloads a file, opens another application, or performs another action the reader might not expect.

Refer to content by its heading, figure, table, equation, label, or descriptive link. Do not make "above," "below," "on the left," "on the right," or color the reader's only way to find or identify something, because page layout and presentation can change. When color carries meaning, repeat that meaning in a label, symbol, or text.

### Procedures

Before a procedure, state its outcome, required starting state, and prerequisites that the reader must prepare. Keep background explanation outside the numbered steps unless the reader needs it while performing a step.

Put each reader decision or main action in its own numbered step. Keep actions together only when separating them would make the procedure harder to follow. Put a condition, tool, location, or goal before the action when the reader needs that context to perform it correctly. Use the exact command, control, field, or menu label that the reader will encounter.

Mark an optional step as optional at its beginning, and distinguish an optional action from an alternative way to complete the task. After an action, state the expected result when the reader needs it to confirm success or find the next step. Preserve necessary safety warnings and place them before the action that creates the risk.

## Writing, review, repair, and recheck

### Draft, review, repair, recheck

Apply these roles to new explanations and already written text. Review connected chunks with their audience baseline, needed preceding material, and applicable rules. Choose chunks small enough to inspect every statement while retaining its context, not isolated sentences. For substantive teaching work, create an independent reviewer with a fresh agent or context when delegation is available and authorized. A role label in the writer's conversation does not satisfy this requirement. If delegation is unavailable or not authorized, record the missing independent review and keep acceptance pending. Deterministic presentation-only fixes need only their relevant checks. This workflow does not authorize manuscript edits or publication.

1. **Writer:** Identify the question answered and the knowledge the reader brings. Draft the direct explanation in familiar language, then add the exact terms, necessary qualifications, and simplest useful example. Teach meanings before later reasoning relies on them; use the existing first-definition and glossary rules. This is a drafting sequence, not a compulsory question heading, separate document, or fixed paragraph template.
2. **Reviewer:** Omit the writer's defense, intended findings, proposed repairs, and previous verdicts from the first review input. Request the three stages below in separate calls, completing one before requesting the next. The same independent reviewer may continue across stages, or different reviewers may cover them. Parallelize disjoint chunks, not dependent stages of one chunk. Each stage reads the actual text and records its own answers; carrying all questions in a generation prompt is not three completed reviews.
3. **Editor:** Correct evidenced failures within the authorized scope. In an existing-text pass, test before rewriting; retain sufficient passages. Preserve correct claims, conditions, distinctions, units, uncertainty, and required steps. A correction to a false claim needs appropriate evidence, not preservation of the error. Record the original, repair, and reason, and reread the surrounding explanation.
4. **Recheck:** Review the repaired passage and affected prerequisites and connections against the same questions, plus any new questions or terms the repair introduces. Keep unresolved or disputed findings open. Use fresh content and rule hashes; a completed record or fluent rewrite is not approval.

#### Review rounds, levels, and parallel work

Begin a round with a fixed source and rule version, the intended audience and
assumed knowledge, a declared scope, and one owner for overlapping edits. Use the
existing plan, chapter/section IDs, paragraph locations and hashes. Do not invent
word-count thresholds or another manually maintained division of the book.

Inventory the reader-facing text, not just what a paragraph extractor returns.
Include project/landing text, Part openings, typed block fields, captions, alt
text and titles held in HTML attributes when used by the output. Exclude pure
markup with a reason, but inspect mixed comment/text records and visible title
fields before classifying them as structural. Source wording and rendered or
pixel fidelity are separate checks.

For a book-wide review, establish the book's learning goal, each Part's question
and each chapter's contribution from the actual teaching content. Compare what
the chapters teach with what their reasoning requires, and consider another
order where a dependency or purpose mismatch gives a reason. Then inspect section
and paragraph purpose and order. For a local task, use the relevant larger frame
and expand only through connections that may affect meaning. A sound local
paragraph does not establish a sound chapter or book arrangement.

Compare learning progression as well as strict prerequisites. For a book, Part
or chapter order concern, compare the present path with a plausible alternative,
including moving a short shared foundation rather than swapping whole chapters.
Check whether the reader learns how to choose and interpret an input before a
later method uses it for a decision. Derive that learning task from the actual
purpose and teaching, not only from the smallest calculation the reader can do.
Passing a prerequisite-order check does not establish the best teaching order.
Distinguish a missing prerequisite from a supported order improvement and record
the teaching benefit and cost of rearrangement.

At the start of the first review call, read for anything that seems misplaced,
missing, contradictory, misleading or needlessly complicated before applying the
detailed questions. Treat this open-ended read as a search for evidenced concerns,
not a demand to find defects. Repeat a connected read at the end of the flow stage.
Do not add a separate compulsory agent or extra whole-book pass for this step.

Keep meaning and definitions together in truth review: identify the literal actor,
action, object and conditions; compare the likely reader interpretation with the
source, code, calculation or described system. State an unfamiliar term's meaning
and purpose before reasoning depends on it. Check a plausible counterexample when
a claim promises more than its evidence establishes. Do not infer intended meaning
merely because an expert can repair the sentence mentally.

Before confirming a defect, test the strongest reasonable reading that retains
the full passage, including its qualifiers and nearby limits. Do not strengthen
an objection by ignoring a condition, treating a partial illustration as a complete
schema, or reading a possible inference as an established false claim. Keep a
remaining interpretation risk separate from a confirmed contradiction.

For reader-understanding questions, identify what the reader must explain or do
at this point, what knowledge that requires, and where the reading path supplies
it or the audience baseline permits it. Cite the exact missing step rather than
calling prose confusing. A passing label, glossary entry, preview or present-day
cross-reference does not establish a prerequisite or adequate teaching. A concept
can be needed without its entire current chapter being needed. Use the concept
index as an evidence aid, not as a substitute for these judgments.

Check the actual earlier reading path before calling a term undefined, including
teaching outside the assigned target group. Record missing local clarity separately
from missing book teaching. Check relationships and transitions between adjacent
definitions too; adequate individual definitions do not establish how they fit.

Parallelize independent target chapter groups on the same fixed version. Each
group receives its needed earlier context and shared definitions, and completes
truth/reasoning, necessity/terminology and understanding/flow in separate sequential
calls. Source retrieval and separate code, calculation or figure checks may run
alongside the relevant call, but its final conclusion must incorporate their
results or retain the limit. Do not run dependent stages on the same text in
parallel, and do not let reviewers modify the shared text while others read it.

Keep stage answers brief and reuse existing locations, hashes and shared evidence.
Do not copy every older packet field into each stage as a new writing task. This
does not waive a claim check or an acceptance record: link the applicable evidence
and keep unperformed checks pending. A mechanically filled retain decision is not
a completed paragraph judgment.

One coordinator integrates the findings across groups: first teaching locations,
shared meanings, chapter roles, repeated teaching, Part/chapter order and handoffs.
Read the relevant actual passages, not only reviewer summaries. Conflicting
findings return to the earliest question they depend on. A majority of local
approvals cannot approve the overall reading path. Preserve each actual call and
its source/rule hashes; do not rewrite historical answers after integration.

If repairs are authorized, record the original, repair, reason and affected
connections, then freeze a new version. A meaning, definition, assumption or source
change returns to truth/reasoning; a necessity or wording change returns there too
when meaning may change, otherwise to necessity/terminology; a move returns to
truth review when prerequisites or meaning may change, otherwise to flow review.
Repeat later dependent checks on the affected text. Pure formatting keeps its
directly relevant fast path. Do not repeat a whole-book audit for every local edit.
In a review-only task, retain book findings as pending; do not invent repair
rechecks when no book repair occurred. Disputed findings can still receive an
independent clarification round on the unchanged text.

A new meaning question found during wording or flow also returns to a focused
truth clarification, even without an edit. Preserve the first verdict and add the
later disposition and reason. Repeating a full book pass is unnecessary when only
that question and its connected passages need checking.

Finish with a current independent connected read of the affected learning path,
plus only the requested output checks. Stop when no required correction in the
reviewed scope remains unresolved and no later edit has invalidated its checks,
or report the unresolved decisions and limits. Optional wording choices do not
justify endless loops. Unchanged source, rules and finding status do not justify
another automatic round. If revisions repeat an earlier content hash or undo one
another, stop and expose the underlying purpose or structure choice to the author.
A stopping rule prevents wasted work; it does not prove the text is correct.

The three review stages are:

| Stage | Questions to answer from the text and its reading path |
| --- | --- |
| 1. Truth and reasoning | What does each key statement literally claim, what would its intended reader infer, and do those agree with the evidence? Are definitions, symbol meanings, roles, conditions and claim strength correct? Can the subject perform the action? Does the reason explain the conclusion? Trace necessary inputs, changes and results; check relevant code, math, tables, sources and figures. |
| 2. Necessity and terminology | Is there a real need to make this claim here? Apply the deletion test before proposing wording repairs. Is this word needed? Identify uncommon words, specialist meanings of ordinary words, and specialist phrases made of familiar words. Keep an exact term when needed, but establish its meaning before use. Test a simpler sufficient explanation or example without losing conditions or distinctions. |
| 3. Reader understanding and flow | What must the reader explain or do here, which knowledge does that require, and where is it supplied? Give plain answers supported by the reading path or declared background, without filling gaps from expertise. Check purpose and order at all levels in scope: book, Part, chapter, section and paragraph. What does each passage add, why is it here, and does its connection follow? End with an open-ended connected read. |

A fluent sentence with familiar words still needs all three stages. For example, a sentence may explain what selects an operation while claiming to explain why a system can perform it. Word familiarity does not establish correct reasoning. Familiarity also depends on the audience and the meaning used here, not only on how often a word occurs.

For each stage, give brief passage-based answers, not just locations or a general clarity verdict. Check earlier teaching before filing an omission. Retain sufficient passages with a reason. Separate defects, optional preferences, and unsupported objections; do not invent a defect to demonstrate effort. Unresolved questions remain findings. The third stage must not fill a missing explanation from outside expertise. First-definition styling helps readers find a term but does not establish its meaning.

Review locally as writing progresses; before book acceptance, review the complete reading path for teaching order, inconsistent meanings, missing prerequisites, and repetition. A local review cannot approve unread chapters. Keep technical correctness, code, math, sources, and visuals under their existing checks.

When changing this workflow, test its behavior on a small mixed set of flawed and sufficient passages, including new subjects or wording. Give a fresh reviewer the rules and reading context without an answer key. Compare its findings and proposed repairs with independently prepared expectations: count missed defects, unnecessary repairs, and lost qualifications. Scripts may check coverage and evidence presence; they cannot establish reader understanding. Record test limits rather than promising the skill prevents every lapse.

### Review word choice in context

During a teaching review, read every paragraph in the requested scope for meaning and placement, including words that no lint rule flags. A familiar or technically permissible word can still suggest the wrong object, relationship, or action. Passing a banned-word scan does not satisfy this review.

For each questionable phrase, check:

- **Literal meaning:** What concrete object, operation, or relationship does it describe? Does the ordinary or established technical meaning fit?
- **Reader interpretation:** What is the reader likely to understand at this point? Does the phrase depend on a distinction or connection taught only later?
- **Actor and action:** Who performs the action, and has that person or software component been introduced? Establish a person's purpose before explaining how software serves it when that purpose motivates the example.
- **Analogy and limits:** Would the direct term be clearer? Retain an analogy only when its mapping is explained and it does not imply false properties. Do not turn the example below into a ban on a word used correctly elsewhere.
- **Local relevance:** Which question raised by the surrounding explanation does this sentence answer? Place supporting details where the reader needs them. Explaining a term somewhere before its eventual use is insufficient if that explanation interrupts the current reasoning.

For example, calling token IDs “addresses” before explaining any lookup leaves readers to invent the relationship and may suggest memory addresses. Use “token IDs” or “integer identifiers for vocabulary entries” there. “Embedding-table row” fits a later explanation of row selection. Actual memory addresses remain the correct term when teaching memory addressing. Similarly, explain a software library beside the operation or code that needs it, unless its role is necessary to understand the earlier discussion.

### Paragraph purpose and connections

In a flow review, account for every paragraph in the requested scope, including prose in lists and callouts. Record its source location and hash, the point it adds, how it follows from the preceding explanation and prepares what follows, and a decision to retain, revise, move, or remove it with a reason. A self-contained reference item needs no invented transition. Keep this record brief; repeat the paragraph only when quoting a finding or when the review tool supplies it. Review the full book before book acceptance. A local pass covers the changed paragraphs and the passages whose meaning or connection they affect, without claiming that unread material passed.

### Review records and limits

For a finding, record **passage and location, failed check, missing or misleading point, prerequisite locations checked, and proposed repair**. "Unclear" or "convoluted" alone is insufficient. Reuse the paragraph and unit records. Record stage call IDs, reviewer identity, initial fresh context, covered units, source/rule hashes, answers and unresolved questions in their workflow section. Use platform call IDs when exposed; otherwise label a local request ID and retain its actual request/result evidence, without claiming it is a platform ID. The coordinating agent requests each stage, checks its coverage and resolves or carries forward findings before requesting the next. Do not infer completed stages from one final verdict or fabricate execution evidence. A definition needs meaning and purpose, not an invented input/output process. Short references need no artificial bridge.

For existing text, assess before rewriting. Apply only authorized repairs, then review the resulting passages and affected connections, including new terms or claims introduced by the repair. Record the previous and resulting source hashes and the recheck call. Recheck unchanged material only when its meaning or connection can be affected. A source change makes an earlier approval stale; a word-level diff alone does not establish that meaning survived.

Preserve earlier reviewer calls with their original source and rule hashes. A separate current reuse record may adopt their answers for verified unchanged units after an independent reviewer checks the original source connection, current rules, and affected prerequisites and transitions. Do not change an older call's hashes, scope, answers, or time to make it current. A format mismatch or changed whole-book hash alone is not a missing teaching answer. The quality gate's reviewer-call reference describes the binding; acceptance still requires full current coverage and unresolved conditions must remain visible.

The quality-gate companion prepares records and checks documented completion. It does not create reviewer agents, count invisible internal passes, prove the recorded agent ran, or judge answers true. The agent using the skill must launch available reviewers and record actual call identities; if that cannot be done, report the limit. Passing completion checks never establishes complete teaching.

Record the exact phrase and its line or paragraph location, a plain-language paraphrase, the actor, object, action or state change, condition or consequence, and a verdict to retain, revise, or delete it. A retained phrase needs a concrete reason; a revised or deleted phrase needs the replacement or removal decision. For each reviewed unit, provide passage-specific evidence of this assessment and of paragraph continuity. When no correction is needed, explain why the cited wording and placement serve the reader rather than writing only “clear,” “reviewed,” or generic statements such as “gives the definition.” Do not claim a contextual review of unchanged passages that were not read.

Automated scans may identify candidates and validators may check evidence completeness. Neither establishes that an analogy is accurate, an actor is clear, or a paragraph belongs in its current location. Unresolved findings prevent a semantic pass for the affected unit.

### Wording passes across a guide

Changing one word wherever it appears is a review of many separate sentences, not one edit. The rules above are judgments about a particular sentence, so a pass that applies them in bulk removes the judgment they depend on. A pass that revisits wording across chapters follows these rules.

1. **Decide each occurrence in its own sentence.** Read the sentence, and the sentence on either side, before changing a word. The same word can be filler in one paragraph and the precise name in the next. A count of occurrences is a list of places to look, never a list of places to edit.
2. **Do not apply a substitution across files.** Editor-wide or scripted replacement of a word, a phrase, or a callout title is not permitted, whatever the expected count. Matching the expected number of replacements is not evidence that any of them was right.
3. **Record the replacements before they land.** List each change as its location, the original wording, and the replacement, so a reviewer can read them without reconstructing the diff. A pass that cannot produce that list has not been reviewed.
4. **Re-read the whole changed paragraph, not the changed word.** Splitting a sentence, cutting a connector, or shortening a clause changes what the neighbouring sentences attach to. Check that the paragraph still states the same premise, limit, and consequence in the same order.
5. **Treat a lost qualifier as a defect.** A replacement that widens or narrows a claim, drops a condition, weakens a requirement to a capability, or turns a measured result into a general statement is a correctness error, not a style preference. Restore the original wording rather than repairing it with a second substitution.
6. **Leave the exact term alone.** Established names of metrics, methods, components, protocols, and mathematical objects stay as they are, even when a plainer word exists. Repetition diagnostics and prose linters are editorial warnings; they do not authorize a synonym.

A wording pass is a content change. It needs the same per-unit review evidence, acceptance record, and fresh checks as any other edit to the guide.
