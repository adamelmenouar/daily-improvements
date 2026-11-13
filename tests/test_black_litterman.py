import numpy as np
from portfolio.black_litterman import black_litterman_mu

COV = np.array([[0.04, 0.01], [0.01, 0.09]])
PI = np.array([0.05, 0.07])
P = np.array([[1.0, -1.0]])
Q = np.array([0.05])  # vue : l'actif 1 bat l'actif 2 de 5 points


def test_vague_views_keep_the_prior():
    mu = black_litterman_mu(PI, COV, P, Q, np.array([[1e9]]))
    assert np.allclose(mu, PI, atol=1e-6)


def test_confident_views_are_respected():
    mu = black_litterman_mu(PI, COV, P, Q, np.array([[1e-10]]))
    assert abs(P @ mu - Q).max() < 1e-4
