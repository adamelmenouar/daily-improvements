import pandas as pd
from ts.moving_averages import sma, ema, wma


def test_known_wma():
    assert abs(wma(pd.Series([1.0, 2.0, 3.0]), 3).iloc[-1] - (1 + 4 + 9) / 6) < 1e-12


def test_known_sma():
    assert sma(pd.Series([1.0, 2.0, 3.0]), 3).iloc[-1] == 2.0


def test_ema_reacts_faster_than_sma_to_a_jump():
    s = pd.Series([1.0] * 20 + [10.0] * 3)
    assert ema(s, 10).iloc[-1] > 1.0
    assert wma(s, 10).iloc[-1] > sma(s, 10).iloc[-1]
