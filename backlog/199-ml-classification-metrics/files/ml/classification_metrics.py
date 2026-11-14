"""Métriques de classification binaire."""
import numpy as np


def confusion_counts(y_true, y_pred):
    t, p = np.asarray(y_true, dtype=int), np.asarray(y_pred, dtype=int)
    return int(((p == 1) & (t == 1)).sum()), int(((p == 1) & (t == 0)).sum()), \
        int(((p == 0) & (t == 0)).sum()), int(((p == 0) & (t == 1)).sum())  # tp, fp, tn, fn


def precision_recall_f1(y_true, y_pred):
    tp, fp, _, fn = confusion_counts(y_true, y_pred)
    precision = tp / (tp + fp) if tp + fp else 0.0
    recall = tp / (tp + fn) if tp + fn else 0.0
    f1 = 2 * precision * recall / (precision + recall) if precision + recall else 0.0
    return precision, recall, f1
