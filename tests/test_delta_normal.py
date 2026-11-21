import numpy as np
from scipy.stats import norm
from risk.delta_normal import delta_normal_var


def test_single_position():
    assert abs(delta_normal_var([1_000_000], [[0.0001]], 0.99) - 1_000_000 * 0.01 * norm.ppf(0.99)) < 1e-6


def test_diversification_reduces_var():
    cov = np.diag([0.0001, 0.0001])
    assert delta_normal_var([500_000, 500_000], cov) < delta_normal_var([1_000_000, 0], cov)


def test_horizon_scaling():
    a = delta_normal_var([1e6], [[1e-4]], 0.99, 1)
    assert abs(delta_normal_var([1e6], [[1e-4]], 0.99, 10) - a * 10**0.5) < 1e-6
