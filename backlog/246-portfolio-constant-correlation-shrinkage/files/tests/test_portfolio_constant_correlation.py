import numpy as np
import pytest
from portfolio.constant_correlation import constant_correlation_covariance

X = np.random.default_rng(239).multivariate_normal([0] * 4, np.diag([1e-4, 2e-4, 3e-4, 4e-4]) + 5e-5, 300)


def test_delta_zero_is_the_sample_covariance():
    assert np.allclose(constant_correlation_covariance(X, 0), np.cov(X, rowvar=False))


def test_variances_are_preserved_and_matrix_is_valid():
    c = constant_correlation_covariance(X, 0.5)
    assert np.allclose(np.diag(c), np.diag(np.cov(X, rowvar=False))) and np.linalg.eigvalsh(c).min() > 0


def test_full_shrinkage_gives_one_common_correlation():
    c = constant_correlation_covariance(X, 1.0)
    sd = np.sqrt(np.diag(c))
    off = (c / np.outer(sd, sd))[np.triu_indices(4, 1)]
    assert np.allclose(off, off[0])


def test_invalid_delta():
    with pytest.raises(ValueError):
        constant_correlation_covariance(X, -0.1)
