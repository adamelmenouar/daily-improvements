import numpy as np
from risk.liquidity import amihud_illiquidity, half_spread_cost


def test_less_volume_means_more_illiquid():
    r = np.array([0.01, -0.02, 0.015])
    assert amihud_illiquidity(r, np.array([1e5] * 3)) > amihud_illiquidity(r, np.array([1e7] * 3))


def test_half_spread_known_value():
    assert abs(half_spread_cost(99.0, 101.0) - 0.01) < 1e-12
