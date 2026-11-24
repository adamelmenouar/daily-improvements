"""Stratégie long/flat sur croisement de deux EMA."""


def ema_cross_strategy(prices, fast=12, slow=26):
    if fast >= slow:
        raise ValueError("fast doit être < slow")
    signal = (prices.ewm(span=fast, adjust=False).mean() > prices.ewm(span=slow, adjust=False).mean()).astype(float)
    return prices.pct_change() * signal.shift(1)
