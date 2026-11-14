from credit.altman import altman_z, altman_zone


def test_known_value():
    z = altman_z(20, 30, 15, 120, 150, 100, 60)
    assert abs(z - (1.2 * 0.2 + 1.4 * 0.3 + 3.3 * 0.15 + 0.6 * 2.0 + 1.0 * 1.5)) < 1e-12


def test_zones():
    assert altman_zone(4.0) == "safe" and altman_zone(2.0) == "grey" and altman_zone(1.0) == "distress"


def test_healthier_company_scores_higher():
    assert altman_z(30, 40, 20, 150, 160, 100, 50) > altman_z(5, 5, 1, 20, 80, 100, 90)
