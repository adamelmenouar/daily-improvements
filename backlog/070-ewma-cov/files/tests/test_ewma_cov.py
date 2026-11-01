import numpy as np
from portfolio.ewma_cov import ewma_covariance

X = np.random.default_rng(70).multivariate_normal([0, 0], [[1e-4, 5e-5], [5e-5, 4e-4]], 5000)


def test_symmetric_positive_semidefinite():
    c = ewma_covariance(X)
    assert np.allclose(c, c.T) and np.linalg.eigvalsh(c).min() >= -1e-15


def test_close_to_true_covariance_with_slow_decay():
    c = ewma_covariance(X, lam=0.995)
    assert abs(c[0, 0] - 1e-4) < 4e-5 and abs(c[1, 1] - 4e-4) < 1.6e-4
