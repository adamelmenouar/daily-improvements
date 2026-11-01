import numpy as np
from pricing.nelson_siegel import nelson_siegel


def test_long_end_converges_to_beta0():
    assert abs(nelson_siegel(1000.0, 0.04, -0.02, 0.01, 2.0) - 0.04) < 1e-3


def test_short_end_is_beta0_plus_beta1():
    assert abs(nelson_siegel(1e-6, 0.04, -0.02, 0.01, 2.0) - 0.02) < 1e-5


def test_negative_slope_means_upward_curve():
    y = nelson_siegel(np.array([0.5, 2, 5, 10]), 0.04, -0.02, 0.0, 2.0)
    assert (np.diff(y) > 0).all()
