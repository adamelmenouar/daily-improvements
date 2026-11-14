from execution.shortfall import implementation_shortfall_bps


def test_buying_above_the_decision_price_costs_money():
    assert abs(implementation_shortfall_bps(100.0, [100.1, 100.3], [500, 500]) - 20.0) < 1e-9


def test_selling_below_the_decision_price_costs_money():
    assert implementation_shortfall_bps(100.0, [99.8], [100], side="sell") > 0


def test_price_improvement_is_negative_cost():
    assert implementation_shortfall_bps(100.0, [99.9], [100], side="buy") < 0
