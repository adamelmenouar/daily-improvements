import numpy as np
import pytest
from risk.garch import garch_variance


def test_positive_and_same_length():
    r = np.random.default_rng(14).normal(0, 0.01, 500)
    s2 = garch_variance(r)
    assert len(s2) == 500 and (s2 > 0).all()


def test_shock_raises_next_variance():
    r = np.zeros(10)
    r[3] = 0.1
    s2 = garch_variance(r)
    assert s2[4] > s2[3]


def test_non_stationary_rejected():
    with pytest.raises(ValueError):
        garch_variance([0.01, 0.02], alpha=0.5, beta=0.6)
