import numpy as np
from portfolio.mv_utility import mean_variance_weights, utility

MU = np.array([0.06, 0.09])
COV = np.array([[0.04, 0.006], [0.006, 0.09]])


def test_optimum_beats_random_perturbations():
    w = mean_variance_weights(MU, COV, 4.0)
    rng = np.random.default_rng(137)
    best = utility(w, MU, COV, 4.0)
    assert all(best >= utility(w + rng.normal(0, 0.1, 2), MU, COV, 4.0) for _ in range(200))


def test_more_risk_aversion_means_smaller_positions():
    assert np.abs(mean_variance_weights(MU, COV, 8.0)).sum() < np.abs(mean_variance_weights(MU, COV, 2.0)).sum()
