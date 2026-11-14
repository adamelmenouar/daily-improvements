import numpy as np
from trading.parabolic_sar import parabolic_sar


def test_sar_stays_below_the_lows_in_a_steady_uptrend():
    c = np.linspace(100, 200, 100)
    sar, trend = parabolic_sar(c + 1, c - 1)
    assert (trend == 1).all() and (sar[1:] < (c - 1)[1:]).all()


def test_reversal_flips_the_trend_and_puts_sar_above_prices():
    c = np.concatenate([np.linspace(100, 150, 50), np.linspace(150, 90, 50)])
    sar, trend = parabolic_sar(c + 1, c - 1)
    assert trend[-1] == -1 and sar[-1] > (c + 1)[-1]


def test_acceleration_is_capped():
    c = np.linspace(100, 300, 200)
    sar, _ = parabolic_sar(c + 1, c - 1, 0.02, 0.2)
    assert np.isfinite(sar).all()
