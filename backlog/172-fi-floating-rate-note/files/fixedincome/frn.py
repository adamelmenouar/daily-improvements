"""Obligation à taux variable (FRN), évaluée à une date de refixing."""


def frn_price(face, reference_rate, quoted_margin, discount_margin, years, freq=2):
    """Coupons figés au taux de référence courant + marge cotée, actualisés à référence + marge d'actualisation."""
    n = int(years * freq)
    coupon = face * (reference_rate + quoted_margin) / freq
    y = (reference_rate + discount_margin) / freq
    return sum(coupon / (1 + y) ** k for k in range(1, n + 1)) + face / (1 + y) ** n
