import numpy as np
from risk.capm import beta, alpha

M = np.random.default_rng(12).normal(0.0004, 0.01, 2000)


def test_beta_of_scaled_market():
    assert abs(beta(2 * M, M) - 2) < 1e-9


def test_alpha_zero_for_pure_beta():
    assert abs(alpha(1.5 * M, M)) < 1e-9


def test_constant_excess_return_shows_as_alpha():
    assert abs(alpha(M + 0.0001, M) - 0.0001 * 252) < 1e-9
