"""Prix à terme (coût de portage), capitalisation continue."""
from math import exp


def forward_price(spot, r, t, dividend_yield=0.0, storage=0.0):
    return spot * exp((r - dividend_yield + storage) * t)


def basis(spot, futures_price):
    """Base = spot - terme (négative en contango)."""
    return spot - futures_price
