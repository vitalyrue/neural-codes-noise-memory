# Independent check of Opus stage 1 finding F01

Started: 2026-11-03 13:20:45 UTC, measured with the clock tool.
Checkpoint: 2026-11-03 13:23:41 UTC, measured with the clock tool.
Finished substantive check: 2026-11-03 13:25:47 UTC, measured with the clock tool.
Wall-clock elapsed: 5 min 2 sec. Time since the measured checkpoint: 2 min 6 sec. Awake execution time was not independently measured from sleep/resume events. An earlier message's estimated 13:24 timestamp was inaccurate; no evidence of a system clock change was found. This record uses measured timestamps only.
Reviewer: independent Codex subagent, identified by system instructions as based on GPT-6. The exact model build and reasoning setting are not exposed to this subagent. This is not an Opus5.5 result.
Scope: F01 and its connected ideal-readout formulas only. No guide text was changed.

## Decision

Retain F01 as a supported, reviewer-derived modelling question or optional qualification. Do not call it a confirmed guide error or replace the paper's readout equations automatically. The guide already says explicitly that process increments and observation errors are independent in its approximation, and that its derivations are exact within that model.

The physical concern is real: reading the same spikes that drive the network generally introduces a process/observation cross covariance. The paper's SI S62 factorizes those noises and omits this connection. A local Gaussian two-cell calculation reproduces the proposed factor of two in limiting variance. However, F01 overstates how directly its result covers the full Poisson network and compares two different definitions of a time constant.

## What was checked against the sources

- Frozen chapter: inputs/guide/03b-memory-readout.md, setup and ideal readout sections.
- Original main PDF: inputs/papers/burak-fiete-2012-persistent-activity.pdf, pp. 5 and 6, visually checked; Eqs. 7 to 11 and the two-cell simulation model.
- Original SI PDF: inputs/papers/burak-fiete-2012-persistent-activity-si.pdf, p. 13, visually checked; Eqs. S58 to S63. Page-separated text also checked on pp. 12 to 15, including S57 and S64 to S75.

Main Eq. 7 is the exponential filter of each neuron's own spike train. Main Eqs. 8 and 9 turn those filtered spikes into rates. SI p. 12 specifies access to all spikes after the cue. SI p. 13 introduces the Gaussian approximation and constant D. Its S58 to S61 specify separate covariance laws; independence between the two kinds of noise is implemented by the factorized exponent in S62. The paper does not discuss the same-spike cross covariance there. The guide makes the assumed independence more explicit than the paper does.

## 1. Same-spike noise is correlated

Write dM_i=dN_i-r_i dt for the spike innovation, with local covariance E[dM_i dM_j]=delta_ij r_i dt. In the weak fluctuation projection,

    dtheta = sum_i v_i dM_i,
    sum_i v_i r_i' = 1/tau,
    2D = sum_i v_i^2 r_i.

The local efficient score observation can be written

    dY = theta dt + dn,
    dn = (1/J) sum_i (r_i'/r_i) dM_i,
    E[dn^2] = dt/J.

Consequently,

    E[dtheta dn] = dt/(tau J),
    correlation = 1/(tau sqrt(2DJ)).

This is positive and is one at equality in the information/diffusion inequality. For a bin of width h, the same calculation gives Cov(eta,epsilon)=1/(tau J), and at equality eta=(h/tau)epsilon. Independence does not become correct merely by sending h to zero.

These are statements about a local score observation using the same spike innovations. A separate observation population, or an observation process specified to have independent noise, gives a different model. Full versus partial access also changes which innovations are observed, and requires its own calculation.

## 2. Exact filtering identity, and the additional assumptions needed for J tau/2

Set the cue time to zero. Given every later spike time,

    s(t) = exp(-t/tau) s(0)
           + integral_0^t exp(-(t-u)/tau) dN(u).

This identity is exact for Eq. 7. However, the remaining unknown is the whole initial synaptic vector s(0), not just theta(0).

Suppose an oracle supplies all initial state components except one cue coordinate x, so that s(0)=f(x) is known. Also assume W, b, phi and tau are known. Conditional on an observed spike history, differentiating the conditional intensity gives

    partial_x r_i(t) = exp(-t/tau) phi'(g_i(t)) [W f'(x)]_i.

For a regular counting process likelihood, the Fisher information is

    I_x(L) = integral_0^L exp(-2t/tau)
             E[sum_i {phi'(g_i(t)) [W f'(x)]_i}^2 / r_i(t)] dt.

This is the appropriate conditional-history formula. One must still take the expectation over the actual stochastic trajectory. It does not equal J times an exponential integral exactly for arbitrary nonlinear, state-dependent Poisson rates.

Now take f(x)=s_bar(x), freeze rates and gains at that attractor state, and work locally. The fixed point identity implies phi'_i [W f']_i=r_i'. Then

    I_x(L) approximately (J tau/2) [1-exp(-2L/tau)].

