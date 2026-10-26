"""Grecques d'un call européen (Black-Scholes)."""
from math import sqrt
from scipy.stats import norm
from pricing.black_scholes import _d1_d2


def call_delta(s, k, t, r, sigma):
    return float(norm.cdf(_d1_d2(s, k, t, r, sigma)[0]))


def gamma(s, k, t, r, sigma):
    return float(norm.pdf(_d1_d2(s, k, t, r, sigma)[0]) / (s * sigma * sqrt(t)))


def vega(s, k, t, r, sigma):
    """Variation du prix pour +1.00 de volatilité (divisez par 100 pour +1 point)."""
    return float(s * norm.pdf(_d1_d2(s, k, t, r, sigma)[0]) * sqrt(t))
