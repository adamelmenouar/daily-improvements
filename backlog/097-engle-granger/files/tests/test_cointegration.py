import numpy as np
from ts.cointegration import engle_granger


def test_cointegrated_pair_detected():
    rng = np.random.default_rng(99)
    x = np.cumsum(rng.normal(size=2000))
    y = 1.5 * x + rng.normal(size=2000)
    beta, stat, ok = engle_granger(y, x)
    assert ok and abs(beta - 1.5) < 0.05


def test_independent_random_walks_not_cointegrated():
    rng = np.random.default_rng(100)
    x, y = np.cumsum(rng.normal(size=2000)), np.cumsum(rng.normal(size=2000))
    assert not engle_granger(y, x)[2]