The equality is exact in the corresponding linear Gaussian experiment with constant noise covariance and known initial transverse state. In that experiment a linear unbiased estimator attains

    V_same(L) = 2 / {J tau [1-exp(-2L/tau)]},
    V_same(infinity) = 2/(J tau).

For the actual Poisson experiment, 1/I_x is a Cramer Rao lower bound for a regular locally unbiased estimator. Finite count likelihoods need not be Gaussian, an unbiased efficient estimator need not exist, and increasing L alone does not provide unlimited information because I_x saturates. A many spike or repeated-trial local normal approximation is needed to turn this bound into an attained variance claim.

At a recall cue after a storage delay, s(0) generally contains random deviations away from the attractor manifold. Their distribution, their relation to x, and whether they are known to the observer matter. Unknown initial gains, biases, time constants or additional hidden dynamical states also matter. A nuisance-parameter or prior calculation is required. The one-parameter oracle calculation is not automatically the paper's full recall experiment. It also does not by itself establish a replacement for the total storage-plus-readout error law.

## 3. Concrete two-cell check

Use the source's linear mutual inhibition model:

    r1=(b-s2)/tau, r2=(b-s1)/tau,
    theta=s1-s2, z=s1+s2.

The attractor has z=b, and r1-r2=theta/tau even away from that attractor. Subtracting the two exact synaptic equations gives

    dtheta = -(theta/tau)dt + dN1-dN2
           = dM1-dM2,
    dN1-dN2 = (theta/tau)dt + dtheta.

Thus the difference spike train and the state increment contain the same innovation. These identities are exact while the linear rates remain valid and positive.

At the symmetric cue state theta=0,z=b, freeze local noise at r1=r2=b/(2tau). Then

    2D=b/tau, J=1/(b tau), 2DJ=1/tau^2.

The difference observation dY=tau(dN1-dN2) obeys

    dY=theta dt+tau dtheta.

Given dY, the unknown initial theta contributes exp(-t/tau)theta(0). The constant Gaussian noise variance is tau^2(2D)dt=dt/J. Therefore the calculation above gives

    V_same(L)=2b/[1-exp(-2L/tau)]
             =b[coth(L/tau)+1],
    V_paper(L)=b coth(L/tau).

The discrepancy is the constant b, and the limits are 2b and b. With the source parameters b=5000 and tau=0.1 s, at L=0.1 s these are 11565.1764 and 6565.1764 in activation-coordinate variance units; their limits are 10000 and 5000.

A separate deterministic discrete Gaussian check used h=L/n and the exact Euler observation transformation. Its information is

    I_n = h/(2D tau^2) sum_{k=0}^{n-1}(1-h/tau)^(2k).

At L=tau, n=10,100,1000,10000 gave variances 10814.8310,11489.3377,11557.5846,11564.4172, converging to 11565.1764. This checks the same-spike calculation independently of the paper's backward recursion. No broad tests or network simulation were run.

For the Poisson two-cell model, the derivative of each rate with respect to the initial theta at fixed observed history is exactly plus/minus exp(-t/tau)/(2tau), but the exact information still contains E[1/r1(t)+1/r2(t)]. Replacing it by its value at the cue is a weak fluctuation step. The linear model also needs positive rates; it is not an unrestricted global Poisson process for arbitrarily large excursions.

As an illustration of the hidden-state issue, at a general attractor cue theta=x, allow unknown z(0)=b+u. The frozen local information matrix for (x,u) has diagonal J=b/[tau(b^2-x^2)] and off-diagonal x/[tau(b^2-x^2)], all multiplied by c=(tau/2)[1-exp(-2L/tau)]. Treating u as an unknown parameter gives the x variance bound 2b/[1-exp(-2L/tau)], whereas knowing u gives 2(b^2-x^2)/{b[1-exp(-2L/tau)]}. At x=0 they coincide locally; away from zero they differ. This is a concrete reason to specify the initial-state information supplied to the observer.

## 4. Timing claim in F01 needs correction

The conditional intensity sensitivity decays as exp(-t/tau); its local information rate decays as exp(-2t/tau). Cumulative information increases toward its limit. It is imprecise to say that cumulative cue information itself decays as exp(-t/tau).

F01 contrasts an approach time tau/2 with the paper's L*=1/sqrt(2DJ). These are different conventions. At equality, L*=tau, but the paper's excess variance already has the tail

    coth(L/tau)-1 approximately 2 exp(-2L/tau).

The same-spike variance above its own limit also decays as exp(-2L/tau). Both therefore have late residual-variance decay time tau/2 at equality. The limiting variances differ; this does not establish a factor of two difference in that decay time.

## Recommended handling

Keep the existing coth result with its stated independent-noise assumption. If the guide is expanded, add a short optional note that state motion and count noise can share spike fluctuations, and that readout from the network's actual spike stream needs a joint observation model. Keep the derived 2/(J tau) limit in a clearly marked research check with its initial-state, local Gaussian and attainability conditions until the full recall experiment is worked through. No author confirmation or direct source statement of this alternative calculation was found in the supplied material.

Token stats unavailable.
