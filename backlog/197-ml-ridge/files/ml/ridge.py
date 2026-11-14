"""Régression ridge : moindres carrés pénalisés (l'intercept n'est pas pénalisé)."""
import numpy as np


def fit_ridge(X, y, alpha=1.0):
    """Retourne (intercept, coefficients)."""
    X, y = np.asarray(X, dtype=float), np.asarray(y, dtype=float)
    xm, ym = X.mean(axis=0), y.mean()
    xc, yc = X - xm, y - ym
    coef = np.linalg.solve(xc.T @ xc + alpha * np.eye(X.shape[1]), xc.T @ yc)
    return float(ym - xm @ coef), coef


def predict_ridge(intercept, coef, X):
    return intercept + np.asarray(X, dtype=float) @ coef
