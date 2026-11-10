"""Population Stability Index : compare la distribution actuelle à celle d'origine."""
import numpy as np


def psi(expected, actual, bins=10, eps=1e-6):
    """< 0.1 stable, 0.1-0.25 à surveiller, > 0.25 dérive importante."""
    e, a = np.asarray(expected, dtype=float), np.asarray(actual, dtype=float)
    edges = np.quantile(e, np.linspace(0, 1, bins + 1))
    edges[0], edges[-1] = -np.inf, np.inf
    pe = np.histogram(e, edges)[0] / len(e) + eps
    pa = np.histogram(a, edges)[0] / len(a) + eps
    return float(np.sum((pa - pe) * np.log(pa / pe)))
