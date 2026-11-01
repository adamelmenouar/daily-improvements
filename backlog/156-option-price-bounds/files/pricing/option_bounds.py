"""Bornes de no-arbitrage pour un call européen sur actif sans dividende."""
from math import exp


def call_bounds(s, k, t, r):
    """(borne inférieure, borne supérieure) : max(S - K e^-rT, 0) <= C <= S."""
    return max(s - k * exp(-r * t), 0.0), s


def violates_bounds(price, s, k, t, r):
    lo, hi = call_bounds(s, k, t, r)
    return not (lo - 1e-12 <= price <= hi + 1e-12)
