import numpy as np
import pandas as pd
from trading.pairs import spread, zscore, pairs_signal


def test_signal_values_and_hysteresis():
    z = pd.Series([0.0, -2.5, -1.0, -0.2, 2.5, 1.0])
    assert pairs_signal(z).tolist() == [0.0, 1.0, 1.0, 0.0, -1.0, -1.0]


def test_cointegrated_pair_has_stationary_spread():
    rng = np.random.default_rng(21)
    b = pd.Series(100 * np.exp(np.cumsum(rng.normal(0, 0.01, 800))))
    a = b**1.2 * np.exp(rng.normal(0, 0.005, 800))
    z = zscore(spread(a, b)).dropna()
    assert abs(z.mean()) < 0.3
