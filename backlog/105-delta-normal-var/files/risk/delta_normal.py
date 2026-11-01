"""VaR delta-normale pour des positions exprimées en valeur monétaire."""
import numpy as np
from scipy.stats import norm


def delta_normal_var(position_values, cov, alpha=0.99, horizon=1):
    """Perte maximale (positive, en monnaie) avec confiance alpha. cov : covariance des rendements journaliers."""
    v = np.asarray(position_values, dtype=float)
    sigma = np.sqrt(v @ np.asarray(cov, dtype=float) @ v)
    return float(norm.ppf(alpha) * sigma * np.sqrt(horizon))
