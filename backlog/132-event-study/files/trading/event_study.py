"""Étude d'événement : comportement moyen autour de dates d'annonce."""
import numpy as np


def average_car(returns, event_indices, before=2, after=5):
    """Rendement anormal cumulé moyen, de -before à +after jours autour des événements.
    Anormal = rendement - rendement moyen de la série. Les événements trop proches des bords sont ignorés."""
    r = np.asarray(returns, dtype=float)
    ab = r - r.mean()
    paths = [np.cumsum(ab[i - before:i + after + 1]) for i in event_indices
             if i - before >= 0 and i + after < len(r)]
    if not paths:
        raise ValueError("aucun événement exploitable")
    return np.mean(paths, axis=0)
