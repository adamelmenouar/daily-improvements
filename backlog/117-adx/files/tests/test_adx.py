import numpy as np
import pandas as pd
from trading.adx import adx


def test_clean_uptrend_gives_very_high_adx():
    c = pd.Series(np.arange(1, 200, dtype=float))
    plus, minus, a = adx(c + 0.5, c - 0.5, c)
    assert a.iloc[-1] > 90 and plus.iloc[-1] > minus.iloc[-1]


def test_bounds_on_a_random_walk():
    c = pd.Series(100 + np.cumsum(np.random.default_rng(118).normal(0, 1, 500)))
    _, _, a = adx(c + 0.5, c - 0.5, c)
    assert a.dropna().between(0, 100).all()
