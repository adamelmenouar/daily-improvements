import pandas as pd
from trading.obv import on_balance_volume


def test_known_values():
    close = pd.Series([10, 11, 11, 10, 12])
    vol = pd.Series([100, 200, 300, 400, 500])
    assert on_balance_volume(close, vol).tolist() == [0, 200, 200, -200, 300]


def test_flat_prices_give_zero():
    assert (on_balance_volume(pd.Series([5.0] * 4), pd.Series([1, 2, 3, 4])) == 0).all()
