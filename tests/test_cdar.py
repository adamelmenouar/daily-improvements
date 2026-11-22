import numpy as np
from risk.cdar import cdar
from risk.drawdown import max_drawdown

R = np.random.default_rng(111).normal(0.0003, 0.01, 2000)


def test_between_quantile_and_max_drawdown():
    assert 0 < cdar(R, 0.9) <= abs(max_drawdown(R)) + 1e-12


def test_higher_alpha_means_deeper_average():
    assert cdar(R, 0.99) >= cdar(R, 0.9)


def test_rising_market_has_zero_cdar():
    assert cdar([0.01] * 50) == 0.0
