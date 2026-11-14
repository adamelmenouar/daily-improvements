"""Simulation historique filtrée : rejoue les chocs standardisés du passé à la volatilité d'aujourd'hui."""
import numpy as np


def filtered_hs_var(returns, alpha=0.99, lam=0.94):
    r = np.asarray(returns, dtype=float)
    sigma = np.empty_like(r)
    var = r[:20].var()
    for t in range(len(r)):
        sigma[t] = np.sqrt(var)
        var = lam * var + (1 - lam) * r[t] ** 2
    shocks = r / sigma
    return float(-np.quantile(shocks, 1 - alpha) * np.sqrt(var))  # var = variance prévue pour demain
