# Stage 1 repair recheck

**Final status: PASS after the two narrow repairs verified at 2026-11-04T18:16:27.534574+02:00.** The initial snapshot finding below is retained as the repair record; it is closed in the final verification section. Total wall time from recheck start: 1m47.546s. Awake time unverified.

Reviewer: `/root/math_table_review`; requested GPT-6.1 Sol high. Backend request ID and exact serving build unavailable. Separate truth/reasoning call; no stage2 wording judgment is claimed.

Start 2026-11-04T18:14:39.988610+02:00; finished 2026-11-04T18:16:16.475747+02:00. Wall elapsed 0:01:36.487137. Awake execution time unverified. Time since prior stage1 report checkpoint 0:02:06.809470. No system-time change observed. All times are host clock readings.

Reviewed both current reader files completely for the affected passage: the new top reference link, corrected beta-units paragraph, result-table introduction, and all 35 parsed table rows. Reused primary-source mathematics checked in `stage1-truth.md`; reread connected parameter/width and eye-scale passages for new claims. No reader-source edits.

Current source SHA256:

- `content\chapters\00-mathematical-tools.md`: `BECA4E530159D77B49C58495FC126530C6671AF8994E4310EF1F95BF9BC0DA02`
- `content\chapters\00-mathematical-tools.yaml`: `66D302B80CC1607268807F6ED03CAA1C23A807BD0CEA093629746B61B83FE844`

## Result

All nine added rows have sound formulas, derivation claims and physical interpretations within their conditions. Previous beta-units and tensor-source errors are fixed. No further required major-result omission was identified. One small scope correction remains in row14's total-error explanation before the truth stage can close: say explicitly that the asymptotic value using J alone is for full spike access.

The current sentence 'The general ideal total-error limit is 2DT+sqrt(2D/J)' sits in the partial-readout row. With alpha<1 its limit is instead 2DT+sqrt(2D/(alpha J)). The row already gives that alpha formula correctly. Change the sentence to 'With full spike access, the ideal total-error limit is ...'; the stated equality to 2D(T+tau) then correctly requires attaining the information-diffusion bound. The displayed lower bound using full J remains a valid weaker bound with partial access, so no displayed inequality needs reversal.

## Changed-row judgments

