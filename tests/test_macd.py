import pandas as pd
from trading.backtest.ma_crossover import simulate_prices
from trading.macd import macd


def test_constant_price_gives_zero_macd():
    line, sig, hist = macd(pd.Series([100.0] * 100))
    assert line.abs().max() < 1e-12 and hist.abs().max() < 1e-12


def test_histogram_is_line_minus_signal():
    line, sig, hist = macd(simulate_prices(200))
    assert (hist - (line - sig)).abs().max() < 1e-12
