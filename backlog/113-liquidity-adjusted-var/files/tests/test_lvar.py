import pytest
from risk.lvar import liquidity_adjusted_var


def test_adds_liquidation_cost():
    assert abs(liquidity_adjusted_var(0.02, 0.003) - 0.023) < 1e-12


def test_perfect_liquidity_changes_nothing():
    assert liquidity_adjusted_var(0.02, 0.0) == 0.02


def test_negative_inputs_rejected():
    with pytest.raises(ValueError):
        liquidity_adjusted_var(-0.01, 0.0)
