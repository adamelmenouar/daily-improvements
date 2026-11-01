import numpy as np
from risk.nearest_psd import nearest_correlation

BAD = np.array([[1, 0.9, -0.9], [0.9, 1, 0.9], [-0.9, 0.9, 1]])


def test_input_is_indeed_invalid():
    assert np.linalg.eigvalsh(BAD).min() < 0


def test_output_is_valid_correlation_matrix():
    out = nearest_correlation(BAD)
    assert np.linalg.eigvalsh(out).min() > -1e-10
    assert np.allclose(np.diag(out), 1) and np.allclose(out, out.T)


def test_valid_matrix_is_unchanged():
    ok = np.array([[1, 0.3], [0.3, 1]])
    assert np.allclose(nearest_correlation(ok), ok, atol=1e-6)
