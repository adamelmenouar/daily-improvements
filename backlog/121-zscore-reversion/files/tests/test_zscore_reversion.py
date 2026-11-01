import numpy as np
import pandas as pd
from trading.backtest.ma_crossover import simulate_prices
from trading.zscore_reversion import zscore_reversion


def test_no_position_before_the_window_is_full():
    r = zscore_reversion(simulate_prices(200), window=20)
    assert r.iloc[:20].fillna(0).abs().sum() == 0


def test_profits_on_a_strongly_mean_reverting_price():
    rng = np.random.default_rng(120)
    x = np.zeros(3000)
    for t in range(1, 3000):
        x[t] = 0.8 * x[t - 1] + rng.normal()
    p = pd.Series(100 + x * 0.1)
    assert zscore_reversion(p, 30, 1.0, 0.0).sum() > 0
