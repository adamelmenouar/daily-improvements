from trading.turnover import average_turnover, annual_turnover


def test_constant_position_has_no_turnover():
    assert average_turnover([1.0] * 10) == 0.0


def test_known_value():
    assert average_turnover([0, 1, 0, 1]) == 1.0


def test_annualisation():
    assert annual_turnover([0, 1, 0, 1], 252) == 252.0
