"""Risk budgeting : chaque actif reçoit une part cible de la volatilité du portefeuille."""
import numpy as np


def risk_budget_weights(cov, budgets, n_iter=2000, tol=1e-13):
    c = np.asarray(cov, dtype=float)
    b = np.asarray(budgets, dtype=float)
    b = b / b.sum()
    w = b.copy()
    for _ in range(n_iter):
        new = b / (c @ w)
        new /= new.sum()
        new = 0.5 * w + 0.5 * new
        if np.abs(new - w).max() < tol:
            return new
        w = new
    return w
