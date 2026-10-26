from pricing.black_scholes import bs_call
from pricing.greeks import call_delta, gamma, vega

ARGS = (100, 100, 1, 0.05, 0.2)


def test_delta_matches_finite_difference():
    h = 1e-4
    fd = (bs_call(100 + h, 100, 1, 0.05, 0.2) - bs_call(100 - h, 100, 1, 0.05, 0.2)) / (2 * h)
    assert abs(call_delta(*ARGS) - fd) < 1e-6


def test_vega_matches_finite_difference():
    h = 1e-5
    fd = (bs_call(100, 100, 1, 0.05, 0.2 + h) - bs_call(100, 100, 1, 0.05, 0.2 - h)) / (2 * h)
    assert abs(vega(*ARGS) - fd) < 1e-4


def test_gamma_positive():
    assert gamma(*ARGS) > 0
