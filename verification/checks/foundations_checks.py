"""Check the guide's constructed examples and draw their stated geometry.

These checks do not reproduce an experimental paper. The numerical inputs are
the teaching examples in chapters 1 and 6.
"""
from pathlib import Path
import json
import math
import datetime
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[2]
results = {}

lam = 20 * 0.05
assert lam == 1
results["poisson_zero_probability"] = math.exp(-lam)
results["population_count_sd"] = math.sqrt(20)
results["population_relative_sd"] = 1 / math.sqrt(20)
assert math.isclose(results["poisson_zero_probability"], 0.36787944117, rel_tol=1e-10)

b, k = 40.0, 2.0
state = np.array([50., 30.])
common = state + [3, 3]
along = state + [3, -3]
angle = lambda p: (p[0] - p[1]) / (2*k)
mean_error = lambda p: p.mean() - b
assert angle(common) == 5 and mean_error(common) == 3
assert angle(along) == 6.5 and mean_error(along) == 0
results["toy_angles_degrees"] = {"initial": angle(state), "common_perturbation": angle(common), "along_perturbation": angle(along)}

D, v = .02, .10
results["angular_variance_035s"] = 2*D*.35
results["angular_rms_arcmin_035s"] = math.sqrt(2*D*.35)*60
results["angular_rms_degrees_1s"] = math.sqrt(2*D)
results["bias_diffusion_crossover_seconds"] = 2*D/v**2
assert math.isclose(results["bias_diffusion_crossover_seconds"],4)
assert math.isclose(v**2*4**2, 2*D*4)

variance = 2*.01*.5
slopes = np.array([2.,-1.])
cov = variance*np.outer(slopes,slopes)
assert np.allclose(cov,[[.04,-.02],[-.02,.01]])
assert np.linalg.eigvalsh(cov).min() >= -1e-14
results["joint_rate_covariance_Hz2"] = cov.tolist()

plt.rcParams.update({"font.size":11,"font.family":"DejaVu Sans","svg.fonttype":"none"})
fig,ax=plt.subplots(figsize=(7.2,5.1),layout="constrained")
r1=np.linspace(19,61,300)
ax.plot(r1,80-r1,color="#17365d",lw=2.3,label="Fixed points: r₁ + r₂ = 80 Hz")
ax.scatter(*state,color="#17365d",s=55,zorder=5)
ax.scatter(*common,color="#ba6a15",s=55,zorder=5)
ax.scatter(*along,color="#0f6b78",s=55,zorder=5)
ax.annotate("",xy=state,xytext=common,arrowprops={"arrowstyle":"->","color":"#ba6a15","lw":2})
ax.annotate("",xy=along,xytext=state,arrowprops={"arrowstyle":"->","color":"#0f6b78","lw":1.8,"linestyle":"--"})
ax.annotate("Initial state\n(50, 30): 5°",state,xytext=(-105,17),textcoords="offset points",ha="left",color="#17365d")
ax.annotate("Common change (53, 33)\nrestores toward initial state",common,xytext=(-135,45),textcoords="offset points",color="#8a4a09")
ax.annotate("Along-line change (53, 27)\npersists at 6.5°",along,xytext=(-80,-65),textcoords="offset points",color="#0f6b78")
ax.set(xlim=(18,62),ylim=(18,62),xlabel="Activity r₁ (Hz)",ylabel="Activity r₂ (Hz)")
ax.set_aspect("equal");ax.spines[["top","right"]].set_visible(False)
ax.grid(alpha=.16);ax.legend(loc="upper right",frameon=False,fontsize=10)
target=ROOT/"assets/approved/visuals/attractor-directions.svg"
target.parent.mkdir(parents=True,exist_ok=True)
fig.savefig(target,format="svg");plt.close(fig)
results["figure"] = str(target.relative_to(ROOT))
results["checked_at"] = datetime.datetime.now().astimezone().isoformat()
(ROOT/"verification/checks/foundations-results.json").write_text(json.dumps(results,indent=2),encoding="utf-8")
print(json.dumps(results,indent=2))
