import numpy as np
from ml.ridge import fit_ridge, predict_ridge


def _data():
    rng = np.random.default_rng(183)
    X = rng.normal(size=(2000, 3))
    y = 1.5 + X @ np.array([2.0, -1.0, 0.5]) + rng.normal(0, 0.1, 2000)
    return X, y


def test_small_penalty_recovers_ols():
    X, y = _data()
    b0, b = fit_ridge(X, y, 1e-9)
    assert abs(b0 - 1.5) < 0.02 and np.allclose(b, [2.0, -1.0, 0.5], atol=0.02)


def test_larger_penalty_shrinks_coefficients():
    X, y = _data()
    assert np.linalg.norm(fit_ridge(X, y, 5000)[1]) < np.linalg.norm(fit_ridge(X, y, 1)[1])


def test_prediction_shape():
    X, y = _data()
    assert predict_ridge(*fit_ridge(X, y), X).shape == (2000,)
