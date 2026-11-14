import numpy as np
from risk.psr import probabilistic_sharpe


def test_strong_track_record_is_nearly_certain():
    r = np.random.default_rng(200).normal(0.003, 0.01, 2000)
    assert probabilistic_sharpe(r) > 0.99


def test_zero_edge_is_a_coin_flip():
    r = np.random.default_rng(201).normal(0.0, 0.01, 2000)
    assert 0.05 < probabilistic_sharpe(r) < 0.95


def test_longer_history_raises_confidence():
    r = np.random.default_rng(202).normal(0.0008, 0.01, 4000)
    assert probabilistic_sharpe(r) > probabilistic_sharpe(r[:500])
