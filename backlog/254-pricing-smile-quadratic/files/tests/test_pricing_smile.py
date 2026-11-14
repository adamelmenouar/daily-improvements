import numpy as np
from pricing.smile import fit_smile, smile_vol


def test_recovers_an_exact_quadratic_smile():
    f = 100.0
    ks = np.array([80, 90, 100, 110, 120.0])
    true = (0.20, -0.10, 0.50)
    vols = np.array([smile_vol(k, f, true) for k in ks])
    assert np.allclose(fit_smile(ks, vols, f), true)


def test_atm_vol_is_the_intercept():
    assert abs(smile_vol(100.0, 100.0, (0.22, -0.1, 0.3)) - 0.22) < 1e-12


def test_positive_curvature_makes_wings_richer_than_the_center():
    co = (0.20, 0.0, 0.8)
    assert smile_vol(70, 100, co) > smile_vol(100, 100, co) and smile_vol(140, 100, co) > smile_vol(100, 100, co)
