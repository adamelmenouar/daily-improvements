import pytest
from risk.var_scaling import scale_var


def test_ten_day_var():
    assert abs(scale_var(0.02, 10) - 0.02 * 10**0.5) < 1e-12


def test_one_day_is_identity():
    assert scale_var(0.02, 1) == 0.02


def test_invalid_horizon():
    with pytest.raises(ValueError):
        scale_var(0.02, 0)
