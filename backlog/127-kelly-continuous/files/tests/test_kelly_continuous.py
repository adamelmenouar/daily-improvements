import pytest
from trading.kelly_continuous import continuous_kelly


def test_known_value():
    assert abs(continuous_kelly(0.08, 0.2) - 2.0) < 1e-12


def test_no_edge_means_no_bet():
    assert continuous_kelly(0.03, 0.2, rf=0.03) == 0.0


def test_invalid_sigma():
    with pytest.raises(ValueError):
        continuous_kelly(0.05, 0.0)
