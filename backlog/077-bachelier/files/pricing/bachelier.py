"""Modèle de Bachelier (taux/prix pouvant être négatifs), sur un sous-jacent forward F."""
from math import sqrt
from scipy.stats import norm


def bachelier_call(f, k, t, sigma_n):
    """Prix non actualisé. sigma_n : volatilité normale (en unités de prix par racine d'année)."""
    s = sigma_n * sqrt(t)
    d = (f - k) / s
    return (f - k) * norm.cdf(d) + s * norm.pdf(d)


def bachelier_put(f, k, t, sigma_n):
    s = sigma_n * sqrt(t)
    d = (f - k) / s
    return (k - f) * norm.cdf(-d) + s * norm.pdf(d)
