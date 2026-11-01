import numpy as np
from scipy.stats import norm
from risk.es_backtest import es_backtest_z1

SIGMA = 0.01
R = np.random.default_rng(108).normal(0, SIGMA, 200_000)
VAR95 = norm.ppf(0.95) * SIGMA
ES95 = SIGMA * norm.pdf(norm.ppf(0.95)) / 0.05


def test_correct_es_gives_z1_near_zero():
    assert abs(es_backtest_z1(R, VAR95, ES95)) < 0.02


def test_underestimated_es_gives_positive_z1():
    assert es_backtest_z1(R, VAR95, 0.7 * ES95) > 0.3


def test_no_exception_gives_nan():
    assert np.isnan(es_backtest_z1([0.01, 0.0], 0.05, 0.08))
