from fixedincome.immunization import is_immunized, duration_gap


def test_matched_portfolio_is_immunized():
    assert is_immunized(105, 5.0, 100, 5.02)


def test_duration_mismatch_fails():
    assert not is_immunized(105, 3.0, 100, 5.0)


def test_underfunded_portfolio_fails():
    assert not is_immunized(95, 5.0, 100, 5.0)


def test_duration_gap_known_value():
    assert abs(duration_gap(100, 5.0, 80, 4.0) - (5.0 - 0.8 * 4.0)) < 1e-12
