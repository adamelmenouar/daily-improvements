import numpy as np
from trading.ou_halflife import ou_half_life


def test_recovers_known_speed():
    rng = np.random.default_rng(62)
    x = np.zeros(5000)
    for t in range(1, 5000):
        x[t] = 0.9 * x[t - 1] + rng.normal()  # b = -0.1 -> demi-vie ~ 6.6
    assert abs(ou_half_life(x) - 6.6) < 1.5


def test_random_walk_has_no_mean_reversion():
    x = np.cumsum(np.random.default_rng(63).normal(size=3000))
    assert ou_half_life(x) > 50
