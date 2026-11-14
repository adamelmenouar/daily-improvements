"""Régime de volatilité : 1 si la volatilité récente dépasse sa médiane historique (connue à date), sinon 0."""


def volatility_regime(returns, window=20):
    vol = returns.rolling(window).std()
    threshold = vol.expanding().median().shift(1)  # médiane des valeurs passées uniquement
    return (vol > threshold).astype(float).where(threshold.notna())
