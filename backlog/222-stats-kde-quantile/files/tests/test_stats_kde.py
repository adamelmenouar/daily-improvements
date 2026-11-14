import numpy as np
from stats.kde import kde_quantile


def test_close_to_the_true_normal_quantile():
    x = np.random.default_rng(221).normal(0, 0.01, 2000)
    assert abs(kde_quantile(x, 0.01) - (-0.02326)) < 0.003


def test_reproducible():
    x = np.random.default_rng(222).normal(size=300)
    assert kde_quantile(x, 0.05, 20_000, seed=1) == kde_quantile(x, 0.05, 20_000, seed=1)


def test_monotone_in_q():
    x = np.random.default_rng(223).normal(size=500)
    assert kde_quantile(x, 0.05, 20_000) < kde_quantile(x, 0.5, 20_000) < kde_quantile(x, 0.95, 20_000)
