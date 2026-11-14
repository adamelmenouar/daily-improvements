import numpy as np
import pytest
from execution.vwap_schedule import vwap_schedule


def test_sums_to_the_order_size():
    assert abs(vwap_schedule(1000, [5, 3, 2, 10]).sum() - 1000) < 1e-9


def test_proportional_to_volume():
    s = vwap_schedule(100, [1, 3])
    assert np.allclose(s, [25, 75])


def test_flat_profile_is_twap():
    assert np.allclose(vwap_schedule(100, [1, 1, 1, 1]), 25)


def test_invalid_profile():
    with pytest.raises(ValueError):
        vwap_schedule(100, [0, 0])
