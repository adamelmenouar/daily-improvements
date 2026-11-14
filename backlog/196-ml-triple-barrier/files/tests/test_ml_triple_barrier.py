from ml.triple_barrier import triple_barrier_label


def test_profit_barrier_first():
    assert triple_barrier_label([100, 101, 104, 90], 0, 0.03, 0.05, 10) == 1


def test_stop_barrier_first():
    assert triple_barrier_label([100, 99, 94, 110], 0, 0.10, 0.05, 10) == -1


def test_time_barrier():
    assert triple_barrier_label([100, 101, 99, 105], 0, 0.10, 0.10, 2) == 0


def test_horizon_is_respected():
    assert triple_barrier_label([100, 100, 100, 120], 0, 0.1, 0.1, 2) == 0
