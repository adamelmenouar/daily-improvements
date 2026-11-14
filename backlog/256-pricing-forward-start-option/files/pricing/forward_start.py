"""Call à départ différé : payoff max(S_T2 - alpha * S_T1, 0) payé en T2 (sans dividende)."""
from pricing.black_scholes import bs_call


def forward_start_call(s, alpha, t1, t2, r, sigma):
    """Par homogénéité, vaut S0 fois un call de strike alpha sur un spot de 1, d'échéance t2 - t1."""
    if t2 <= t1:
        raise ValueError("t2 doit être > t1")
    return s * bs_call(1.0, alpha, t2 - t1, r, sigma)
