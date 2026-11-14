"""Volatilité implicite d'un call européen (Black-Scholes)."""
from scipy.optimize import brentq
from pricing.black_scholes import bs_call


def implied_vol_call(price, s, k, t, r, lo=1e-6, hi=5.0):
    """Volatilité telle que bs_call(...) = price. ValueError si le prix est hors bornes d'arbitrage."""
    return float(brentq(lambda v: bs_call(s, k, t, r, v) - price, lo, hi))
