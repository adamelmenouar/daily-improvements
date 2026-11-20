"""CUSUM unilatéral : détecte une hausse de la moyenne par rapport à une période de référence."""
import numpy as np


def cusum_alarm(x, baseline=50, k=0.5, h=5.0):
    """Premier indice d'alarme (ou None). La moyenne/écart-type viennent des `baseline` premières valeurs ;
    k : tolérance, h : seuil, tous deux en écarts-types."""
    a = np.asarray(x, dtype=float)
    mu, sd = a[:baseline].mean(), a[:baseline].std(ddof=1)
    s = 0.0
    for t in range(baseline, len(a)):
        s = max(0.0, s + (a[t] - mu) / sd - k)
        if s > h:
            return t
    return None
