"""Canal de Donchian et stratégie de cassure (breakout)."""
import pandas as pd


def donchian_channel(prices, window=20):
    """Plus haut / plus bas des `window` jours précédents (décalés : pas d'anticipation)."""
    return prices.rolling(window).min().shift(1), prices.rolling(window).max().shift(1)


def donchian_strategy(prices, entry=20, exit_=10):
    """Long à la cassure du plus haut d'`entry` jours, sortie sous le plus bas d'`exit_` jours."""
    up = prices.rolling(entry).max().shift(1)
    lo = prices.rolling(exit_).min().shift(1)
    pos = pd.Series(float("nan"), index=prices.index)
    pos[prices > up] = 1.0
    pos[prices < lo] = 0.0
    pos = pos.ffill().fillna(0.0)
    return prices.pct_change() * pos.shift(1)
