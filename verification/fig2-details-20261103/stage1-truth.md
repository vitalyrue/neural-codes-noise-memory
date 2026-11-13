# Stage 1: Figure 2 factual and mathematical review

Scope: only the additions to `content/chapters/02b-memory-long-delays.md` and `content/chapters/11-simulating-memory.md`, compared with the two baseline copies in this folder. The short simulation chapter was also read for local consistency. No guide text was edited. This is not a whole-book review or release approval.

Review started UTC: 2026-11-03T17:50:21Z
Review ended UTC: 2026-11-03T17:51:11Z
Wall-clock duration: 51 seconds
Awake execution time: unverified; sleep/resume events were not checked.

## Reviewed file hashes (SHA256)

- `content/chapters/02b-memory-long-delays.md`: `C0F51C1EC21A8C50230BF7CDFBC0D5A32E6331BD122E24334908E0E3F9C02CEA`
- `content/chapters/11-simulating-memory.md`: `D907DA29338C9045DC020DB361CF4111E5CA477BBF4012EB3F70882D114F9AFB`

## Sources checked

- Original Figure 2 image: `research/burak-fiete-2012-page-3.png`.
- Original paper text: `research/burak-fiete-2012-main.txt`, Figure 2 caption and Network Simulations, particularly the mutual-inhibition measurement definition.
- Original supporting text: `research/burak-fiete-2012-si.txt`, S31 and S32.

## Supported conclusions

1. Panel B details match the caption: exponential transfer, 1,024 neurons, two snapshots 10 seconds apart, neural index on the horizontal axis, rate curves with peaks approximately 85 Hz, and spike marks from a 10 ms interval. The distinction between a persistent pattern and its changing position correctly explains the displayed trace.
2. Panel C correctly identifies circles as simulations, solid lines as Eq. 2 predictions, the dashed information bound as applying to the sigmoidal case, and the transfer-function inset. The caption explicitly says C and D error bars are standard errors over 100 trials and that C bars are smaller than the symbols.
3. Panel D correctly refers to the periodic variance formula S32, as the Methods explicitly do. The interpretation of saturation is correct: wrapping bounds the reported angular displacement while diffusion continues. For a uniform wrapped displacement on (-pi, pi), its mean square is pi squared divided by 3.
4. Panel E correctly describes a nonperiodic stored rate difference in a mutually inhibiting pair, also interpretable as two populations. Equal opposing connections and the linear rate rule support the stated continuous family in the positive-rate range. This claim does not require the coordinate to be unbounded.
5. Panel F rate units and the population interpretation are correct. The caption uses inverse milliseconds. The Methods explicitly identify each group rate as the sum of its cells' rates. One inverse millisecond is 1,000 inverse seconds.
6. Panel G is correctly described as the squared change in r1 minus r2, averaged over starting times from 0 to recording duration minus lag. The Methods explicitly give this statistic and the 200-second duration. The displayed equation, 2-second example with starts up to 198 seconds, overlapping-interval explanation, and distinction from the ring's 100-trial error bars follow from that definition.
7. G has squared rate units. Converting rates from inverse seconds to inverse milliseconds divides rates by 1,000 and squared displacements by 1,000,000. The theoretical line must therefore use the rate-coordinate diffusion coefficient with matching time units in 2 D_r times lag. The chapter's existing relation D_r = D_s / tau squared provides the needed coordinate conversion. As a numerical consistency check, b = 5,000 and tau = 0.1 seconds give D_s = b/(2 tau) = 25,000 per second and D_r = 2,500,000 per second cubed; a 2-second lag gives squared displacement 10 in inverse milliseconds squared, matching G's plotted endpoint scale.
8. The limits of the simulation evidence are accurately described. These are network simulations, with no claim of a directly measured animal memory error.

## Required findings

None for the new claims, equations, units, or source support at the reviewed hashes. Stage 1 passes within this scope. Wording and connected reading are separate review stages.

Token stats unavailable.
