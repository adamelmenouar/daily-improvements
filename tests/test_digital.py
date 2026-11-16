from math import exp
from pricing.black_scholes import bs_call
from pricing.digital import digital_call, digital_put


def test_call_plus_put_is_discounted_cash():
    assert abs(digital_call(100, 100, 1, 0.05, 0.2, 10) + digital_put(100, 100, 1, 0.05, 0.2, 10)
               - 10 * exp(-0.05)) < 1e-12


def test_digital_call_is_minus_derivative_of_vanilla_wrt_strike():
    h = 1e-4
    fd = -(bs_call(100, 100 + h, 1, 0.05, 0.2) - bs_call(100, 100 - h, 1, 0.05, 0.2)) / (2 * h)
    assert abs(digital_call(100, 100, 1, 0.05, 0.2) - fd) < 1e-6
