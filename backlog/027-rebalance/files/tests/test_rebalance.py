import numpy as np
from portfolio.rebalance import rebalance_trades, turnover


def test_trades_are_self_financing():
    t = rebalance_trades([700, 200, 100], [1 / 3, 1 / 3, 1 / 3])
    assert abs(t.sum()) < 1e-9


def test_already_on_target_means_no_trade():
    assert turnover([50, 50], [0.5, 0.5]) == 0.0
    assert np.allclose(rebalance_trades([50, 50], [0.5, 0.5]), 0)


def test_turnover_known_value():
    assert abs(turnover([80, 20], [0.5, 0.5]) - 0.3) < 1e-12
