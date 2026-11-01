import numpy as np
from pricing.black_scholes import bs_call
from pricing.asian_geometric import geometric_asian_call


def test_cheaper_than_the_vanilla_call():
    assert 0 < geometric_asian_call(100, 100, 1, 0.05, 0.2) < bs_call(100, 100, 1, 0.05, 0.2)


def test_short_maturity_atm_is_vanilla_divided_by_sqrt_three():
    ratio = geometric_asian_call(100, 100, 1e-4, 0.05, 0.2) / bs_call(100, 100, 1e-4, 0.05, 0.2)
    assert abs(ratio - 1 / 3**0.5) < 0.01


def test_close_to_monte_carlo_with_discrete_monitoring():
    rng = np.random.default_rng(149)
    n, steps, s0, k, t, r, sig = 40_000, 250, 100.0, 100.0, 1.0, 0.05, 0.2
    dt = t / steps
    z = rng.standard_normal((n, steps))
    logp = np.log(s0) + np.cumsum((r - 0.5 * sig**2) * dt + sig * np.sqrt(dt) * z, axis=1)
    pay = np.maximum(np.exp(logp.mean(axis=1)) - k, 0)
    mc, se = np.exp(-r * t) * pay.mean(), np.exp(-r * t) * pay.std() / np.sqrt(n)
    assert abs(geometric_asian_call(s0, k, t, r, sig) - mc) < 4 * se + 0.1
