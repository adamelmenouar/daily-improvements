"""Corrélations en crise : tout le monde se met à bouger ensemble."""
import numpy as np


def stress_correlation(corr, intensity=0.5):
    """Rapproche chaque corrélation hors diagonale de 1 : rho' = rho + intensity * (1 - rho)."""
    if not 0 <= intensity <= 1:
        raise ValueError("intensity doit être dans [0, 1]")
    c = np.asarray(corr, dtype=float)
    out = c + intensity * (1 - c)
    np.fill_diagonal(out, 1.0)
    return out
