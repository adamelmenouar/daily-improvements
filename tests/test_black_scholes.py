from math import exp
from pricing.black_scholes import bs_call, bs_put


def test_known_value():
    # S=100, K=100, T=1, r=5%, sigma=20% -> call ~ 10.4506
    assert abs(bs_call(100, 100, 1, 0.05, 0.2) - 10.4506) < 1e-3


def test_put_call_parity():
    s, k, t, r, sig = 100, 95, 0.5, 0.03, 0.25
    assert abs(bs_call(s, k, t, r, sig) - bs_put(s, k, t, r, sig) - (s - k * exp(-r * t))) < 1e-9
