import numpy as np
from risk.parametric_es import parametric_es
from risk.var.var import expected_shortfall, parametric_var

R = np.random.default_rng(197).normal(0.0003, 0.01, 200_000)


def test_matches_the_empirical_es_on_gaussian_data():
    assert abs(parametric_es(R, 0.975) - expected_shortfall(R, 0.975)) < 5e-4


def test_es_exceeds_var():
    assert parametric_es(R, 0.99) > parametric_var(R, 0.99)
