"""Options de change : deux taux, domestique r_d et étranger r_f."""
from math import exp, log, sqrt
from scipy.stats import norm


def _d(s, k, t, r_d, r_f, sigma):
    d1 = (log(s / k) + (r_d - r_f + 0.5 * sigma**2) * t) / (sigma * sqrt(t))
    return d1, d1 - sigma * sqrt(t)


def fx_call(s, k, t, r_d, r_f, sigma):
    d1, d2 = _d(s, k, t, r_d, r_f, sigma)
    return s * exp(-r_f * t) * norm.cdf(d1) - k * exp(-r_d * t) * norm.cdf(d2)


def fx_put(s, k, t, r_d, r_f, sigma):
    d1, d2 = _d(s, k, t, r_d, r_f, sigma)
    return k * exp(-r_d * t) * norm.cdf(-d2) - s * exp(-r_f * t) * norm.cdf(-d1)
