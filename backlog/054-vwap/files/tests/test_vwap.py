import pandas as pd
from trading.vwap import vwap


def test_constant_price():
    assert (vwap(pd.Series([50.0] * 5), pd.Series([1, 2, 3, 4, 5])) == 50.0).all()


def test_known_value():
    v = vwap(pd.Series([10.0, 20.0]), pd.Series([1, 3]))
    assert abs(v.iloc[-1] - 17.5) < 1e-12
