# Stage 2: wording and necessity, dynamics and reading guide

Local request ID: stage2-dynamics-reading-20261028-170039. Reviewer: separate_readout, Sol high, independent of these files' authors. Started 2026-10-28T17:00:39.335809+02:00; completed 2026-10-28T17:02:00.132747+02:00. Separate call after Stage 1. No manuscript edits or new source audit.

Scope: current changed passages and their connected context in `02-memory-dynamics.md`, the new role explanation in `00-reading-guide.md`, and the new appendix table fields. Audience: undergraduate mathematics, no assumed neuroscience. Hashes are unchanged from Stage 1.

## Verdict and required changes

No required Stage 2 changes. The role labels serve the requested distinction and the added sentences give assumptions, a general rule, a mapping, or an interpretation needed to follow that distinction. The repeated labels function as reading markers; replacing them with varied synonyms would obscure their consistent purpose.

## Passage judgments

- **Dynamics spike model:** the assumption list earns its place before formal manipulation. The later Poisson covariance and weight descriptions supply the details used by the calculation, so their overlap with this list is useful rather than an unnecessary second explanation. The count-process sentence says what the mathematical object records before mapping it to spikes. The added final balance sentence explains what the steady-state equation means physically.
- **Dynamics return flow:** the added one-neutral-direction, decaying-other-modes and small-perturbation conditions establish the circumstances in which the following projection argument works. Removing them would leave the model's required local behavior less visible before the proof. Defining linearization before substituting the neural state lowers the number of unfamiliar objects introduced together without adding technical vocabulary.
- **Dynamics diffusion:** the added first paragraph connects fluctuating outgoing activation to the lasting memory change and states where rates/flow are evaluated. The next paragraph teaches the general variance rule before supplying its neural weights. These paragraphs explain different steps and should remain. Later cautions about changing firing rates and local time windows still add necessary limits rather than repeating the mechanism.
- **Dynamics symmetric weights:** equal reciprocal weights are explained in ordinary language while preserving differing firing responses. The repeated assumptions identify the scope of this special case. The chain-rule sentence connects the familiar mathematical operation to the response/input slopes used next. The interpretation tells the reader which measured/model curves enter the result before preserving the source square warning and its uncertainty.
- **Reading-guide three roles and example:** each list item answers a different reader question. The spike example connects the roles to one transformation, and its final sentence explains why a general mathematical tool only becomes a neural prediction after neural assumptions are assigned. The following observer paragraph makes a distinct point about implementation evidence, so it is needed despite its related language. The conceptual-route instruction and the appendix table serve different purposes: one tells how to read a topic, the other where to find each source topic.
- **Appendix table:** its questions translate the source section headings into problems a reader can recognize. Labels such as Fisher information remain useful because they identify the source topic, while the neighboring question explains their purpose. The mathematical-link wording gives useful destinations rather than repeating each source heading. No rare word or unnecessary general claim requires replacement.

## Model equations versus derived results

The current roles describe purposes, not a ban on equations in the neural-model discussion. Thus no correctness or wording defect requires another sentence. For this particular separation request, the coordinator's proposed clarification is useful but optional. One sentence is sufficient if the author chooses to include it immediately after the three roles:

> A model equation specifies how a cell responds; the derivation shows what follows from that choice.

It concretely distinguishes an assumption from a consequence. It should not be expanded into a general discussion of scientific modeling, nor treated as requiring every equation to move to a different block.

## Current hashes

- `02-memory-dynamics.md`: `837c4b2490bee22b449b75db2d0d575ec639dddf2e4583797fff46a302963607`
- `00-reading-guide.md`: `359fc0791f1e99150a55e621fc3b3637e0d427c5038d3ec2c256049301cbdba5`
- `00-reading-guide.yaml`: `7ee74d6dfe7e8c88a63a258a351a6e01a574ff3eb99fd242503dee6da010687e`

Stage 3 reader-understanding/flow remains pending. Completion checkpoint 2026-10-28T17:02:00.132747+02:00: wall elapsed since this review began 80.8 seconds; same interval since its opening command checkpoint. Awake execution unverified; no clock change established. Token stats unavailable.
