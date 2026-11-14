"""Importance par permutation : baisse de score quand on casse le lien d'une variable avec la cible."""
import numpy as np


def permutation_importance(predict, X, y, score, n_repeats=10, seed=0):
    """predict(X) -> prédictions ; score(y, pred) -> plus grand = mieux. Retourne une baisse moyenne par colonne."""
    X = np.asarray(X, dtype=float)
    rng = np.random.default_rng(seed)
    base = score(y, predict(X))
    out = np.zeros(X.shape[1])
    for j in range(X.shape[1]):
        drops = []
        for _ in range(n_repeats):
            Xp = X.copy()
            Xp[:, j] = rng.permutation(Xp[:, j])
            drops.append(base - score(y, predict(Xp)))
        out[j] = np.mean(drops)
    return out
