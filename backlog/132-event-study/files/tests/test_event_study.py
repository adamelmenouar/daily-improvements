import numpy as np
import pytest
from trading.event_study import average_car


def test_jump_at_the_event_date_shows_up():
    rng = np.random.default_rng(132)
    r = rng.normal(0, 0.002, 3000)
    events = list(range(50, 2900, 50))
    r[events] += 0.05
    car = average_car(r, events, before=2, after=5)
    assert abs(car[1]) < 0.01 and car[3] > 0.04  # position 2 = jour 0


def test_edge_events_are_ignored():
    r = np.zeros(20)
    assert len(average_car(r, [0, 10, 19], 2, 2)) == 5


def test_no_usable_event():
    with pytest.raises(ValueError):
        average_car(np.zeros(10), [0], 2, 2)
