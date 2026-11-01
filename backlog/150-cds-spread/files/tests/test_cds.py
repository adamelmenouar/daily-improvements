import pytest
from pricing.cds import cds_spread, implied_default_prob


def test_known_value():
    assert abs(cds_spread(0.02, 0.4) - 0.012) < 1e-12


def test_round_trip():
    assert abs(implied_default_prob(cds_spread(0.035, 0.3), 0.3) - 0.035) < 1e-12


def test_full_recovery_is_rejected():
    with pytest.raises(ValueError):
        implied_default_prob(0.01, 1.0)
