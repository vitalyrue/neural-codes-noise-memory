# Focused truth recheck of three wording repairs

**PASS.** Separate truth/reasoning call, not a new wording or flow review.

Reviewer `/root/math_table_review`; requested GPT-6.1 Sol high. Backend request ID and exact serving build unavailable. Host start 2026-11-04T18:19:54.071447+02:00, finish 2026-11-04T18:20:11.899414+02:00. Wall elapsed 0:00:17.827967. Awake execution time unverified. Since previous stage2 report checkpoint: 0:00:58.477400. No observed clock change.

Read current YAML through its parser, checking every cell of rows1,26,27 and their adjacent model/interpretation context. The three repaired derivation claims now match their formulas and source derivations:

- **Row1:** Each individual spike increases activation by one; N_i records those events. Thus dN_i=1 at a spike matches the unit jump in ds_i. Decay applies between events, and W_ij still sends j's activation to receiver i. The change fixes the actor and amount without changing the model.
- **Row26:** 'Mean positive part of the spatial slope' now means E[(z')_+ | z=q], the quantity required by the upcrossing integral. Gaussian height-slope independence then permits the displayed crossing density. This avoids using the larger conditional mean E[z'|z'>0]. Endpoint contribution and counting convention remain intact.
- **Row27:** The active-fraction ratio is explicitly mu_s/(mu_s+mu_g), consistent with Q(q)/nu_+ and (1-Q(q))/nu_+. Q inversion and the spatial scale formula remain correct. Complete-field/gap and selection qualifications remain intact.

No new truth issue or lost qualification found. Previous stage1 conclusions remain valid for this narrow repair scope. Wording/flow closure requires its separately requested calls. No reader files were edited; no full build, visual review or source rereading beyond the connected checked derivations was required. Token stats unavailable.

## Current reader hashes

- `content\chapters\00-mathematical-tools.md`: SHA256 `BECA4E530159D77B49C58495FC126530C6671AF8994E4310EF1F95BF9BC0DA02`
- `content\chapters\00-mathematical-tools.yaml`: SHA256 `ADE8100D6E7F9271C0BBD3DDBD9A708BDF252B60AACE126D9FF708BF00F48BF6`

The rule and primary-source hashes in stage1-truth.md and stage2-wording.md continue to identify the unchanged review basis.
