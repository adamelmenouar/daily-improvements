import numpy as np
import pytest
from risk.volatility import ewma_volatility


def test_converges_near_true_sigma():
    r = np.random.default_rng(5).normal(0, 0.01, 5000)
    assert abs(ewma_volatility(r)[-500:].mean() - 0.01) < 0.003


def test_invalid_lambda():
    with pytest.raises(ValueError):
        ewma_volatility([0.01, 0.02], lam=1.5)
