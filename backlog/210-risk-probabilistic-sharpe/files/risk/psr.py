"""Probabilistic Sharpe Ratio (Bailey et López de Prado) : probabilité que le vrai Sharpe dépasse un seuil."""
import numpy as np
from scipy.stats import norm, skew, kurtosis


def probabilistic_sharpe(returns, benchmark_sharpe=0.0):
    """Sharpe par période (non annualisé). Tient compte de la taille de l'échantillon, de l'asymétrie et du kurtosis."""
    r = np.asarray(returns, dtype=float)
    n = len(r)
    sr = r.mean() / r.std(ddof=1)
    g3, g4 = skew(r), kurtosis(r, fisher=False)
    denom = np.sqrt(1 - g3 * sr + (g4 - 1) / 4 * sr**2)
    return float(norm.cdf((sr - benchmark_sharpe) * np.sqrt(n - 1) / denom))
