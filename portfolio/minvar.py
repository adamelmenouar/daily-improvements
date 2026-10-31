"""Optimisation de portefeuille."""
import numpy as np


def min_variance_weights(cov):
    """Poids de variance minimale (somme = 1, ventes à découvert autorisées)."""
    cov = np.asarray(cov, dtype=float)
    ones = np.ones(len(cov))
    w = np.linalg.solve(cov, ones)
    return w / w.sum()


def portfolio_volatility(weights, cov):
    w = np.asarray(weights, dtype=float)
    return float(np.sqrt(w @ np.asarray(cov, dtype=float) @ w))
