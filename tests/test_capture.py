import numpy as np
from risk.capture import up_capture, down_capture

B = np.random.default_rng(40).normal(0, 0.01, 500)


def test_identical_portfolio_captures_everything():
    assert abs(up_capture(B, B) - 1) < 1e-12 and abs(down_capture(B, B) - 1) < 1e-12


def test_defensive_portfolio_captures_less_downside():
    assert down_capture(0.5 * B, B) < 1 and abs(down_capture(0.5 * B, B) - 0.5) < 1e-12
