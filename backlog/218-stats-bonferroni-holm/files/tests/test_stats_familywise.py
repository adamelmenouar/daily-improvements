import numpy as np
from stats.familywise import bonferroni, holm

P = [0.01, 0.04, 0.03, 0.005]


def test_bonferroni_known_values():
    assert np.allclose(bonferroni(P), [0.04, 0.16, 0.12, 0.02])


def test_holm_known_values():
    assert np.allclose(holm(P), [0.03, 0.06, 0.06, 0.02])


def test_holm_is_never_larger_than_bonferroni():
    p = np.random.default_rng(214).random(50)
    assert (holm(p) <= bonferroni(p) + 1e-12).all()


def test_adjusted_values_are_at_least_the_raw_ones():
    p = np.random.default_rng(215).random(20)
    assert (holm(p) >= p - 1e-12).all()
