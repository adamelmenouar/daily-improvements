import pandas as pd
from trading.volatility_breakout import volatility_breakout_returns


def test_known_day():
    o = pd.Series([100.0, 100.0])
    h = pd.Series([104.0, 108.0])
    l = pd.Series([96.0, 99.0])
    c = pd.Series([100.0, 107.0])
    r = volatility_breakout_returns(o, h, l, c, k=0.5)
    assert r.iloc[0] == 0.0  # pas de veille -> pas de signal
    assert abs(r.iloc[1] - (107 / 104 - 1)) < 1e-12  # déclencheur = 100 + 0.5 * 8 = 104


def test_no_trade_when_the_trigger_is_not_reached():
    o = pd.Series([100.0, 100.0])
    h = pd.Series([110.0, 101.0])
    l = pd.Series([90.0, 99.0])
    assert volatility_breakout_returns(o, h, l, o, 0.5).iloc[1] == 0.0
