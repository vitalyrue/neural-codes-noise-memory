# SEM repair recheck

Local request ID: fig2-SEM-recheck-20261103. Reviewer: fig2_edit_review. Separate request after the completed Stage 2 call. No source edits.

UTC start: 2026-11-03T17:53:26Z
UTC end: 2026-11-03T17:53:55Z
Wall-clock duration: 29 seconds
Awake execution time: unverified.

Current reviewed source:
- `content/chapters/02b-memory-long-delays.md`: SHA256 `5A81E4F76DD1B221D30729C307AAA0B20E04E09A32C7BF90C8A120528FA3EBA3`
- `content/chapters/11-simulating-memory.md`: SHA256 `D907DA29338C9045DC020DB361CF4111E5CA477BBF4012EB3F70882D114F9AFB`

Repaired passage, 02b line 189: standard error of the mean (SEM) is now explained as uncertainty in the mean MSD estimated from 100 trials, rather than the spread of individual trial values.

Correctness: pass. The paper caption says standard errors over 100 trials; the replacement accurately states what this means. It does not claim the bars describe the standard deviation of individual trial MSD values.

Necessity and wording: the Stage 2 missing-meaning finding is resolved. The new explanation uses the familiar mean and MSD, identifies the trials providing the estimate, and explains the distinction the reader needs at the figure. No SEM formula is necessary here.

First-definition styling: the new occurrence is correctly marked. At this recheck, `04-eye-drift.md:243` still has the later SEM occurrence marked as a first definition. The contract marks each term once per book. Remove that later term marking while retaining its explanation of uncertainty across cells. This is a narrow styling consistency item, not a new mathematical or reader-flow defect. The coordinator was notified.

Rule source remains the current pedagogy-language-contract.md, SHA256 `F4C1EB544CF640B708E1970D9572FDC758FCC6AEA806675D01A0256658DF847A`.

Token stats unavailable.
