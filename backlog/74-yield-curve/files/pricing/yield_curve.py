"""Courbe de taux zéro-coupon (capitalisation continue), interpolation linéaire."""
import numpy as np


def zero_rate(maturities, rates, t):
    return float(np.interp(t, maturities, rates))


def discount_factor(maturities, rates, t):
    return float(np.exp(-zero_rate(maturities, rates, t) * t))


def forward_rate(maturities, rates, t1, t2):
    """Taux forward implicite entre t1 et t2."""
    if t2 <= t1:
        raise ValueError("t2 doit être > t1")
    r1, r2 = zero_rate(maturities, rates, t1), zero_rate(maturities, rates, t2)
    return (r2 * t2 - r1 * t1) / (t2 - t1)
