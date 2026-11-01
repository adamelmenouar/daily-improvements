"""Décomposition de la VaR paramétrique d'un portefeuille."""
import numpy as np
from scipy.stats import norm


def component_var(weights, cov, alpha=0.95):
    """Contribution de chaque actif à la VaR (rendements centrés). La somme est la VaR du portefeuille."""
    w = np.asarray(weights, dtype=float)
    c = np.asarray(cov, dtype=float)
    z = norm.ppf(alpha)
    vol = np.sqrt(w @ c @ w)
    marginal = z * (c @ w) / vol
    return w * marginal
