"""Décomposition de la CVaR : contribution de chaque actif dans les pires scénarios du portefeuille."""
import numpy as np


def cvar_contributions(returns, weights, alpha=0.95):
    """returns : (T, N). La somme des contributions est la CVaR du portefeuille (perte positive)."""
    r, w = np.asarray(returns, dtype=float), np.asarray(weights, dtype=float)
    p = r @ w
    tail = p <= np.quantile(p, 1 - alpha)
    return -w * r[tail].mean(axis=0)
