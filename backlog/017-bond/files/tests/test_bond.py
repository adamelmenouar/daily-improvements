from pricing.bond import bond_price, macaulay_duration, modified_duration


def test_par_bond_prices_at_face():
    assert abs(bond_price(100, 0.05, 0.05, 10) - 100) < 1e-9


def test_zero_coupon_duration_equals_maturity():
    assert abs(macaulay_duration(100, 0.0, 0.04, 7) - 7) < 1e-9


def test_price_falls_when_yield_rises():
    assert bond_price(100, 0.05, 0.06, 10) < bond_price(100, 0.05, 0.04, 10)


def test_duration_predicts_price_move():
    p0, p1 = bond_price(100, 0.05, 0.05, 10), bond_price(100, 0.05, 0.0501, 10)
    approx = -modified_duration(100, 0.05, 0.05, 10) * 0.0001 * p0
    assert abs((p1 - p0) - approx) < 1e-3
