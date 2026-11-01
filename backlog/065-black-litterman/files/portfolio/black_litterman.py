"""Rendements espérés a posteriori de Black-Litterman."""
import numpy as np


def black_litterman_mu(pi, cov, P, q, omega, tau=0.05):
    """pi : rendements d'équilibre, P : matrice des vues (K, N), q : valeurs des vues, omega : incertitude des vues."""
    pi, q = np.asarray(pi, dtype=float), np.asarray(q, dtype=float)
    cov, P, omega = (np.asarray(x, dtype=float) for x in (cov, P, omega))
    prior_prec = np.linalg.inv(tau * cov)
    view_prec = P.T @ np.linalg.inv(omega) @ P
    return np.linalg.solve(prior_prec + view_prec, prior_prec @ pi + P.T @ np.linalg.inv(omega) @ q)
