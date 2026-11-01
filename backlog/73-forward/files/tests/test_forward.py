from pricing.forward import forward_price, basis


def test_no_carry_equals_spot():
    assert forward_price(100, 0.0, 1.0) == 100


def test_known_value():
    assert abs(forward_price(100, 0.05, 1.0) - 105.1271) < 1e-3


def test_dividends_lower_the_forward():
    assert forward_price(100, 0.05, 1, dividend_yield=0.03) < forward_price(100, 0.05, 1)


def test_contango_basis_negative():
    assert basis(100, forward_price(100, 0.05, 1)) < 0
