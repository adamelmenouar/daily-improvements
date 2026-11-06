import numpy as np
from risk.normality import jarque_bera


def test_normal_data_not_rejected():
    assert jarque_bera(np.random.default_rng(30).normal(0, 0.01, 5000))[1] > 0.01


def test_fat_tails_rejected():
    assert jarque_bera(np.random.default_rng(30).standard_t(3, 5000) * 0.01)[1] < 0.01
