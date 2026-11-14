"""Rendement d'une obligation callable si elle est remboursée à la première date de call."""
from scipy.optimize import brentq


def yield_to_call(price, face, coupon_rate, call_years, call_price):
    cfs = [face * coupon_rate] * call_years
    cfs[-1] += call_price

    def pv(y):
        return sum(cf / (1 + y) ** t for t, cf in enumerate(cfs, start=1))

    return float(brentq(lambda y: pv(y) - price, -0.5, 1.0))
