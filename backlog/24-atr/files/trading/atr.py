"""Average True Range et taille de position."""
import pandas as pd


def true_range(high, low, close):
    prev = close.shift(1)
    return pd.concat([high - low, (high - prev).abs(), (low - prev).abs()], axis=1).max(axis=1)


def atr(high, low, close, window=14):
    return true_range(high, low, close).rolling(window).mean()


def position_size(capital, risk_fraction, atr_value, atr_multiple=2.0):
    """Nombre d'unités pour risquer `risk_fraction` du capital avec un stop à atr_multiple * ATR."""
    if atr_value <= 0:
        raise ValueError("atr_value doit être > 0")
    return capital * risk_fraction / (atr_multiple * atr_value)
