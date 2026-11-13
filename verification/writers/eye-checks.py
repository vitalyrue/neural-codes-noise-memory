"""Deterministic checks of the guide's teaching examples, not a paper reproduction."""
import cmath
import hashlib
import json
import math
from datetime import datetime
from pathlib import Path

HERE = Path(__file__).resolve().parent
GUIDE = HERE.parents[1]
CHAPTER = GUIDE / "content/chapters/04-eye-drift.md"
results = {}
expected_sources = {
    "ben-shushan-2022-fixational-drift.pdf": "15f273f99bd8d8e8daa09a9f7809e04c53da514b146750c0ec517812e3478caa",
    "ben-shushan-2022-supplement-1.pdf": "323335499cb6428f68714fb1c855a9b87d5fe38449d31e26acce76417358a7d6",
    "ben-shushan-2022-supplement-2.pdf": "3f3c933f7cd1326d847565363481d7e79e922025ac354ae3872818f5aca3aa7c",
}
for filename, expected_hash in expected_sources.items():
    actual = hashlib.sha256((GUIDE.parent / "papers" / filename).read_bytes()).hexdigest()
    assert actual == expected_hash
results["source_sha256"] = expected_sources

k, tp, tm = 4.0, 0.120, 0.005
r, m = k * (tp + tm), k * tp * tm
prefactor = tp * tm / (m * (tp - tm))
assert math.isclose(r, 0.5)
assert math.isclose(m, 0.0024)
assert math.isclose(prefactor * (tp - tm), 1 / k)
roots = (2 / (r / m - math.sqrt((r / m) ** 2 - 4 * k / m)),
         2 / (r / m + math.sqrt((r / m) ** 2 - 4 * k / m)))
assert all(math.isclose(x, y) for x, y in zip(roots, (tp, tm)))
for omega in (0.0, 1.0, 10.0, 100.0):
    delay = 0.010
    forward = cmath.exp(1j * omega * delay) * (k - m * omega**2 + 1j * r * omega)
    inverse = cmath.exp(-1j * omega * delay) / (k - m * omega**2 + 1j * r * omega)
    assert abs(forward * inverse - 1) < 1e-12
results["kernel"] = dict(k=k, tau_slow_s=tp, tau_fast_s=tm,
                         r=r, m=m, prefactor_deg_per_spike=prefactor,
                         area_deg_s_per_spike=prefactor * (tp - tm),
                         static_offset_at_80Hz_deg=80 / k,
                         frequency_inverse_check="0, 1, 10, 100 rad/s; delay 10 ms")

vc, veta, veps = 0.00820, 0.00180, 0.22446
vy, vx = vc + veta, vc + veps
R, chi = vc / math.sqrt(vx * vy), vc / vy
assert abs(R - 0.17) < 1e-5
assert math.isclose(chi, 0.82)
assert math.isclose(R * math.sqrt(vx / vy), chi)
results["correlation_example"] = dict(var_common=vc, var_private_eye=veta,
                                    var_predictor_error=veps, var_eye=vy,
                                    var_predictor=vx, R=R, chi=chi, R_squared=R**2,
                                    independence_bound_at_1000=1/1000)

def simpson(f, upper, n=2000):
    step = upper / n
    return step / 3 * (f(0) + f(upper) +
                       4 * sum(f(i * step) for i in range(1, n, 2)) +
                       2 * sum(f(i * step) for i in range(2, n, 2)))

D, tau = 0.02, 0.12
msd_results = []
for ratio in (0.001, 0.1, 1, 5, 100):
    lag = ratio * tau
    exact = 2 * D * (lag + tau * math.expm1(-lag / tau))
    integral = 2 * simpson(lambda s: (lag - s) * D / tau * math.exp(-s / tau), lag)
    assert abs(integral / exact - 1) < 2e-6
    alpha = lag * (-math.expm1(-lag/tau)) / (lag + tau * math.expm1(-lag/tau))
    assert 1 < alpha < 2
    msd_results.append(dict(lag_over_tau=ratio, MSD=exact, alpha=alpha,
                            covariance_integral_relative_error=integral/exact-1))
assert abs(msd_results[2]["alpha"] - (math.e - 1)) < 1e-12
assert abs(msd_results[3]["alpha"] - 1.240) < 0.001
short = msd_results[0]["MSD"]
assert abs(short / (D / tau * (0.001 * tau)**2) - 1) < 0.001
results["filtered_brownian"] = msd_results

A = 0.01
lag = tau
cv_integral = A * simpson(lambda u: math.exp(-u/tau) / tau * math.exp(-(u+lag)/tau) / tau,
                         30*tau, n=6000)
cv_expected = A / (2*tau) * math.exp(-lag/tau)
assert abs(cv_integral/cv_expected - 1) < 1e-8
results["filtered_white"] = dict(lag_s=lag, covariance=cv_expected,
                                numerical_covariance=cv_integral,
                                asymptotic_MSD=A/tau)

a, twoD, duration, rate = 1/15, 100, 0.5, 80
cv_drift = a * math.sqrt(twoD * duration / 6) / rate
assert abs(cv_drift - 0.0024056261) < 1e-9
results["supplement_CV"] = dict(CV_from_drift=cv_drift,
                                D_deg2_per_s=(twoD / 2) / 60**2)
results["measurement_example"] = dict(measured=0.0014, noise_offset=0.001,
                                      corrected=0.0014-0.001,
                                      fractional_error=0.0001/(0.0014-0.001))

text = CHAPTER.read_text(encoding="utf-8")
import re
definitions = set(re.findall(r"^\[\^([^]]+)\]:", text, re.M))
uses = set(re.findall(r"\[\^([^]]+)\](?!:)", text))
assert uses == definitions, (uses-definitions, definitions-uses)
ids = re.findall(r"\{#([^}]+)\}", text)
assert len(ids) == len(set(ids))
assert all(re.fullmatch(r"(?:ch|sec):[A-Z0-9-]+", item) for item in ids)
assert "—" not in text
assert text.count("$$") % 2 == 0
results["structure"] = dict(footnote_count=len(definitions), heading_ids=ids,
                            display_math_delimiters=text.count("$$"),
                            no_emdash=True, chapter_sha256=hashlib.sha256(text.encode()).hexdigest())
payload = dict(checked_at=datetime.now().astimezone().isoformat(),
               description="Teaching math and source structure; no experimental reproduction",
               checks=results)
(HERE / "eye-checks.json").write_text(json.dumps(payload, indent=2), encoding="utf-8")
print(json.dumps(payload, indent=2))
