"""Swaption européenne de Black sur le taux de swap forward."""
from math import log, sqrt
from scipy.stats import norm


def _d(swap_rate, strike, vol, expiry):
    d1 = (log(swap_rate / strike) + 0.5 * vol**2 * expiry) / (vol * sqrt(expiry))
    return d1, d1 - vol * sqrt(expiry)


def payer_swaption(swap_rate, strike, vol, expiry, annuity):
    d1, d2 = _d(swap_rate, strike, vol, expiry)
    return annuity * (swap_rate * norm.cdf(d1) - strike * norm.cdf(d2))


def receiver_swaption(swap_rate, strike, vol, expiry, annuity):
    d1, d2 = _d(swap_rate, strike, vol, expiry)
    return annuity * (strike * norm.cdf(-d2) - swap_rate * norm.cdf(-d1))
