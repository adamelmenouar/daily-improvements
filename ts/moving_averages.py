"""Moyennes mobiles (séries pandas)."""
import numpy as np


def sma(x, window):
    return x.rolling(window).mean()


def ema(x, window):
    return x.ewm(span=window, adjust=False).mean()


def wma(x, window):
    """Moyenne pondérée linéairement : le poids le plus fort va à la valeur la plus récente."""
    w = np.arange(1, window + 1)
    return x.rolling(window).apply(lambda v: np.dot(v, w) / w.sum(), raw=True)
