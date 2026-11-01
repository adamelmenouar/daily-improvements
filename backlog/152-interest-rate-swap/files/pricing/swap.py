"""Swap de taux vanille (paiements annuels) à partir de facteurs d'actualisation."""
import numpy as np


def par_swap_rate(dfs):
    d = np.asarray(dfs, dtype=float)
    return float((1 - d[-1]) / d.sum())


def payer_swap_value(fixed_rate, dfs, notional=1.0):
    """Valeur pour celui qui paie le taux fixe et reçoit le variable."""
    d = np.asarray(dfs, dtype=float)
    return float(notional * ((1 - d[-1]) - fixed_rate * d.sum()))
