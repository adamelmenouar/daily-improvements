import numpy as np
import pandas as pd
from trading.bollinger_indicators import percent_b, bandwidth
from trading.backtest.ma_crossover import simulate_prices


def test_percent_b_is_half_when_price_equals_its_moving_average():
    p = pd.Series([100.0, 102.0] * 30)
    pb = percent_b(p, 20)
    assert abs(pb.iloc[-1] - (p.iloc[-1] - p.rolling(20).mean().iloc[-1] + 2 * p.rolling(20).std().iloc[-1]) / (4 * p.rolling(20).std().iloc[-1])) < 1e-12


def test_bandwidth_is_positive_and_scales_with_volatility():
    calm = pd.Series(100 + np.random.default_rng(233).normal(0, 0.1, 200))
    wild = pd.Series(100 + np.random.default_rng(234).normal(0, 2.0, 200))
    assert bandwidth(wild).dropna().mean() > 10 * bandwidth(calm).dropna().mean()


def test_percent_b_length():
    assert len(percent_b(simulate_prices(100))) == 100
