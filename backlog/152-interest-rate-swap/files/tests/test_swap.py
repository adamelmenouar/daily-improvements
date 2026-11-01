import numpy as np
from pricing.swap import par_swap_rate, payer_swap_value

DFS = 1.03 ** -np.arange(1, 6)


def test_par_rate_on_a_flat_curve():
    assert abs(par_swap_rate(DFS) - 0.03) < 1e-12


def test_value_is_zero_at_the_par_rate():
    assert abs(payer_swap_value(par_swap_rate(DFS), DFS, 1_000_000)) < 1e-6


def test_payer_gains_when_the_fixed_rate_is_below_par():
    assert payer_swap_value(0.02, DFS) > 0 > payer_swap_value(0.04, DFS)
