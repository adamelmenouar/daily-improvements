import numpy as np
import pandas as pd
from trading.aroon import aroon


def test_uptrend_gives_plus_100_oscillator():
    c = pd.Series(np.linspace(100, 200, 80))
    up, down, osc = aroon(c + 1, c - 1)
    assert up.iloc[-1] == 100 and down.iloc[-1] == 0 and osc.iloc[-1] == 100


def test_downtrend_gives_minus_100_oscillator():
    c = pd.Series(np.linspace(200, 100, 80))
    assert aroon(c + 1, c - 1)[2].iloc[-1] == -100


def test_bounds():
    c = pd.Series(100 + np.cumsum(np.random.default_rng(231).normal(0, 1, 300)))
    up, down, _ = aroon(c + 1, c - 1)
    assert up.dropna().between(0, 100).all() and down.dropna().between(0, 100).all()
