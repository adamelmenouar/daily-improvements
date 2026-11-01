"""Options européennes sur contrat à terme (Black 1976)."""
from math import exp, log, sqrt
from scipy.stats import norm


def black76_call(f, k, t, r, sigma):
    d1 = (log(f / k) + 0.5 * sigma**2 * t) / (sigma * sqrt(t))
    return exp(-r * t) * (f * norm.cdf(d1) - k * norm.cdf(d1 - sigma * sqrt(t)))


def black76_put(f, k, t, r, sigma):
    d1 = (log(f / k) + 0.5 * sigma**2 * t) / (sigma * sqrt(t))
    return exp(-r * t) * (k * norm.cdf(-(d1 - sigma * sqrt(t))) - f * norm.cdf(-d1))
