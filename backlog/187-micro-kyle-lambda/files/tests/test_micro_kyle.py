import numpy as np
from microstructure.kyle import kyle_lambda


def test_recovers_known_impact():
    rng = np.random.default_rng(172)
    q = rng.normal(0, 1000, 5000)
    dp = 2e-5 * q + rng.normal(0, 0.005, 5000)
    assert abs(kyle_lambda(dp, q) - 2e-5) < 2e-6


def test_no_relation_gives_near_zero():
    rng = np.random.default_rng(173)
    assert abs(kyle_lambda(rng.normal(0, 0.01, 5000), rng.normal(0, 1000, 5000))) < 1e-5
