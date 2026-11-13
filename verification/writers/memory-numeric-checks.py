"""Bounded arithmetic and linear algebra checks for the memory chapters.

No paper simulation or empirical reproduction. Run with Python and NumPy.
The reader chapters contain no code listing dependent on this script.
"""
from pathlib import Path
from datetime import datetime
import json
import math
import numpy as np

checks = []


def close(label, value, expected, rel_tol=1e-10, abs_tol=1e-12):
    if not math.isclose(float(value), float(expected), rel_tol=rel_tol, abs_tol=abs_tol):
        raise AssertionError((label, value, expected))
    checks.append({"check": label, "value": float(value), "expected": float(expected)})


tau = 0.1
bias = 200.0
W = np.array([[0.0, -1.0], [-1.0, 0.0]])
u = np.array([0.5, -0.5])
v = np.array([1.0, -1.0])
K = (-np.eye(2) + W) / tau
assert np.allclose(K @ u, 0)
assert np.allclose(v @ K, 0)
close("left-right normalization", v @ u, 1)
for theta, expected_J, expected_bound in [(0.0, 0.05, 1000.0), (100.0, 1 / 15, 750.0)]:
    rates = np.array([(bias + theta) / (2 * tau), (bias - theta) / (2 * tau)])
    slopes = u / tau
    D = np.sum(v * v * rates) / 2
    J = np.sum(slopes * slopes / rates)
    close(f"mutual inhibition D at {theta}", D, 1000)
    close(f"mutual inhibition J at {theta}", J, expected_J)
    close(f"mutual inhibition lower bound at {theta}", 1 / (2 * tau**2 * J), expected_bound)

theta = 100
v_exc = np.array([0.5, 0.5])
r_exc = np.array([theta + 10, theta - 10]) / tau
D_exc = np.sum(v_exc**2 * r_exc) / 2
close("mutual excitation D from projection", D_exc, theta / (4 * tau))
close("mutual excitation variance slope", 2 * D_exc, theta / (2 * tau))

D = 0.005
J = 10000.0
star = 1 / math.sqrt(2 * D * J)
floor = math.sqrt(2 * D / J)
close("saturating characteristic interval", star, 0.1)
close("saturating readout floor", floor, 0.001)
close("naive optimum interval", math.sqrt(3) * star, 0.17320508075688773)
close("naive optimum variance", (2 / math.sqrt(3)) * floor, 0.0011547005383792516)
close("alpha .1 characteristic interval", star / math.sqrt(.1), 0.31622776601683794)
close("alpha .1 readout floor", floor / math.sqrt(.1), 0.0031622776601683794)
close("alpha .1 naive optimum interval", math.sqrt(3) * star / math.sqrt(.1), 0.5477225575051661)
close("two second full recall floor", 2 * D * 2 + floor, .021)
close("two second partial recall floor", 2 * D * 2 + floor / math.sqrt(.1), .02316227766016838)
close("strict inequality recall floor", 2 * D * 2 + math.sqrt(2 * D / 40000), .0205)
close("printed Eq6 comparison value", 2 * D * (2 + tau), .021)
for z in [1.0, 2.0, 3.0]:
    checks.append({"check": f"ideal variance ratio at L/star={z}", "value": 1 / math.tanh(z)})

# Compare direct discrete Gaussian covariance inversion with a separately
# implemented backward precision recursion and the continuous limit.
for duration in [0.02, 0.1, 0.3]:
    exact_continuous = floor / math.tanh(duration / star)
    for n in [80, 240]:
        h = duration / n
        times = np.arange(1, n + 1) * h
        covariance = 2 * D * np.minimum.outer(times, times) + np.eye(n) / (J * h)
        one = np.ones(n)
        direct_variance = 1 / (one @ np.linalg.solve(covariance, one))
        p = 0.0
        for _ in range(n):
            p = J * h + p / (1 + 2 * D * h * p)
        # y_1 occurs after the first transition from the requested x0.
        recursive_variance = 1 / p + 2 * D * h
        close(f"direct covariance vs precision L={duration}, n={n}", direct_variance, recursive_variance)
        assert abs(direct_variance / exact_continuous - 1) < .025
        checks.append({"check": f"continuous limit relative discrepancy L={duration}, n={n}",
                       "value": direct_variance / exact_continuous - 1})
        direct_naive = (one @ covariance @ one) / n**2
        continuous_naive = 2 * D * duration / 3 + 1 / (J * duration)
        assert abs(direct_naive / continuous_naive - 1) < .025

# The two-time-scale left vector, normalization, and projected diffusion.
tau_m = 0.04
F = np.eye(2) / tau
A = np.block([[-np.eye(2) / tau, np.eye(2)], [F @ W / tau_m, -np.eye(2) / tau_m]])
rprime = np.array([1, -1]) / (2 * tau)
gprime = np.array([.5, -.5])
a = gprime / ((tau + tau_m) * (gprime @ rprime))
left = np.concatenate([a, tau_m * a])
right = np.concatenate([tau * rprime, rprime])
assert np.allclose(A @ right, 0)
assert np.allclose(left @ A, 0)
close("two-scale left-right normalization", left @ right, 1)
rates = np.array([1000, 1000])
two_D = np.sum(a**2 * rates)
close("two-scale equality", two_D * .05, 1 / (tau + tau_m)**2)

# General matrix inequality checked from a nontrivial conjugate pair.
rng = np.random.default_rng(7386109)
U = rng.normal(size=(9, 3))
Uplus = U @ np.linalg.inv(U.T @ U)
Q = (np.eye(9) - Uplus @ U.T) @ rng.normal(size=(9, 3))
V = Uplus + Q
assert np.allclose(U.T @ V, np.eye(3))
residual = V.T @ V - np.linalg.inv(U.T @ U)
assert np.allclose(residual, Q.T @ Q)
assert np.linalg.eigvalsh(residual).min() > -1e-10
checks.append({"check": "matrix bound smallest residual eigenvalue", "value": float(np.linalg.eigvalsh(residual).min())})

out = {"timestamp": datetime.now().astimezone().isoformat(),
       "scope": "Teaching arithmetic, finite covariance and projection checks; no paper simulation",
       "numpy": np.__version__, "checks": checks, "result": "passed"}
target = Path(__file__).with_name("memory-numeric-results.json")
target.write_text(json.dumps(out, indent=2), encoding="utf-8")
print(json.dumps({"result": out["result"], "checks": len(checks), "timestamp": out["timestamp"], "output": str(target)}))
