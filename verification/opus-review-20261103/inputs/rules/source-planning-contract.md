# Sources and teaching structure

## Inventory and coverage

Assign a stable `source_id` to every PDF page, slide, DOCX semantic unit, notebook cell, assignment requirement, instructor clarification, figure candidate, and external claim. Record source file/hash, unit locator, presentation order, type, and concise teaching value. Distinguish a file inventory from a unit inventory: counting files does not establish page/cell coverage.

Create chapter work packets from this inventory. Reopen originals for ambiguity, exact formatting, equations, quotations, or visual meaning, not for repeated whole-corpus scans.

Every source unit needs one final status:

- `covered`: explained at a specific guide location;
- `intentional-consolidation`: explained with the identified related units;
- `duplicate`: the equivalent unit is identified;
- `intentional-omission`: a reason explains why it is unnecessary for the guide.

An unexplained missing unit, duplicate ID, unresolved status, or absent explanation location prevents final source acceptance. Match the unit inventory and coverage IDs exactly. Separately review whether the referenced text teaches the material; a row marked covered is not that review.

## Structure and order

Preserve chronological coverage by week and presentation order. Arrange chapters by prerequisites and causal relationships when that teaches better, recording both orders. Establish a baseline before variations, and explain the assumptions and conditions under which its conclusions apply.

Choose the appropriate overall relationship: a sequence of transformations, a branching comparison, or a layered system. Do not force every subject into a software pipeline. Each Part and chapter needs a coherent purpose. Chapter packets record the complete section list, source IDs, claims, examples, equations, code, visuals, and connections to adjacent material.

For an existing book, apply `structural-preservation-contract.md` before moving, merging, renaming, or removing teaching material. A changed heading is not evidence that the underlying explanation survived.

## Front matter and reference material

Front matter establishes the book's central subject, expected starting knowledge, useful reading paths, scope, and access to its appendices. These are content requirements, not four compulsory headings or a filename convention. Use the chapter plan's actual IDs and paths.

Include front matter, all Parts and chapters, and appendices in navigation. Keep a link's description visually separate from its title. Part descriptions may be compact noun phrases or complete declarative sentences; avoid verbs without a subject.

Keep formula sheets, glossaries, answer keys, source maps, and other lookup material in suitable appendices rather than a miscellaneous final chapter. Link each appendix from relevant main text or a useful front-matter guide. A table is appropriate when it helps readers compare several reference resources; it is unnecessary for one entry.

## External claims

Record the exact claim, primary paper or official documentation, URL or durable identifier, publication/version date, access date, guide location, and category: `course-claim`, `stable-background`, or `dated-current-supplement`. Use `verified`, `needs-refresh`, `superseded`, or `rejected` as status. A required claim awaiting verification or refresh prevents final release. Date claims about changing software or provider behavior.

Keep source evidence separate from checks on the publishing process. External evidence-package services are not implemented merely because a storage field exists; use the publisher's stated capabilities.
