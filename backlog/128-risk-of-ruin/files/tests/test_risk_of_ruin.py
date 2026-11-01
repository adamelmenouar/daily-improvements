import pytest
from trading.risk_of_ruin import risk_of_ruin


def test_fair_game_is_certain_ruin():
    assert risk_of_ruin(0.5, 20) == 1.0


def test_known_value():
    assert abs(risk_of_ruin(0.6, 10) - (0.8 / 1.2) ** 10) < 1e-12


def test_more_capital_means_less_ruin():
    assert risk_of_ruin(0.55, 50) < risk_of_ruin(0.55, 10)


def test_invalid_probability():
    with pytest.raises(ValueError):
        risk_of_ruin(1.5, 10)
