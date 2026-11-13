# Eye/place revised passages: stage 2 necessity and terminology

Local review request ID: eye-place-stage2-20261029-111229. Reviewer task: /root/physics_eye_place_review. Requested stage: necessity, terminology, and insertion-related wording attachments only. Manuscript not edited. Separate stage 3 reader-flow review remains pending.

Started: 2026-10-29T11:12:29.1569856+02:00.
Checkpoint: 2026-10-29T11:12:59.6718362+02:00. Measured wall elapsed: 30.51 seconds. Awake execution time unverified; sleep/resume logs not read.

Read the current changed passages and their surrounding equations and paragraphs in 04-eye-drift.md, 04b-eye-timing.md, 05-place-fields.md, and 05c-place-tests.md. Checked matching edits.json entries and the earlier correctness result. Rules are course-study-guide-builder/SKILL.md and references/pedagogy-language-contract.md, loaded for this task. This stage does not reopen source claims that passed stage 1 or approve the entire four chapters.

## Two local wording repairs

S2-1. 04-eye-drift.md lines 124-130. The sentence "In this case both components decay without oscillation" originally referred directly to k,r,m>0 and r^2>4km. The new static-gain paragraph now separates them, and "this case" follows a statement about changing a single neuron's firing. Keep the sentence, but attach it to its actual condition:

> These are the paired signs in the paper's Eq. 7, with tau_+>tau_- when k,r,m>0 and r^2>4km. In this case both components decay without oscillation.

Then retain the static-gain paragraph. Start a new paragraph with "The same factorization gives two useful identities:" before the product/sum equations. This adds no content and restores the intended mathematical referent. All formulas and their conditions stay unchanged.

S2-2. 04b-eye-timing.md line 171. The inserted paragraph mentions ordinary MSD growth rate approaching 2D and proportional scaling by D, followed by "Its local slope is". The equation that follows is the logarithmic slope alpha, not the ordinary derivative. Replace that short bridge with:

> The local logarithmic slope of this MSD is

This is the same quantity already defined earlier in the chapter. The wording should identify it because two meanings of slope are now adjacent. No equation change is needed.

## Passage-based retain decisions

- 04-eye-drift.md lines 61-78: retain the new position/velocity/acceleration explanation. It gives three distinct roles missing from a units list; deleting it would remove the physical interpretation requested by the user. "Fitted coefficients" accurately limits the claim. The mass clarification prevents an easy but unsupported reading of m. The sentence "Thus k, r, and m describe different demands on the motor signal" repeats the preceding concrete explanation and can be deleted if the coordinator wants a tighter paragraph, but this is optional. A paragraph break before "The delay Delta t is in seconds" would separate coefficient roles from timing; also optional. No added force, stiffness, or inertia account is needed.

- 04-eye-drift.md line 126: retain x=f/k and the doubling example. It makes the parameter useful, unlike another abstract statement that k sets gain. Retain the one-cell causal limitation because inversion of the fit can otherwise be read as direct control. Apply S2-1 to the inherited trailing sentence; do not delete a scientific condition to shorten the paragraph.

- 04b-eye-timing.md lines 110-126: retain B and E as command and eye angle, the mismatch interpretation, the fixed-mismatch comparison for tau, and the distinction from synaptic time. Each answers a different question about what the simplified filter represents. "Mismatch" is immediately given by B-E. "Response time" is supported by the equation and the following decay calculation. Existing "teaching reconstruction" remains the needed scope. There is no new unexplained biological term.

- 04b-eye-timing.md lines 157-178: retain the tau-versus-D comparison. The limiting formulas alone do not state the different parameter effects. The comparison specifies what is held fixed and does not duplicate the earlier command mechanism: it now describes the measured statistic. Apply S2-2 to distinguish logarithmic slope from growth rate. No further numerical example is necessary.

