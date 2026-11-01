"""Portefeuille long-only de CVaR minimale, par programmation linéaire."""
import numpy as np
from scipy.optimize import linprog


def min_cvar_weights(returns, alpha=0.95):
    """returns : (T, N) scénarios de rendements. Retourne des poids >= 0 de somme 1."""
    r = np.asarray(returns, dtype=float)
    t, n = r.shape
    # variables : w (n), zeta (1), u (t) ; minimiser zeta + sum(u) / ((1 - alpha) * t)
    c = np.concatenate([np.zeros(n), [1.0], np.full(t, 1.0 / ((1 - alpha) * t))])
    a_ub = np.hstack([-r, -np.ones((t, 1)), -np.eye(t)])  # -r.w - zeta - u <= 0
    a_eq = np.concatenate([np.ones(n), [0.0], np.zeros(t)])[None, :]
    bounds = [(0, None)] * n + [(None, None)] + [(0, None)] * t
    res = linprog(c, A_ub=a_ub, b_ub=np.zeros(t), A_eq=a_eq, b_eq=[1.0], bounds=bounds, method="highs")
    return res.x[:n]


def cvar(returns, weights, alpha=0.95):
    """CVaR (perte moyenne dans les pires 1 - alpha cas) du portefeuille."""
    p = np.asarray(returns, dtype=float) @ np.asarray(weights, dtype=float)
    cutoff = np.quantile(p, 1 - alpha)
    return float(-p[p <= cutoff].mean())
