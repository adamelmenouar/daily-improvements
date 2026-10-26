"""Drawdown d'une série de rendements."""
import numpy as np


def drawdown_series(returns):
    """Drawdown (<= 0) à chaque date, relatif au plus haut atteint."""
    equity = np.cumprod(1 + np.asarray(returns, dtype=float))
    peak = np.maximum.accumulate(equity)
    return equity / peak - 1


def max_drawdown(returns):
    """Pire baisse depuis un sommet (valeur négative)."""
    return float(drawdown_series(returns).min())
