# Independent memory figure Stage1 review

Completed: 2026-10-23T22:10:58.783206+03:00. Reviewer: /root/draw_place_figures. Author: /root/draw_memory_figures.

Verdict: PASS for V02, V03A and V03B. No open findings. This allows insertion of these frozen figures with the reviewed packet; Stage2 wording and Stage3 reading-flow reviews remain separate.

Wall since root start: 866.9 seconds. Review stage: 225.7 seconds. Since previous checkpoint: 136.0 seconds. Awake execution unverified. Token stats unavailable.

The companion JSON records exact file hashes, every visible label and connection, caption/alt/intro/interpretation checks, numeric derivations, scene evidence and objections. No art or chapter was changed.

## Findings resolved

- V02 interpretation could imply that the flow ran on the fixed-point line. Root changed it to: "As y decays, x changes by one; the left vector extracts that lasting shift." I reread and accepted that exact sentence.
- The three brief IDs now match the integration packet.

## Figure judgments

### V02: pass

A horizontal line of fixed points, separate jump and flow arrows, equal-time points on a straight tilted line, a perpendicular foot and a tangent arrow. The decay changes x before y vanishes, reaching a different memory point from the perpendicular foot. The lasting memory shift and the purpose of the left vector become visible without relying only on vector formulas.

Full size and 700 pixel preview: readable. Palette tokens and visible color roles: pass. Internal-figure coverage rule: not applicable.

Strongest objection: A tilted drawing might suggest curved recovery or perpendicular projection, and its left vector might be mistaken for a path.

Resolution: The recovery line is straight, the perpendicular foot is explicitly distinguished from the endpoint, and the left-vector sentence defines it as a measurement. The interpretation sentence was also repaired and reread.

### V03A: pass

A time arrow, constructed wandering path, cue-state point, separate estimate diamond, storage/readout brackets and an observation interval. Storage displacement happens before T; later spikes estimate the state at T, not the state at T+L. The reader can identify which difference each error term measures, and see why two separately defined errors are added.

Full size and 700 pixel preview: readable. Palette tokens and visible color roles: pass. Internal-figure coverage rule: not applicable.

Strongest objection: An estimate drawn at T+L could be mistaken for the terminal state, and variance addition could be claimed without zero cross covariance.

Resolution: The orange estimate is visibly separate from the teal endpoint and explicitly estimates the cue state. The image lists unbiasedness and future-noise independence; the adjacent chapter gives the conditional-mean argument and translation assumption.

### V03B: pass

Two calculated curves, a marked minimum, asymptote and normalized axes. The equal-weight curve turns upward while the ideal curve approaches a limit. The cost of late equal weighting is visible, including the exact optimum and the distinct long-observation behavior.

Full size and 700 pixel preview: readable. Palette tokens and visible color roles: pass. Internal-figure coverage rule: not applicable.

Strongest objection: The displayed plateau might be interpreted as total recall error, or the plotted positive start as a finite zero-duration value.

Resolution: The axis says readout variance and the caption explicitly excludes 2DT. The zero-duration divergence is directly labeled, and the graph never evaluates zero.

## Mathematical and source checks

- V02 obeys x=1-exp(-lambda t), y=2 exp(-lambda t), hence x+y/2=1. With a/lambda=1/2 the lasting shift is one; v^T K=0, K u=0 and v^T u=1.
- V03A retains conditional unbiasedness, independent future noise and translation invariance. These justify Cov(s,e)=0; storage variance is 2DT only for the shown constant-D, no-drift, unbounded setting. The estimate diamond differs from the terminal state.
- V03B uses coth(z) and z/3+1/z. Its minimum, asymptotes, dimensionless axes and absence of 2DT are correct. The actual plotted domain begins at positive z.
- Targeted SI extracted passages S10-S16, S57, S75 and S79-S81 were read. No broad source audit was performed.

## Scope limits

No artwork or chapter changed, no full paper/book audit, and no later-stage prose review claimed. Exact frozen image, source, brief and packet hashes are recorded; later edits require checking affected review bindings.
