import numpy as np
import pandas as pd
from utils.rolling_stats import rolling_zscore, rolling_skew


def test_known_zscore():
    assert abs(rolling_zscore(pd.Series([1.0, 2.0, 3.0]), 3).iloc[-1] - 1.0) < 1e-12


def test_zscore_leading_nan():
    assert rolling_zscore(pd.Series(range(30), dtype=float), 10).iloc[:9].isna().all()


def test_skew_of_symmetric_data_near_zero():
    s = pd.Series(np.random.default_rng(89).normal(size=5000))
    assert abs(rolling_skew(s, 1000).dropna().mean()) < 0.1
