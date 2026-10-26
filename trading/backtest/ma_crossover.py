"""Backtest vectorisé d'un croisement de moyennes mobiles (long/flat)."""
import numpy as np
import pandas as pd


def simulate_prices(n=1000, mu=0.0003, sigma=0.01, seed=0, start=100.0):
    rng = np.random.default_rng(seed)
    return pd.Series(start * np.exp(np.cumsum(rng.normal(mu, sigma, n))))


def backtest(prices, fast=20, slow=50):
    """Retourne les rendements de la stratégie. Signal décalé d'un jour (pas de look-ahead)."""
    if fast >= slow:
        raise ValueError("fast doit être < slow")
    signal = (prices.rolling(fast).mean() > prices.rolling(slow).mean()).astype(float)
    return prices.pct_change() * signal.shift(1)


def sharpe(returns, periods=252):
    r = returns.dropna()
    return float(np.sqrt(periods) * r.mean() / r.std(ddof=1))


if __name__ == "__main__":
    p = simulate_prices()
    print("Sharpe:", round(sharpe(backtest(p)), 2))
