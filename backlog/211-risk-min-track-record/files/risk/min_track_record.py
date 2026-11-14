"""Nombre minimal d'observations pour que le Sharpe observé dépasse un seuil avec la confiance voulue."""
import numpy as np
from scipy.stats import norm, skew, kurtosis


def min_track_record_length(returns, benchmark_sharpe=0.0, confidence=0.95):
    r = np.asarray(returns, dtype=float)
    sr = r.mean() / r.std(ddof=1)
    if sr <= benchmark_sharpe:
        return float("inf")
    g3, g4 = skew(r), kurtosis(r, fisher=False)
    z = norm.ppf(confidence)
    return float(1 + (1 - g3 * sr + (g4 - 1) / 4 * sr**2) * (z / (sr - benchmark_sharpe)) ** 2)
