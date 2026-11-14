"""Aroon : ancienneté du dernier plus haut / plus bas sur la fenêtre (0-100)."""
import numpy as np


def aroon(high, low, window=25):
    """Retourne (aroon_up, aroon_down, oscillateur)."""
    def since_max(x):
        return len(x) - 1 - int(np.argmax(x))

    def since_min(x):
        return len(x) - 1 - int(np.argmin(x))

    up = 100 * (window - high.rolling(window + 1).apply(since_max, raw=True)) / window
    down = 100 * (window - low.rolling(window + 1).apply(since_min, raw=True)) / window
    return up, down, up - down
