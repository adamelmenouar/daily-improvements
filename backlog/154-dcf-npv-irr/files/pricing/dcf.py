"""Valeur actuelle nette, taux de rentabilité interne et délai de récupération."""
import numpy as np
from scipy.optimize import brentq


def npv(rate, cashflows):
    """cashflows[0] est à t = 0 (en général l'investissement, négatif)."""
    cf = np.asarray(cashflows, dtype=float)
    return float(np.sum(cf / (1 + rate) ** np.arange(len(cf))))


def irr(cashflows, lo=-0.99, hi=10.0):
    return float(brentq(lambda r: npv(r, cashflows), lo, hi))


def payback_period(cashflows):
    """Premier indice où le cumul devient >= 0 (None s'il n'est jamais récupéré)."""
    cum = np.cumsum(cashflows)
    idx = np.nonzero(cum >= 0)[0]
    return int(idx[0]) if len(idx) else None
