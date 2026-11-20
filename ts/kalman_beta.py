"""Filtre de Kalman scalaire : y_t = beta_t * x_t + bruit, beta_t suit une marche aléatoire."""
import numpy as np


def kalman_beta(y, x, q=1e-5, r=1e-2, beta0=0.0, p0=1.0):
    """q : variance du bruit d'état, r : variance de mesure. Retourne la trajectoire de beta."""
    y, x = np.asarray(y, dtype=float), np.asarray(x, dtype=float)
    beta, p = beta0, p0
    out = np.empty(len(y))
    for t in range(len(y)):
        p += q                                  # prédiction
        gain = p * x[t] / (x[t] ** 2 * p + r)   # gain de Kalman
        beta += gain * (y[t] - beta * x[t])     # correction
        p *= 1 - gain * x[t]
        out[t] = beta
    return out
