"""Convexité d'une obligation à coupons annuels."""
from pricing.bond import bond_price


def bond_convexity(face, coupon_rate, ytm, years):
    cfs = [face * coupon_rate] * years
    cfs[-1] += face
    p = bond_price(face, coupon_rate, ytm, years)
    return sum(t * (t + 1) * cf / (1 + ytm) ** (t + 2) for t, cf in enumerate(cfs, start=1)) / p
