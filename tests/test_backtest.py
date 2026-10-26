import pytest
from trading.backtest.ma_crossover import simulate_prices, backtest, sharpe


def test_flat_before_slow_window_is_filled():
    r = backtest(simulate_prices(200))
    assert r.iloc[:50].fillna(0).abs().sum() == 0


def test_invalid_windows():
    with pytest.raises(ValueError):
        backtest(simulate_prices(100), fast=50, slow=20)


def test_sharpe_is_finite():
    assert abs(sharpe(backtest(simulate_prices()))) < 10
