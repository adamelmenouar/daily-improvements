import numpy as np
from utils.outliers import mad_outliers


def test_obvious_outlier_is_flagged():
    x = np.append(np.random.default_rng(84).normal(0, 1, 200), 50.0)
    flags = mad_outliers(x)
    assert flags[-1] and flags.sum() <= 5


def test_constant_data_has_no_outliers():
    assert not mad_outliers([2.0] * 10).any()
