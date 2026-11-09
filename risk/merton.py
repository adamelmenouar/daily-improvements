"""Modèle de Merton : le défaut survient si la valeur des actifs finit sous la dette."""
from math import log, sqrt
from scipy.stats import norm


def merton_pd(asset_value, debt, mu, sigma, horizon=1.0):
    d2 = (log(asset_value / debt) + (mu - 0.5 * sigma**2) * horizon) / (sigma * sqrt(horizon))
    return float(norm.cdf(-d2))
