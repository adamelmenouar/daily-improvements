import pytest
from utils.ts_split import time_split


def test_sizes_and_order():
    train, test = time_split(100, 0.7)
    assert len(train) == 70 and len(test) == 30 and max(train) < min(test)


def test_covers_everything_without_overlap():
    train, test = time_split(53, 0.6)
    assert list(train) + list(test) == list(range(53))


def test_invalid_fraction():
    with pytest.raises(ValueError):
        time_split(10, 1.0)
