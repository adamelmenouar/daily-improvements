"""Active share : part du portefeuille qui diffère de son indice de référence."""
import numpy as np


def active_share(portfolio_weights, benchmark_weights):
    p, b = np.asarray(portfolio_weights, dtype=float), np.asarray(benchmark_weights, dtype=float)
    return float(0.5 * np.abs(p - b).sum())
