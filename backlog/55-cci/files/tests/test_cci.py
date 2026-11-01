import numpy as np
import pandas as pd
from trading.cci import cci


def test_rising_series_has_positive_cci():
    c = pd.Series(np.linspace(100, 130, 60))
    assert cci(c + 1, c - 1, c).dropna().iloc[-1] > 0


def test_length_preserved():
    c = pd.Series(np.random.default_rng(55).normal(100, 1, 80))
    assert len(cci(c + 1, c - 1, c)) == 80
