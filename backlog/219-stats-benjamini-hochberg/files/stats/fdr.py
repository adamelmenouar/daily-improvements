"""Benjamini-Hochberg : contrôle de la proportion de fausses découvertes parmi les rejets."""
import numpy as np


def benjamini_hochberg(pvalues):
    p = np.asarray(pvalues, dtype=float)
    n = len(p)
    order = np.argsort(p)
    scaled = p[order] * n / np.arange(1, n + 1)
    adj_sorted = np.minimum.accumulate(scaled[::-1])[::-1]
    adj = np.empty(n)
    adj[order] = np.minimum(adj_sorted, 1.0)
    return adj
