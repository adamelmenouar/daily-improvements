import numpy as np
from trading.ratios import sortino, calmar


def test_sortino_infinite_without_losses():
    assert sortino([0.01, 0.02, 0.0]) == float("inf")


def test_sortino_positive_for_drifting_series():
    r = np.random.default_rng(3).normal(0.001, 0.01, 1000)
    assert sortino(r) > 0


def test_calmar_sign():
    r = np.random.default_rng(3).normal(0.001, 0.01, 1000)
    assert calmar(r) > 0
