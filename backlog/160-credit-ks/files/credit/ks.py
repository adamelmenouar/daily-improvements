"""KS : écart maximal entre les distributions de scores des défaillants et des sains."""
import numpy as np
from scipy.stats import ks_2samp


def ks_statistic(scores, defaulted):
    s, y = np.asarray(scores, dtype=float), np.asarray(defaulted, dtype=int)
    return float(ks_2samp(s[y == 1], s[y == 0]).statistic)
