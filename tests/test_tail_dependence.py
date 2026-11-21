import numpy as np
from risk.tail_dependence import lower_tail_dependence


def test_independent_series_give_about_q():
    rng = np.random.default_rng(106)
    assert abs(lower_tail_dependence(rng.normal(size=20_000), rng.normal(size=20_000), 0.05) - 0.05) < 0.03


def test_identical_series_give_one():
    x = np.random.default_rng(106).normal(size=2000)
    assert lower_tail_dependence(x, x) == 1.0


def test_crash_together_is_detected():
    rng = np.random.default_rng(107)
    common = rng.standard_t(3, 20_000)
    x, y = common + 0.3 * rng.normal(size=20_000), common + 0.3 * rng.normal(size=20_000)
    assert lower_tail_dependence(x, y) > 0.5
