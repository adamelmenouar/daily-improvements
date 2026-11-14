import numpy as np
from portfolio.diversification import diversification_ratio
from portfolio.max_diversification import max_diversification_weights

S = np.array([0.15, 0.20, 0.30])
RHO = np.array([[1, 0.3, 0.2], [0.3, 1, 0.4], [0.2, 0.4, 1]])
COV = np.outer(S, S) * RHO


def test_weights_sum_to_one():
    assert abs(max_diversification_weights(COV).sum() - 1) < 1e-12


def test_beats_equal_weight_and_random_portfolios():
    w = max_diversification_weights(COV)
    best = diversification_ratio(w, COV)
    assert best >= diversification_ratio(np.ones(3) / 3, COV)
    rng = np.random.default_rng(237)
    assert all(best >= diversification_ratio(rng.dirichlet(np.ones(3)), COV) - 1e-9 for _ in range(300))
