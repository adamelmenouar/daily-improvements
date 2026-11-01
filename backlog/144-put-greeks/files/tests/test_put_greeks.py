from pricing.black_scholes import bs_put
from pricing.put_greeks import put_delta, put_rho, put_theta

ARGS = (100, 105, 0.75, 0.04, 0.25)


def test_delta_matches_finite_difference():
    h = 1e-4
    fd = (bs_put(100 + h, 105, 0.75, 0.04, 0.25) - bs_put(100 - h, 105, 0.75, 0.04, 0.25)) / (2 * h)
    assert abs(put_delta(*ARGS) - fd) < 1e-6


def test_rho_matches_finite_difference():
    h = 1e-6
    fd = (bs_put(100, 105, 0.75, 0.04 + h, 0.25) - bs_put(100, 105, 0.75, 0.04 - h, 0.25)) / (2 * h)
    assert abs(put_rho(*ARGS) - fd) < 1e-4


def test_theta_matches_finite_difference():
    h = 1e-5
    fd = -(bs_put(100, 105, 0.75 + h, 0.04, 0.25) - bs_put(100, 105, 0.75 - h, 0.04, 0.25)) / (2 * h)
    assert abs(put_theta(*ARGS) - fd) < 1e-4
