import numpy as np
from utils.returns import to_log, to_simple, cumulative_return, annualize_return, annualize_vol


def test_log_round_trip():
    r = np.array([0.01, -0.02, 0.03])
    assert np.allclose(to_simple(to_log(r)), r)


def test_cumulative_known_value():
    assert abs(cumulative_return([0.1, 0.1]) - 0.21) < 1e-12


def test_annualize_return_of_daily_one_percent_for_a_year():
    assert abs(annualize_return([0.01] * 252) - (1.01**252 - 1)) < 1e-9


def test_annualize_vol_scaling():
    r = np.random.default_rng(81).normal(0, 0.01, 500)
    assert abs(annualize_vol(r) - r.std(ddof=1) * np.sqrt(252)) < 1e-12
