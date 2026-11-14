from microstructure.volume_bars import volume_bars


def test_known_bars():
    bars = volume_bars([10, 11, 9, 12, 13], [60, 50, 40, 70, 20], 100)
    assert bars == [(10, 11, 10, 11, 110), (9, 12, 9, 12, 110)]


def test_partial_bar_is_not_emitted():
    assert volume_bars([10, 11], [10, 10], 100) == []


def test_every_bar_reaches_the_threshold():
    bars = volume_bars(list(range(1, 51)), [7] * 50, 30)
    assert all(b[4] >= 30 for b in bars)
