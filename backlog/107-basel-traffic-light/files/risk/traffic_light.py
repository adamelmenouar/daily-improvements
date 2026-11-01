"""Zones de Bâle : jugement du nombre d'exceptions de VaR via la loi binomiale."""
from scipy.stats import binom


def traffic_light(n_exceptions, n_obs=250, alpha=0.99):
    """'green' si P(X <= n) < 95 %, 'yellow' si < 99.99 %, sinon 'red'."""
    p = binom.cdf(n_exceptions, n_obs, 1 - alpha)
    if p < 0.95:
        return "green"
    return "yellow" if p < 0.9999 else "red"
