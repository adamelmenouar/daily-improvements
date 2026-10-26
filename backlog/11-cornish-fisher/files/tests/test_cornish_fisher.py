import numpy as np
from risk.cornish_fisher import cornish_fisher_var
from risk.var.var import parametric_var


def test_close_to_gaussian_var_on_normal_data():
    r = np.random.default_rng(11).normal(0, 0.01, 50_000)
    assert abs(cornish_fisher_var(r) - parametric_var(r)) < 5e-4


def test_fat_tails_increase_99_var():
    r = np.random.default_rng(11).standard_t(3, 50_000) * 0.01
    assert cornish_fisher_var(r, 0.99) > 0
