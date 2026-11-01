import numpy as np
import pytest
from risk.hill import hill_estimator


def test_recovers_pareto_tail_index():
    x = np.random.default_rng(37).pareto(3.0, 50_000) + 1  # alpha = 3 -> xi = 1/3
    assert abs(hill_estimator(x, 1000) - 1 / 3) < 0.05


def test_invalid_k():
    with pytest.raises(ValueError):
        hill_estimator([1.0, 2.0, 3.0], k=10)
