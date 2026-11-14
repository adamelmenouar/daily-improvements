from pricing.black_scholes import bs_call
from pricing.margrabe import margrabe_exchange


def test_reduces_to_a_black_scholes_call_when_the_second_asset_is_riskless():
    assert abs(margrabe_exchange(100, 95, 1.0, 0.2, 0.0, 0.0) - bs_call(100, 95, 1.0, 0.0, 0.2)) < 1e-10


def test_higher_correlation_makes_the_option_cheaper():
    assert margrabe_exchange(100, 100, 1, 0.3, 0.25, 0.9) < margrabe_exchange(100, 100, 1, 0.3, 0.25, 0.1)


def test_deep_out_of_the_money_is_nearly_worthless():
    assert margrabe_exchange(50, 200, 0.5, 0.2, 0.2, 0.3) < 1e-6
