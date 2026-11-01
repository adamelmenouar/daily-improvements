"""Stress test : impact de chocs prédéfinis sur un portefeuille."""
import numpy as np

SCENARIOS = {
    "krach_actions": np.array([-0.30, -0.05, 0.02]),   # actions, crédit, obligations d'État
    "hausse_taux": np.array([-0.08, -0.06, -0.10]),
    "crise_credit": np.array([-0.15, -0.20, 0.03]),
}


def stress_pnl(weights, shocks):
    """Variation de valeur du portefeuille pour un vecteur de chocs par classe d'actifs."""
    return float(np.dot(np.asarray(weights, dtype=float), np.asarray(shocks, dtype=float)))


def run_scenarios(weights, scenarios=SCENARIOS):
    return {name: stress_pnl(weights, s) for name, s in scenarios.items()}
