from math import exp
from pricing.black_scholes import bs_call
from pricing.garman_kohlhagen import fx_call, fx_put


def test_zero_foreign_rate_reduces_to_black_scholes():
    assert abs(fx_call(1.10, 1.12, 0.5, 0.03, 0.0, 0.1) - bs_call(1.10, 1.12, 0.5, 0.03, 0.1)) < 1e-12


def test_put_call_parity():
    s, k, t, rd, rf = 1.10, 1.12, 0.5, 0.03, 0.01
    lhs = fx_call(s, k, t, rd, rf, 0.1) - fx_put(s, k, t, rd, rf, 0.1)
    assert abs(lhs - (s * exp(-rf * t) - k * exp(-rd * t))) < 1e-12
