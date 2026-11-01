"""Commodity Channel Index."""
import numpy as np


def cci(high, low, close, window=20):
    tp = (high + low + close) / 3
    sma = tp.rolling(window).mean()
    mad = tp.rolling(window).apply(lambda x: np.mean(np.abs(x - x.mean())), raw=True)
    return (tp - sma) / (0.015 * mad)
