import numpy as np
from portfolio.partial_rebalance import partial_rebalance

W, T = np.array([0.7, 0.3]), np.array([0.5, 0.5])


def test_small_move_goes_all_the_way():
    assert np.allclose(partial_rebalance(W, T, 0.5), T)


def test_cap_binds_and_turnover_equals_the_cap():
    out = partial_rebalance(W, T, 0.1)
    assert abs(0.5 * np.abs(out - W).sum() - 0.1) < 1e-12 and abs(out.sum() - 1) < 1e-12


def test_moves_toward_the_target():
    out = partial_rebalance(W, T, 0.1)
    assert abs(out[0] - 0.5) < abs(W[0] - 0.5)
