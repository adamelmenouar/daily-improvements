"""Calibration du modèle coût = k * sigma * sqrt(taille / volume) par moindres carrés sans constante."""
import numpy as np


def calibrate_impact_coefficient(costs, sigmas, order_sizes, daily_volumes):
    x = np.asarray(sigmas, dtype=float) * np.sqrt(np.asarray(order_sizes, dtype=float) / np.asarray(daily_volumes, dtype=float))
    c = np.asarray(costs, dtype=float)
    return float(x @ c / (x @ x))
