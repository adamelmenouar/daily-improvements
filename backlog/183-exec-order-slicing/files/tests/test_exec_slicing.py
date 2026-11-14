import pytest
from execution.slicing import iceberg_slices


def test_known_split():
    assert iceberg_slices(1050, 200) == [200, 200, 200, 200, 200, 50]


def test_exact_multiple():
    assert iceberg_slices(1000, 250) == [250] * 4


def test_sum_preserved():
    assert sum(iceberg_slices(12_345, 777)) == 12_345


def test_invalid_display():
    with pytest.raises(ValueError):
        iceberg_slices(100, 0)
