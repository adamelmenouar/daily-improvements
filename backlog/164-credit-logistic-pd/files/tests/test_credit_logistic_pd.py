import numpy as np
from credit.logistic_pd import fit_logistic, predict_pd


def _data(n=20_000, seed=165):
    rng = np.random.default_rng(seed)
    X = rng.normal(size=(n, 2))
    p = 1 / (1 + np.exp(-(-2.0 + 1.0 * X[:, 0] - 0.5 * X[:, 1])))
    return X, (rng.random(n) < p).astype(int)


def test_recovers_true_coefficients():
    X, y = _data()
    assert np.allclose(fit_logistic(X, y), [-2.0, 1.0, -0.5], atol=0.1)


def test_probabilities_in_unit_interval_and_calibrated():
    X, y = _data()
    p = predict_pd(fit_logistic(X, y), X)
    assert ((p > 0) & (p < 1)).all() and abs(p.mean() - y.mean()) < 0.01
