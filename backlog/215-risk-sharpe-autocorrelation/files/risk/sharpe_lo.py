"""Annualisation du Sharpe corrigée de l'autocorrélation (Lo, 2002)."""
import numpy as np


def annualization_factor(returns, q=12):
    """Facteur multiplicatif du Sharpe par période pour passer à q périodes : q / sqrt(q + 2 sum (q - k) rho_k).
    Vaut sqrt(q) sans autocorrélation, moins si les rendements sont positivement autocorrélés."""
    r = np.asarray(returns, dtype=float)
    r = r - r.mean()
    rho = [np.dot(r[:-k], r[k:]) / np.dot(r, r) for k in range(1, q)]
    return float(q / np.sqrt(q + 2 * sum((q - k) * rho[k - 1] for k in range(1, q))))


def adjusted_annual_sharpe(returns, q=12):
    r = np.asarray(returns, dtype=float)
    return float(r.mean() / r.std(ddof=1) * annualization_factor(r, q))
