"""Perte attendue de crédit."""
import numpy as np


def expected_loss(pd_, lgd, ead):
    """Fonctionne pour un prêt (scalaires) ou un portefeuille (tableaux). Retourne la somme."""
    pd_, lgd, ead = (np.asarray(x, dtype=float) for x in (pd_, lgd, ead))
    if ((pd_ < 0) | (pd_ > 1) | (lgd < 0) | (lgd > 1)).any():
        raise ValueError("PD et LGD doivent être dans [0, 1]")
    return float(np.sum(pd_ * lgd * ead))