- **Row5, multidimensional result:** pass. SI S22-S24 label now matches the tensor. J_ab, invertibility and positive-semidefinite inequality correctly carry the matrix extension to all coordinate combinations. It does not claim an ordinary inverse for singular J.
- **Row6, wrapped error:** pass. Constant angular diffusion eventually gives uniform wrapped error, pi^2/3 in radian-squared units for one full circle. This describes bounded reported error, not cessation of noise. The earlier line formula remains restricted to an unbounded coordinate.
- **Row9, attaining bound, added:** pass. v_i=r_i'/(tau J r_i) is the pointwise Cauchy Schwarz equality condition. Symmetric exponential transfer is a sufficient class under the earlier tuned continuous-family assumptions. The row explicitly avoids the source's unsupported general necessity claim.
- **Row10, controlled parameters, added:** pass. Population replication with weights1/N gives J proportional N and D proportional1/N. Rate scaling needs a bound-attaining network or preserved tuning/input geometry, expressly stated. Tau^-2 holds when rate tuning and its input relation are held fixed by circuit adjustment. These are controlled comparisons, not unrestricted changes to one biological parameter.
- **Row11, tuning width, added:** pass. At fixed density, peak rate and radial shape, change of variables gives J_aa proportional rho a w^(d-2). Isotropic information and equality then give D_aa proportional w^(2-d). Different total firing constraints change the result, as the row says.
- **Row14, recall/partial:** formulas pass. Corrected full-access lower bound is a sound consequence of the coth solution; the printed main Eq6 is correctly restricted to equality. The decoding sentence requires the full-access scope correction described above.
- **Row15, two times, added:** pass. Symmetric two-stage model, Poisson drive placement and stable transverse directions are explicit. Combined left-mode normalization gives tau+tau_m, agreeing with SI S84-S92. No claim that arbitrary response times can be summed.
- **Row16, Gaussian noise, added:** pass. Constant independent intensity q_n gives J=sum(r_i')^2/q_n and 2D=q_n sum v_i^2. The same Cauchy Schwarz relation follows. Equality v proportional r' and a sufficient symmetric linear class are correct. The matched likelihood/noise normalization is explicit.
- **Row23, eye noise-scale estimate, added:** pass as an estimate. J approximately N a^2/lambda_0 is the simpler Poisson information, not the full renewal-network FI. Renewal long-window variance supplies CV squared. Absolute versus fractional slope substitution correctly explains opposite rate comparisons. Source Eq1 normalization ambiguity and saturating/sub-Poisson full-model limits are explicit; the row does not pretend to reproduce a proven exact full-network law.
- **Row28, rare locations/counts/gaps, added:** pass limiting approximation. Sufficient decay of spatial dependence is stated, rare excursion width is separated from spacing, and bulk Poisson counts omit endpoints. Conditioning a Poisson mean gives lambda/(1-exp(-lambda)). No exact finite-threshold Poisson or gap claim is made.
- **Row30, peak rate/size, added:** pass. Fmax=a epsilon and epsilon approximately q r_*^2/(2ell_c^2) yield the displayed power2/d. Dimension of size is respected. The finite-threshold measured/model exponents are not relabeled as the limiting exponent.
- **Row32, slices, added:** pass. Joint Gaussian laws remain Gaussian under restriction, covariance restricts accordingly, and isotropy gives the same local scale. Laws use slice dimension and slice-component sampling, with central cuts distinguished from spatially sampled intersections.

## Context, notation and previous findings

- Corrected prelude now states beta has inverse-distance-squared units in every dimension and only its geometric factor changes. This is correct.
- New top link is a truthful reference pointer. Updated introduction correctly explains extension and guide-derivation labels. Exact/approximate labels remain model statements.
- Size law isotropy is explicitly taught in the connected prelude and detailed rare-peak derivation. The unchanged size row uses that established setting. Repeating 'isotropic' in its compact derivation would be optional reinforcement, not a newly missing premise on this reading path.
- Gaussian-noise and two-stage qualifications are in their rows, not left solely to remote source passages. Rare-gap dependence conditions and count-selection effects are also visible.
- YAML parsed successfully. The raw single-quoted YAML doubles apostrophes as escaping, but parsed formula strings contain first derivatives r_i' and g_i', second covariance derivative C'' and time argument t' as intended. There are no remaining raw `\prime` tokens. This checks source notation, not rendered math appearance.
- Equality attainment, matrix constraint, corrected recall result, count/gap distributions, amplitude-size law and slice predictions address the prior required omissions. Added parameter comparisons and two noise/time extensions reasonably cover the supporting main results without adding every simulation setting.

## Limits

Source and rule hashes from the first report still identify the underlying primary texts and teaching rules; they were not edited. No source paper was downloaded again. No visual or full-publication check was run or claimed. No full excursion/kinematic theorem proof, raw-data reanalysis or simulation-code audit was performed. New mathematical formulas were checked through the already-read primary passages and direct algebra. Wording and reader-understanding review remain separate. Token stats unavailable.

## Final narrow repair verification

At 2026-11-04T18:16:27.534574+02:00, reread parsed rows14 and29 after the coordinator made the two announced edits. Row14 now explicitly says 'With full spike access, the ideal total-error limit is ...'. This resolves the remaining scope correction. Row29 now explicitly begins its derivation with a smooth stationary isotropic Gaussian map at large positive q. This makes the existing isotropy condition visible directly in the row and is mathematically correct. No further source issue remains from this stage1 review. **Stage1 truth/reasoning review passes for the sources below.** Wording and reader-understanding stages remain pending.

Final reader SHA256:

- `content\chapters\00-mathematical-tools.md`: `BECA4E530159D77B49C58495FC126530C6671AF8994E4310EF1F95BF9BC0DA02`
- `content\chapters\00-mathematical-tools.yaml`: `66D302B80CC1607268807F6ED03CAA1C23A807BD0CEA093629746B61B83FE844`
