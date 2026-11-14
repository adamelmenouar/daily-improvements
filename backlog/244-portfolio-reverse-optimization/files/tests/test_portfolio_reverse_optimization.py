import numpy as np
from portfolio.mv_utility import mean_variance_weights
from portfolio.reverse_optimization import implied_returns

COV = np.array([[0.04, 0.006, 0.0], [0.006, 0.09, 0.01], [0.0, 0.01, 0.16]])
W = np.array([0.5, 0.3, 0.2])


def test_round_trip_with_the_mean_variance_optimizer():
    pi = implied_returns(W, COV, 3.5)
    assert np.allclose(mean_variance_weights(pi, COV, 3.5), W)


def test_riskier_assets_get_higher_implied_returns():
    pi = implied_returns(np.ones(3) / 3, COV)
    assert pi[2] > pi[0]
