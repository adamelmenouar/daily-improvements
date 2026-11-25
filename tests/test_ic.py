import numpy as np
from trading.information_coefficient import information_coefficient


def test_monotone_relation_gives_one():
    x = np.arange(100.0)
    assert abs(information_coefficient(x, x**3) - 1) < 1e-12


def test_inverse_relation_gives_minus_one():
    x = np.arange(100.0)
    assert abs(information_coefficient(x, -x) + 1) < 1e-12


def test_independent_signal_is_near_zero():
    rng = np.random.default_rng(125)
    assert abs(information_coefficient(rng.normal(size=5000), rng.normal(size=5000))) < 0.05
