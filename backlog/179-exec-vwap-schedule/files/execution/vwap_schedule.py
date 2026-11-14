"""VWAP : répartir un ordre proportionnellement au volume attendu de chaque période."""
import numpy as np


def vwap_schedule(total_quantity, volume_profile):
    v = np.asarray(volume_profile, dtype=float)
    if (v < 0).any() or v.sum() == 0:
        raise ValueError("profil de volume invalide")
    return total_quantity * v / v.sum()
