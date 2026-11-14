import pandas as pd
from trading.trix import trix


def test_constant_price_gives_zero():
    assert trix(pd.Series([100.0] * 100)).dropna().abs().max() < 1e-12


def test_rising_prices_give_positive_values_and_falling_negative():
    assert trix(pd.Series([100 * 1.01**i for i in range(200)])).iloc[-1] > 0
    assert trix(pd.Series([100 * 0.99**i for i in range(200)])).iloc[-1] < 0
