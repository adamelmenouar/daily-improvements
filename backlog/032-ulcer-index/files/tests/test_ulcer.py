import numpy as np
from risk.ulcer import ulcer_index


def test_rising_prices_have_zero_ulcer():
    assert ulcer_index([100, 101, 102, 105]) == 0.0


def test_known_value():
    assert abs(ulcer_index([100, 50, 100]) - np.sqrt(0.25 / 3)) < 1e-12
