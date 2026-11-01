"""Thêta (par an) et rho d'un call européen (Black-Scholes)."""
from math import exp, sqrt
from scipy.stats import norm
from pricing.black_scholes import _d1_d2


def call_theta(s, k, t, r, sigma):
    """Variation de valeur par année qui s'écoule (négative en général)."""
    d1, d2 = _d1_d2(s, k, t, r, sigma)
    return -s * norm.pdf(d1) * sigma / (2 * sqrt(t)) - r * k * exp(-r * t) * norm.cdf(d2)


def call_rho(s, k, t, r, sigma):
    """Variation de valeur pour +1.00 de taux (divisez par 100 pour +1 point)."""
    return k * t * exp(-r * t) * norm.cdf(_d1_d2(s, k, t, r, sigma)[1])
