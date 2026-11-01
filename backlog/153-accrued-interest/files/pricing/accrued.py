"""Prix 'clean' (pied de coupon) et 'dirty' (coupon couru inclus)."""


def accrued_interest(face, coupon_rate, days_since_last, days_in_period, freq=2):
    """Coupon couru depuis le dernier détachement."""
    return face * coupon_rate / freq * days_since_last / days_in_period


def dirty_price(clean, accrued):
    return clean + accrued


def clean_price(dirty, accrued):
    return dirty - accrued
