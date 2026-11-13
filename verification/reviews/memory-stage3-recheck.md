# Focused stage 3 recheck: storage and readout variance

Reviewer: independent agent /root/review_memory_guide. Local request ID memory-stage3-recheck-20261022T201006+0300. Separate call after the original stage 3 findings. Start 2026-10-22T20:10:06.8588944+03:00; checkpoint20:10:42.4812993+03:00. End, measured wall duration and exact hashes are in JSON. Awake execution is unverified. Token stats unavailable. No prose edits or builds.

## U1 closed

Read actual current `03-memory-information.md`, sec:MEMORY-READOUT-SETUP, lines205–235, with the preceding tuning comparison at201 and subsequent naive-readout paragraphs239–247.

- At207, x=theta(T), s=x-Theta and e=hat{x}-x are defined before being added. The observer estimates the cue-time state using later spikes; its error relative to the original value is therefore s+e. The displayed sum-variance identity retains the cross covariance instead of dropping it.
- At215, unbiasedness is assumed at every possible cue-time x, and future noise is independent of storage history in the local model. These stronger assumptions justify conditional mean E[e|history]=0. The text uses the fact that s is fixed by history to derive E[se]=E[s E(e|history)]=0. This correctly uses conditional expectation; it does not infer independence from marginal unbiasedness alone.
- Both errors have zero mean under the stated zero-drift storage and conditional readout assumptions. Translation-invariant readout then permits one Vread(L) independent of x. Together with Var(s)=2DT, the addition follows at218.
- The following paragraph221 retains the limits for state dependence, boundaries, priors and uncertain encoding. Paragraphs223–235 give the Gaussian increment/observation approximation supporting this local independent-future-noise model. The repeated x definition at223 is a harmless reminder at the start of a new representation, not a contradictory object.

The reader can now reconstruct the addition from the covariance identity taught in foundations and the unbiasedness definition taught earlier in information. The repair supplies the missing step without creating another prerequisite. U1 and the conditional source-coverage hold for P1SI-p12 are closed. The downstream partial-readout and printed-bound uses can retain their original decisions because this repair establishes their required decomposition without changing their formulas.

## Reuse of prior decisions

Compared the before-repair03 snapshot with current03 after replacing only sec:MEMORY-READOUT-SETUP by a marker: whitespace-normalized text outside that section is identical. The original288 paragraph judgments remain usable for unchanged passages; the current changed/connected records in `memory-stage3-recheck-paragraphs.json` supersede original p207/p213 decisions at their new locations. They are local UTF-8 source extractions while root refreshes the shared packet, with exact text hashes, rather than pretending the earlier packet already contains the new paragraph215.

Read the supplied whitespace-only footnote-format evidence. It records normalized text identity for02/03/05 and identifies the inserted blank blocks needed by the renderer. No definition wording, mathematical fact or paragraph reasoning changes through that formatting repair. This focused review reuses the earlier semantic judgments; root owns verification that the output footnotes now resolve individually. The05 body remains the other reviewer's scope.

Metadata purpose copies strip raw footnote call markers while canonical body citations remain. That is a navigation-display repair, not new teaching content; the authored Part-purpose meaning and earlier handoff judgments remain usable. Root's browser output check remains separate.

The original stage3 report and original snapshot are preserved as an actual findings-required call. This recheck closes the finding on the current source. No open findings remain in this focused scope; no new full-book read or output acceptance is claimed.
