import numpy as np
from risk.psi import psi

RNG = np.random.default_rng(50)
BASE = RNG.normal(0, 1, 20_000)


def test_same_distribution_is_stable():
    assert psi(BASE, RNG.normal(0, 1, 20_000)) < 0.1


def test_shifted_distribution_drifts():
    assert psi(BASE, RNG.normal(1.0, 1, 20_000)) > 0.25
