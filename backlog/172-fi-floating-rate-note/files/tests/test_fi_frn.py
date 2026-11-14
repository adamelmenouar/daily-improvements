from fixedincome.frn import frn_price


def test_prices_at_par_when_discount_margin_equals_quoted_margin():
    assert abs(frn_price(100, 0.03, 0.01, 0.01, 5) - 100) < 1e-9


def test_discount_when_market_demands_a_wider_margin():
    assert frn_price(100, 0.03, 0.01, 0.02, 5) < 100


def test_premium_when_market_demands_a_narrower_margin():
    assert frn_price(100, 0.03, 0.01, 0.005, 5) > 100
