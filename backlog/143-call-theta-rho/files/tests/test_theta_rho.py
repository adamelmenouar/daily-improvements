from pricing.black_scholes import bs_call
from pricing.theta_rho import call_theta, call_rho

ARGS = (100, 100, 1, 0.05, 0.2)


def test_theta_matches_finite_difference_in_maturity():
    h = 1e-5
    fd = -(bs_call(100, 100, 1 + h, 0.05, 0.2) - bs_call(100, 100, 1 - h, 0.05, 0.2)) / (2 * h)
    assert abs(call_theta(*ARGS) - fd) < 1e-4


def test_rho_matches_finite_difference_in_rate():
    h = 1e-6
    fd = (bs_call(100, 100, 1, 0.05 + h, 0.2) - bs_call(100, 100, 1, 0.05 - h, 0.2)) / (2 * h)
    assert abs(call_rho(*ARGS) - fd) < 1e-4


def test_time_decay_is_negative_and_rho_positive():
    assert call_theta(*ARGS) < 0 < call_rho(*ARGS)
