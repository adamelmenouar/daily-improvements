"""Hierarchical Risk Parity (López de Prado) : regroupement hiérarchique puis bissection récursive."""
import numpy as np
from scipy.cluster.hierarchy import leaves_list, linkage
from scipy.spatial.distance import squareform


def _cluster_variance(cov, idx):
    sub = cov[np.ix_(idx, idx)]
    ivp = 1 / np.diag(sub)
    ivp /= ivp.sum()
    return float(ivp @ sub @ ivp)


def hrp_weights(cov):
    cov = np.asarray(cov, dtype=float)
    sd = np.sqrt(np.diag(cov))
    corr = cov / np.outer(sd, sd)
    dist = np.sqrt(np.clip((1 - corr) / 2, 0, None))
    order = list(leaves_list(linkage(squareform(dist, checks=False), "single")))
    w = np.ones(len(cov))
    clusters = [order]
    while clusters:
        clusters = [c[i:j] for c in clusters if len(c) > 1
                    for i, j in ((0, len(c) // 2), (len(c) // 2, len(c)))]
        for k in range(0, len(clusters), 2):
            left, right = clusters[k], clusters[k + 1]
            vl, vr = _cluster_variance(cov, left), _cluster_variance(cov, right)
            alpha = 1 - vl / (vl + vr)
            w[left] *= alpha
            w[right] *= 1 - alpha
    return w / w.sum()
