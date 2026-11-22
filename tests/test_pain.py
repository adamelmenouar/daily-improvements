import numpy as np
from risk.pain import pain_index, pain_ratio


def test_known_value():
    # equity 1.1, 0.99 -> drawdowns 0 et -10 % : moyenne 5 %
    assert abs(pain_index([0.1, -0.1]) - 0.05) < 1e-12


def test_rising_market_has_infinite_ratio():
    assert pain_ratio([0.01] * 20) == float("inf")


def test_ratio_positive_for_a_profitable_noisy_series():
    assert pain_ratio(np.random.default_rng(112).normal(0.001, 0.01, 1000)) > 0
