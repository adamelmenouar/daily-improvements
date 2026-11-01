import pytest
from portfolio.leverage import levered_return


def test_no_leverage_is_unchanged():
    assert levered_return(0.07, 1.0, 0.03) == 0.07


def test_known_value():
    assert abs(levered_return(0.10, 2.0, 0.04) - 0.16) < 1e-12


def test_leverage_amplifies_losses_too():
    assert levered_return(-0.05, 3.0, 0.02) < -0.05


def test_invalid_leverage():
    with pytest.raises(ValueError):
        levered_return(0.1, 0.5, 0.02)
