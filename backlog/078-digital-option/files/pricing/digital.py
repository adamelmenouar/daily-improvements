"""Options digitales cash-or-nothing (Black-Scholes)."""
from math import exp
from scipy.stats import norm
from pricing.black_scholes import _d1_d2


def digital_call(s, k, t, r, sigma, cash=1.0):
    return cash * exp(-r * t) * float(norm.cdf(_d1_d2(s, k, t, r, sigma)[1]))


def digital_put(s, k, t, r, sigma, cash=1.0):
    return cash * exp(-r * t) * float(norm.cdf(-_d1_d2(s, k, t, r, sigma)[1]))
