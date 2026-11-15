from math import pi, sqrt
from pricing.bachelier import bachelier_call, bachelier_put


def test_put_call_parity():
    f, k = 101.0, 99.0
    assert abs(bachelier_call(f, k, 1, 5) - bachelier_put(f, k, 1, 5) - (f - k)) < 1e-12


def test_atm_closed_form():
    assert abs(bachelier_call(100, 100, 1, 8) - 8 / sqrt(2 * pi)) < 1e-12


def test_works_with_negative_forward():
    assert bachelier_call(-0.5, 0.0, 1, 1.0) > 0
