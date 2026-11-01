"""ADX de Wilder : mesure la force d'une tendance, quel que soit son sens (0-100)."""
import numpy as np
import pandas as pd
from trading.atr import true_range


def adx(high, low, close, window=14):
    """Retourne (+DI, -DI, ADX)."""
    up, down = high.diff(), -low.diff()
    plus_dm = pd.Series(np.where((up > down) & (up > 0), up, 0.0), index=high.index)
    minus_dm = pd.Series(np.where((down > up) & (down > 0), down, 0.0), index=high.index)
    a = 1 / window
    tr = true_range(high, low, close).ewm(alpha=a, adjust=False).mean()
    plus_di = 100 * plus_dm.ewm(alpha=a, adjust=False).mean() / tr
    minus_di = 100 * minus_dm.ewm(alpha=a, adjust=False).mean() / tr
    dx = 100 * (plus_di - minus_di).abs() / (plus_di + minus_di)
    return plus_di, minus_di, dx.ewm(alpha=a, adjust=False).mean()
