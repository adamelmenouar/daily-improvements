"""Ratio de diversification : moyenne pondérée des volatilités / volatilité du portefeuille."""
import numpy as np


def diversification_ratio(weights, cov):
    w = np.asarray(weights, dtype=float)
    c = np.asarray(cov, dtype=float)
    return float(w @ np.sqrt(np.diag(c)) / np.sqrt(w @ c @ w))
