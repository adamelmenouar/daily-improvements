import numpy as np
import pandas as pd
from trading.ichimoku import ichimoku


def test_constant_price_collapses_every_line_to_the_price():
    s = pd.Series([100.0] * 120)
    out = ichimoku(s, s)
    assert (out.dropna() == 100.0).all().all()


def test_tenkan_reacts_faster_than_kijun_in_an_uptrend():
    c = pd.Series(np.linspace(100, 200, 120))
    out = ichimoku(c + 1, c - 1)
    assert (out["tenkan"].dropna().iloc[-20:] > out["kijun"].dropna().iloc[-20:]).all()


def test_cloud_is_shifted_forward_in_time():
    c = pd.Series(np.linspace(100, 200, 120))
    out = ichimoku(c + 1, c - 1)
    assert out["senkou_a"].iloc[:26].isna().all()
