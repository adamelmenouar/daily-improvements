import numpy as np
import pandas as pd
from trading.stochastic import stochastic


def _ohlc(n=200, seed=52):
    c = pd.Series(100 + np.cumsum(np.random.default_rng(seed).normal(0, 1, n)))
    return c + 0.5, c - 0.5, c


def test_bounds():
    h, l, c = _ohlc()
    k, d = stochastic(h, l, c)
    assert (k.dropna().between(0, 100)).all()


def test_close_at_top_of_range_gives_high_reading():
    h = pd.Series(range(1, 30), dtype=float)
    k, _ = stochastic(h, h - 1, h, k_window=5)
    assert k.dropna().iloc[-1] > 75
