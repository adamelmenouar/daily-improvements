"""VaR gaussienne pilotée par une volatilité EWMA (RiskMetrics) : réagit vite aux changements de régime."""
import numpy as np
from scipy.stats import norm


def ewma_var(returns, alpha=0.99, lam=0.94):
    """VaR (perte positive) pour la période suivante, rendements supposés centrés."""
    r = np.asarray(returns, dtype=float)
    var = r[0] ** 2
    for x in r:
        var = lam * var + (1 - lam) * x**2
    return float(norm.ppf(alpha) * np.sqrt(var))
