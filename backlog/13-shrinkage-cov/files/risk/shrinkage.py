"""Matrice de covariance régularisée par rétrécissement vers une cible diagonale."""
import numpy as np


def shrunk_covariance(returns, delta=0.2):
    """(1 - delta) * S + delta * moyenne(diag(S)) * I. returns : (T, N)."""
    if not 0 <= delta <= 1:
        raise ValueError("delta doit être dans [0, 1]")
    s = np.cov(np.asarray(returns, dtype=float), rowvar=False)
    target = np.eye(len(s)) * np.trace(s) / len(s)
    return (1 - delta) * s + delta * target
