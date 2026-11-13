# Bounded check of stage 3 finding SF1

Started: 2026-11-03 13:32:59 UTC, measured with clock tool.
Checkpoint: 2026-11-03 13:33:53 UTC, measured with clock tool.
Finished substantive check: 2026-11-03 13:35:05 UTC, measured with clock tool. Wall-clock elapsed: 2 min 6 sec. Time since checkpoint: 1 min 12 sec. Awake execution time was not independently verified from system sleep/resume events. No evidence of a system time change was observed.
Reviewer: independent Codex subagent based on GPT-6; exact model build and reasoning setting not exposed. This is a check of the Opus5.5 finding, not an Opus5.5 response.
Scope: original Ben-Shushan main text p.6, Figure 4d on p.7, Figure 5d on p.8, and SI p.3 around S4 to S6. No manuscript edits, simulations or broad figure audit. The earlier readout check is preserved.

## Finding

SF1 does not establish an internal contradiction in the source. Its comparison mixes the integrator's internal output E_OI with the actual eye position E after the model's downstream dynamics. The source's phrase about an MSD on the order of 0.1 deg^2 is loose, but Figure 4d supports that rough scale more closely than Figure 3a does. It should not be quoted as a precise prediction for measured eye MSD.

## Direct evidence

1. **Main PDF p.6, opening paragraph.** The paragraph concerns the adapted spiking oculomotor integrator alone. It names examples in Figure 4c and the near-unit logarithmic slope in Figure 4d, then gives the 350 ms, order-0.1-deg^2 statement. The next paragraph introduces the more complete model with OMNs, muscles, ocular plant and delayed visual feedback. Thus the first number is not explicitly the full model's actual eye MSD.

2. **Main PDF p.7, Figure 4c and d, visually checked.** Panel c labels its signal E_OI. Panel d has log(Delta t [s]) from approximately -2 to 1 and log(MSD [deg^2]) from approximately -3 to 0. The near-unit-slope segment is around log(MSD)=-0.8 to -0.9 at log(time)=0. At 350 ms, log10(time)=-0.456, giving a visual MSD around 0.04 to 0.06 deg^2. This is a visual estimate, not a digitized value. It is within a factor of about two of 0.1 deg^2. The caption explicitly describes these as trajectories from the oculomotor integrator simulation. There is a visible short-lag floor before the simple diffusion regime.

3. **Main PDF p.8, Figure 5c and d, visually checked.** Panel c separately labels the noisy internal output E_OI and the smoother actual eye position E. Panel d compares the full model's eye MSD with both monkeys. Its axes are log(time [s]), roughly -2 to 0, and log(MSD [deg^2]), roughly -5 to -1. At 350 ms the full-model black curve is around 0.01 deg^2, and the two measured curves are of a similar scale, with the monkeys differing. This is a visual estimate only. The full model's eye curve and Figure 4d's internal-output curve therefore should not be equated at a single lag.

4. **Main PDF p.6, following paragraphs.** The source explicitly says the eye is smoother due to muscle and eyeball mechanics and follows E_OI on a coarser scale. It also says several uncertain network parameters permit adjustment of D and that the fit is not unique. These statements support a mechanism-based comparison, not one universal numerical D fixed by all panels.

5. **SI PDF p.3, text immediately before S6.** The source assumes 2D approximately 100 arcmin^2/s for an illustrative calculation of how much diffusion contributes to an OMN's measured interspike-interval CV. It is not introduced there as the fitted diffusion coefficient for Figure 4d or Figure 5d. S4 also concerns time variance within a trajectory segment, 2D*T/6, which differs from the endpoint MSD, 2D*T. Using these quantities interchangeably would add another error.

The main figure pages p.7 and p.8 were rendered from the frozen original PDF and visually inspected. The bounded text checks used the supplied page-separated original-paper extracts for main p.6 and SI p.3. Main Methods p.11 was read only to confirm that E_OI is an internal synaptic readout and that the OMN stage is separate. No additional figure pages were audited.

## What the SI number safely supports

Unit conversion gives

    2D approximately 100/3600 = 0.02778 deg^2/s,
    D approximately 0.01389 deg^2/s.

For a constructed unfiltered Brownian example at 350 ms,

    MSD = 2D*t approximately 0.00972 deg^2,
    RMS displacement approximately 0.0986 degrees.

This calculation is correct for that stated illustrative assumption. It does not independently reproduce the full model's filtered eye MSD or the standalone integrator simulation in Figure 4d. An apparent numerical agreement with Figure 5d is not enough to show that it is the exact fitted D used there.

## Recommended safe handling

There is no existing guide error here because the guide does not quote the 0.1-deg^2 sentence. Keep SF1 as a warning against a future misleading comparison, not as a confirmed source error. A future running example may use D approximately 0.014 deg^2/s if it is labeled an illustrative Brownian value converted from the SI assumption. Explicitly distinguish internal E_OI from measured/modelled eye E, and distinguish 2D*t endpoint MSD from the 2D*T/6 time-variance calculation. Do not present the source's rough order-0.1 statement as a measured 350 ms eye MSD or label it a typo without additional evidence.

Token stats unavailable.
