import numpy as np
from fixedincome.spot_forward import forwards_from_spots, spots_from_forwards


def test_flat_curve_has_flat_forwards():
    assert np.allclose(forwards_from_spots([0.04] * 5), 0.04)


def test_round_trip():
    spots = [0.02, 0.025, 0.03, 0.034]
    assert np.allclose(spots_from_forwards(forwards_from_spots(spots)), spots)


def test_upward_curve_has_forwards_above_spots():
    f = forwards_from_spots([0.02, 0.03, 0.04])
    assert f[1] > 0.03 and f[2] > f[1]
