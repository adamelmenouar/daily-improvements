import numpy as np
from portfolio.risk_parity import inverse_vol_weights, equal_risk_contribution

COV = np.array([[0.04, 0.006, 0.0], [0.006, 0.09, 0.01], [0.0, 0.01, 0.16]])


def test_inverse_vol_sums_to_one_and_favours_low_vol():
    w = inverse_vol_weights(COV)
    assert abs(w.sum() - 1) < 1e-12 and w[0] > w[2]


def test_erc_equalises_risk_contributions():
    w = equal_risk_contribution(COV)
    rc = w * (COV @ w)
    assert rc.max() - rc.min() < 1e-6
