from pathlib import Path
import yaml, json, datetime
root=Path(__file__).resolve().parents[2]
path=root/'content/chapters/01-foundations.md'
old=path.read_text(encoding='utf-8')
start=old.index('## Mean squared displacement')
end=old.index('[^f-eye]:',start)
new=r'''## Shared neural signals and a biased command leave different signs in eye motion {#sec:FOUNDATIONS-COVARIANCE}

During fixation, a monkey tries to keep looking at a stationary target, yet its eye moves slightly. A changing command from the brain can make many motor neurons change their firing together; their spikes act on the eye muscles, which turn the eye. An individual motor neuron also adds spike variability of its own. The 2022 paper asks how much of the observed movement follows a shared neural command, and whether that command itself wanders over time.[^f-eye]

[Two distinct questions require two measurements: covariance asks which recorded changes occur together; displacement statistics ask how far the eye moves and how that movement grows with elapsed time.]{.key-statement} Neither measurement by itself identifies a particular neural circuit.

**Physical meaning: a shared command can survive averaging across neurons.** If a common input raises the firing of many motor neurons that pull the eye in the same direction, their effects add. Independent extra and missing spikes partly cancel when those neurons act together. The paper compares the measured eye displacement with a displacement predicted from one neuron's spikes, after converting both to degrees. That prediction is an analysis of a recording, not an extra command sent to the muscles. A relationship between the two is evidence to test against a model of shared input and private noise; it does not mean that the one recorded cell causes all the movement.

[**Covariance** measures whether two signals tend to be above their own averages together or on opposite sides of those averages.]{.definition-explanation} Positive covariance between the two displacements means that above-average changes in the neural prediction tend to accompany above-average changes in eye position. [The **correlation coefficient**, written $\rho$, expresses this shared variation relative to the spread of each signal.]{.definition-explanation} Extra private noise can lower $\rho$ even when the shared drive has not weakened. The [eye-drift calculation](ch-eye-drift.html#sec-eye-chi) explains why a modest correlation need not mean a small shared contribution to movement.

::: {.publisher-clarification-note .publisher-fold-always title="Mathematical definitions: covariance, variance and correlation"}

Let $X$ and $Y$ be the two displacements, in degrees, across repeated intervals of the same duration. Subtracting each average leaves its fluctuation. Their covariance is

$$
\operatorname{Cov}(X,Y)=\mathbb E[(X-\mathbb E[X])(Y-\mathbb E[Y])].
$$

Here it has units degrees squared; in general its units are the product of the two signals' units. Variance is $\operatorname{Cov}(X,X)$. Expanding the square of a centered sum or difference gives

$$
\operatorname{Var}(X\pm Y)=\operatorname{Var}(X)+\operatorname{Var}(Y)\pm2\operatorname{Cov}(X,Y).
$$

For nonzero variances, correlation is

$$
\rho_{XY}=\frac{\operatorname{Cov}(X,Y)}{\sqrt{\operatorname{Var}(X)\operatorname{Var}(Y)}}.
$$

It is dimensionless and lies between $-1$ and $1$. Independence gives zero covariance when these moments exist; zero covariance alone does not imply independence.

To see the physical roles, write $X=g_X S+\epsilon_X$ and $Y=g_Y S+\epsilon_Y$. Here $S$ is a shared displacement signal in degrees, the dimensionless gains $g_X,g_Y$ convert its effect into each recording, and $\epsilon_X,\epsilon_Y$ are private contributions in degrees. If all three random contributions are independent,

$$
\operatorname{Cov}(X,Y)=g_Xg_Y\operatorname{Var}(S),\qquad
\operatorname{Var}(X)=g_X^2\operatorname{Var}(S)+\operatorname{Var}(\epsilon_X).
$$

Increasing private variance increases the denominator of $\rho$ without increasing the covariance. Changing a gain changes the measured covariance even if the shared source is unchanged. This simple construction explains the need for calibration and explicit noise assumptions; it is not the paper's full inference model.

:::

**Physical meaning: random wandering differs from a persistent directional error.** Let $x(t)$ be horizontal eye angle in degrees and let $\ell$ be an elapsed time in seconds. [The **displacement** $\Delta x=x(t+\ell)-x(t)$ is the change in that angle.]{.definition-explanation} A random change in the maintained command can move the eye left in one interval and right in another. The average displacement can then be close to zero while individual displacements are large. A persistent imbalance in the command can instead make the average displacement grow in one direction. Muscles smooth the command before it becomes eye movement, so the timescale of the observation also matters.

[The **mean squared displacement**, or MSD, averages $(\Delta x)^2$ across repeated intervals and has units degrees squared.]{.definition-explanation} Its two contributions are

$$
\mathbb E[(\Delta x)^2]=\operatorname{Var}(\Delta x)+\mathbb E[\Delta x]^2.
$$

[A larger MSD can mean stronger random movement, a larger directional bias, or both. Measuring the mean displacement separately prevents mistaking bias for increased noise.]{.key-statement}

::: {.publisher-clarification-note .publisher-fold-always title="Derivation: separating spread from mean displacement"}

Write $\mu=\mathbb E[\Delta x]$ and $\eta=\Delta x-\mu$, so $\mathbb E[\eta]=0$. Squaring and averaging gives

$$
\mathbb E[(\mu+\eta)^2]=\mu^2+2\mu\mathbb E[\eta]+\mathbb E[\eta^2]
=\mu^2+\operatorname{Var}(\Delta x).
$$

The cross term vanishes because the fluctuations are measured relative to their own mean. This identity needs finite second moments, but no diffusion assumption.

:::

**What changes the physical movement?** The model must say which part of the pathway a parameter controls:

- **Random changes in the stored command:** more frequent or larger lasting changes make the stored angle spread faster. The next chapter calls this rate of spreading the diffusion coefficient $D$ and explains why it depends on spike variability and the circuit's response to each spike.
- **A persistent directional imbalance:** this changes the mean displacement. In a constant-velocity approximation, doubling that velocity doubles the mean displacement at a fixed lag and quadruples its squared contribution to MSD.
- **The gain from command to eye angle:** if every displacement is multiplied by a gain $G$, with the input fluctuations and other noise held fixed, its variance and MSD are multiplied by $G^2$. A fitted tuning slope, which describes rate as a function of angle, is not by itself a causal muscle gain.
- **Muscle response time:** a slower response smooths rapid command changes more strongly. It changes the short-lag shape of the MSD curve, not just its height. The [timing chapter](ch-eye-timing.html#sec-eye-msd) separates this smoothing from growth of noise inside the memory circuit.

Measurement error is a separate contribution: it changes recorded positions without moving the eye. Independent zero-mean position errors, each of variance $\sigma_m^2$ and independent of true motion, add $2\sigma_m^2$ to displacement MSD at nonzero lags. Thus an upward shift in the observed curve need not be a physical increase in movement. The [measurement-noise calculation](ch-eye-timing.html#sec-eye-msd) shows the conditions needed to remove it.

The next chapter follows the proposed source upstream: how a circuit can keep a pattern of activity while random spikes change the angle that pattern represents.

'''
path.write_text(old[:start]+new+old[end:],encoding='utf-8',newline='\n')
side=root/'content/chapters/01-foundations.yaml'
y=side.read_text(encoding='utf-8')
y=y.replace('title: Mean squared displacement combines random spread with mean motion','title: Shared neural signals and a biased command leave different signs in eye motion')
y=y.replace('summary: To identify where variability enters a pathway, the eye paper compares measurements\n    that share some fluctuations and have other fluctuations of their own.','summary: Shared neural commands, private spike variability, directional bias and muscle response affect different features of eye displacement. Covariance and mean squared displacement help distinguish these effects under explicit assumptions.')
side.write_text(y,encoding='utf-8',newline='\n')
print('Revised foundations section; original saved separately.')
