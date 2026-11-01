import numpy as np
from ts.adf import adf_statistic, is_stationary


def test_random_walk_is_not_stationary():
    assert not is_stationary(np.cumsum(np.random.default_rng(98).normal(size=2000)))


def test_mean_reverting_series_is_stationary():
    rng = np.random.default_rng(98)
    x = np.zeros(2000)
    for t in range(1, 2000):
        x[t] = 0.5 * x[t - 1] + rng.normal()
    assert is_stationary(x) and adf_statistic(x) < -10
