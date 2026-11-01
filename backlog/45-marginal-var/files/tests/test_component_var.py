import numpy as np
from scipy.stats import norm
from risk.component_var import component_var

COV = np.array([[0.04, 0.01], [0.01, 0.09]])


def test_components_sum_to_portfolio_var():
    w = np.array([0.6, 0.4])
    assert abs(component_var(w, COV, 0.99).sum() - norm.ppf(0.99) * np.sqrt(w @ COV @ w)) < 1e-12


def test_zero_weight_zero_contribution():
    assert component_var([1.0, 0.0], COV)[1] == 0.0
