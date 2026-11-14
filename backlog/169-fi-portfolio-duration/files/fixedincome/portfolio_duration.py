"""Duration et DV01 d'un portefeuille de positions obligataires."""
import numpy as np


def portfolio_duration(market_values, durations):
    """Moyenne des durations pondérée par les valeurs de marché."""
    mv, d = np.asarray(market_values, dtype=float), np.asarray(durations, dtype=float)
    return float(mv @ d / mv.sum())


def portfolio_dv01(market_values, durations):
    """Gain/perte approximatif pour 1 point de base de variation de rendement."""
    return portfolio_duration(market_values, durations) * float(np.sum(market_values)) * 1e-4
