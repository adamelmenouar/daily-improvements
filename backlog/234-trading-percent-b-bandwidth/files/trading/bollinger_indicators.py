"""Indicateurs dérivés des bandes de Bollinger."""
from trading.bollinger import bollinger_bands


def percent_b(prices, window=20, k=2.0):
    """0 sur la bande basse, 1 sur la bande haute, 0.5 sur la moyenne."""
    lo, _, up = bollinger_bands(prices, window, k)
    return (prices - lo) / (up - lo)


def bandwidth(prices, window=20, k=2.0):
    """Largeur relative des bandes : signal de compression (squeeze) quand elle est faible."""
    lo, mid, up = bollinger_bands(prices, window, k)
    return (up - lo) / mid
