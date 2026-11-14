import numpy as np
from risk.filtered_hs import filtered_hs_var
from risk.var.var import historical_var


def test_high_current_volatility_raises_the_var_above_plain_historical():
    rng = np.random.default_rng(193)
    r = np.concatenate([rng.normal(0, 0.005, 1000), rng.normal(0, 0.02, 30)])
    assert filtered_hs_var(r, 0.99) > 1.5 * historical_var(r, 0.99)


def test_low_current_volatility_lowers_it():
    rng = np.random.default_rng(194)
    r = np.concatenate([rng.normal(0, 0.02, 1000), rng.normal(0, 0.004, 60)])
    assert filtered_hs_var(r, 0.99) < historical_var(r, 0.99)
