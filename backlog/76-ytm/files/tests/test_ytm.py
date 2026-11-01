from pricing.bond import bond_price
from pricing.ytm import yield_to_maturity


def test_round_trip():
    p = bond_price(100, 0.04, 0.065, 8)
    assert abs(yield_to_maturity(p, 100, 0.04, 8) - 0.065) < 1e-9


def test_par_bond_yields_its_coupon():
    assert abs(yield_to_maturity(100, 100, 0.05, 10) - 0.05) < 1e-9


def test_discount_bond_yields_more_than_coupon():
    assert yield_to_maturity(90, 100, 0.05, 10) > 0.05
