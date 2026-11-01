"""Ulcer Index : profondeur et durée des baisses depuis les sommets."""
import numpy as np


def ulcer_index(prices):
    p = np.asarray(prices, dtype=float)
    dd = p / np.maximum.accumulate(p) - 1
    return float(np.sqrt(np.mean(dd**2)))
