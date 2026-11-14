"""VaR sous loi de Student ajustée : queues plus épaisses que la loi normale."""
import numpy as np
from scipy.stats import t


def student_t_var(returns, alpha=0.99):
    df, loc, scale = t.fit(np.asarray(returns, dtype=float))
    return float(-(loc + scale * t.ppf(1 - alpha, df)))
