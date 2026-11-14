from fixedincome.horizon_return import horizon_total_return


def test_par_bond_with_stable_rates_returns_its_yield():
    assert abs(horizon_total_return(100, 0.05, 0.05, 10, 5, 0.05, 0.05) - 0.05) < 1e-9


def test_rising_exit_yield_hurts():
    base = horizon_total_return(100, 0.05, 0.05, 10, 5, 0.05, 0.05)
    assert horizon_total_return(100, 0.05, 0.05, 10, 5, 0.05, 0.08) < base


def test_better_reinvestment_helps():
    assert horizon_total_return(100, 0.05, 0.05, 10, 5, 0.07, 0.05) > horizon_total_return(100, 0.05, 0.05, 10, 5, 0.03, 0.05)
