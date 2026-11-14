"""Variables prédictives calculées uniquement avec le passé (pas de fuite du futur)."""
import pandas as pd


def market_features(prices, windows=(5, 20)):
    """DataFrame de rendements passés, volatilité et momentum pour chaque fenêtre."""
    r = prices.pct_change()
    cols = {}
    for w in windows:
        cols[f"ret_{w}"] = prices.pct_change(w)
        cols[f"vol_{w}"] = r.rolling(w).std()
        cols[f"mom_{w}"] = prices / prices.rolling(w).mean() - 1
    return pd.DataFrame(cols)
