"""Rendement d'un an d'une obligation à coupons annuels si la courbe reste inchangée."""
import numpy as np
from pricing.bond import bond_price


def rolldown_return(face, coupon_rate, years, curve_maturities, curve_yields):
    """Achat aujourd'hui au rendement lu sur la courbe pour `years`, revente dans un an au rendement
    lu pour `years - 1` (la courbe ne bouge pas). Rendement total = (prix futur + coupon) / prix actuel - 1."""
    if years < 2:
        raise ValueError("years doit être >= 2")
    y0 = np.interp(years, curve_maturities, curve_yields)
    y1 = np.interp(years - 1, curve_maturities, curve_yields)
    p0 = bond_price(face, coupon_rate, y0, years)
    p1 = bond_price(face, coupon_rate, y1, years - 1)
    return (p1 + face * coupon_rate) / p0 - 1
