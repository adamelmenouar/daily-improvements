"""Limiter la part du volume de marché qu'un algorithme peut représenter."""
import numpy as np


def capped_schedule(desired, market_volume, max_participation=0.10):
    """Quantité exécutée par période (plafonnée) et reliquat non exécuté."""
    d, v = np.asarray(desired, dtype=float), np.asarray(market_volume, dtype=float)
    executed = np.minimum(d, max_participation * v)
    return executed, float(d.sum() - executed.sum())
