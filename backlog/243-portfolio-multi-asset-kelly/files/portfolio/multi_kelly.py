"""Kelly multi-actifs en temps continu : f* = inv(Sigma) @ (mu - rf). Maximise la croissance géométrique."""
import numpy as np


def kelly_vector(mu, cov, rf=0.0):
    return np.linalg.solve(np.asarray(cov, dtype=float), np.asarray(mu, dtype=float) - rf)


def growth_rate(f, mu, cov, rf=0.0):
    f = np.asarray(f, dtype=float)
    return float(rf + f @ (np.asarray(mu, dtype=float) - rf) - 0.5 * f @ np.asarray(cov, dtype=float) @ f)
