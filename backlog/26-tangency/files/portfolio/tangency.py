"""Portefeuille de Sharpe maximal (ventes à découvert autorisées)."""
import numpy as np


def tangency_weights(mu, cov, rf=0.0):
    ex = np.asarray(mu, dtype=float) - rf
    w = np.linalg.solve(np.asarray(cov, dtype=float), ex)
    return w / w.sum()


def sharpe_ratio(weights, mu, cov, rf=0.0):
    w = np.asarray(weights, dtype=float)
    return float((w @ np.asarray(mu, dtype=float) - rf) / np.sqrt(w @ np.asarray(cov, dtype=float) @ w))
