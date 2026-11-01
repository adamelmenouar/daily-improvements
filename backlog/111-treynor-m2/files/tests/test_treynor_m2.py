import numpy as np
from risk.treynor_m2 import treynor_ratio, modigliani_m2

M = np.random.default_rng(113).normal(0.0004, 0.01, 2000)


def test_treynor_of_the_market_is_its_excess_return():
    assert abs(treynor_ratio(M, M) - M.mean() * 252) < 1e-9


def test_m2_of_the_market_is_the_market_return():
    assert abs(modigliani_m2(M, M) - M.mean() * 252) < 1e-9


def test_leveraging_does_not_change_m2():
    assert abs(modigliani_m2(2 * M, M) - modigliani_m2(M, M)) < 1e-9
