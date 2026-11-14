import numpy as np
from risk.rachev import rachev_ratio


def test_symmetric_returns_give_about_one():
    assert abs(rachev_ratio(np.random.default_rng(207).normal(0, 0.01, 50_000)) - 1) < 0.05


def test_positive_skew_gives_ratio_above_one():
    r = np.random.default_rng(208).lognormal(0, 0.5, 50_000) - np.exp(0.125)
    assert rachev_ratio(r) > 1.5


def test_known_value():
    assert abs(rachev_ratio([-3, -1, 0, 1, 2, 4, 5, -2, 3, 0], 0.2) - (4.5 / 2.5)) < 1e-12
