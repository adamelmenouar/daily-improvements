from fixedincome.tbill import discount_yield, bond_equivalent_yield, price_from_discount_yield


def test_known_values():
    assert abs(discount_yield(100, 99, 90) - 0.04) < 1e-12
    assert abs(bond_equivalent_yield(100, 99, 90) - (1 / 99) * 365 / 90) < 1e-12


def test_price_round_trip():
    p = price_from_discount_yield(100, 0.04, 90)
    assert abs(discount_yield(100, p, 90) - 0.04) < 1e-12


def test_bey_exceeds_discount_yield():
    assert bond_equivalent_yield(100, 98.5, 120) > discount_yield(100, 98.5, 120)
