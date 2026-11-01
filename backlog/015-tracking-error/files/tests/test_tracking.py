import numpy as np
from risk.tracking import tracking_error, information_ratio

B = np.random.default_rng(15).normal(0, 0.01, 500)


def test_identical_portfolio_has_zero_tracking_error():
    assert tracking_error(B, B) == 0.0


def test_outperformance_gives_positive_ir():
    noise = np.random.default_rng(16).normal(0, 0.001, 500)
    assert information_ratio(B + 0.0005 + noise, B) > 0
