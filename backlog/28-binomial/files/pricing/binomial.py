"""Arbre binomial de Cox-Ross-Rubinstein."""
import numpy as np


def crr_price(s, k, t, r, sigma, steps=200, kind="call", american=False):
    dt = t / steps
    u = np.exp(sigma * np.sqrt(dt))
    d = 1 / u
    p = (np.exp(r * dt) - d) / (u - d)
    disc = np.exp(-r * dt)
    sign = 1.0 if kind == "call" else -1.0
    prices = s * u ** np.arange(steps, -1, -1) * d ** np.arange(0, steps + 1)
    values = np.maximum(sign * (prices - k), 0.0)
    for i in range(steps - 1, -1, -1):
        values = disc * (p * values[:-1] + (1 - p) * values[1:])
        if american:
            prices = s * u ** np.arange(i, -1, -1) * d ** np.arange(0, i + 1)
            values = np.maximum(values, sign * (prices - k))
    return float(values[0])
