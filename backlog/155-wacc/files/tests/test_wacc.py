from pricing.wacc import cost_of_equity, wacc


def test_capm_known_value():
    assert abs(cost_of_equity(0.03, 1.2, 0.05) - 0.09) < 1e-12


def test_wacc_known_value():
    assert abs(wacc(600, 400, 0.10, 0.05, 0.25) - (0.6 * 0.10 + 0.4 * 0.05 * 0.75)) < 1e-12


def test_all_equity_wacc_is_the_cost_of_equity():
    assert wacc(1000, 0, 0.09, 0.05, 0.3) == 0.09


def test_tax_shield_lowers_wacc():
    assert wacc(500, 500, 0.1, 0.06, 0.3) < wacc(500, 500, 0.1, 0.06, 0.0)
