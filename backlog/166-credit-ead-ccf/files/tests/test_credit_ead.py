import pytest
from credit.ead import exposure_at_default


def test_known_value():
    assert exposure_at_default(40, 100, 0.5) == 70.0


def test_fully_drawn_line_has_no_ccf_effect():
    assert exposure_at_default(100, 100, 0.9) == 100.0


def test_invalid_inputs():
    with pytest.raises(ValueError):
        exposure_at_default(120, 100)
    with pytest.raises(ValueError):
        exposure_at_default(10, 100, 1.5)
