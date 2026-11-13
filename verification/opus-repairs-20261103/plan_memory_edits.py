import json
from pathlib import Path
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parents[2]
edits = []
def add(file, label, before, after, sources):
    path = 'content/chapters/' + file + '.md'
    text = (ROOT / path).read_text(encoding='utf-8')
    assert text.count(before) == 1, (label, text.count(before))
    edits.append(dict(path=path, label=label, before=before, after=after, sources=sources))

add('01-foundations', 'MSD before simulation measurement',
    '**What is measured and compared.** At each step,',
    r'''Before comparing simulated motion with theory, we need a measure of how far the represented value moves. Let $x(t)$ be that value at absolute time $t$, and let $\ell$ be the time between two observations, called the lag. [The [**displacement**]{.definition-term custom-style="Definition Term"} is $\Delta x=x(t+\ell)-x(t)$. The [**mean squared displacement**]{.definition-term custom-style="Definition Term"}, or MSD, is the average of $(\Delta x)^2$ over intervals with the same lag.]{.definition-explanation} The average can use different starting times along a recording, repeated trials, or both; which intervals can be combined depends on whether their movement statistics are comparable. Squaring prevents leftward and rightward changes from cancelling.

For an angle measured in degrees, MSD has units degrees squared. An MSD plot puts lag on the horizontal axis and MSD on the vertical axis. Lag is a duration, not the clock time at which an interval starts. If the statistics change during a trial, the MSD can depend on that starting time as well as on lag.

[A straight MSD curve on ordinary axes means that squared displacement grows at a constant rate over that range.]{.key-statement} The zero-mean diffusion model taught in the next chapter gives $\operatorname{MSD}(\ell)=2D\ell$, with slope $2D$ in degrees squared per second. On axes that plot logarithms, a relation $\operatorname{MSD}\propto\ell^\beta$ has slope $\beta$: diffusion has slope one, while constant-velocity motion has slope two. A slope alone does not identify the neural cause. Bias, smoothing by muscles, boundaries and the range of lags measured can change the curve.

**What is measured and compared.** At each step,''',
    ['Burak and Fiete 2012 main Fig.2 pp.3-4; SI S26-S31 pp.6-7', 'Guide mathematical definition; no new data'])

add('01-foundations', 'Reuse displacement already taught',
    r'''**Physical meaning: random wandering differs from a persistent directional error.** Let $x(t)$ be horizontal eye angle in degrees and let $\ell$ be the time between two measurements, called the lag, in seconds. [The [**displacement**]{.definition-term custom-style="Definition Term"} $\Delta x=x(t+\ell)-x(t)$ is the change in that angle.]{.definition-explanation}''',
    r'''**Physical meaning: random wandering differs from a persistent directional error.** Apply the displacement measure above to horizontal eye angle $x(t)$ in degrees, using a lag $\ell$ in seconds.''',
    ['Same mathematical definition, now applied to measured eye motion'])

add('01-foundations', 'MSD reminder preserves variance identity',
    r'''[The **mean squared displacement**, or MSD, averages $(\Delta x)^2$ across repeated intervals and has units degrees squared.]{.definition-explanation} Its two contributions are''',
    r'''The MSD of this eye displacement has units degrees squared. Its two contributions are''',
    ['Existing variance and squared-mean identity retained'])

add('01b-persistence', 'Rate toy to paper network bridge',
    '## Independent steps with equal duration and variance give linear variance growth {#sec:FOUNDATIONS-DIFFUSION}',
    r'''The paper's two-unit mutual-inhibition network has this same geometry. Over its positive linear firing range, its rate dynamics reproduce the example with common-mode decay rate $a=2/\tau$, where $\tau$ is the synaptic decay time. The difference between the rates remains neutral. The [network chapter](ch-memory-dynamics.html#sec-memory-symmetric) uses synaptic activations to describe this network and gives the conversion between its coordinate and the angle used here. This small network illustrates one possible memory mechanism; the gaze-holding circuit also needs the motor and muscle stages described above.

## Independent steps with equal duration and variance give linear variance growth {#sec:FOUNDATIONS-DIFFUSION}''',
    ['Burak and Fiete 2012 SI two-population mutual-inhibition model pp.8-9', 'Guide algebra: dot r1=dot r2=-(r1+r2-2b)/tau'])

