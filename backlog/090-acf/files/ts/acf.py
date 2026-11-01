"""Autocorrélation empirique."""
import numpy as np


def acf(x, nlags=20):
    """Autocorrélations aux retards 0..nlags (le retard 0 vaut 1)."""
    a = np.asarray(x, dtype=float)
    a = a - a.mean()
    denom = np.dot(a, a)
    return np.array([np.dot(a[: len(a) - k], a[k:]) / denom for k in range(nlags + 1)])
