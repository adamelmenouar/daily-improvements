"""Dérive des poids entre deux rééquilibrages."""
import numpy as np


def drifted_weights(weights, asset_returns):
    """Poids après une période sans rééquilibrage."""
    grown = np.asarray(weights, dtype=float) * (1 + np.asarray(asset_returns, dtype=float))
    return grown / grown.sum()


def needs_rebalance(weights, target, threshold=0.05):
    """Vrai si un poids s'écarte de sa cible de plus de `threshold` (en valeur absolue)."""
    return bool(np.max(np.abs(np.asarray(weights, dtype=float) - np.asarray(target, dtype=float))) > threshold)
