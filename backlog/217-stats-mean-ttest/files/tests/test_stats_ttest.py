import numpy as np
from scipy.stats import ttest_1samp
from stats.ttest import mean_ttest


def test_matches_scipy():
    x = np.random.default_rng(212).normal(0.1, 1, 200)
    t, p = mean_ttest(x)
    ref = ttest_1samp(x, 0.0)
    assert abs(t - ref.statistic) < 1e-12 and abs(p - ref.pvalue) < 1e-12


def test_true_edge_is_detected_and_no_edge_is_not():
    rng = np.random.default_rng(213)
    assert mean_ttest(rng.normal(0.2, 1, 2000))[1] < 1e-6
    assert mean_ttest(rng.normal(0.0, 1, 2000))[1] > 0.01
