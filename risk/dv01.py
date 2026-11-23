"""DV01 : variation de prix pour 1 point de base de rendement."""
from pricing.bond import bond_price


def dv01(face, coupon_rate, ytm, years):
    """Perte de valeur positive pour +1 bp (différence centrée)."""
    bp = 1e-4
    return (bond_price(face, coupon_rate, ytm - bp, years) - bond_price(face, coupon_rate, ytm + bp, years)) / 2
