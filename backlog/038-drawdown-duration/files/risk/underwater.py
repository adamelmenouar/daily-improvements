"""Durée passée sous le dernier sommet."""
import numpy as np


def max_underwater_duration(returns):
    """Plus longue suite de périodes consécutives où la valeur est sous son plus haut."""
    equity = np.cumprod(1 + np.asarray(returns, dtype=float))
    under = equity < np.maximum.accumulate(equity)
    best = cur = 0
    for u in under:
        cur = cur + 1 if u else 0
        best = max(best, cur)
    return best
