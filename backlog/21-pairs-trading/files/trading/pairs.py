"""Pairs trading : spread de deux actifs et signal sur son z-score."""
import numpy as np
import pandas as pd


def spread(a, b):
    """log(a) - beta * log(b), beta estimé par régression."""
    la, lb = np.log(a), np.log(b)
    beta = np.cov(la, lb, ddof=1)[0, 1] / np.var(lb, ddof=1)
    return la - beta * lb


def zscore(s, window=60):
    return (s - s.rolling(window).mean()) / s.rolling(window).std()


def pairs_signal(z, entry=2.0, exit_=0.5):
    """+1 (long spread) si z < -entry, -1 si z > entry, 0 quand |z| < exit_, sinon position conservée."""
    pos = pd.Series(float("nan"), index=z.index)
    pos[z < -entry] = 1.0
    pos[z > entry] = -1.0
    pos[z.abs() < exit_] = 0.0
    return pos.ffill().fillna(0.0)
