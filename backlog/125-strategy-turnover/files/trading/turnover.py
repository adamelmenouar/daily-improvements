"""Rotation d'une stratégie : part du capital échangée par période."""
import numpy as np


def average_turnover(positions):
    """Moyenne de |variation de position| (positions en fraction du capital)."""
    p = np.asarray(positions, dtype=float)
    return float(np.mean(np.abs(np.diff(p))))


def annual_turnover(positions, periods=252):
    return average_turnover(positions) * periods
