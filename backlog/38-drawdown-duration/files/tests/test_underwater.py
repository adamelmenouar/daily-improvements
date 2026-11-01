from risk.underwater import max_underwater_duration


def test_known_case():
    assert max_underwater_duration([0.10, -0.05, -0.02, 0.20, -0.01]) == 2


def test_always_rising_is_zero():
    assert max_underwater_duration([0.01] * 20) == 0


def test_never_recovering():
    assert max_underwater_duration([0.1, -0.5, 0.01, 0.01]) == 3
