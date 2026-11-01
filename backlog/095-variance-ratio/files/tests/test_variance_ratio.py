import numpy as np
from ts.variance_ratio import variance_ratio


def _ar(phi, n=20_000, seed=97):
    rng = np.random.default_rng(seed)
    r = np.zeros(n)
    for t in range(1, n):
        r[t] = phi * r[t - 1] + rng.normal()
    return r


def test_iid_returns_have_ratio_near_one():
    assert abs(variance_ratio(_ar(0.0)) - 1) < 0.1


def test_momentum_gives_ratio_above_one():
    assert variance_ratio(_ar(0.3)) > 1.3


def test_mean_reversion_gives_ratio_below_one():
    assert variance_ratio(_ar(-0.3)) < 0.8
