import numpy as np
from ml.permutation_importance import permutation_importance


def test_informative_feature_matters_and_noise_does_not():
    rng = np.random.default_rng(185)
    X = rng.normal(size=(2000, 3))
    y = 3 * X[:, 0] + 0.5 * X[:, 1]
    predict = lambda A: 3 * A[:, 0] + 0.5 * A[:, 1]
    r2 = lambda t, p: 1 - np.var(t - p) / np.var(t)
    imp = permutation_importance(predict, X, y, r2)
    assert imp[0] > imp[1] > 0 and abs(imp[2]) < 1e-12


def test_reproducible():
    X = np.random.default_rng(186).normal(size=(200, 2))
    y = X[:, 0]
    f = lambda A: A[:, 0]
    s = lambda t, p: -np.mean((t - p) ** 2)
    assert np.array_equal(permutation_importance(f, X, y, s, seed=3), permutation_importance(f, X, y, s, seed=3))
