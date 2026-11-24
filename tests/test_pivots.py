from trading.pivots import pivot_points


def test_known_values():
    lv = pivot_points(110.0, 90.0, 100.0)
    assert lv["P"] == 100.0 and lv["R1"] == 110.0 and lv["S1"] == 90.0
    assert lv["R2"] == 120.0 and lv["S2"] == 80.0


def test_levels_are_ordered():
    lv = pivot_points(105.0, 95.0, 101.0)
    assert lv["S2"] < lv["S1"] < lv["P"] < lv["R1"] < lv["R2"]
