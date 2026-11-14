import numpy as np
from stats.permutation import permutation_test_mean_diff


def test_identical_distributions_are_not_rejected():
    rng = np.random.default_rng(218)
    assert permutation_test_mean_diff(rng.normal(size=200), rng.normal(size=200), 2000) > 0.05


def test_shifted_distribution_is_rejected():
    rng = np.random.default_rng(219)
    assert permutation_test_mean_diff(rng.normal(0, 1, 200), rng.normal(1, 1, 200), 2000) < 0.01


def test_reproducible():
    a, b = [1.0, 2, 3, 4], [2.0, 3, 4, 9]
    assert permutation_test_mean_diff(a, b, 500, seed=4) == permutation_test_mean_diff(a, b, 500, seed=4)
