"""Call down-and-out (désactivé si le prix touche la barrière), surveillance discrète, Monte Carlo."""
import numpy as np


def down_and_out_call(s, k, barrier, t, r, sigma, n=20_000, steps=100, seed=0):
    dt = t / steps
    z = np.random.default_rng(seed).standard_normal((n, steps))
    paths = s * np.exp(np.cumsum((r - 0.5 * sigma**2) * dt + sigma * np.sqrt(dt) * z, axis=1))
    alive = (paths.min(axis=1) > barrier)
    payoff = np.maximum(paths[:, -1] - k, 0.0) * alive
    return float(np.exp(-r * t) * payoff.mean())
