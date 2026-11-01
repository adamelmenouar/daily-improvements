import numpy as np
from portfolio.drift import drifted_weights, needs_rebalance


def test_winner_gains_weight():
    w = drifted_weights([0.5, 0.5], [0.20, 0.0])
    assert abs(w.sum() - 1) < 1e-12 and w[0] > 0.5


def test_equal_returns_leave_weights_unchanged():
    assert np.allclose(drifted_weights([0.3, 0.7], [0.05, 0.05]), [0.3, 0.7])


def test_threshold_logic():
    assert needs_rebalance([0.58, 0.42], [0.5, 0.5], 0.05)
    assert not needs_rebalance([0.52, 0.48], [0.5, 0.5], 0.05)
