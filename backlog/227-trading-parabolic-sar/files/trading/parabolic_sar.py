"""Parabolic SAR de Wilder : stop suiveur qui accélère avec la tendance."""
import numpy as np


def parabolic_sar(high, low, step=0.02, max_step=0.2):
    """Retourne (sar, tendance) : tendance = +1 (SAR sous les prix) ou -1 (SAR au-dessus)."""
    h, l = np.asarray(high, dtype=float), np.asarray(low, dtype=float)
    n = len(h)
    sar, trend = np.empty(n), np.empty(n)
    up, af, ep, s = True, step, h[0], l[0]
    sar[0], trend[0] = s, 1
    for i in range(1, n):
        s = s + af * (ep - s)
        if up:
            s = min(s, l[i - 1], l[i - 2] if i > 1 else l[i - 1])
            if l[i] < s:
                up, s, ep, af = False, ep, l[i], step
            elif h[i] > ep:
                ep, af = h[i], min(af + step, max_step)
        else:
            s = max(s, h[i - 1], h[i - 2] if i > 1 else h[i - 1])
            if h[i] > s:
                up, s, ep, af = True, ep, h[i], step
            elif l[i] < ep:
                ep, af = l[i], min(af + step, max_step)
        sar[i], trend[i] = s, 1 if up else -1
    return sar, trend
