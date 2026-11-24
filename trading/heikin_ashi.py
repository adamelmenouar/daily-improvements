"""Bougies Heikin-Ashi : lissage des bougies japonaises."""
import pandas as pd


def heikin_ashi(open_, high, low, close):
    """Retourne un DataFrame (open, high, low, close) Heikin-Ashi."""
    ha_close = (open_ + high + low + close) / 4
    ha_open = ha_close.copy()
    ha_open.iloc[0] = (open_.iloc[0] + close.iloc[0]) / 2
    for i in range(1, len(ha_open)):
        ha_open.iloc[i] = (ha_open.iloc[i - 1] + ha_close.iloc[i - 1]) / 2
    return pd.DataFrame({
        "open": ha_open,
        "high": pd.concat([high, ha_open, ha_close], axis=1).max(axis=1),
        "low": pd.concat([low, ha_open, ha_close], axis=1).min(axis=1),
        "close": ha_close,
    })
