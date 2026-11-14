import numpy as np
from credit.transitions import estimate_transition_matrix, n_year_matrix


def test_known_counts():
    p = estimate_transition_matrix([0, 0, 0, 0, 1, 1], [0, 0, 0, 1, 1, 2], 3)
    assert np.allclose(p[0], [0.75, 0.25, 0.0]) and np.allclose(p[1], [0, 0.5, 0.5])


def test_rows_sum_to_one_and_unseen_state_stays_put():
    p = estimate_transition_matrix([0, 1], [1, 2], 3)
    assert np.allclose(p.sum(axis=1), 1) and p[2, 2] == 1.0


def test_default_probability_grows_with_horizon():
    p = np.array([[0.90, 0.08, 0.02], [0.10, 0.80, 0.10], [0, 0, 1.0]])
    assert n_year_matrix(p, 5)[0, 2] > n_year_matrix(p, 1)[0, 2]
