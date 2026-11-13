# Software source checks

Checked October 30, 2026 with the web tool against official documentation. These support optional reconstruction tools and their limits, not a claim that the three papers all used them. Author software is documented separately in the three source reports.

- NumPy 2.5, Random Generator: https://numpy.org/doc/stable/reference/random/generator.html . Generator supplies random distributions; default_rng accepts a seed to initialize generator state. The page explicitly gives no cross-version bit-stream compatibility guarantee. Supports recording generator, version and call order alongside the seed.
- SciPy 1.18.0, solve_ivp: https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.solve_ivp.html . Solves dy/dt=f(t,y) with an initial condition; adaptive deterministic ODE integration is not a complete specification of Poisson events or Brownian increments.
- SciPy 1.18.0, ndimage.label: https://docs.scipy.org/doc/scipy/reference/generated/scipy.ndimage.label.html . Labels nonzero connected components, controlled by a centrosymmetric structuring element. Default two-dimensional connectivity joins side neighbors, not diagonal-only neighbors.
- Brian 2.11.0: https://brian2.readthedocs.io/en/stable/ and https://brian2.readthedocs.io/en/stable/user/models.html . A spiking-neural-network simulator with equation-defined neuron groups, physical units, threshold/reset event handling and stochastic equations. Its default examples are not evidence of equivalence with the Burak models.

The numerical example is a guide calculation from Var(increment)=2Dh, already derived in the preceding guide. It does not use a new simulation run. For D=.5, h=.01 gives SD .1; h=.0025 gives SD .05; both accumulate variance 1 per second. Reducing the original SD by four yields variance .25 per second at the smaller h.

The Part III links in the tools chapter refer back to previously cited hardware studies. Their role is to distinguish simulated neural equations, post-layout circuit calculations and measured physical devices. No new hardware benchmark or device claim is introduced.
