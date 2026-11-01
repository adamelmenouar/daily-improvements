from risk.merton import merton_pd


def test_more_assets_means_safer():
    assert merton_pd(200, 100, 0.05, 0.2) < merton_pd(120, 100, 0.05, 0.2)


def test_far_from_default_is_tiny():
    assert merton_pd(1000, 100, 0.05, 0.2) < 1e-6


def test_more_volatility_means_riskier():
    assert merton_pd(150, 100, 0.05, 0.4) > merton_pd(150, 100, 0.05, 0.2)
