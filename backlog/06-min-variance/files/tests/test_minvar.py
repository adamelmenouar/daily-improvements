import numpy as np
from portfolio.minvar import min_variance_weights, portfolio_volatility

COV = np.array([[0.04, 0.006, 0.0], [0.006, 0.09, 0.01], [0.0, 0.01, 0.16]])


def test_weights_sum_to_one():
    assert abs(min_variance_weights(COV).sum() - 1) < 1e-12


def test_beats_equal_weight():
    w = min_variance_weights(COV)
    assert portfolio_volatility(w, COV) <= portfolio_volatility(np.ones(3) / 3, COV)
