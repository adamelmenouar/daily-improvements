"""Allocations de type risk parity."""
import numpy as np


def inverse_vol_weights(cov):
    inv = 1 / np.sqrt(np.diag(np.asarray(cov, dtype=float)))
    return inv / inv.sum()


def equal_risk_contribution(cov, n_iter=500, tol=1e-12):
    """Poids où chaque actif apporte la même contribution au risque (point fixe amorti)."""
    c = np.asarray(cov, dtype=float)
    w = inverse_vol_weights(c)
    for _ in range(n_iter):
        new = 1 / (c @ w)
        new /= new.sum()
        new = 0.5 * w + 0.5 * new
        if np.abs(new - w).max() < tol:
            return new
        w = new
    return w
