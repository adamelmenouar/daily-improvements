import numpy as np
from risk.kupiec import kupiec_test
from risk.var.var import historical_var


def test_well_calibrated_var_is_not_rejected():
    r = np.random.default_rng(7).normal(0, 0.01, 5000)
    _, _, p = kupiec_test(r, historical_var(r))
    assert p > 0.05


def test_too_small_var_is_rejected():
    r = np.random.default_rng(7).normal(0, 0.01, 5000)
    _, _, p = kupiec_test(r, 0.5 * historical_var(r))
    assert p < 0.01
