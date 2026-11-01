"""Ratio Oméga : gains au-dessus d'un seuil sur pertes en dessous."""
import numpy as np


def omega_ratio(returns, threshold=0.0):
    r = np.asarray(returns, dtype=float)
    gains = np.maximum(r - threshold, 0.0).sum()
    losses = np.maximum(threshold - r, 0.0).sum()
    return float("inf") if losses == 0 else float(gains / losses)
