"""TRIX : variation en % d'une triple moyenne exponentielle, qui filtre le bruit de court terme."""


def trix(prices, window=15):
    e = prices.ewm(span=window, adjust=False).mean()
    e = e.ewm(span=window, adjust=False).mean()
    e = e.ewm(span=window, adjust=False).mean()
    return 100 * e.pct_change()
