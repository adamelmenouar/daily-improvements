from math import exp
from pricing.kirk import kirk_spread_call
from pricing.margrabe import margrabe_exchange


def test_zero_strike_is_the_discounted_margrabe_price():
    assert abs(kirk_spread_call(100, 98, 1e-9, 1.0, 0.03, 0.3, 0.25, 0.6)
               - exp(-0.03) * margrabe_exchange(100, 98, 1.0, 0.3, 0.25, 0.6)) < 1e-6


def test_higher_strike_means_cheaper_option():
    assert kirk_spread_call(100, 90, 5, 1, 0.03, 0.3, 0.25, 0.5) < kirk_spread_call(100, 90, 1, 1, 0.03, 0.3, 0.25, 0.5)


def test_price_is_positive():
    assert kirk_spread_call(100, 95, 3, 0.5, 0.02, 0.2, 0.2, 0.7) > 0
