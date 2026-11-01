"""Concentration d'un portefeuille."""
import numpy as np


def herfindahl(weights):
    w = np.asarray(weights, dtype=float)
    return float(np.sum(w**2))


def effective_n(weights):
    """Nombre de lignes équivalentes à poids égaux."""
    return 1.0 / herfindahl(weights)
