import numpy as np
from portfolio.tangency import tangency_weights, sharpe_ratio

MU = np.array([0.08, 0.10, 0.12])
COV = np.array([[0.04, 0.006, 0.0], [0.006, 0.09, 0.01], [0.0, 0.01, 0.16]])


def test_weights_sum_to_one():
    assert abs(tangency_weights(MU, COV, 0.02).sum() - 1) < 1e-12


def test_beats_equal_weight_and_random_portfolios():
    w = tangency_weights(MU, COV, 0.02)
    best = sharpe_ratio(w, MU, COV, 0.02)
    assert best >= sharpe_ratio(np.ones(3) / 3, MU, COV, 0.02)
    rng = np.random.default_rng(26)
    for _ in range(200):
        x = rng.dirichlet(np.ones(3))
        assert best >= sharpe_ratio(x, MU, COV, 0.02) - 1e-12
