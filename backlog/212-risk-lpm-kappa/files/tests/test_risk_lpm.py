import numpy as np
from risk.lpm import lower_partial_moment, kappa_ratio
from risk.omega import omega_ratio

R = np.random.default_rng(204).normal(0.001, 0.01, 3000)


def test_kappa_one_is_omega_minus_one():
    assert abs(kappa_ratio(R, 1, 0.0) - (omega_ratio(R, 0.0) - 1)) < 1e-9


def test_known_lpm():
    assert abs(lower_partial_moment([-0.02, 0.01, -0.01], 2, 0.0) - (0.0004 + 0.0001) / 3) < 1e-15


def test_no_losses_gives_infinity():
    assert kappa_ratio([0.01, 0.02], 2) == float("inf")
