"""Erreur-type de la moyenne robuste à l'autocorrélation (noyau de Bartlett)."""
import numpy as np


def newey_west_se(x, lags=None):
    a = np.asarray(x, dtype=float)
    n = len(a)
    if lags is None:
        lags = int(np.floor(4 * (n / 100) ** (2 / 9)))
    e = a - a.mean()
    var = np.dot(e, e) / n
    for k in range(1, lags + 1):
        w = 1 - k / (lags + 1)
        var += 2 * w * np.dot(e[k:], e[:-k]) / n
    return float(np.sqrt(var / n))
