"""Estimateur de Hill : épaisseur de la queue (xi = 1/alpha)."""
import numpy as np


def hill_estimator(losses, k=200):
    """Utilise les k plus grandes pertes positives. Retourne xi (plus grand = queue plus épaisse)."""
    x = np.sort(np.asarray(losses, dtype=float))[::-1]
    x = x[x > 0]
    if not 0 < k < len(x):
        raise ValueError("k doit être dans ]0, nb de pertes positives[")
    return float(np.mean(np.log(x[:k] / x[k])))
