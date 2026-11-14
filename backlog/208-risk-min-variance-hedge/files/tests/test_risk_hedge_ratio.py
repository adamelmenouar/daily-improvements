import numpy as np
from risk.hedge_ratio import min_variance_hedge_ratio, hedge_effectiveness

F = np.random.default_rng(198).normal(0, 0.01, 5000)
S = 0.9 * F + np.random.default_rng(199).normal(0, 0.003, 5000)


def test_recovers_the_true_hedge_ratio():
    assert abs(min_variance_hedge_ratio(S, F) - 0.9) < 0.03


def test_hedging_reduces_variance_by_the_effectiveness():
    h = min_variance_hedge_ratio(S, F)
    assert abs(1 - np.var(S - h * F) / np.var(S) - hedge_effectiveness(S, F)) < 1e-3


def test_perfect_hedge():
    assert abs(hedge_effectiveness(2 * F, F) - 1) < 1e-12
