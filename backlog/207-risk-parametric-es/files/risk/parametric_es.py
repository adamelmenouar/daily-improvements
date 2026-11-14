"""Expected Shortfall sous hypothèse gaussienne : ES = -mu + sigma * phi(z) / (1 - alpha)."""
import numpy as np
from scipy.stats import norm


def parametric_es(returns, alpha=0.975):
    r = np.asarray(returns, dtype=float)
    z = norm.ppf(alpha)
    return float(-r.mean() + r.std(ddof=1) * norm.pdf(z) / (1 - alpha))
