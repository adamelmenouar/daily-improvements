"""Réparation d'une matrice de corrélation (valeurs propres négatives)."""
import numpy as np


def nearest_correlation(corr, eps=1e-8):
    """Coupe les valeurs propres négatives puis renormalise la diagonale à 1."""
    c = (np.asarray(corr, dtype=float) + np.asarray(corr, dtype=float).T) / 2
    vals, vecs = np.linalg.eigh(c)
    fixed = vecs @ np.diag(np.maximum(vals, eps)) @ vecs.T
    d = 1 / np.sqrt(np.diag(fixed))
    return fixed * np.outer(d, d)
