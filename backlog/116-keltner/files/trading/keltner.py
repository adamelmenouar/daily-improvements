"""Canaux de Keltner : EMA du prix +/- k fois l'ATR."""
from trading.atr import atr


def keltner_channels(high, low, close, window=20, k=2.0):
    mid = close.ewm(span=window, adjust=False).mean()
    width = k * atr(high, low, close, window)
    return mid - width, mid, mid + width
