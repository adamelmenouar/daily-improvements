"""Décomposition du risque d'un portefeuille."""
import numpy as np


def risk_contributions(weights, cov):
    """Contribution de chaque actif à la volatilité du portefeuille (somme = volatilité)."""
    w = np.asarray(weights, dtype=float)
    c = np.asarray(cov, dtype=float)
    vol = np.sqrt(w @ c @ w)
    return w * (c @ w) / vol
