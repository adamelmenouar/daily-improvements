"""Estimateurs de position peu sensibles aux valeurs extrêmes."""
import numpy as np
from scipy.stats import trim_mean


def trimmed_mean(x, proportion=0.1):
    """Moyenne après retrait de `proportion` des valeurs de chaque côté."""
    return float(trim_mean(np.asarray(x, dtype=float), proportion))


def median_of_means(x, n_blocks=10, seed=0):
    a = np.random.default_rng(seed).permutation(np.asarray(x, dtype=float))
    return float(np.median([b.mean() for b in np.array_split(a, n_blocks)]))