add('01b-persistence', 'Fixational versus systematic drift',
    r'''A theory of random diffusion must account separately for [**systematic drift**]{.definition-term custom-style="Definition Term"}, a nonzero mean velocity.''',
    r'''A theory of random diffusion must account separately for [**systematic drift**]{.definition-term custom-style="Definition Term"}, a nonzero mean velocity. The eye paper's term “fixational drift” names the eye's slow motion between saccades, which can be largely random; it does not imply a nonzero mean velocity.''',
    ['Ben-Shushan et al. 2022 abstract and Introduction; Burak and Fiete 2012 SI Systematic drift pp.4-5'])

add('02-memory-dynamics', 'State coordinate estimate distinction and visible flow definition',
    r'''The memory coordinate is $\theta$. Its initial value is $\Theta$. A bar denotes a noise free steady state, so $\bar r_i(\theta)$ is neuron $i$'s steady firing rate at memory value $\theta$. The common synaptic time constant is $\tau$. A one dimensional diffusion coefficient $D$ has units of memory coordinate squared per time, with the convention $\operatorname{Var}[\theta(t)-\Theta]=2Dt$ when $D$ is constant and boundaries do not matter.''',
    r'''Here the physical network state is the vector of synaptic activations $\mathbf s=(s_1,\ldots,s_N)$; firing rates follow from that state through the input and transfer function. The memory coordinate is $\theta$, and its initial value is $\Theta$. “Stored value” and “represented value” refer to this same coordinate, rather than to the whole activation vector. An observer's estimate $\widehat\theta$, obtained from a finite spike sample, can differ from $\theta$.

Noise generally puts $\mathbf s$ slightly away from the attractor. To assign it a memory coordinate, imagine turning off further noise and following the deterministic return flow. [The fixed point reached by this flow is the paper's [**instantaneous attractor state**]{.definition-term custom-style="Definition Term"}; $\theta$ labels that point.]{.definition-explanation} This local definition assumes that nearby states return to a unique point on the continuous family. It uses the circuit's return dynamics, which can differ from a perpendicular geometric projection. [Original definition and Figure 1A, p. 2](../papers/burak-fiete-2012-persistent-activity.pdf#page=2).

A bar denotes a noise free steady state, so $\bar r_i(\theta)$ is neuron $i$'s steady firing rate at memory value $\theta$, and $\bar s_i=\tau\bar r_i$. The common synaptic time constant is $\tau$. A one dimensional diffusion coefficient $D$ has units of memory coordinate squared per time, with the convention $\operatorname{Var}[\theta(t)-\Theta]=2Dt$ when $D$ is constant and boundaries do not matter.''',
    ['Burak and Fiete 2012 main p.2 flow definition and Fig.1A; main Eqs.7-9 p.5'])

add('02-memory-dynamics', 'Map mutual inhibition coordinate to earlier toy',
    r'''The coordinate is $\theta=s_1-s_2$. The sum $s_1+s_2$ relaxes to $b$, while the difference is neutral.''',
    r'''Here $b$ is an activation bias and $\theta=s_1-s_2$ is an activation difference. These have different units from the rate baseline and angle in the [earlier two-cell example](ch-persistence.html#sec-foundations-attractor-example). Writing that example's baseline as $b_{\mathrm{rate}}$ and its angle as $\theta_{\mathrm{angle}}$, the conversion is $b=2\tau b_{\mathrm{rate}}$ and $\theta=2\tau k\theta_{\mathrm{angle}}$. The sum $s_1+s_2$ relaxes to $b$ at rate $2/\tau$, while the difference is neutral.''',
    ['Burak and Fiete 2012 SI mutual inhibition pp.8-9; guide coordinate conversion from linear transfer and rate toy'])

add('02b-memory-long-delays', 'Figure recap points to earlier flow teaching',
    r'''**Neural mechanism in the figures.** [Figure 1A, p. 2](ch-memory-long-delays.html#fig-paper-memory-1) shows the definition of the memory coordinate. Start at a green point off the attractor and follow the noise free flow to the black point on it. This endpoint defines the instantaneous attractor state. After one noisy interval, repeat that flow. The difference between the two endpoints is the retained memory change. The relevant projection follows the flow, as in the [tilted two variable example](ch-memory-dynamics.html#sec-memory-linearization).''',
    r'''**Neural mechanism in the figures.** [Figure 1A, p. 2](ch-memory-long-delays.html#fig-paper-memory-1) illustrates the [flow-defined coordinate established in Chapter 3](ch-memory-dynamics.html#ch-memory-dynamics). The green state returns to the black attractor point under noise free dynamics. Comparing the endpoints before and after one noisy interval isolates the retained memory change. The [tilted two variable example](ch-memory-dynamics.html#sec-memory-linearization) shows why the return path matters.''',
    ['Burak and Fiete 2012 main Fig.1A p.2'])

