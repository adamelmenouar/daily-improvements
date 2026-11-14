"""Money Flow Index : RSI pondéré par les volumes (0-100)."""
import numpy as np


def money_flow_index(high, low, close, volume, window=14):
    tp = (high + low + close) / 3
    flow = tp * volume
    pos = flow.where(tp.diff() > 0, 0.0).rolling(window).sum()
    neg = flow.where(tp.diff() < 0, 0.0).rolling(window).sum()
    total = pos + neg
    return 100 * pos / total.replace(0, np.nan)  # = 100 - 100 / (1 + pos / neg), défini aussi si neg = 0
