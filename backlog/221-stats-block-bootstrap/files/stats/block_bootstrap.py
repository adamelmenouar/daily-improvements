"""Bootstrap par blocs glissants : préserve l'autocorrélation à courte portée."""
import numpy as np


def block_bootstrap_mean_ci(x, block=10, n_boot=2000, level=0.95, seed=0):
    """Retourne (borne basse, moyenne observée, borne haute)."""
    a = np.asarray(x, dtype=float)
    n = len(a)
    rng = np.random.default_rng(seed)
    n_blocks = int(np.ceil(n / block))
    means = np.empty(n_boot)
    for i in range(n_boot):
        starts = rng.integers(0, n - block + 1, n_blocks)
        means[i] = np.concatenate([a[s:s + block] for s in starts])[:n].mean()
    lo, hi = np.quantile(means, [(1 - level) / 2, 1 - (1 - level) / 2])
    return float(lo), float(a.mean()), float(hi)
