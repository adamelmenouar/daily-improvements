import numpy as np
from risk.contributions import risk_contributions

COV = np.array([[0.04, 0.01], [0.01, 0.09]])


def test_contributions_sum_to_portfolio_volatility():
    w = np.array([0.6, 0.4])
    assert abs(risk_contributions(w, COV).sum() - np.sqrt(w @ COV @ w)) < 1e-12


def test_single_asset_carries_all_risk():
    rc = risk_contributions([1.0, 0.0], COV)
    assert abs(rc[0] - 0.2) < 1e-12 and rc[1] == 0.0
