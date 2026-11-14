import numpy as np
from risk.student_t_var import student_t_var
from risk.var.var import parametric_var, historical_var


def test_fat_tailed_data_gives_a_larger_extreme_var_than_the_normal():
    r = np.random.default_rng(195).standard_t(3, 20_000) * 0.01
    assert student_t_var(r, 0.999) > parametric_var(r, 0.999)


def test_close_to_empirical_var_at_99():
    r = np.random.default_rng(196).standard_t(4, 30_000) * 0.01
    assert abs(student_t_var(r, 0.99) - historical_var(r, 0.99)) / historical_var(r, 0.99) < 0.1
