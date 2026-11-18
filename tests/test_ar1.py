import numpy as np
from ts.ar1 import fit_ar1, forecast_ar1


def _sim(phi=0.7, c=0.1, n=20_000, seed=94):
    rng = np.random.default_rng(seed)
    x = np.zeros(n)
    for t in range(1, n):
        x[t] = c + phi * x[t - 1] + rng.normal()
    return x


def test_recovers_parameters():
    c, phi = fit_ar1(_sim())
    assert abs(phi - 0.7) < 0.02 and abs(c - 0.1) < 0.05


def test_forecast_reverts_to_long_run_mean():
    x = _sim()
    f = forecast_ar1(x, 200)
    c, phi = fit_ar1(x)
    assert abs(f[-1] - c / (1 - phi)) < 1e-6
