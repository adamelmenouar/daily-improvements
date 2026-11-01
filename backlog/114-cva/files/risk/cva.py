"""Credit Valuation Adjustment simplifiée : (1 - R) * somme(EE_i * PD_i * DF_i)."""
import numpy as np


def cva(expected_exposure, marginal_pd, discount_factors, recovery=0.4):
    ee, pd_, df = (np.asarray(x, dtype=float) for x in (expected_exposure, marginal_pd, discount_factors))
    return float((1 - recovery) * np.sum(ee * pd_ * df))
