"""Régression logistique par Newton-Raphson (IRLS), avec une petite pénalité ridge."""
import numpy as np


def fit_logistic(X, y, ridge=1e-6, n_iter=50):
    """Retourne les coefficients (intercept en premier)."""
    x = np.column_stack([np.ones(len(X)), np.asarray(X, dtype=float)])
    y = np.asarray(y, dtype=float)
    beta = np.zeros(x.shape[1])
    for _ in range(n_iter):
        p = 1 / (1 + np.exp(-x @ beta))
        grad = x.T @ (y - p) - ridge * beta
        hess = x.T @ (x * (p * (1 - p))[:, None]) + ridge * np.eye(len(beta))
        step = np.linalg.solve(hess, grad)
        beta += step
        if np.abs(step).max() < 1e-10:
            break
    return beta


def predict_pd(beta, X):
    x = np.column_stack([np.ones(len(X)), np.asarray(X, dtype=float)])
    return 1 / (1 + np.exp(-x @ beta))
