import numpy as np
from portfolio.frontier import min_variance_for_target
from portfolio.minvar import min_variance_weights

MU = np.array([0.06, 0.09, 0.12])
COV = np.array([[0.04, 0.006, 0.0], [0.006, 0.09, 0.01], [0.0, 0.01, 0.16]])


def test_constraints_hold():
    w = min_variance_for_target(MU, COV, 0.09)
    assert abs(w.sum() - 1) < 1e-10 and abs(w @ MU - 0.09) < 1e-10


def test_variance_is_at_least_global_minimum():
    wg = min_variance_weights(COV)
    w = min_variance_for_target(MU, COV, 0.11)
    assert w @ COV @ w >= wg @ COV @ wg - 1e-12


def test_higher_target_means_higher_variance_above_minimum():
    lo = min_variance_for_target(MU, COV, 0.10)
    hi = min_variance_for_target(MU, COV, 0.12)
    assert hi @ COV @ hi > lo @ COV @ lo
