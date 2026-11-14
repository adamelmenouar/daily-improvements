import numpy as np
import pandas as pd
from trading.supertrend import supertrend


def _ohlc(values):
    c = pd.Series(values, dtype=float)
    return c + 1, c - 1, c


def test_uptrend_then_downtrend_flips_the_direction():
    up = np.linspace(100, 200, 100)
    down = np.linspace(200, 100, 100)
    d, line = supertrend(*_ohlc(np.concatenate([up, down])))
    assert d.iloc[90] == 1 and d.iloc[-1] == -1


def test_line_is_below_price_in_an_uptrend():
    h, l, c = _ohlc(np.linspace(100, 200, 100))
    d, line = supertrend(h, l, c)
    assert (line.iloc[20:] < c.iloc[20:]).all()


def test_only_plus_or_minus_one_after_warmup():
    c = pd.Series(100 + np.cumsum(np.random.default_rng(230).normal(0, 1, 300)))
    d, _ = supertrend(c + 1, c - 1, c)
    assert set(d.dropna().unique()) <= {-1.0, 1.0}
