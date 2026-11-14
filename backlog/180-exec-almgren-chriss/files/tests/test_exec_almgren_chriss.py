import numpy as np
from execution.almgren_chriss import optimal_holdings, kappa_from_params


def test_endpoints():
    x = optimal_holdings(1000, 1.0, 10, 2.0)
    assert abs(x[0] - 1000) < 1e-9 and abs(x[-1]) < 1e-9


def test_zero_risk_aversion_is_linear():
    x = optimal_holdings(1000, 1.0, 10, 0.0)
    assert np.allclose(np.diff(x), -100)


def test_more_risk_aversion_sells_faster_early_on():
    slow, fast = optimal_holdings(1000, 1.0, 10, 0.5), optimal_holdings(1000, 1.0, 10, 5.0)
    assert fast[3] < slow[3]


def test_monotone_decreasing_and_kappa():
    assert (np.diff(optimal_holdings(1000, 1.0, 20, 3.0)) < 0).all()
    assert abs(kappa_from_params(4.0, 0.5, 1.0) - 1.0) < 1e-12
