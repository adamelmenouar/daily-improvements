"""Portefeuille de diversification maximale (Choueifaty) : maximise le ratio de diversification."""
import numpy as np


def max_diversification_weights(cov):
    """Solution sans contrainte de signe : w proportionnel à inv(Sigma) @ sigma, normalisé à 1."""
    c = np.asarray(cov, dtype=float)
    w = np.linalg.solve(c, np.sqrt(np.diag(c)))
    return w / w.sum()
