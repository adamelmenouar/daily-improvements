"""ACP de la covariance des rendements : quels facteurs portent le risque ?"""
import numpy as np


def explained_variance_ratio(returns):
    """returns : (T, N). Part de variance de chaque composante, par ordre décroissant."""
    vals = np.linalg.eigvalsh(np.cov(np.asarray(returns, dtype=float), rowvar=False))[::-1]
    return vals / vals.sum()
