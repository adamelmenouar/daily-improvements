"""MACD (Moving Average Convergence Divergence)."""
import pandas as pd


def macd(prices, fast=12, slow=26, signal=9):
    """Retourne (macd, ligne de signal, histogramme)."""
    line = prices.ewm(span=fast, adjust=False).mean() - prices.ewm(span=slow, adjust=False).mean()
    sig = line.ewm(span=signal, adjust=False).mean()
    return line, sig, line - sig
