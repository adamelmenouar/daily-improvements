import numpy as np
from portfolio.cvar_contributions import cvar_contributions
from portfolio.min_cvar import cvar

R = np.random.default_rng(240).normal([0.0004, 0.0005, 0.0003], [0.005, 0.01, 0.02], (3000, 3))
W = np.array([0.5, 0.3, 0.2])


def test_contributions_sum_to_the_portfolio_cvar():
    assert abs(cvar_contributions(R, W).sum() - cvar(R, W)) < 1e-12


def test_riskiest_asset_contributes_most_per_unit_of_weight():
    c = cvar_contributions(R, np.ones(3) / 3)
    assert c.argmax() == 2


def test_zero_weight_contributes_nothing():
    assert cvar_contributions(R, np.array([0.5, 0.5, 0.0]))[2] == 0.0
