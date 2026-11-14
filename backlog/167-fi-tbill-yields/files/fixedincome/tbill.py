"""Conventions de cotation des bons du Trésor à court terme."""


def discount_yield(face, price, days):
    """Taux d'escompte (base 360 jours)."""
    return (face - price) / face * 360 / days


def bond_equivalent_yield(face, price, days):
    """Rendement équivalent obligataire (base 365 jours)."""
    return (face - price) / price * 365 / days


def price_from_discount_yield(face, dy, days):
    return face * (1 - dy * days / 360)
