"""Jackknife : erreur-type d'une statistique en retirant une observation à la fois."""
import numpy as np


def jackknife_se(x, statistic=np.mean):
    a = np.asarray(x, dtype=float)
    n = len(a)
    leave_one_out = np.array([statistic(np.delete(a, i)) for i in range(n)])
    return float(np.sqrt((n - 1) / n * np.sum((leave_one_out - leave_one_out.mean()) ** 2)))
