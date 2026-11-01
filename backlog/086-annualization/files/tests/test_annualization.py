import pytest
from utils.annualization import periods_per_year, scale_volatility


def test_known_frequencies():
    assert periods_per_year("D") == 252 and periods_per_year("m") == 12


def test_daily_to_annual_volatility():
    assert abs(scale_volatility(0.01, "D", "Y") - 0.01 * 252**0.5) < 1e-12


def test_round_trip():
    assert abs(scale_volatility(scale_volatility(0.02, "M", "Y"), "Y", "M") - 0.02) < 1e-12


def test_unknown_frequency():
    with pytest.raises(ValueError):
        periods_per_year("H")
