import numpy as np
from risk.stressed_var import stressed_var
from risk.var.var import historical_var


def test_stressed_var_exceeds_normal_var_when_a_crisis_exists():
    rng = np.random.default_rng(114)
    r = np.concatenate([rng.normal(0, 0.005, 1000), rng.normal(0, 0.025, 250), rng.normal(0, 0.005, 1000)])
    assert stressed_var(r, 250, 0.99) > 2 * historical_var(r, 0.99)


def test_equals_plain_var_when_window_covers_everything():
    r = np.random.default_rng(115).normal(0, 0.01, 300)
    assert abs(stressed_var(r, 300, 0.95) - historical_var(r, 0.95)) < 1e-12
