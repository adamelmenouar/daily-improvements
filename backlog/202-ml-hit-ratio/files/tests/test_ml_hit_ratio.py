import numpy as np
from ml.hit_ratio import hit_ratio


def test_perfect_and_inverted_forecasts():
    r = np.array([0.01, -0.02, 0.03, -0.01])
    assert hit_ratio(r, r) == 1.0 and hit_ratio(-r, r) == 0.0


def test_random_forecast_is_near_half():
    rng = np.random.default_rng(187)
    assert abs(hit_ratio(rng.normal(size=20_000), rng.normal(size=20_000)) - 0.5) < 0.02


def test_zero_returns_are_ignored():
    assert hit_ratio([1, 1], [0.0, 0.01]) == 1.0
