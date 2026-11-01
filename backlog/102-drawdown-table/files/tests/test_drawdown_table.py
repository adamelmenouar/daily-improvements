from risk.drawdown_table import top_drawdowns

R = [0.1, -0.1, -0.1, 0.3, -0.05]


def test_known_episodes():
    eps = top_drawdowns(R, 5)
    assert len(eps) == 2
    assert abs(eps[0]["depth"] - (0.891 / 1.1 - 1)) < 1e-12 and eps[0]["end"] == 3
    assert abs(eps[1]["depth"] + 0.05) < 1e-12 and eps[1]["end"] is None


def test_sorted_worst_first_and_limited():
    eps = top_drawdowns(R, 1)
    assert len(eps) == 1 and eps[0]["depth"] < -0.15


def test_no_drawdown_in_a_rising_market():
    assert top_drawdowns([0.01] * 10) == []
