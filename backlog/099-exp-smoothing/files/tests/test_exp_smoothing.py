import numpy as np
import pytest
from ts.exp_smoothing import simple_exponential_smoothing


def test_alpha_one_returns_input():
    x = np.array([1.0, 5.0, 2.0])
    assert np.array_equal(simple_exponential_smoothing(x, 1.0), x)


def test_constant_series_is_unchanged():
    assert np.allclose(simple_exponential_smoothing([3.0] * 10), 3.0)


def test_known_value():
    assert abs(simple_exponential_smoothing([10.0, 20.0], 0.5)[1] - 15.0) < 1e-12


def test_invalid_alpha():
    with pytest.raises(ValueError):
        simple_exponential_smoothing([1.0, 2.0], 0.0)
