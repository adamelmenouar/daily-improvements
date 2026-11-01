"""Retour à la moyenne : long quand le prix est bas par rapport à sa moyenne glissante."""
import pandas as pd
from utils.rolling_stats import rolling_zscore


def zscore_reversion(prices, window=20, entry=1.5, exit_=0.0):
    z = rolling_zscore(prices, window)
    pos = pd.Series(float("nan"), index=prices.index)
    pos[z < -entry] = 1.0
    pos[z >= exit_] = 0.0
    pos = pos.ffill().fillna(0.0)
    return prices.pct_change() * pos.shift(1)
