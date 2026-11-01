import numpy as np
from pricing.bootstrap import bootstrap_discount_factors, zero_rates


def test_flat_curve_gives_geometric_discount_factors():
    dfs = bootstrap_discount_factors([0.03] * 5)
    assert np.allclose(dfs, 1.03 ** -np.arange(1, 6))


def test_reprices_each_par_bond_at_one():
    par = [0.02, 0.025, 0.03, 0.033]
    dfs = bootstrap_discount_factors(par)
    for n, c in enumerate(par, start=1):
        assert abs(c * dfs[:n].sum() + dfs[n - 1] - 1) < 1e-12


def test_flat_par_curve_has_flat_zero_rates():
    assert np.allclose(zero_rates(bootstrap_discount_factors([0.04] * 6)), 0.04)
