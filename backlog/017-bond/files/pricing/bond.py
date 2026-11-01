"""Obligation à coupons annuels."""


def bond_price(face, coupon_rate, ytm, years):
    cfs = [face * coupon_rate] * years
    cfs[-1] += face
    return sum(cf / (1 + ytm) ** t for t, cf in enumerate(cfs, start=1))


def macaulay_duration(face, coupon_rate, ytm, years):
    cfs = [face * coupon_rate] * years
    cfs[-1] += face
    price = bond_price(face, coupon_rate, ytm, years)
    return sum(t * cf / (1 + ytm) ** t for t, cf in enumerate(cfs, start=1)) / price


def modified_duration(face, coupon_rate, ytm, years):
    return macaulay_duration(face, coupon_rate, ytm, years) / (1 + ytm)
