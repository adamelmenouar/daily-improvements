import pandas as pd
import pytest
from trading.backtest.ma_crossover import simulate_prices
from trading.ema_cross import ema_cross_strategy


def test_rising_market_earns_the_market_return():
    p = pd.Series([100 * 1.01**i for i in range(200)])
    r = ema_cross_strategy(p).dropna()
    assert (r.iloc[10:] - 0.01).abs().max() < 1e-12


def test_same_length_and_no_lookahead():
    p = simulate_prices(300)
    r = ema_cross_strategy(p)
    assert len(r) == 300 and pd.isna(r.iloc[0])


def test_invalid_windows():
    with pytest.raises(ValueError):
        ema_cross_strategy(simulate_prices(100), 30, 10)
