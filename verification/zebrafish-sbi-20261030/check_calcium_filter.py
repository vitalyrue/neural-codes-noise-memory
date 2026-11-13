"""Check a proposed filter identity, not the CILVA fit or a lab workload.

Matches k[j] = exp(-j/tau_decay) - exp(-j/tau_rise), k[0] = 0,
causal convolution truncated to T, with zero initial filter state.
"""
import json
from pathlib import Path
import numpy as np
import scipy
from scipy.signal import lfilter


def filter_trace(values, tau_rise, tau_decay):
    values = np.asarray(values, dtype=np.float64)
    if values.ndim != 2:
        raise ValueError("Expected a neurons by time array")
    if not (np.isfinite(tau_rise) and np.isfinite(tau_decay)) or min(tau_rise, tau_decay) <= 0:
        raise ValueError("Time constants must be positive and finite")
    if values.shape[1] == 0:
        return values.copy()
    decay = lfilter([1.0], [1.0, -np.exp(-1.0 / tau_decay)], values, axis=1)
    rise = lfilter([1.0], [1.0, -np.exp(-1.0 / tau_rise)], values, axis=1)
    return decay - rise


def main():
    rng = np.random.default_rng(20261030)
    errors = []
    comparisons = 0
    for neurons in (1, 4):
        for length in (1, 2, 17, 257, 2048):
            for tau_rise, tau_decay in ((5.68, 11.5), (2.0, 10.0), (10.0, 10.0), (10.0, 10.01)):
                values = rng.normal(size=(neurons, length))
                kernel = np.exp(-np.arange(length) / tau_decay) - np.exp(-np.arange(length) / tau_rise)
                expected = np.stack([np.convolve(row, kernel)[:length] for row in values])
                actual = filter_trace(values, tau_rise, tau_decay)
                np.testing.assert_allclose(actual, expected, rtol=1e-10, atol=1e-12)
                reverse_expected = np.stack([values[:, t:] @ kernel[:length-t] for t in range(length)], axis=1)
                reverse_actual = filter_trace(values[:, ::-1], tau_rise, tau_decay)[:, ::-1]
                np.testing.assert_allclose(reverse_actual, reverse_expected, rtol=1e-10, atol=1e-12)
                errors.extend([float(np.max(np.abs(actual-expected))), float(np.max(np.abs(reverse_actual-reverse_expected)))])
                comparisons += 2
    assert filter_trace(np.empty((3, 0)), 2.0, 10.0).shape == (3, 0)
    np.testing.assert_array_equal(filter_trace(np.zeros((3, 20)), 2.0, 10.0), np.zeros((3, 20)))
    for values, rise, decay in [(np.ones(3), 2.0, 10.0), (np.ones((1, 3)), 0.0, 10.0), (np.ones((1, 3)), 2.0, np.nan)]:
        try:
            filter_trace(values, rise, decay)
        except ValueError:
            pass
        else:
            raise AssertionError("Expected input validation failure")
    result = {
        "status": "pass", "scope": "Synthetic forward filter and reverse gradient filter identity only",
        "comparisons": comparisons, "max_absolute_error": max(errors),
        "numpy": np.__version__, "scipy": scipy.__version__, "dtype": "float64",
        "runtime_speedup": "not measured", "full_CILVA_fit": "not run", "GPU": "not used"
    }
    Path(__file__).with_name("filter-check-result.json").write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result))


if __name__ == "__main__":
    main()
