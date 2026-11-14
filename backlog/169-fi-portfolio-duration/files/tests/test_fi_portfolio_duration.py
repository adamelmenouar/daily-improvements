from fixedincome.portfolio_duration import portfolio_duration, portfolio_dv01


def test_equal_values_average_the_durations():
    assert portfolio_duration([100, 100], [2.0, 6.0]) == 4.0


def test_weighting_by_market_value():
    assert abs(portfolio_duration([300, 100], [2.0, 6.0]) - 3.0) < 1e-12


def test_dv01_known_value():
    assert abs(portfolio_dv01([1_000_000], [5.0]) - 500.0) < 1e-9
