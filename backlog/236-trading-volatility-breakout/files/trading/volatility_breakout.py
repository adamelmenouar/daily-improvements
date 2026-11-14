"""Cassure de volatilité : achat si le prix dépasse l'ouverture + k fois l'amplitude de la veille ; sortie à la clôture."""
import pandas as pd


def volatility_breakout_returns(open_, high, low, close, k=0.5):
    prev_range = (high - low).shift(1)
    trigger = open_ + k * prev_range
    hit = high >= trigger
    daily = pd.Series(0.0, index=close.index)
    daily[hit] = close[hit] / trigger[hit] - 1
    return daily
