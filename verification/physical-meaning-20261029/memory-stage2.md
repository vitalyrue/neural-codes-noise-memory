# Memory chapters: independent stage 2 necessity and terminology

Reviewer: physics_memory_review. Local request ID: memory-stage2-20261029-111235. This labels this actual call, not a platform-generated call ID.

Start and hash checkpoint: 2026-10-29T11:12:35.0798422+02:00.
Connected-text read checkpoint: 2026-10-29T11:13:13.9613768+02:00.

Scope: additions, new folds, and their connected prose in the five memory chapters. Actual current passages were reread. All five source hashes match the completed stage 1 versions, including its repaired readout fence. Rules: course-study-guide-builder/SKILL.md and references/pedagogy-language-contract.md, already read in this reviewer session. Stage 1 results establish the reviewed claims' correctness; this call judges whether the claims and words are needed. This is not the later reader-understanding/flow call.

## Verdict

No required wording or necessity repair in this local scope. The additions answer the requested physical questions in direct language. None needs another example, a new section, or an extra technical label. No manuscript changes were made.

## Passage decisions

| Passage | What it adds and deletion test | Terminology and decision |
| --- | --- | --- |
| `01b-persistence.md:9` | Gives a concrete maintained eye-angle pattern, a disturbance, a correcting response, and the case the response cannot correct. The chapter opening gives the general distinction; this paragraph supplies its neural setting before definitions. Deleting it restores the earlier jump from general geometry to formal terms. | “Recurrent input” is taught in foundations. “Originally intended” refers to the cue-supplied value, not an actor inside the circuit. Retain. |
| `01b-persistence.md:15` | States the two-cell code and distinguishes common rate changes from opposite changes outside the worked-calculation fold. It lets a reader skip the algebra without losing the example's point. | “Difference,” “equally,” and “persists” describe explicit operations and outcomes. “Illustrative” and the fit qualification distinguish this teaching example from recorded data. Retain. |
| `01b-persistence.md:49` | Separates the recovery parameter a from the encoding slope k. The first changes correction speed; the second changes the angle corresponding to a fixed rate disturbance. These are different effects, so combining them here is useful. | “Common activity disturbance” refers to the already defined shared rate deviation x. “Decoded angle” has the explicit difference-over-2k formula immediately above. Retain. |
| `01b-persistence.md:68` | Connects physical spikes, return dynamics, and surviving angle changes before the independent-increment model. The final sentence prevents the common confusion between independent retained increments and independent complete recurrent spike trains. | “Extra or missing spike” is more concrete than a generic noise label. The paragraph follows one causal chain and needs no new terminology. Retain. |
| `01b-persistence.md:100–108` | Defines D, gives units, identifies two ways its value can grow, and explains doubling D. It then distinguishes an individual wandering path from trial-to-trial spread. These are the physical reading and parameter consequences of the folded model. | “Diffusion coefficient” is the needed technical name; its meaning comes in the same sentence. Variance, standard deviation, and MSD have distinct uses and should not be replaced by one vague word such as error. Retain. |
| `01b-persistence.md:138–153` | Keeps shared accumulated errors visible and places the covariance proof inside its own fold. The repeated covariance explanation within the fold prepares its equation rather than repeating the whole visible paragraph. | “Shared history” is immediately explained as earlier errors present in later states. Brownian motion and covariance are needed names for the formal calculation. Retain. |
| `02-memory-dynamics.md:48–50` | Completes the cell-j spike to cell-i input to cell-i firing chain. The closing summary maps weight, transfer function, and tau to three different roles, matching the user's parameter question. The model-input qualification prevents treating g as a measured voltage. | “Transfer function” is defined one paragraph before use. Weight signs use “raises” and “lowers” with the necessary increasing-function condition. The summary repeats roles briefly for comparison, rather than adding an empty general conclusion. Retain. |
| `02-memory-dynamics.md:113–115` | Reads the two terms of K as physical decay and feedback. It distinguishes a stronger local response from stability of the whole circuit. Deleting it leaves the parameter combination as algebra alone. | “Local slope” is ordinary calculus, and “recurrent renewal” is immediately unpacked into changes in activation, input, and firing. “Combined feedback” has a concrete object, the whole network. Retain. |
| `02b-memory-long-delays.md:72–74` | Establishes the coordinate/domain, explains persistent common activation and decaying differences, then links larger activation to larger spike variability with unchanged projection weights. These are the needed parts of one two-cell example. | “Activation coordinate” is distinguished from angle at first local use. “Projection weights” refers to v already taught in the dynamics chapter. The paragraph has several sentences but one connected purpose; a sentence-count limit would not establish overload. Retain. |
| `03-memory-information.md:220–226` | Explains why the controlled tau change makes one unit spike a smaller coordinate disturbance, then preserves the separate comparison that changes rates. The visible conditions prevent a parameter recommendation detached from what is held fixed. | “Projection weights” names the previously derived lasting effect; “retuning” means changing network parameters to preserve the curves already specified in the preceding sentence. No additional definition or analogy is needed. Retain. |
| `03b-memory-readout.md:142–199` | Keeps the information-gain versus diffusion interpretation visible, places special-function definitions and the finite-duration solution together, then returns to the physical long-time limit. | Tanh, artanh, and coth are necessary exact mathematical terms inside the solution fold. They no longer interrupt the main interpretation. “Precision” remains correctly defined where the preceding recursion needs it. Retain. |

## Required repairs versus preferences

None of the retained paragraphs requires rewriting just to shorten the page. Splitting the mutual-excitation paragraph at “Larger theta” would be an optional reading preference; its present sequence already develops one model and does not need a compulsory edit. Likewise, changing “more of that variability remains as memory error” to “the retained memory fluctuations become larger” would express the same point. The fixed projection weights and immediately preceding larger variances already supply its intended meaning, so this is not recorded as a defect.

No broad science recheck or unrelated chapter work was performed. The later flow stage should still judge whether the visible reading path, with folds closed, supplies the required learning steps.

## Source and rule SHA256

| File | SHA256 |
| --- | --- |
| 01b-persistence.md | 5BEA2D0482DBC15B2862E5FD2B16ECC8E7F257056D224AEEE2FBE07E370A7EA5 |
| 02-memory-dynamics.md | 869913AA0DFBC2E06145D5458DD0B7F14535E9CFFD985B2122FEA54E1816F858 |
| 02b-memory-long-delays.md | 70B5EFC6650D2B6C1BBF35B0BDAE7A379D80DFF863944A872B45DF257D7B6BAA |
| 03-memory-information.md | 63A62A989B01E89AD8A26A342BF311F987286D75167D8854F708D0A8DE4B2D2C |
| 03b-memory-readout.md | 3FA9CE95117610C8DFE5E9F0C7995ED4D38FE96674D3B2BDD2AF04D1EBE268D5 |
| course-study-guide-builder/SKILL.md | B78068E9874E6D1D97B2017BF8F940492F9B08FC11B74F20FD75019FF388984A |
| references/pedagogy-language-contract.md | F4C1EB544CF640B708E1970D9572FDC758FCC6AEA806675D01A0256658DF847A |

Completion checkpoint: 2026-10-29T11:14:28.2297040+02:00. Wall-clock time is measured from the recorded start. Awake execution time is unverified because no Windows sleep/resume-event check was performed. Token stats unavailable.
