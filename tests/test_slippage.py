import pytest
from trading.slippage import fixed_bps_cost, square_root_impact


def test_fixed_cost():
    assert fixed_bps_cost(1_000_000, 2.0) == 200.0


def test_impact_grows_with_size_but_less_than_linearly():
    a = square_root_impact(10_000, 1_000_000, 0.02)
    b = square_root_impact(40_000, 1_000_000, 0.02)
    assert abs(b / a - 2.0) < 1e-12


def test_zero_order_has_no_impact():
    assert square_root_impact(0, 1e6, 0.02) == 0.0


def test_invalid_volume():
    with pytest.raises(ValueError):
        square_root_impact(1, 0, 0.02)
