"""VaR de Cornish-Fisher : corrige la VaR gaussienne par l'asymétrie et le kurtosis."""
import numpy as np
from scipy.stats import norm, skew, kurtosis


def cornish_fisher_var(returns, alpha=0.95):
    r = np.asarray(returns, dtype=float)
    z = norm.ppf(1 - alpha)
    s, k = skew(r), kurtosis(r)  # k = kurtosis en excès
    z_cf = z + (z**2 - 1) * s / 6 + (z**3 - 3 * z) * k / 24 - (2 * z**3 - 5 * z) * s**2 / 36
    return float(-(r.mean() + r.std(ddof=1) * z_cf))
