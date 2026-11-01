import pandas as pd
from trading.backtest.ma_crossover import simulate_prices
from trading.momentum import momentum_strategy


def test_no_position_before_lookback():
    r = momentum_strategy(simulate_prices(300), lookback=60)
    assert r.iloc[:61].fillna(0).abs().sum() == 0


def test_rising_prices_earn_the_market_return():
    p = pd.Series([100 * 1.01**i for i in range(200)])
    r = momentum_strategy(p, lookback=20).dropna()
    assert (r.iloc[-50:] - 0.01).abs().max() < 1e-12
