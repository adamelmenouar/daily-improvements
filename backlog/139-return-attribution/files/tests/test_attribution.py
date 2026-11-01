import numpy as np
from portfolio.attribution import contributions, top_contributors


def test_contributions_sum_to_portfolio_return():
    w, r = [0.5, 0.3, 0.2], [0.10, -0.05, 0.02]
    assert abs(contributions(w, r).sum() - np.dot(w, r)) < 1e-12


def test_top_contributors():
    out = top_contributors(["A", "B", "C"], [0.5, 0.3, 0.2], [0.10, -0.05, 0.02], 2)
    assert [name for name, _ in out] == ["A", "C"]
