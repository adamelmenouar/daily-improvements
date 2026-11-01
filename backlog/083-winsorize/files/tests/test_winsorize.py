import numpy as np
import pytest
from utils.winsorize import winsorize


def test_extremes_are_clipped():
    x = np.append(np.random.default_rng(83).normal(0, 1, 999), 100.0)
    assert winsorize(x).max() < 5


def test_middle_values_unchanged():
    x = np.arange(101, dtype=float)
    out = winsorize(x, 0.05, 0.95)
    assert (out[10:90] == x[10:90]).all()


def test_invalid_limits():
    with pytest.raises(ValueError):
        winsorize([1, 2, 3], 0.9, 0.1)
