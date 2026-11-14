"""Caplet / floorlet de Black sur un taux forward."""
from math import log, sqrt
from scipy.stats import norm


def _d(forward, strike, vol, expiry):
    d1 = (log(forward / strike) + 0.5 * vol**2 * expiry) / (vol * sqrt(expiry))
    return d1, d1 - vol * sqrt(expiry)


def caplet(forward, strike, vol, expiry, accrual, discount_factor):
    d1, d2 = _d(forward, strike, vol, expiry)
    return accrual * discount_factor * (forward * norm.cdf(d1) - strike * norm.cdf(d2))


def floorlet(forward, strike, vol, expiry, accrual, discount_factor):
    d1, d2 = _d(forward, strike, vol, expiry)
    return accrual * discount_factor * (strike * norm.cdf(-d2) - forward * norm.cdf(-d1))
