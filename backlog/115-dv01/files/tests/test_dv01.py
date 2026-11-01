from pricing.bond import bond_price, modified_duration
from risk.dv01 import dv01


def test_matches_modified_duration():
    args = (100, 0.05, 0.05, 10)
    assert abs(dv01(*args) - modified_duration(*args) * bond_price(*args) * 1e-4) < 1e-6


def test_longer_bond_has_larger_dv01():
    assert dv01(100, 0.05, 0.05, 20) > dv01(100, 0.05, 0.05, 5)
