"""Value-at-Risk et Expected Shortfall sur une série de rendements."""
import numpy as np
from scipy.stats import norm


def historical_var(returns, alpha=0.95):
    """VaR historique : perte (positive) dépassée avec probabilité 1 - alpha."""
    r = np.asarray(returns, dtype=float)
    return float(-np.quantile(r, 1 - alpha))


def parametric_var(returns, alpha=0.95):
    """VaR paramétrique sous hypothèse de rendements gaussiens."""
    r = np.asarray(returns, dtype=float)
    return float(-(r.mean() + r.std(ddof=1) * norm.ppf(1 - alpha)))


def expected_shortfall(returns, alpha=0.95):
    """Perte moyenne dans les pires (1 - alpha) cas."""
    r = np.asarray(returns, dtype=float)
    cutoff = np.quantile(r, 1 - alpha)
    return float(-r[r <= cutoff].mean())
