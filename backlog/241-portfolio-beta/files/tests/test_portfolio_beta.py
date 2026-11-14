import numpy as np
from portfolio.portfolio_beta import portfolio_beta, betas_from_returns


def test_known_value():
    assert abs(portfolio_beta([0.5, 0.5], [1.2, 0.8]) - 1.0) < 1e-12


def test_beta_of_the_portfolio_equals_weighted_betas():
    rng = np.random.default_rng(238)
    m = rng.normal(0, 0.01, 2000)
    a = np.column_stack([1.3 * m + rng.normal(0, 0.005, 2000), 0.6 * m + rng.normal(0, 0.005, 2000)])
    w = np.array([0.7, 0.3])
    direct = np.cov(a @ w, m, ddof=1)[0, 1] / m.var(ddof=1)
    assert abs(portfolio_beta(w, betas_from_returns(a, m)) - direct) < 1e-12
