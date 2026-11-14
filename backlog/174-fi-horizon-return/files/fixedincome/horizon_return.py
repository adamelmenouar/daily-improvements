"""Rendement annualisé d'une obligation détenue `horizon` ans, coupons annuels réinvestis."""
from pricing.bond import bond_price


def horizon_total_return(face, coupon_rate, ytm, years, horizon, reinvest_rate, exit_yield):
    price0 = bond_price(face, coupon_rate, ytm, years)
    coupon = face * coupon_rate
    reinvested = sum(coupon * (1 + reinvest_rate) ** (horizon - t) for t in range(1, horizon + 1))
    sale = bond_price(face, coupon_rate, exit_yield, years - horizon) if years > horizon else face
    return ((reinvested + sale) / price0) ** (1 / horizon) - 1
