import numpy as np
from ts.acf import acf


def test_lag_zero_is_one():
    assert acf(np.random.default_rng(91).normal(size=100), 5)[0] == 1.0


def test_white_noise_has_small_autocorrelation():
    a = acf(np.random.default_rng(91).normal(size=5000), 10)[1:]
    assert np.abs(a).max() < 0.05


def test_ar1_autocorrelation_decays_geometrically():
    rng = np.random.default_rng(92)
    x = np.zeros(20_000)
    for t in range(1, len(x)):
        x[t] = 0.8 * x[t - 1] + rng.normal()
    a = acf(x, 2)
    assert abs(a[1] - 0.8) < 0.03 and abs(a[2] - 0.64) < 0.05
