"""Indicateurs de momentum."""


def roc(prices, window=12):
    """Variation relative sur `window` périodes."""
    return prices / prices.shift(window) - 1


def williams_r(high, low, close, window=14):
    """Entre -100 (plus bas) et 0 (plus haut)."""
    hh, ll = high.rolling(window).max(), low.rolling(window).min()
    return -100 * (hh - close) / (hh - ll)
