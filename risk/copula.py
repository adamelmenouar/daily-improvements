"""Copule gaussienne : dépendance entre actifs, indépendamment des lois marginales."""
import numpy as np
from scipy.stats import norm


def simulate_gaussian_copula(corr, n=100_000, seed=0):
    """Retourne n tirages uniformes (n, d) dont la dépendance suit la corrélation `corr`."""
    chol = np.linalg.cholesky(np.asarray(corr, dtype=float))
    z = np.random.default_rng(seed).standard_normal((n, len(chol))) @ chol.T
    return norm.cdf(z)


def joint_exceedance(u, q=0.05):
    """Probabilité que toutes les marginales soient simultanément dans leur queue basse (<= q)."""
    return float((u <= q).all(axis=1).mean())
