import numpy as np
import pandas as pd
from trading.mfi import money_flow_index


def test_bounds_on_a_random_walk():
    rng = np.random.default_rng(232)
    c = pd.Series(100 + np.cumsum(rng.normal(0, 1, 400)))
    v = pd.Series(rng.uniform(1e3, 1e4, 400))
    m = money_flow_index(c + 1, c - 1, c, v).dropna()
    assert m.between(0, 100).all()


def test_strong_buying_pushes_it_high_and_selling_low():
    v = pd.Series([1000.0] * 60)
    up = pd.Series(np.linspace(100, 160, 60))
    down = pd.Series(np.linspace(160, 100, 60))
    assert money_flow_index(up + 1, up - 1, up, v).iloc[-1] > 90
    assert money_flow_index(down + 1, down - 1, down, v).iloc[-1] < 10
