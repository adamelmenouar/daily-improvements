"""Awesome Oscillator de Bill Williams : SMA(5) - SMA(34) du prix médian."""


def awesome_oscillator(high, low, fast=5, slow=34):
    median = (high + low) / 2
    return median.rolling(fast).mean() - median.rolling(slow).mean()
