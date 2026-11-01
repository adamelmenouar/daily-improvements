import pytest
from portfolio.glidepath import equity_weight


def test_endpoints_and_midpoint():
    assert equity_weight(25) == 0.9 and abs(equity_weight(65) - 0.3) < 1e-12
    assert abs(equity_weight(45) - 0.6) < 1e-12


def test_clipped_outside_the_range():
    assert equity_weight(18) == 0.9 and abs(equity_weight(80) - 0.3) < 1e-12


def test_monotonic_decrease():
    w = [equity_weight(a) for a in range(25, 66)]
    assert w == sorted(w, reverse=True)


def test_invalid_ages():
    with pytest.raises(ValueError):
        equity_weight(40, start_age=65, retire_age=25)
