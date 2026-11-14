from ml.classification_metrics import confusion_counts, precision_recall_f1

Y, P = [1, 1, 1, 0, 0, 0, 0, 1], [1, 1, 0, 0, 0, 1, 0, 0]


def test_confusion_counts():
    assert confusion_counts(Y, P) == (2, 1, 3, 2)


def test_known_scores():
    p, r, f = precision_recall_f1(Y, P)
    assert abs(p - 2 / 3) < 1e-12 and abs(r - 0.5) < 1e-12 and abs(f - 4 / 7) < 1e-12


def test_perfect_prediction():
    assert precision_recall_f1([1, 0, 1], [1, 0, 1]) == (1.0, 1.0, 1.0)


def test_no_positive_prediction_does_not_crash():
    assert precision_recall_f1([1, 0], [0, 0]) == (0.0, 0.0, 0.0)
