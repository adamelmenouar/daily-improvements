import numpy as np
import pandas as pd
from trading.roc_williams import roc, williams_r


def test_roc_known_value():
    p = pd.Series([100.0, 105.0, 110.0])
    assert abs(roc(p, 2).iloc[-1] - 0.10) < 1e-12


def test_williams_bounds():
    c = pd.Series(100 + np.cumsum(np.random.default_rng(56).normal(0, 1, 200)))
    w = williams_r(c + 0.5, c - 0.5, c).dropna()
    assert w.between(-100, 0).all()
