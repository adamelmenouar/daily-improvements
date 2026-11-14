import pytest
from execution.twap import twap_schedule


def test_sum_is_exact():
    assert sum(twap_schedule(10_007, 12)) == 10_007


def test_slices_differ_by_at_most_one():
    s = twap_schedule(103, 10)
    assert max(s) - min(s) <= 1


def test_invalid_slices():
    with pytest.raises(ValueError):
        twap_schedule(100, 0)
