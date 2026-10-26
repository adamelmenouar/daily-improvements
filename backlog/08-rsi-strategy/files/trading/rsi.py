"""RSI et stratégie simple basée dessus."""
import pandas as pd


def rsi(prices, window=14):
    """RSI de Wilder (0-100)."""
    delta = prices.diff()
    gain = delta.clip(lower=0).ewm(alpha=1 / window, adjust=False).mean()
    loss = (-delta.clip(upper=0)).ewm(alpha=1 / window, adjust=False).mean()
    rs = gain / loss
    return 100 - 100 / (1 + rs)


def rsi_strategy(prices, window=14, low=30, high=70):
    """Long quand RSI < low, flat quand RSI > high, sinon position conservée. Signal décalé d'un jour."""
    r = rsi(prices, window)
    pos = pd.Series(float("nan"), index=prices.index)
    pos[r < low] = 1.0
    pos[r > high] = 0.0
    pos = pos.ffill().fillna(0.0)
    return prices.pct_change() * pos.shift(1)
