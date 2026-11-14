import numpy as np
from stats.robust_mean import trimmed_mean, median_of_means


def test_trimmed_mean_resists_an_outlier():
    x = np.append(np.random.default_rng(226).normal(1, 1, 999), 1e6)
    assert abs(trimmed_mean(x, 0.05) - 1) < 0.1 and np.mean(x) > 100


def test_median_of_means_resists_heavy_tails():
    x = np.random.default_rng(227).standard_t(2, 5000) + 1
    assert abs(median_of_means(x, 20) - 1) < 0.2


def test_trimming_nothing_gives_the_mean():
    x = [1.0, 2.0, 3.0, 10.0]
    assert trimmed_mean(x, 0.0) == np.mean(x)
