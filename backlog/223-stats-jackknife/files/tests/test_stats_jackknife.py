import numpy as np
from stats.jackknife import jackknife_se


def test_equals_the_classical_standard_error_for_the_mean():
    x = np.random.default_rng(224).normal(size=300)
    assert abs(jackknife_se(x) - x.std(ddof=1) / np.sqrt(300)) < 1e-12


def test_standard_error_of_the_standard_deviation():
    x = np.random.default_rng(225).normal(size=400)
    assert abs(jackknife_se(x, np.std) - 1 / np.sqrt(2 * 400)) < 0.01


def test_constant_data_has_zero_error():
    assert jackknife_se([2.0] * 10) == 0.0
