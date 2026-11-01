import numpy as np
from portfolio.cppi import cppi_values


def test_floor_holds_when_no_gap_risk():
    r = np.random.default_rng(68).normal(0.0003, 0.008, 1000)  # pas de saut > 1/multiplicateur
    v = cppi_values(r, 0.8, 4.0)
    assert v.min() >= 80.0 - 1e-9


def test_all_cash_when_cushion_is_zero():
    v = cppi_values([0.5, -0.5], floor_fraction=1.0, rf=0.01)
    assert abs(v[1] - 101.0) < 1e-9


def test_starts_at_initial_value():
    assert cppi_values([0.01])[0] == 100.0
