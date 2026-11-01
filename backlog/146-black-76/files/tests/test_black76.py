from math import exp
from pricing.black_scholes import bs_call
from pricing.black76 import black76_call, black76_put


def test_matches_black_scholes_on_the_equivalent_forward():
    s, k, t, r, sig = 100, 95, 0.5, 0.04, 0.2
    assert abs(black76_call(s * exp(r * t), k, t, r, sig) - bs_call(s, k, t, r, sig)) < 1e-10


def test_put_call_parity():
    f, k, t, r = 50.0, 52.0, 0.75, 0.03
    assert abs(black76_call(f, k, t, r, 0.3) - black76_put(f, k, t, r, 0.3) - exp(-r * t) * (f - k)) < 1e-12
