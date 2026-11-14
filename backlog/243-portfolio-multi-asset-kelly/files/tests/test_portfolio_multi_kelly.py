import numpy as np
from portfolio.multi_kelly import kelly_vector, growth_rate
from trading.kelly_continuous import continuous_kelly

MU = np.array([0.08, 0.10])
COV = np.array([[0.04, 0.01], [0.01, 0.09]])


def test_single_asset_matches_the_scalar_formula():
    assert abs(kelly_vector([0.08], [[0.04]], 0.02)[0] - continuous_kelly(0.08, 0.2, 0.02)) < 1e-12


def test_kelly_maximizes_the_growth_rate():
    f = kelly_vector(MU, COV, 0.02)
    best = growth_rate(f, MU, COV, 0.02)
    assert best > growth_rate(0.5 * f, MU, COV, 0.02) and best > growth_rate(1.5 * f, MU, COV, 0.02)
