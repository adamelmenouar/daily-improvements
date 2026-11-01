from trading.bracket import simulate_bracket


def test_target_hit_first():
    assert simulate_bracket([100, 101, 103, 98], 0, 0.05, 0.03) == (2, 0.03)


def test_stop_hit_first():
    assert simulate_bracket([100, 99, 94, 110], 0, 0.05, 0.10) == (2, -0.05)


def test_no_touch_exits_at_the_end():
    i, r = simulate_bracket([100, 101, 100.5], 0, 0.05, 0.05)
    assert i == 2 and abs(r - 0.005) < 1e-12
