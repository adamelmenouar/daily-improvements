import numpy as np
import pandas as pd
from risk.rolling_beta import rolling_beta

M = pd.Series(np.random.default_rng(39).normal(0, 0.01, 400))


def test_scaled_market_has_constant_beta():
    b = rolling_beta(1.7 * M, M).dropna()
    assert (b - 1.7).abs().max() < 1e-9


def test_leading_values_are_nan():
    assert rolling_beta(M, M, 60).iloc[:59].isna().all()
