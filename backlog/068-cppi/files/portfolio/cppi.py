"""CPPI : exposition au risque = multiplicateur x coussin au-dessus d'un plancher."""
import numpy as np


def cppi_values(risky_returns, floor_fraction=0.8, multiplier=4.0, rf=0.0, v0=100.0):
    """Valeur du portefeuille période par période. Le plancher grandit au taux sans risque `rf`."""
    value, floor = v0, floor_fraction * v0
    path = [value]
    for r in risky_returns:
        cushion = max(value - floor, 0.0)
        exposure = min(multiplier * cushion, value)  # sans levier
        value = exposure * (1 + r) + (value - exposure) * (1 + rf)
        floor *= 1 + rf
        path.append(value)
    return np.array(path)
