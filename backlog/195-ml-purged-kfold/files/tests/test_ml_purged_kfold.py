import numpy as np
from ml.purged_kfold import purged_kfold_splits


def test_no_overlap_and_gap_around_the_test_block():
    for train, test in purged_kfold_splits(100, 5, purge=3, embargo=4):
        assert not set(train) & set(test)
        near = [i for i in train if test[0] - 3 <= i <= test[-1] + 4]
        assert near == []


def test_tests_cover_everything_once():
    covered = np.concatenate([t for _, t in purged_kfold_splits(103, 4)])
    assert sorted(covered) == list(range(103))


def test_no_purge_keeps_all_other_observations():
    for train, test in purged_kfold_splits(50, 5, purge=0, embargo=0):
        assert len(train) + len(test) == 50
