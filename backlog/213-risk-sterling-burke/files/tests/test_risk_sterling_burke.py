import numpy as np
from risk.sterling_burke import sterling_ratio, burke_ratio

R = np.random.default_rng(205).normal(0.001, 0.01, 1500)


def test_positive_for_a_profitable_noisy_strategy():
    assert sterling_ratio(R) > 0 and burke_ratio(R) > 0


def test_no_drawdown_means_infinite_ratios():
    assert sterling_ratio([0.01] * 20) == float("inf") and burke_ratio([0.01] * 20) == float("inf")


def test_a_more_volatile_strategy_with_the_same_mean_has_lower_ratios():
    calm = np.random.default_rng(206).normal(0.001, 0.005, 1500)
    wild = np.random.default_rng(206).normal(0.001, 0.02, 1500)
    assert sterling_ratio(calm) > sterling_ratio(wild) and burke_ratio(calm) > burke_ratio(wild)
