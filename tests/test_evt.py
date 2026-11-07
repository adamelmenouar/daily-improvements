import numpy as np
from risk.evt import evt_var


def test_close_to_empirical_on_fat_tails():
    r = np.random.default_rng(36).standard_t(3, 20_000) * 0.01
    emp = -np.quantile(r, 0.01)
    assert abs(evt_var(r, 0.99) - emp) / emp < 0.25


def test_higher_confidence_means_larger_var():
    r = np.random.default_rng(36).standard_t(3, 20_000) * 0.01
    assert evt_var(r, 0.999) > evt_var(r, 0.99)
