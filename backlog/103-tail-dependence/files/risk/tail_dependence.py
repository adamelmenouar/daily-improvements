"""Dépendance de queue inférieure : probabilité que Y soit extrême sachant que X l'est."""
import numpy as np


def lower_tail_dependence(x, y, q=0.05):
    x, y = np.asarray(x, dtype=float), np.asarray(y, dtype=float)
    mask = x <= np.quantile(x, q)
    return float((y[mask] <= np.quantile(y, q)).mean())
