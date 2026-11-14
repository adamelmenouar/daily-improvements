import numpy as np
from microstructure.roll import roll_spread


def test_recovers_the_bid_ask_spread():
    rng = np.random.default_rng(171)
    mid = 100 + np.cumsum(rng.normal(0, 0.01, 50_000))
    side = rng.choice([-1, 1], 50_000)
    assert abs(roll_spread(mid + 0.05 * side) - 0.10) < 0.01


def test_trending_prices_give_nan():
    assert np.isnan(roll_spread(np.cumsum(np.arange(1, 200, dtype=float))))
