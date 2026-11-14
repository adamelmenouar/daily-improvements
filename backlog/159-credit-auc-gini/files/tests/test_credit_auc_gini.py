import numpy as np
from credit.auc_gini import auc, gini


def test_perfect_and_inverted_scores():
    y = [0, 0, 0, 1, 1]
    assert auc([1, 2, 3, 4, 5], y) == 1.0 and gini([1, 2, 3, 4, 5], y) == 1.0
    assert auc([5, 4, 3, 2, 1], y) == 0.0


def test_random_scores_give_auc_near_half():
    rng = np.random.default_rng(160)
    assert abs(auc(rng.random(5000), rng.random(5000) < 0.2) - 0.5) < 0.03


def test_ties_count_half():
    assert abs(auc([1, 1, 1, 1], [0, 1, 0, 1]) - 0.5) < 1e-12
