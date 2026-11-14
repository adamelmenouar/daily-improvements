"""Part des périodes où le signe de la prévision correspond à celui du rendement réalisé."""
import numpy as np


def hit_ratio(predictions, realized):
    p, r = np.sign(np.asarray(predictions, dtype=float)), np.sign(np.asarray(realized, dtype=float))
    mask = r != 0
    return float((p[mask] == r[mask]).mean())
