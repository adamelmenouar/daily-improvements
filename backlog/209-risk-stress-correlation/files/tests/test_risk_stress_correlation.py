import numpy as np
import pytest
from risk.stress_correlation import stress_correlation

C = np.array([[1, 0.2, -0.3], [0.2, 1, 0.5], [-0.3, 0.5, 1]])


def test_extremes():
    assert np.allclose(stress_correlation(C, 0), C) and np.allclose(stress_correlation(C, 1), 1)


def test_correlations_increase_and_stay_valid():
    s = stress_correlation(C, 0.5)
    assert (s >= C - 1e-12).all() and np.allclose(np.diag(s), 1) and np.linalg.eigvalsh(s).min() > -1e-12


def test_invalid_intensity():
    with pytest.raises(ValueError):
        stress_correlation(C, 1.5)
