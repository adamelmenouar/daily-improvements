"""Covariance régularisée vers un modèle à corrélation constante (Ledoit-Wolf, 2003)."""
import numpy as np


def constant_correlation_covariance(returns, delta=0.3):
    """(1 - delta) * S + delta * F, où F a les mêmes variances que S et la corrélation moyenne partout."""
    if not 0 <= delta <= 1:
        raise ValueError("delta doit être dans [0, 1]")
    s = np.cov(np.asarray(returns, dtype=float), rowvar=False)
    sd = np.sqrt(np.diag(s))
    corr = s / np.outer(sd, sd)
    n = len(s)
    rho = (corr.sum() - n) / (n * (n - 1))
    target = rho * np.outer(sd, sd)
    np.fill_diagonal(target, np.diag(s))
    return (1 - delta) * s + delta * target
