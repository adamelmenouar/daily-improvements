import pandas as pd
from trading.cmf import chaikin_money_flow


def test_closing_at_the_high_every_day_gives_plus_one():
    h, l = pd.Series([11.0] * 40), pd.Series([9.0] * 40)
    assert abs(chaikin_money_flow(h, l, h, pd.Series([100.0] * 40)).iloc[-1] - 1) < 1e-12


def test_closing_at_the_low_gives_minus_one():
    h, l = pd.Series([11.0] * 40), pd.Series([9.0] * 40)
    assert abs(chaikin_money_flow(h, l, l, pd.Series([100.0] * 40)).iloc[-1] + 1) < 1e-12


def test_closing_mid_range_gives_zero():
    h, l, c = pd.Series([11.0] * 40), pd.Series([9.0] * 40), pd.Series([10.0] * 40)
    assert abs(chaikin_money_flow(h, l, c, pd.Series([100.0] * 40)).iloc[-1]) < 1e-12
