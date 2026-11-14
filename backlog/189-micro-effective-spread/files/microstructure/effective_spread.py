"""Spread effectif : coût réel payé par rapport au prix milieu, aller simple doublé."""


def effective_spread(trade_price, mid_price):
    """En fraction du prix milieu : 2 * |prix - milieu| / milieu."""
    return 2 * abs(trade_price - mid_price) / mid_price
