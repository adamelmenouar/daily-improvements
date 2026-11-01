"""On-Balance Volume : volume cumulé signé par le sens du prix."""
import numpy as np


def on_balance_volume(close, volume):
    direction = np.sign(close.diff()).fillna(0.0)
    return (direction * volume).cumsum()
