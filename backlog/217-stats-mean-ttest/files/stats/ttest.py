"""Test t : la moyenne diffère-t-elle d'une valeur de référence (bilatéral) ?"""
import numpy as np
from scipy.stats import t


def mean_ttest(x, mu0=0.0):
    """Retourne (statistique t, p-value bilatérale)."""
    a = np.asarray(x, dtype=float)
    stat = (a.mean() - mu0) / (a.std(ddof=1) / np.sqrt(len(a)))
    return float(stat), float(2 * (1 - t.cdf(abs(stat), len(a) - 1)))
