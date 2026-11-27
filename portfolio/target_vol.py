"""Ajustement de l'exposition pour viser une volatilité annuelle donnée."""
import numpy as np


def scale_to_target_vol(weights, cov_annual, target=0.10):
    """Multiplie les poids pour que la volatilité du portefeuille vaille `target` (peut créer du levier)."""
    w = np.asarray(weights, dtype=float)
    vol = np.sqrt(w @ np.asarray(cov_annual, dtype=float) @ w)
    return w * (target / vol)
