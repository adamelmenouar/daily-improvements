import numpy as np
from ml.ols import ols


def test_significant_and_insignificant_regressors():
    rng = np.random.default_rng(184)
    X = rng.normal(size=(3000, 2))
    y = 1.0 + 0.5 * X[:, 0] + rng.normal(size=3000)  # X[:, 1] n'a aucun effet
    beta, se, t, r2 = ols(X, y)
    assert abs(t[1]) > 10 and abs(t[2]) < 3 and 0 < r2 < 1


def test_exact_linear_relation_gives_r2_one():
    X = np.arange(20, dtype=float)[:, None]
    assert abs(ols(X, 2 * X[:, 0] + 3)[3] - 1) < 1e-12