- 05-place-fields.md line 17 and formal fold: retain the visible description with h(x) and x. It states the input object, the role of spatial covariance, the required smoothness, and why movement samples a fixed map. The formal fold supplies the exact Gaussian definition and independence property without replacing the visible mechanism. Repetition of the fixed-map condition is limited to its role at the point where a random-function model is introduced. No need to unfold the formal definitions or add another general covariance lesson.

- 05-place-fields.md lines 48-50: retain the threshold interpretation and comparison with sigma_h and a. "Absolute threshold above the input mean" is longer than "threshold" because the distinction is necessary for the normalization to mean what it says. The positive-threshold condition must remain. The zero-rate boundary statement and positive-Hz-cutoff qualification distinguish a model field from a field extracted from finite rate maps. The last sentence prevents identifying a hidden biological cause from a fitted threshold. A plain optional alternative for the cutoff sentence is "With a fixed positive detection cutoff in Hz, changing a can also move the detected field boundaries." The present sentence is understandable in context, so this is not a required repair.

- 05c-place-tests.md lines 200-210: retain the physical input/connection roles and effective-background qualification. The next paragraph assigns the symbols and statistical assumptions. These are complementary paragraphs rather than duplicate definitions. The signed-weight limitation prevents the simplified sum being mistaken for measured synapse types; no explanation of biological synapse classes should be added here.

- 05c-place-tests.md lines 214-228: retain the interpretation of shared weights at both positions, the positive-profile condition, and the negative-product allowance for centered profiles. These sentences explain why the sum has its covariance rather than merely repeat the algebra. "Overlap" is tied to input cells active at both positions. "Broad spatial covariance" is made concrete by the following Gaussian profile example; no new term definition is required for the declared mathematical audience.

- 05c-place-tests.md lines 236-247: retain the amplitude-versus-width comparison. It explains how v_W, rho, and profile width affect different parts of the model and what must be fixed in the comparison. "Normalized spatial dependence" is the dependence on distance with its overall amplitude removed, already set against "covariance amplitude" in adjacent sentences. Replacing this with a new normalization equation would add detail without helping the current physical comparison. The existing example verifies the width convention, so no second example is needed.

## Disposition

Two small wording repairs are required, S2-1 and S2-2. Optional paragraph breaks or deletion of one summary sentence do not block this stage. No additional biological claims, broad material, repeated tutorial, full build, or visual check requested. Stage 3 remains separate. Token stats unavailable.

## Source and rule hashes

C:\dev\clsc\burak-papers\guide\content\chapters\04-eye-drift.md SHA256 79AB27AFD4B79AE930308B5AAE2AB7372DF51438FAA28A8453772DA213E4D916
C:\dev\clsc\burak-papers\guide\content\chapters\04b-eye-timing.md SHA256 5EC09C5367F2EB8FD042B8736FE2019B7E11B5D39D6E550797EFB01DC8373693
C:\dev\clsc\burak-papers\guide\content\chapters\05-place-fields.md SHA256 342268F4D10C4D5ACE00D23D10372638AC7BBE982CF574BB08B33764E921FCB9
C:\dev\clsc\burak-papers\guide\content\chapters\05c-place-tests.md SHA256 A30E5C2DD6F101524AFFD5761922B18D95D76361B46698F1EB9120C3755689C4
C:\dev\clsc\burak-papers\guide\verification\physical-meaning-20261029\edits.json SHA256 33AC4A9B600782B7F7E350348072362E2376D41C5857A9D8B51AF28059D7F391
C:\Users\vital\.codex\skills\course-study-guide-builder\SKILL.md SHA256 B78068E9874E6D1D97B2017BF8F940492F9B08FC11B74F20FD75019FF388984A
C:\Users\vital\.codex\skills\course-study-guide-builder\references\pedagogy-language-contract.md SHA256 F4C1EB544CF640B708E1970D9572FDC758FCC6AEA806675D01A0256658DF847A
Completed: 2026-10-29T11:14:07.2100208+02:00. Measured wall elapsed 98.05 seconds. Awake execution time unverified.
