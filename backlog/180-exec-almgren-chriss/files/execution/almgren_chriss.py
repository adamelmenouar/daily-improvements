"""Liquidation optimale d'Almgren-Chriss (temps continu, impact linéaire) : compromis coût / risque."""
import numpy as np


def optimal_holdings(total_quantity, horizon, n_steps, kappa):
    """Position restante à chaque date : X * sinh(kappa * (T - t)) / sinh(kappa * T).
    kappa -> 0 : liquidation linéaire (TWAP) ; kappa grand : on liquide vite pour limiter le risque."""
    t = np.linspace(0, horizon, n_steps + 1)
    if kappa < 1e-9:
        return total_quantity * (1 - t / horizon)
    return total_quantity * np.sinh(kappa * (horizon - t)) / np.sinh(kappa * horizon)


def kappa_from_params(risk_aversion, sigma, eta):
    """kappa = sqrt(lambda * sigma^2 / eta) avec eta le coefficient d'impact temporaire."""
    return float(np.sqrt(risk_aversion * sigma**2 / eta))
