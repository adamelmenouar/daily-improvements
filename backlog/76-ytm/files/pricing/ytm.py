"""Rendement à l'échéance d'une obligation à coupons annuels."""
from scipy.optimize import brentq
from pricing.bond import bond_price


def yield_to_maturity(price, face, coupon_rate, years):
    return float(brentq(lambda y: bond_price(face, coupon_rate, y, years) - price, -0.5, 1.0))
