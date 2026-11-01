import numpy as np
from portfolio.factor_exposure import factor_betas


def test_recovers_known_exposures():
    rng = np.random.default_rng(142)
    f = rng.normal(0, 0.01, (3000, 2))
    y = 0.0002 + f @ np.array([1.2, -0.5]) + rng.normal(0, 0.001, 3000)
    alpha, betas, r2 = factor_betas(y, f)
    assert abs(alpha - 0.0002) < 0.0001 and np.allclose(betas, [1.2, -0.5], atol=0.03) and r2 > 0.95


def test_unrelated_factor_explains_little():
    rng = np.random.default_rng(143)
    assert factor_betas(rng.normal(size=2000), rng.normal(size=(2000, 1)))[2] < 0.01
