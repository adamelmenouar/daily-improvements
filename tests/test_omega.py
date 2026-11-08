from risk.omega import omega_ratio


def test_known_value():
    assert abs(omega_ratio([0.02, -0.01, 0.01, -0.02]) - 1.0) < 1e-12


def test_no_losses_is_infinite():
    assert omega_ratio([0.01, 0.02]) == float("inf")


def test_higher_threshold_lowers_omega():
    r = [0.03, -0.01, 0.02, 0.01, -0.02]
    assert omega_ratio(r, 0.01) < omega_ratio(r, 0.0)
