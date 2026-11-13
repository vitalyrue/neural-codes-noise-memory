# Independent stage 3: reader understanding and flow

Reviewer: `/root/terms_observations`. Local request ID: `terms-observations-stage3-20261030-125549` (local label, not platform call ID). Start: 2026-10-30T12:55:49.5445211+02:00. This reviewer did not write the repaired passages. Reviewed current connected text, not historical findings. Known background includes expected value, variance, standard deviation and probability density. No manuscript edits, pixels or whole-book acceptance.

Verdict: the requested midpoint section and five glossary entries have no unresolved reader-understanding or flow defect in this connected reading. The reader can explain the physical step asymmetry, reproduce its local correction, and distinguish the calculation from determining neural drift. This is local acceptance of this review stage only.

## Connected paragraph reading

Earlier setup: `02b-memory-long-delays.md:11` identifies the current coordinate, local diffusion and limits. `:17` defines Itô evaluation at the start of an increment. `:21-39` uses its zero conditional mean to obtain the density evolution. `:90-100` then derives constant mean and state-dependent variance growth for that zero-drift process. This gives a real question for the next section: does the same noise-strength formula settle the mean motion when the process itself changes?

| Paragraph or block | What it adds and how it connects | Decision |
| --- | --- | --- |
| `02b-memory-long-delays.md:129` | Separates trial-to-trial spread from movement of the average. It follows the variance calculation and makes the limit of that calculation the new question. | Retain. |
| `:134` | Defines systematic drift, supplies two possible sources, and states why the leading variance calculation cannot identify exact neural drift. This prepares a deliberately limited illustrative convention comparison. | Retain. |
| `:139` | Defines midpoint evaluation against the already-taught starting-point rule. It explains why equally signed opposite noise inputs need not give equal-sized opposite displacements when their amplitude depends on position. It states the local result and the source's limited use of it. The reader can say why increasing noise strength gives a positive correction without first opening the algebra. | Retain. |
| `:143` | Defines `b` and the positive, smooth region, writes the midpoint's actual argument, then announces the leading substitution. This connects the preceding physical explanation to quantities the reader can calculate. | Retain. |
| `:146-147`, displayed block | Shows the two Taylor steps rather than merely naming a convention or quoting a drift. The reader can identify the noise term and the extra squared-increment term. | Retain. |
| `:150` | Averages the two retained terms, relates `bb'` to `D'`, and obtains `D'/2`. The constant-strength check explains when the correction disappears. The final two sentences return to the neural limitation established before the fold. Thus both readers who open the fold and readers who skip it can distinguish mathematical conversion from selecting a neural model. | Retain. |
| `:154` | Compares the mean displacement's scale with random displacement. It answers why a possible mean correction does not replace the leading random-spread result. | Retain. |
| `:156` | Turns that comparison back into the memory interpretation: subtracting or tuning a mean does not remove random increments. Domain and boundary restrictions keep this interpretation local to a justified model. | Retain. |
| `:158` | Closes with the other relevant limit of the variance derivation, its conditional independence assumption, and identifies what an added covariance source would require. This is a connected scope limit, rather than a new general topic inserted into the midpoint proof. | Retain. |

Open-ended read: from the supplied text the reader can answer what changes between the two conventions, why a nonzero mean term appears, where its factor one half comes from, why it vanishes for constant noise strength, and why none of that identifies exact drift in the microscopic neural network. No missing explanation had to be supplied from outside expertise for those questions.

## Glossary lookup and consistency

- `glossary.md:28`, estimator: the reader can identify input data, the estimated quantity and the fact that a rule can be inaccurate. This matches the actual estimator teaching at `03-memory-information.md:105`, without conflating an estimator with its output.
- `glossary.md:35`, Fisher information: the plain description, formal score definition and special Poisson form agree with `03-memory-information.md:19-23`, `:37-52`, and `:89-101`. “Score” has its own consistent glossary entry at `glossary.md:96`. The lookup entry summarizes already-taught content rather than replacing the explanation with a blue label.
- `glossary.md:67`, median filter: the reader can describe a local ordered-value replacement and its effect on isolated rates. The same operation and possible small-feature change appear in `05c-place-tests.md:178`; the glossary does not add a second incompatible definition.
- `glossary.md:75`, one sided t test: the reader can identify the mean being tested, the comparison value zero, the positive direction and the uncertainty used to scale the difference. `04-eye-drift.md:114-120` supplies the fuller reference distribution and sampling limits. The glossary's short form has a real teaching passage behind it.
- `glossary.md:99`, Spearman correlation: the reader can say that both data lists are ranked before correlation and explain what an increasing association means. This matches `04c-eye-circuit.md:214` and uses the earlier ordinary-correlation definition. It does not promise detection of every nonlinear relation.

