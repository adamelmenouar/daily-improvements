"""Filtre GARCH(1,1) à paramètres fixés."""
import numpy as np


def garch_variance(returns, omega=1e-6, alpha=0.08, beta=0.90):
    """Variance conditionnelle sigma2[t] = omega + alpha*r[t-1]^2 + beta*sigma2[t-1]."""
    if alpha < 0 or beta < 0 or omega <= 0 or alpha + beta >= 1:
        raise ValueError("paramètres non stationnaires")
    r = np.asarray(returns, dtype=float)
    s2 = np.empty_like(r)
    s2[0] = omega / (1 - alpha - beta)  # variance de long terme
    for t in range(1, len(r)):
        s2[t] = omega + alpha * r[t - 1] ** 2 + beta * s2[t - 1]
    return s2
