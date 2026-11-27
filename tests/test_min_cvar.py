import numpy as np
from portfolio.min_cvar import min_cvar_weights, cvar

R = np.random.default_rng(136).normal([0.0005, 0.0005, 0.0005], [0.005, 0.01, 0.02], (1000, 3))


def test_valid_long_only_weights():
    w = min_cvar_weights(R)
    assert abs(w.sum() - 1) < 1e-9 and (w >= -1e-9).all()


def test_beats_equal_weights_on_cvar():
    w = min_cvar_weights(R)
    assert cvar(R, w) <= cvar(R, np.ones(3) / 3) + 1e-9


def test_loads_on_the_least_risky_asset():
    assert min_cvar_weights(R).argmax() == 0
