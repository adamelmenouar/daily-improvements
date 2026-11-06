from pricing.binomial import crr_price
from pricing.black_scholes import bs_call, bs_put


def test_converges_to_black_scholes():
    assert abs(crr_price(100, 100, 1, 0.05, 0.2, steps=500) - bs_call(100, 100, 1, 0.05, 0.2)) < 0.03
    assert abs(crr_price(100, 105, 1, 0.05, 0.2, 500, "put") - bs_put(100, 105, 1, 0.05, 0.2)) < 0.03


def test_american_put_worth_at_least_european():
    eu = crr_price(100, 110, 1, 0.05, 0.2, 300, "put")
    am = crr_price(100, 110, 1, 0.05, 0.2, 300, "put", american=True)
    assert am >= eu
