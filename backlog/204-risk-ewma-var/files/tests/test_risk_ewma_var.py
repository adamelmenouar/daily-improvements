import numpy as np
from risk.ewma_var import ewma_var
from risk.var.var import parametric_var


def test_reacts_to_a_volatility_spike_faster_than_a_flat_estimate():
    rng = np.random.default_rng(190)
    r = np.concatenate([rng.normal(0, 0.005, 500), rng.normal(0, 0.03, 20)])
    assert ewma_var(r, 0.99) > 2 * parametric_var(r, 0.99)


def test_close_to_gaussian_var_in_a_stable_regime():
    r = np.random.default_rng(191).normal(0, 0.01, 5000)
    assert abs(ewma_var(r, 0.99) - 2.326 * 0.01) < 0.004


def test_higher_confidence_means_larger_var():
    r = np.random.default_rng(192).normal(0, 0.01, 500)
    assert ewma_var(r, 0.999) > ewma_var(r, 0.95)
