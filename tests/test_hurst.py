import numpy as np
from ts.hurst import hurst_exponent

RNG = np.random.default_rng(96)


def test_random_walk_is_near_half():
    assert abs(hurst_exponent(np.cumsum(RNG.normal(size=5000))) - 0.5) < 0.1


def test_mean_reverting_series_is_below_half():
    x = np.zeros(5000)
    for t in range(1, 5000):
        x[t] = 0.5 * x[t - 1] + RNG.normal()
    assert hurst_exponent(x) < 0.4


def test_persistent_increments_give_a_value_above_half():
    rng = np.random.default_rng(196)
    inc = np.zeros(5000)
    for t in range(1, 5000):
        inc[t] = 0.6 * inc[t - 1] + rng.normal()  # momentum dans les variations
    assert hurst_exponent(np.cumsum(inc)) > 0.6
