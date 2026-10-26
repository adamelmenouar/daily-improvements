import numpy as np
from risk.var.var import historical_var, parametric_var, expected_shortfall

R = np.random.default_rng(1).normal(0, 0.01, 10_000)


def test_es_at_least_var():
    assert expected_shortfall(R) >= historical_var(R) > 0


def test_param_close_to_historical_on_gaussian():
    assert abs(parametric_var(R) - historical_var(R)) < 0.002
