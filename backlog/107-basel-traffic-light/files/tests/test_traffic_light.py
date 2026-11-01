from risk.traffic_light import traffic_light


def test_zones_for_the_standard_basel_setting():
    assert traffic_light(2) == "green" and traffic_light(4) == "green"
    assert traffic_light(5) == "yellow" and traffic_light(9) == "yellow"
    assert traffic_light(20) == "red"


def test_more_exceptions_never_improve_the_zone():
    order = {"green": 0, "yellow": 1, "red": 2}
    zones = [order[traffic_light(k)] for k in range(0, 30)]
    assert zones == sorted(zones)
