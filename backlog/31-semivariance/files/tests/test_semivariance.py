import numpy as np
from risk.semivariance import downside_deviation, semivariance


def test_known_value():
    assert abs(downside_deviation([-1.0, 1.0]) - np.sqrt(0.5)) < 1e-12


def test_no_losses_means_zero():
    assert downside_deviation([0.01, 0.02, 0.03]) == 0.0


def test_semivariance_about_half_of_variance_for_symmetric_data():
    r = np.random.default_rng(31).normal(0, 0.01, 50_000)
    assert abs(semivariance(r) / r.var() - 0.5) < 0.03
