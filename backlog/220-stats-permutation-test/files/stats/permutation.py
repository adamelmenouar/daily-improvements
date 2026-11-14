"""Test de permutation : p-value sans hypothèse de loi."""
import numpy as np


def permutation_test_mean_diff(a, b, n_perm=5000, seed=0):
    """p-value bilatérale de la différence de moyennes entre deux échantillons."""
    a, b = np.asarray(a, dtype=float), np.asarray(b, dtype=float)
    observed = abs(a.mean() - b.mean())
    pool = np.concatenate([a, b])
    rng = np.random.default_rng(seed)
    count = 0
    for _ in range(n_perm):
        rng.shuffle(pool)
        if abs(pool[: len(a)].mean() - pool[len(a):].mean()) >= observed:
            count += 1
    return (count + 1) / (n_perm + 1)
