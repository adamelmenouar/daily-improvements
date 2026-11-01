import numpy as np
import pandas as pd
from risk.rolling_var import rolling_var

R = pd.Series(np.random.default_rng(34).normal(0, 0.01, 1000))


def test_first_values_are_nan():
    assert rolling_var(R, 100).iloc[:99].isna().all()


def test_values_positive_and_plausible():
    v = rolling_var(R, 250).dropna()
    assert (v > 0).all() and abs(v.mean() - 0.0165) < 0.004
