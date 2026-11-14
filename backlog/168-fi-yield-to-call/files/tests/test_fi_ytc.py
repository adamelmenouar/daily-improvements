from pricing.bond import bond_price
from pricing.ytm import yield_to_maturity
from fixedincome.ytc import yield_to_call


def test_call_at_par_equals_ytm_to_the_call_date():
    p = bond_price(100, 0.06, 0.05, 5)
    assert abs(yield_to_call(p, 100, 0.06, 5, 100) - yield_to_maturity(p, 100, 0.06, 5)) < 1e-9


def test_premium_bond_has_lower_ytc_than_ytm_to_final_maturity():
    p = 110.0
    assert yield_to_call(p, 100, 0.08, 5, 100) < yield_to_maturity(p, 100, 0.08, 15)


def test_higher_call_price_means_higher_yield():
    assert yield_to_call(105, 100, 0.06, 5, 110) > yield_to_call(105, 100, 0.06, 5, 100)
