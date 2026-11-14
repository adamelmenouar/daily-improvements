"""Chaikin Money Flow : pression acheteuse (+1) ou vendeuse (-1) sur la fenêtre."""


def chaikin_money_flow(high, low, close, volume, window=20):
    mfm = ((close - low) - (high - close)) / (high - low)
    return (mfm * volume).rolling(window).sum() / volume.rolling(window).sum()
