"""Test de cointégration d'Engle-Granger en deux étapes."""
import numpy as np
from ts.adf import adf_statistic

CRITICAL_5PCT = -3.34  # approximation pour 2 séries


def engle_granger(y, x):
    """Régresse y sur x puis teste la stationnarité des résidus. Retourne (hedge ratio, stat ADF, cointégrées ?)."""
    y, x = np.asarray(y, dtype=float), np.asarray(x, dtype=float)
    beta, alpha = np.polyfit(x, y, 1)
    stat = adf_statistic(y - beta * x - alpha)
    return float(beta), stat, stat < CRITICAL_5PCT
