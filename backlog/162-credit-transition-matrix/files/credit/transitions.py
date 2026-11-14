"""Matrices de migration de notations (la dernière classe est le défaut, absorbant)."""
import numpy as np


def estimate_transition_matrix(ratings_t0, ratings_t1, n_states):
    """Fréquences de passage observées entre deux dates. Les lignes sans observation restent sur place."""
    counts = np.zeros((n_states, n_states))
    for a, b in zip(ratings_t0, ratings_t1):
        counts[a, b] += 1
    rows = counts.sum(axis=1, keepdims=True)
    p = np.divide(counts, rows, out=np.zeros_like(counts), where=rows > 0)
    for i in np.nonzero(rows.ravel() == 0)[0]:
        p[i, i] = 1.0
    return p


def n_year_matrix(p, years):
    return np.linalg.matrix_power(p, years)
