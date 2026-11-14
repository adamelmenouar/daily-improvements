"""Intervalle de confiance t de la moyenne et taille d'effet."""
import numpy as np
from scipy.stats import t


def mean_confidence_interval(x, level=0.95):
    a = np.asarray(x, dtype=float)
    se = a.std(ddof=1) / np.sqrt(len(a))
    h = t.ppf(0.5 + level / 2, len(a) - 1) * se
    return float(a.mean() - h), float(a.mean() + h)


def cohens_d(a, b):
    """Différence de moyennes en écarts-types poolés."""
    a, b = np.asarray(a, dtype=float), np.asarray(b, dtype=float)
    pooled = np.sqrt(((len(a) - 1) * a.var(ddof=1) + (len(b) - 1) * b.var(ddof=1)) / (len(a) + len(b) - 2))
    return float((a.mean() - b.mean()) / pooled)
