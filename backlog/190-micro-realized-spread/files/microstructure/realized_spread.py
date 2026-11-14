"""Spread réalisé : ce que le teneur de marché garde après le mouvement du prix qui suit la transaction."""


def realized_spread(trade_price, mid_after, mid_before, side):
    """side = +1 achat (le client paie l'ask), -1 vente. En fraction du prix milieu avant la transaction."""
    return 2 * side * (trade_price - mid_after) / mid_before
