import numpy as np
from portfolio.michaud import resampled_tangency
from portfolio.tangency import tangency_weights

MU = np.array([0.06, 0.09, 0.12])
COV = np.array([[0.04, 0.006, 0.0], [0.006, 0.09, 0.01], [0.0, 0.01, 0.16]])


def test_weights_sum_to_one():
    assert abs(resampled_tangency(MU, COV, 100, 0.02).sum() - 1) < 1e-9


def test_converges_to_the_plain_tangency_with_an_enormous_sample():
    assert np.allclose(resampled_tangency(MU, COV, 1e9, 0.02, 200), tangency_weights(MU, COV, 0.02), atol=0.01)


def test_reproducible():
    assert np.array_equal(resampled_tangency(MU, COV, 50, 0.02, 100, seed=3), resampled_tangency(MU, COV, 50, 0.02, 100, seed=3))
