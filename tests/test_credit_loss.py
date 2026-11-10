import pytest
from risk.credit_loss import expected_loss


def test_single_loan():
    assert abs(expected_loss(0.02, 0.45, 1_000_000) - 9000) < 1e-9


def test_portfolio_is_sum_of_loans():
    assert abs(expected_loss([0.01, 0.05], [0.5, 0.4], [100, 200]) - (0.5 + 4.0)) < 1e-12


def test_invalid_probability():
    with pytest.raises(ValueError):
        expected_loss(1.2, 0.4, 100)
