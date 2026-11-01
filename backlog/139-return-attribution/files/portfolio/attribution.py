"""Contribution de chaque ligne à la performance d'une période."""
import numpy as np


def contributions(weights, asset_returns):
    """Contribution = poids de début de période x rendement. La somme est le rendement du portefeuille."""
    return np.asarray(weights, dtype=float) * np.asarray(asset_returns, dtype=float)


def top_contributors(names, weights, asset_returns, n=2):
    c = contributions(weights, asset_returns)
    order = np.argsort(c)[::-1][:n]
    return [(names[i], float(c[i])) for i in order]
