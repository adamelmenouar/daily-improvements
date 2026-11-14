import math
from credit.scorecard import score_from_pd


def test_base_odds_give_base_score():
    pd_ = 1 / 51  # cotes sains/défaillants = 50
    assert abs(score_from_pd(pd_) - 600) < 1e-9


def test_doubling_the_odds_adds_pdo_points():
    p1, p2 = 1 / 51, 1 / 101  # cotes 50 puis 100
    assert abs(score_from_pd(p2) - score_from_pd(p1) - 20) < 1e-9


def test_riskier_borrowers_score_lower():
    assert score_from_pd(0.10) < score_from_pd(0.01)
