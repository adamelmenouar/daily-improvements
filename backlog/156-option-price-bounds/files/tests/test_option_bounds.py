from pricing.black_scholes import bs_call
from pricing.option_bounds import call_bounds, violates_bounds


def test_black_scholes_prices_respect_the_bounds():
    for k in (60, 100, 140):
        assert not violates_bounds(bs_call(100, k, 1, 0.05, 0.3), 100, k, 1, 0.05)


def test_arbitrage_is_flagged():
    assert violates_bounds(5.0, 100, 90, 1, 0.05)       # moins que la valeur intrinsèque actualisée
    assert violates_bounds(120.0, 100, 90, 1, 0.05)     # plus que le sous-jacent


def test_deep_otm_lower_bound_is_zero():
    assert call_bounds(50, 100, 1, 0.05)[0] == 0.0