Lookup-link check: the new Fisher entry's `ch-memory-information.html#sec-memory-fi` targets the source chapter `ch:MEMORY-INFORMATION` and source section `sec:MEMORY-FI`, present in both Markdown and sidecar. Existing generated `site/chapters/ch-memory-information.html` also contains `id="sec-memory-fi"`. This is a static target-existence check, not a claim that the generated page contains all current prose. The other four entries add no links requiring target checks. Glossary Itô (`:53`) and Stratonovich (`:105`) use the same starting-point/midpoint meanings as the chapter.

The read stayed within these connected passages. No new full-build, semantic-book-audit or visual acceptance is claimed. Token stats unavailable.

## Timing and hashes

Actual completion, wall duration and source hashes follow. Awake execution time is not separately verified because sleep/resume events were not inspected. Paragraph hashes use current source text at the cited lines, encoded as UTF-8; the equation-block hash joins its two source lines with LF.

Completion: 2026-10-30T12:56:45.5468027+02:00
Wall-clock elapsed: 56 seconds; since previous checkpoint: 45.2 seconds.

Whole-source SHA256:
```
content/chapters/02b-memory-long-delays.md A088BAE67645F1CEAA3389C8ED71700ECD24C9FCD010B8997F6ADEE0CED978A7
content/chapters/glossary.md 86944917BF60F4128BB7B06AAE1AD872BEFEDA2587F02EC3927447731BF476D3
content/chapters/03-memory-information.md 65060C277A2E3DEB1638D31485CFEC8C983262D1B0900D45E4E9F2A7ABC99222
content/chapters/03-memory-information.yaml 980E32B4180729ED0E7E133E238AFAE4FD27AE8EEEC5A673E240D31DFDA9171D
content/chapters/04-eye-drift.md A6393AA211E9B38D16E0620B7B67D240F24E35A8DDDB5C200CD5CF0B9E218C52
content/chapters/04c-eye-circuit.md EB8DF5D89C1242A4703365D524F2688CA66F0E927229750BE08D44172FEE7E8B
content/chapters/05c-place-tests.md AEAE1E40B4A98166B74CA621A11D4AF46D3CF7BB444F60BD9CC29DE8FC578C41
```

Paragraph/block SHA256:
```
02b-memory-long-delays.md:129 944D04022AB15D36358AEE2060C69D8D8552925D096CBD25371250A27DE84638
02b-memory-long-delays.md:134 BCAA85CCCEE89BEB5526D0E8B8BAED24C2BED85F5C174CF8803163C89477263A
02b-memory-long-delays.md:139 F714BF1C9BE19508180499302421B910E5860BA38A49DA5A7BEF7CB1D52F22FC
02b-memory-long-delays.md:143 829784F93B011113CCBCA435B2336253A43145BFADBBB19EE046DB38890A986A
02b-memory-long-delays.md:150 89830F86B42319CEE78F9D2413F126513E9D075B3595761C4C38F2F0E0584000
02b-memory-long-delays.md:154 30A2A98933048070F2DD040043AC45BC07040E2B76323BB43B36A97EE83D5804
02b-memory-long-delays.md:156 87E9EF0B50577535DFB24322F9E27730D8CF6B29042B8B38824AFB679267920A
02b-memory-long-delays.md:158 2019148D88C7147DD1836CE19071C4C2CED9407E0561820471BCEFE5E873276D
02b-memory-long-delays.md:146-147 9FED8CE88C993211A57DA493F84B4F6C21D8850265FF779595B102DDDC8F030A
glossary.md:28 CB7B4002F96A0182321357FE835E72BCCC6E46D5F5FEC73A715D5D1E40A6060E
glossary.md:35 49593618D90984C5AC37DEF8C1E7298DAF58C549FE96BA81A04CD571897FAE4E
glossary.md:67 1E98175088C4CB620DAE04C7A47F1F60C264344D7E8C17337F3F8119D31341BC
glossary.md:75 42532F6CFE4A646E8BADF2AB02640E56637F0098943AB25289CC77B595A7F295
glossary.md:99 A0364D2590D86268BC891B87063FDB543E0E278D913E8ED83FA45D153BF7688C
```
