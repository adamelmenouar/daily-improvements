"""Détection robuste de valeurs aberrantes (score z modifié, Iglewicz-Hoaglin)."""
import numpy as np


def mad_outliers(x, threshold=3.5):
    """Booléens True pour les valeurs aberrantes. Insensible aux outliers eux-mêmes (médiane / MAD)."""
    a = np.asarray(x, dtype=float)
    med = np.median(a)
    mad = np.median(np.abs(a - med))
    if mad == 0:
        return np.zeros(len(a), dtype=bool)
    return np.abs(0.6745 * (a - med) / mad) > threshold
