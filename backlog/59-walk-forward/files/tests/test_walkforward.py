from trading.walkforward import walk_forward_splits


def test_known_splits():
    s = list(walk_forward_splits(10, 4, 2))
    assert [(list(a), list(b)) for a, b in s] == [
        ([0, 1, 2, 3], [4, 5]), ([2, 3, 4, 5], [6, 7]), ([4, 5, 6, 7], [8, 9])]


def test_test_always_after_train():
    for tr, te in walk_forward_splits(500, 100, 20):
        assert max(tr) < min(te)


def test_too_short_series_yields_nothing():
    assert list(walk_forward_splits(5, 4, 2)) == []
