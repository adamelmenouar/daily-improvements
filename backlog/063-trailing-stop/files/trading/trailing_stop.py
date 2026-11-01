"""Stratégie long avec stop suiveur (trailing stop)."""
import pandas as pd


def trailing_stop_returns(prices, stop=0.10):
    """Long dès le début ; sortie quand le prix recule de `stop` depuis son plus haut depuis l'entrée,
    puis ré-entrée au plus haut suivant. Signal décalé d'un jour."""
    pos = []
    peak, in_trade = prices.iloc[0], True
    for p in prices:
        if in_trade:
            peak = max(peak, p)
            if p < peak * (1 - stop):
                in_trade = False
        else:
            if p >= peak:
                in_trade, peak = True, p
        pos.append(1.0 if in_trade else 0.0)
    return prices.pct_change() * pd.Series(pos, index=prices.index).shift(1)
