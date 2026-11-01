import numpy as np
from risk.copula import simulate_gaussian_copula, joint_exceedance


def test_marginals_are_uniform():
    u = simulate_gaussian_copula([[1, 0.6], [0.6, 1]], 50_000)
    assert np.allclose(u.mean(axis=0), 0.5, atol=0.01)


def test_independence_gives_product_of_marginals():
    u = simulate_gaussian_copula(np.eye(2), 200_000)
    assert abs(joint_exceedance(u, 0.1) - 0.01) < 0.003


def test_correlation_raises_joint_crash_probability():
    hi = joint_exceedance(simulate_gaussian_copula([[1, 0.9], [0.9, 1]], 200_000), 0.05)
    assert hi > 0.0025 * 4
