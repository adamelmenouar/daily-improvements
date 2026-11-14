import pytest
from pricing.black_scholes import bs_call
from pricing.forward_start import forward_start_call


def test_alpha_one_scales_with_the_spot():
    assert abs(forward_start_call(250, 1.0, 1.0, 2.0, 0.03, 0.2) - 250 * bs_call(1, 1, 1.0, 0.03, 0.2)) < 1e-12


def test_only_the_length_of_the_forward_period_matters():
    assert abs(forward_start_call(100, 1.0, 0.0, 1.0, 0.03, 0.2) - forward_start_call(100, 1.0, 3.0, 4.0, 0.03, 0.2)) < 1e-12


def test_higher_strike_percentage_is_cheaper():
    assert forward_start_call(100, 1.1, 1, 2, 0.03, 0.2) < forward_start_call(100, 0.9, 1, 2, 0.03, 0.2)


def test_invalid_dates():
    with pytest.raises(ValueError):
        forward_start_call(100, 1.0, 2.0, 1.0, 0.03, 0.2)
