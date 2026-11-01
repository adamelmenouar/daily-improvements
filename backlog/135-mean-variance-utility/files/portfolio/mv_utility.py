"""Allocation maximisant l'utilité w'mu - (lambda / 2) w'Sigma w (sans contrainte de budget)."""
import numpy as np


def mean_variance_weights(mu, cov, risk_aversion=3.0):
    return np.linalg.solve(np.asarray(cov, dtype=float), np.asarray(mu, dtype=float)) / risk_aversion


def utility(w, mu, cov, risk_aversion=3.0):
    w = np.asarray(w, dtype=float)
    return float(w @ np.asarray(mu, dtype=float) - risk_aversion / 2 * w @ np.asarray(cov, dtype=float) @ w)
