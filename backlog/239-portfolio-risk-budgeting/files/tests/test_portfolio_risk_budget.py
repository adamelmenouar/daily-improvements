import numpy as np
from portfolio.risk_budget import risk_budget_weights
from portfolio.risk_parity import equal_risk_contribution

COV = np.array([[0.04, 0.006, 0.0], [0.006, 0.09, 0.01], [0.0, 0.01, 0.16]])


def test_risk_shares_match_the_budgets():
    b = np.array([0.5, 0.3, 0.2])
    w = risk_budget_weights(COV, b)
    rc = w * (COV @ w)
    assert np.allclose(rc / rc.sum(), b, atol=1e-6)


def test_equal_budgets_reproduce_equal_risk_contribution():
    assert np.allclose(risk_budget_weights(COV, [1, 1, 1]), equal_risk_contribution(COV), atol=1e-6)
