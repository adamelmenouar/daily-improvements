import numpy as np
from risk.pca_risk import explained_variance_ratio


def test_ratios_sum_to_one_and_sorted():
    x = np.random.default_rng(44).normal(0, 0.01, (500, 5))
    r = explained_variance_ratio(x)
    assert abs(r.sum() - 1) < 1e-12 and (np.diff(r) <= 1e-15).all()


def test_single_factor_market_dominates():
    rng = np.random.default_rng(44)
    f = rng.normal(0, 0.01, (1000, 1))
    x = f @ np.ones((1, 6)) + rng.normal(0, 0.002, (1000, 6))
    assert explained_variance_ratio(x)[0] > 0.9
