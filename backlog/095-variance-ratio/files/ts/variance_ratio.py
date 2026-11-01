"""Ratio de variance : VR(q) = Var(rendement sur q périodes) / (q * Var(rendement 1 période)).

VR ~ 1 : marche aléatoire ; > 1 : momentum ; < 1 : retour à la moyenne.
"""
import numpy as np


def variance_ratio(returns, q=5):
    r = np.asarray(returns, dtype=float)
    rq = np.convolve(r, np.ones(q), mode="valid")  # rendements cumulés glissants sur q périodes
    return float(rq.var(ddof=1) / (q * r.var(ddof=1)))
