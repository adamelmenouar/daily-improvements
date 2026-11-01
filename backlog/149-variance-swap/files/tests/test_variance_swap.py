import numpy as np
from pricing.variance_swap import realized_variance, variance_swap_payoff


def _path(sigma, n=2000, seed=151):
    return 100 * np.exp(np.cumsum(np.random.default_rng(seed).normal(0, sigma / np.sqrt(252), n)))


def test_realized_variance_close_to_true_variance():
    assert abs(realized_variance(_path(0.2)) - 0.04) < 0.004


def test_payoff_sign_follows_realized_vs_strike():
    p = _path(0.30)
    assert variance_swap_payoff(p, 0.20, 100_000) > 0
    assert variance_swap_payoff(_path(0.10), 0.20, 100_000) < 0


def test_zero_payoff_when_realized_equals_strike():
    p = _path(0.2)
    k = np.sqrt(realized_variance(p))
    assert abs(variance_swap_payoff(p, k, 100_000)) < 1e-6
