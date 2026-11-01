from risk.stress import run_scenarios, stress_pnl


def test_all_cash_is_unaffected():
    assert stress_pnl([0, 0, 0], [-0.3, -0.1, 0.1]) == 0.0


def test_scenarios_return_all_names():
    res = run_scenarios([0.5, 0.2, 0.3])
    assert set(res) == {"krach_actions", "hausse_taux", "crise_credit"}


def test_equity_heavy_portfolio_suffers_in_crash():
    assert run_scenarios([1, 0, 0])["krach_actions"] == -0.30
