"""Oscillateur stochastique (%K et %D)."""


def stochastic(high, low, close, k_window=14, d_window=3):
    ll = low.rolling(k_window).min()
    hh = high.rolling(k_window).max()
    k = 100 * (close - ll) / (hh - ll)
    return k, k.rolling(d_window).mean()
