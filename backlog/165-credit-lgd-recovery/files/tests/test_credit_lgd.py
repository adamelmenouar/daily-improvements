import pytest
from credit.lgd import lgd_from_recoveries


def test_no_recovery_means_total_loss():
    assert lgd_from_recoveries(100, []) == 1.0


def test_known_value():
    assert abs(lgd_from_recoveries(100, [(1, 52.5)], 0.05) - 0.5) < 1e-12


def test_over_recovery_is_capped_at_zero():
    assert lgd_from_recoveries(100, [(0, 150)]) == 0.0


def test_later_recoveries_are_worth_less():
    assert lgd_from_recoveries(100, [(4, 60)]) > lgd_from_recoveries(100, [(1, 60)])


def test_invalid_exposure():
    with pytest.raises(ValueError):
        lgd_from_recoveries(0, [])
