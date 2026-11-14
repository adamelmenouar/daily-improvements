from fixedincome.fisher import real_rate, breakeven_inflation


def test_known_value():
    assert abs(real_rate(0.05, 0.02) - (1.05 / 1.02 - 1)) < 1e-15


def test_round_trip():
    r = real_rate(0.045, 0.025)
    assert abs(breakeven_inflation(0.045, r) - 0.025) < 1e-12


def test_inflation_above_nominal_gives_negative_real_rate():
    assert real_rate(0.02, 0.05) < 0
