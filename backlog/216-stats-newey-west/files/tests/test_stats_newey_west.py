import numpy as np
from stats.newey_west import newey_west_se


def _ar(phi, n=5000, seed=210):
    rng = np.random.default_rng(seed)
    x = np.zeros(n)
    for t in range(1, n):
        x[t] = phi * x[t - 1] + rng.normal()
    return x


def test_iid_data_matches_the_classical_standard_error():
    x = np.random.default_rng(211).normal(size=5000)
    assert abs(newey_west_se(x) - x.std() / np.sqrt(5000)) < 0.005


def test_autocorrelation_inflates_the_standard_error():
    x = _ar(0.6)
    assert newey_west_se(x, 20) > 1.5 * x.std() / np.sqrt(len(x))
