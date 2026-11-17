"""Mise en base 100 de séries de prix (pandas Series ou DataFrame)."""


def rebase(prices, base=100.0):
    return prices / prices.iloc[0] * base
