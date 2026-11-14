import pytest
from fixedincome.rolldown import rolldown_return

M = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def test_flat_curve_returns_the_yield():
    assert abs(rolldown_return(100, 0.05, 5, M, [0.05] * 10) - 0.05) < 1e-9


def test_steep_curve_adds_roll_down_gain():
    steep = [0.01 + 0.005 * i for i in range(10)]
    r = rolldown_return(100, 0.05, 6, M, steep)
    y0 = steep[5]  # rendement à l'achat (6 ans)
    assert r > y0


def test_invalid_maturity():
    with pytest.raises(ValueError):
        rolldown_return(100, 0.05, 1, M, [0.05] * 10)
