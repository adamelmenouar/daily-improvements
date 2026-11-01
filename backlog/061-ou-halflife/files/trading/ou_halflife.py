"""Demi-vie d'un processus qui revient à sa moyenne."""
import numpy as np


def ou_half_life(series):
    """Régresse dx_t sur x_{t-1} : dx = b * x_{t-1} + c. Demi-vie = -ln(2) / b (jours)."""
    x = np.asarray(series, dtype=float)
    lag, dx = x[:-1], np.diff(x)
    b = np.polyfit(lag, dx, 1)[0]
    if b >= 0:
        return float("inf")  # pas de retour à la moyenne
    return float(-np.log(2) / b)
