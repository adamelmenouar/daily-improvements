import pandas as pd
import pytest
from trading.atr import true_range, position_size


def test_true_range_uses_gap_from_previous_close():
    h, l, c = pd.Series([10, 15]), pd.Series([9, 14]), pd.Series([9.5, 14.5])
    tr = true_range(h, l, c)
    assert tr.iloc[1] == 5.5  # |15 - 9.5|


def test_position_size():
    assert position_size(100_000, 0.01, 2.5, 2.0) == 200.0


def test_invalid_atr():
    with pytest.raises(ValueError):
        position_size(1000, 0.01, 0)
