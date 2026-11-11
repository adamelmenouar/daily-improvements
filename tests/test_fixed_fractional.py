import pytest
from trading.fixed_fractional import fixed_fractional_size


def test_known_value():
    assert fixed_fractional_size(100_000, 0.01, 50.0, 48.0) == 500.0


def test_works_for_short_positions():
    assert fixed_fractional_size(100_000, 0.01, 50.0, 52.0) == 500.0


def test_zero_distance_rejected():
    with pytest.raises(ValueError):
        fixed_fractional_size(1000, 0.01, 10, 10)
