import pandas as pd
from trading.heikin_ashi import heikin_ashi


def test_flat_market_is_unchanged():
    s = pd.Series([100.0] * 5)
    out = heikin_ashi(s, s, s, s)
    assert (out == 100.0).all().all()


def test_high_low_bracket_open_and_close():
    o = pd.Series([10.0, 11.0, 12.0])
    c = pd.Series([11.0, 12.0, 11.5])
    out = heikin_ashi(o, c + 0.5, o - 0.5, c)
    assert (out["high"] >= out[["open", "close"]].max(axis=1)).all()
    assert (out["low"] <= out[["open", "close"]].min(axis=1)).all()
