import numpy as np
import pandas as pd
from trading.keltner import keltner_channels


def _ohlc(n=200, seed=117):
    c = pd.Series(100 + np.cumsum(np.random.default_rng(seed).normal(0, 1, n)))
    return c + 1, c - 1, c


def test_channel_ordering():
    lo, mid, up = keltner_channels(*_ohlc())
    ok = lo.notna()
    assert (lo[ok] <= mid[ok]).all() and (mid[ok] <= up[ok]).all()


def test_wider_multiplier_widens_channel():
    h, l, c = _ohlc()
    a = keltner_channels(h, l, c, k=1.0)
    b = keltner_channels(h, l, c, k=3.0)
    assert (b[2] - b[0]).dropna().iloc[-1] > (a[2] - a[0]).dropna().iloc[-1]
