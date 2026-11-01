"""Bandes de Bollinger."""
import pandas as pd


def bollinger_bands(prices, window=20, k=2.0):
    mid = prices.rolling(window).mean()
    sd = prices.rolling(window).std()
    return mid - k * sd, mid, mid + k * sd


def bollinger_strategy(prices, window=20, k=2.0):
    """Long sous la bande basse, sortie au retour à la moyenne. Signal décalé d'un jour."""
    lower, mid, _ = bollinger_bands(prices, window, k)
    pos = pd.Series(float("nan"), index=prices.index)
    pos[prices < lower] = 1.0
    pos[prices >= mid] = 0.0
    pos = pos.ffill().fillna(0.0)
    return prices.pct_change() * pos.shift(1)
