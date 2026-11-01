import numpy as np
import pytest
from risk.shrinkage import shrunk_covariance

X = np.random.default_rng(13).normal(0, 0.01, (200, 4))


def test_delta_zero_is_sample_covariance():
    assert np.allclose(shrunk_covariance(X, 0), np.cov(X, rowvar=False))


def test_shrinkage_improves_conditioning():
    assert np.linalg.cond(shrunk_covariance(X, 0.5)) <= np.linalg.cond(shrunk_covariance(X, 0))


def test_invalid_delta():
    with pytest.raises(ValueError):
        shrunk_covariance(X, 2)
