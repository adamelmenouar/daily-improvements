import pytest
from trading.fibonacci import fibonacci_retracements


def test_known_levels_in_an_uptrend():
    lv = fibonacci_retracements(200, 100)
    assert lv[0.5] == 150 and abs(lv[0.618] - 138.2) < 1e-9


def test_downtrend_levels_are_mirrored():
    lv = fibonacci_retracements(200, 100, uptrend=False)
    assert lv[0.5] == 150 and abs(lv[0.236] - 123.6) < 1e-9


def test_invalid_swing():
    with pytest.raises(ValueError):
        fibonacci_retracements(100, 100)
