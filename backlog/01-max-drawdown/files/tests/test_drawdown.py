import numpy as np
from risk.drawdown import max_drawdown, drawdown_series


def test_known_value():
    # +10% puis -20% : equity 1.1 -> 0.88, drawdown = -20%
    assert abs(max_drawdown([0.10, -0.20]) - (-0.20)) < 1e-12


def test_monotonic_gain_has_zero_drawdown():
    assert max_drawdown([0.01] * 10) == 0.0


def test_never_positive():
    r = np.random.default_rng(0).normal(0, 0.01, 500)
    assert (drawdown_series(r) <= 0).all()
