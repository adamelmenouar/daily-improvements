import pytest
from pricing.yield_curve import zero_rate, discount_factor, forward_rate

M, R = [1, 2, 5], [0.02, 0.03, 0.04]


def test_interpolation():
    assert abs(zero_rate(M, R, 1.5) - 0.025) < 1e-12


def test_flat_curve_forward_equals_rate():
    assert abs(forward_rate([1, 10], [0.03, 0.03], 2, 5) - 0.03) < 1e-12


def test_upward_curve_forward_above_zero_rate():
    assert forward_rate(M, R, 1, 2) > zero_rate(M, R, 2)


def test_discount_factor_below_one():
    assert 0 < discount_factor(M, R, 3) < 1


def test_invalid_interval():
    with pytest.raises(ValueError):
        forward_rate(M, R, 3, 2)
