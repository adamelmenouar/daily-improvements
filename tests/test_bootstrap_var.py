import numpy as np
from risk.bootstrap_var import bootstrap_var_ci

R = np.random.default_rng(109).normal(0, 0.01, 500)


def test_interval_contains_estimate():
    lo, est, hi = bootstrap_var_ci(R)
    assert lo < est < hi


def test_reproducible():
    assert bootstrap_var_ci(R, seed=3) == bootstrap_var_ci(R, seed=3)


def test_more_data_narrows_interval():
    big = np.random.default_rng(110).normal(0, 0.01, 5000)
    lo1, _, hi1 = bootstrap_var_ci(R)
    lo2, _, hi2 = bootstrap_var_ci(big)
    assert hi2 - lo2 < hi1 - lo1
