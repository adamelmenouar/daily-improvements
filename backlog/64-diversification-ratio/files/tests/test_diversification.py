import numpy as np
from portfolio.diversification import diversification_ratio


def test_single_asset_is_one():
    assert abs(diversification_ratio([1.0], [[0.04]]) - 1) < 1e-12


def test_perfect_correlation_gives_one():
    s = np.array([0.1, 0.2])
    assert abs(diversification_ratio([0.5, 0.5], np.outer(s, s)) - 1) < 1e-12


def test_uncorrelated_assets_diversify():
    assert diversification_ratio([0.5, 0.5], np.diag([0.04, 0.04])) > 1.3
