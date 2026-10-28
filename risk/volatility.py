"""Estimation de volatilité."""
import numpy as np


def ewma_volatility(returns, lam=0.94):
    """Volatilité EWMA (RiskMetrics, lambda=0.94 pour des données journalières)."""
    if not 0 < lam < 1:
        raise ValueError("lam doit être dans ]0, 1[")
    r = np.asarray(returns, dtype=float)
    var = np.empty_like(r)
    var[0] = r[0] ** 2
    for t in range(1, len(r)):
        var[t] = lam * var[t - 1] + (1 - lam) * r[t - 1] ** 2
    return np.sqrt(var)
