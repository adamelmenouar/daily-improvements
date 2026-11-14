import numpy as np
from credit.ks import ks_statistic


def test_perfect_separation_gives_one():
    assert ks_statistic([1, 2, 3, 10, 11, 12], [0, 0, 0, 1, 1, 1]) == 1.0


def test_no_information_gives_small_ks():
    rng = np.random.default_rng(161)
    assert ks_statistic(rng.random(5000), rng.random(5000) < 0.3) < 0.06


def test_better_model_has_larger_ks():
    rng = np.random.default_rng(162)
    y = rng.random(4000) < 0.2
    weak, strong = rng.normal(0, 1, 4000) + 0.3 * y, rng.normal(0, 1, 4000) + 1.5 * y
    assert ks_statistic(strong, y) > ks_statistic(weak, y)
