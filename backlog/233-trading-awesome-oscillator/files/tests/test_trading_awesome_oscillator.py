import numpy as np
import pandas as pd
from trading.awesome_oscillator import awesome_oscillator


def test_constant_market_gives_zero():
    s = pd.Series([50.0] * 80)
    assert awesome_oscillator(s, s).dropna().abs().max() < 1e-12


def test_uptrend_positive_downtrend_negative():
    up = pd.Series(np.linspace(100, 200, 100))
    assert awesome_oscillator(up + 1, up - 1).iloc[-1] > 0
    assert awesome_oscillator(up[::-1].reset_index(drop=True) + 1, up[::-1].reset_index(drop=True) - 1).iloc[-1] < 0


def test_leading_values_are_nan():
    assert awesome_oscillator(pd.Series(range(60), dtype=float), pd.Series(range(60), dtype=float)).iloc[:33].isna().all()
