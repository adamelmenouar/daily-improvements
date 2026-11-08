"""Bêta glissant d'un actif par rapport à un indice (séries pandas)."""


def rolling_beta(asset, market, window=60):
    return asset.rolling(window).cov(market) / market.rolling(window).var()
