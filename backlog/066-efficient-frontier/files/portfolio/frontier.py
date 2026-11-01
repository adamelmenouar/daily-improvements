"""Frontière efficiente de Markowitz (ventes à découvert autorisées)."""
import numpy as np


def min_variance_for_target(mu, cov, target):
    """Poids de variance minimale avec somme = 1 et rendement espéré = target (système de Lagrange)."""
    mu = np.asarray(mu, dtype=float)
    cov = np.asarray(cov, dtype=float)
    n = len(mu)
    ones = np.ones(n)
    kkt = np.zeros((n + 2, n + 2))
    kkt[:n, :n] = 2 * cov
    kkt[:n, n], kkt[:n, n + 1] = ones, mu
    kkt[n, :n], kkt[n + 1, :n] = ones, mu
    rhs = np.concatenate([np.zeros(n), [1.0, target]])
    return np.linalg.solve(kkt, rhs)[:n]
