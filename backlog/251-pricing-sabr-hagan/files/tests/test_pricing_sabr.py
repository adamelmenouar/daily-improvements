from pricing.sabr import sabr_vol


def test_lognormal_case_without_vol_of_vol_is_flat():
    assert abs(sabr_vol(0.05, 0.06, 1.0, 0.2, 1.0, 0.0, 1e-6) - 0.2) < 1e-4


def test_continuity_around_the_money():
    a = sabr_vol(0.05, 0.05, 1.0, 0.04, 0.5, -0.3, 0.4)
    b = sabr_vol(0.05, 0.05 * (1 + 1e-6), 1.0, 0.04, 0.5, -0.3, 0.4)
    assert abs(a - b) < 1e-5


def test_negative_correlation_gives_a_downward_skew():
    low = sabr_vol(0.05, 0.04, 1.0, 0.04, 0.5, -0.5, 0.5)
    high = sabr_vol(0.05, 0.06, 1.0, 0.04, 0.5, -0.5, 0.5)
    assert low > high


def test_more_vol_of_vol_gives_a_stronger_smile():
    k = 0.08
    assert sabr_vol(0.05, k, 1.0, 0.04, 0.5, 0.0, 0.8) > sabr_vol(0.05, k, 1.0, 0.04, 0.5, 0.0, 0.2)
