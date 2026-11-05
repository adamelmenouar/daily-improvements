"""Rééquilibrage vers des poids cibles."""
import numpy as np


def rebalance_trades(current_values, target_weights):
    """Montants à acheter (+) ou vendre (-) pour atteindre les poids cibles, à valeur totale constante."""
    v = np.asarray(current_values, dtype=float)
    return np.asarray(target_weights, dtype=float) * v.sum() - v


def turnover(current_values, target_weights):
    """Part de la valeur du portefeuille échangée (moitié de la somme des |écarts de poids|)."""
    v = np.asarray(current_values, dtype=float)
    return float(0.5 * np.abs(np.asarray(target_weights, dtype=float) - v / v.sum()).sum())
