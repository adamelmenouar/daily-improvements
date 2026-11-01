"""Filtre de régime : n'être investi que si le prix est au-dessus de sa moyenne mobile longue."""


def regime_filtered_returns(prices, window=200):
    in_uptrend = (prices > prices.rolling(window).mean()).astype(float)
    return prices.pct_change() * in_uptrend.shift(1)
