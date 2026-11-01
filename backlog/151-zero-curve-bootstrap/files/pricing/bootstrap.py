"""Bootstrap de facteurs d'actualisation à partir de taux 'par' annuels (échéances 1, 2, ..., n ans)."""
import numpy as np


def bootstrap_discount_factors(par_rates):
    dfs = []
    for c in par_rates:
        dfs.append((1 - c * sum(dfs)) / (1 + c))
    return np.array(dfs)


def zero_rates(dfs):
    """Taux zéro annuels équivalents : DF_n = (1 + z_n)^-n."""
    n = np.arange(1, len(dfs) + 1)
    return dfs ** (-1.0 / n) - 1
