import numpy as np
from ml.quantile_labels import quantile_labels


def test_balanced_classes():
    labels = quantile_labels(np.random.default_rng(188).normal(size=3000), 3)
    assert set(labels) == {0, 1, 2} and all(abs((labels == k).mean() - 1 / 3) < 0.01 for k in range(3))


def test_order_is_preserved():
    r = np.array([0.05, -0.05, 0.0, 0.1, -0.1, 0.02])
    l = quantile_labels(r, 2)
    assert (l[r > np.median(r)] == 1).all() and (l[r < np.median(r)] == 0).all()
