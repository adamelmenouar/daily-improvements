import numpy as np
from trading.bootstrap_sharpe import bootstrap_sharpe_ci

R = np.random.default_rng(60).normal(0.0005, 0.01, 500)


def test_interval_contains_estimate():
    lo, est, hi = bootstrap_sharpe_ci(R)
    assert lo < est < hi


def test_reproducible():
    assert bootstrap_sharpe_ci(R, seed=1) == bootstrap_sharpe_ci(R, seed=1)


def test_more_data_narrows_interval():
    big = np.random.default_rng(61).normal(0.0005, 0.01, 5000)
    lo1, _, hi1 = bootstrap_sharpe_ci(R)
    lo2, _, hi2 = bootstrap_sharpe_ci(big)
    assert hi2 - lo2 < hi1 - lo1
