"""Supertrend : suiveur de tendance fondé sur l'ATR (direction +1 haussière / -1 baissière)."""
import numpy as np
import pandas as pd
from trading.atr import atr


def supertrend(high, low, close, window=10, multiplier=3.0):
    a = atr(high, low, close, window).to_numpy()
    mid = ((high + low) / 2).to_numpy()
    c = close.to_numpy()
    n = len(c)
    upper, lower = mid + multiplier * a, mid - multiplier * a
    direction, line = np.full(n, np.nan), np.full(n, np.nan)
    start = int(np.argmax(~np.isnan(a)))
    final_u, final_l, d = upper[start], lower[start], 1
    for i in range(start, n):
        if i > start:
            final_u = upper[i] if upper[i] < final_u or c[i - 1] > final_u else final_u
            final_l = lower[i] if lower[i] > final_l or c[i - 1] < final_l else final_l
            if d == 1 and c[i] < final_l:
                d = -1
            elif d == -1 and c[i] > final_u:
                d = 1
        direction[i] = d
        line[i] = final_l if d == 1 else final_u
    return pd.Series(direction, index=close.index), pd.Series(line, index=close.index)
