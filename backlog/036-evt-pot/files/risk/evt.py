"""VaR de queue par la méthode des excès au-delà d'un seuil (Peaks Over Threshold)."""
import numpy as np
from scipy.stats import genpareto


def evt_var(returns, alpha=0.99, threshold_quantile=0.90):
    losses = -np.asarray(returns, dtype=float)
    u = np.quantile(losses, threshold_quantile)
    excess = losses[losses > u] - u
    xi, _, beta = genpareto.fit(excess, floc=0)
    n, n_u = len(losses), len(excess)
    ratio = (n / n_u) * (1 - alpha)
    if abs(xi) < 1e-8:
        return float(u - beta * np.log(ratio))
    return float(u + beta / xi * (ratio ** (-xi) - 1))
