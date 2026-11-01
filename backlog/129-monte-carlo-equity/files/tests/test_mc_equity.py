import numpy as np
from trading.mc_equity import simulate_max_drawdowns

TRADES = np.random.default_rng(130).normal(0.002, 0.02, 200)


def test_drawdowns_are_never_positive():
    assert (simulate_max_drawdowns(TRADES, 300) <= 0).all()


def test_reproducible():
    assert np.array_equal(simulate_max_drawdowns(TRADES, 100, seed=2), simulate_max_drawdowns(TRADES, 100, seed=2))


def test_a_riskier_strategy_has_deeper_drawdowns():
    calm = np.median(simulate_max_drawdowns(TRADES * 0.5, 300))
    wild = np.median(simulate_max_drawdowns(TRADES * 2.0, 300))
    assert wild < calm
