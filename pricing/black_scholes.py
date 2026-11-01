"""Prix d'options européennes (Black-Scholes-Merton)."""
from math import exp, log, sqrt
from scipy.stats import norm


def _d1_d2(s, k, t, r, sigma):
    d1 = (log(s / k) + (r + 0.5 * sigma ** 2) * t) / (sigma * sqrt(t))
    return d1, d1 - sigma * sqrt(t)


def bs_call(s, k, t, r, sigma):
    d1, d2 = _d1_d2(s, k, t, r, sigma)
    return s * norm.cdf(d1) - k * exp(-r * t) * norm.cdf(d2)


def bs_put(s, k, t, r, sigma):
    d1, d2 = _d1_d2(s, k, t, r, sigma)
    return k * exp(-r * t) * norm.cdf(-d2) - s * norm.cdf(-d1)
