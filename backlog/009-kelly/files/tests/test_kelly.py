import pytest
from trading.kelly import kelly_fraction, half_kelly


def test_fair_coin_even_odds_is_zero():
    assert kelly_fraction(0.5, 1.0) == 0.0


def test_known_value():
    assert abs(kelly_fraction(0.6, 1.0) - 0.2) < 1e-12


def test_negative_edge_gives_zero_half_kelly():
    assert half_kelly(0.4, 1.0) == 0.0


def test_invalid_input():
    with pytest.raises(ValueError):
        kelly_fraction(1.5, 1.0)
