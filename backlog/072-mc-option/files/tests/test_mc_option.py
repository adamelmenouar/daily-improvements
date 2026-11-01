from pricing.black_scholes import bs_call
from pricing.mc_option import mc_call


def test_matches_black_scholes_within_error():
    price, se = mc_call(100, 100, 1, 0.05, 0.2)
    assert abs(price - bs_call(100, 100, 1, 0.05, 0.2)) < 4 * se


def test_reproducible():
    assert mc_call(100, 100, 1, 0.05, 0.2) == mc_call(100, 100, 1, 0.05, 0.2)
