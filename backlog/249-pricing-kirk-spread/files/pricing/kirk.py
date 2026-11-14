"""Option sur spread max(F1 - F2 - K, 0) : approximation de Kirk (1995)."""
from math import exp, log, sqrt
from scipy.stats import norm


def kirk_spread_call(f1, f2, strike, t, r, sigma1, sigma2, rho):
    b = f2 / (f2 + strike)
    sigma = sqrt(sigma1**2 - 2 * rho * sigma1 * sigma2 * b + (sigma2 * b) ** 2)
    d1 = (log(f1 / (f2 + strike)) + 0.5 * sigma**2 * t) / (sigma * sqrt(t))
    return exp(-r * t) * (f1 * norm.cdf(d1) - (f2 + strike) * norm.cdf(d1 - sigma * sqrt(t)))
