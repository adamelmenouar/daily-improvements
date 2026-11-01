import numpy as np
from risk.tails import tail_ratio, gain_to_pain


def test_symmetric_distribution_has_ratio_near_one():
    r = np.random.default_rng(42).normal(0, 0.01, 100_000)
    assert abs(tail_ratio(r) - 1) < 0.05


def test_gain_to_pain_known_value():
    assert abs(gain_to_pain([0.02, -0.01, 0.03, -0.01]) - 1.5) < 1e-12
