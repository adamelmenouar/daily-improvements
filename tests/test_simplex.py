import numpy as np
from portfolio.simplex import project_to_simplex


def test_known_values():
    assert np.allclose(project_to_simplex([2.0, 0.0]), [1.0, 0.0])
    assert np.allclose(project_to_simplex([1.0, 1.0]), [0.5, 0.5])


def test_output_is_always_a_valid_long_only_allocation():
    rng = np.random.default_rng(139)
    for _ in range(100):
        p = project_to_simplex(rng.normal(0, 2, 6))
        assert abs(p.sum() - 1) < 1e-12 and (p >= 0).all()


def test_valid_weights_are_unchanged():
    w = np.array([0.2, 0.3, 0.5])
    assert np.allclose(project_to_simplex(w), w)
