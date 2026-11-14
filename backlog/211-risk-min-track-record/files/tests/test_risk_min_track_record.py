import numpy as np
from risk.min_track_record import min_track_record_length

R = np.random.default_rng(203).normal(0.001, 0.01, 3000)


def test_better_strategy_needs_less_history():
    assert min_track_record_length(R * 1.0 + 0.002) < min_track_record_length(R)


def test_losing_strategy_never_qualifies():
    assert min_track_record_length(-np.abs(R)) == float("inf")


def test_higher_confidence_needs_more_history():
    assert min_track_record_length(R, 0.0, 0.99) > min_track_record_length(R, 0.0, 0.90)
