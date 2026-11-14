"""Quantile lissé par estimation de densité à noyau gaussien : moins bruité qu'un quantile empirique."""
import numpy as np
from scipy.stats import gaussian_kde


def kde_quantile(x, q, n_samples=200_000, seed=0):
    kde = gaussian_kde(np.asarray(x, dtype=float))
    sample = kde.resample(n_samples, seed=seed)[0]
    return float(np.quantile(sample, q))
