import numpy as np
from stats.fdr import benjamini_hochberg
from stats.familywise import bonferroni


def test_known_values():
    assert np.allclose(benjamini_hochberg([0.01, 0.04, 0.03, 0.005]), [0.02, 0.04, 0.04, 0.02])


def test_more_permissive_than_bonferroni():
    p = np.random.default_rng(216).random(40) ** 2
    assert (benjamini_hochberg(p) <= bonferroni(p) + 1e-12).all()


def test_values_stay_in_the_unit_interval():
    a = benjamini_hochberg(np.random.default_rng(217).random(100))
    assert ((a >= 0) & (a <= 1)).all()
