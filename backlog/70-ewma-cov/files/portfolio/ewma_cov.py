"""Covariance à décroissance exponentielle (RiskMetrics)."""
import numpy as np


def ewma_covariance(returns, lam=0.94):
    """returns : (T, N), supposés centrés. Retourne la matrice (N, N) la plus récente."""
    x = np.asarray(returns, dtype=float)
    cov = np.outer(x[0], x[0])
    for t in range(1, len(x)):
        cov = lam * cov + (1 - lam) * np.outer(x[t], x[t])
    return cov
