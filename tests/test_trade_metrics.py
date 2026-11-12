from trading.trade_metrics import hit_rate, profit_factor, expectancy

P = [100, -50, 200, -50, 0]


def test_hit_rate():
    assert hit_rate(P) == 0.4


def test_profit_factor():
    assert profit_factor(P) == 3.0


def test_expectancy():
    assert expectancy(P) == 40.0


def test_no_loss_gives_infinite_profit_factor():
    assert profit_factor([1, 2]) == float("inf")