add('03-memory-information', 'Physical bound heuristic before proof',
    r'''**Neural mechanism.** The network has no access to its exact firing rates as noiseless numbers. Its recurrent input is built from the same random spikes that an external observer sees. The lower bound on diffusion follows directly by comparing the state sensitivity of the network with the spike information.''',
    r'''**Neural mechanism.** The network has no access to its exact firing rates as noiseless numbers. Its recurrent input is built from the same random spikes that an external observer sees. Burak and Fiete give this physical interpretation: maintaining the state acts like estimating it again from roughly one synaptic time constant $\tau$ of the network's own spikes. That sample supplies information $J\tau$, so even an ideal locally unbiased estimate has variance at least $1/(J\tau)$. Comparing this with the variance $2D\tau$ accumulated over the same time suggests $2D\tau\ge1/(J\tau)$. One factor of $\tau$ comes from collecting information; the other comes from accumulating displacement variance. This is the paper's heuristic interpretation, not a separate model in which the network resets every $\tau$. The proof below establishes the inequality from the projection assumptions. [Paper interpretation, p. 3](../papers/burak-fiete-2012-persistent-activity.pdf#page=3).''',
    ['Burak and Fiete 2012 main p.3 interpretation after Eq.4; unchanged proof SI S45-S49 pp.10-11'])

add('03-memory-information', 'Running model information reminder',
    r'''In the two cell mutual inhibition model, use $b=200$ activation units and $\tau=0.1\,\mathrm{s}$.''',
    r'''Return to the [two cell mutual inhibition model](ch-memory-dynamics.html#sec-memory-symmetric), now using $b=200$ activation units and $\tau=0.1\,\mathrm{s}$. This changes the illustrative bias from the preceding chapter's plot, while retaining the same network equations.''',
    ['Existing numerical example unchanged; previous chapter plot uses b=20'])

add('03b-memory-readout', 'One sentence on readout independence',
    r'''In this approximation, these increments and errors are independent, zero-mean Gaussian variables. The equivalent observation model is''',
    r'''In this approximation, these increments and errors are independent, zero-mean Gaussian variables. This treats the noise moving the state as separate from the noise in the observed counts, excluding the dependence that can arise when the same spikes both change recurrent activation and supply the observation. The equivalent observation model is''',
    ['Burak and Fiete 2012 SI S57-S62 pp.12-13; F01 narrowed Stage3; no alternative formula'])

add('03b-memory-readout', 'Remove transition variance q collision',
    r'''Bringing that likelihood one step backward adds transition variance $q=2Dh$, since the next state equals the earlier state plus an independent Gaussian increment.''',
    r'''Bringing that likelihood one step backward adds transition variance $2Dh$, since the next state equals the earlier state plus an independent Gaussian increment.''',
    ['Existing recursion; direct notation only'])

add('03b-memory-readout', 'Use transition variance directly in recursion',
    r'''\frac{1}{1/P+q}=\frac{P}{1+2DhP}.''',
    r'''\frac{1}{1/P+2Dh}=\frac{P}{1+2DhP}.''',
    ['Existing recursion; algebra unchanged'])

add('03b-memory-readout', 'Carry mutual inhibition through readout without new numbers',
    r'''**Neural question and model.** A decoder designed for a stationary state averages its observations with equal weight. That reduces independent observation noise, but late observations reflect a state that has moved further from $x$.''',
    r'''**Neural question and model.** A decoder designed for a stationary state averages its observations with equal weight. That reduces independent observation noise, but late observations reflect a state that has moved further from $x$.

For the recurring mutual-inhibition example, opposite changes in the two rates signal a change in the activation difference. Its $D$ describes how that difference wanders; its $J$ describes how well the spikes distinguish nearby values. The readout calculation combines those same quantities: longer collection reduces count uncertainty while allowing more motion. Here we apply the local model with $D$ and $J$ held fixed near the chosen state. The two-cell network has state-dependent $J$, so these constant-coefficient formulas do not describe excursions across its whole range.''',
    ['Burak and Fiete 2012 main readout p.4; SI S58-S81 pp.13-16; existing guide mutual inhibition D and J formulas'])

ledger = dict(first_persisted_utc=datetime.now(timezone.utc).isoformat(), stage='intended per-passage edits before execution', edits=edits)
out = ROOT / 'verification/opus-repairs-20261103/edits-memory.json'
assert not out.exists()
out.write_text(json.dumps(ledger, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
print(f'Recorded {len(edits)} intended changes before editing at {ledger["first_persisted_utc"]}')
