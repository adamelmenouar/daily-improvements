import numpy as np
from stats.intervals import mean_confidence_interval, cohens_d


def test_interval_contains_the_mean_and_widens_with_confidence():
    x = np.random.default_rng(228).normal(0, 1, 100)
    lo95, hi95 = mean_confidence_interval(x, 0.95)
    lo99, hi99 = mean_confidence_interval(x, 0.99)
    assert lo95 < x.mean() < hi95 and hi99 - lo99 > hi95 - lo95


def test_coverage_is_about_95_percent():
    rng = np.random.default_rng(229)
    hits = sum(lo < 0 < hi for lo, hi in (mean_confidence_interval(rng.normal(size=30)) for _ in range(1000)))
    assert 0.92 < hits / 1000 < 0.98


def test_cohens_d_known_value():
    a, b = np.array([1.0, 2, 3, 4, 5]), np.array([2.0, 3, 4, 5, 6])
    assert abs(cohens_d(a, b) + 1 / a.std(ddof=1)) < 1e-12
