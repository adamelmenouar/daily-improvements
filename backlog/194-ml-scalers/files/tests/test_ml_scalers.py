import numpy as np
from ml.scalers import StandardScaler, MinMaxScaler, RobustScaler

X = np.random.default_rng(180).normal(5, 3, (500, 3))


def test_standard_scaler_gives_zero_mean_unit_variance():
    z = StandardScaler().fit(X).transform(X)
    assert np.allclose(z.mean(axis=0), 0, atol=1e-12) and np.allclose(z.std(axis=0), 1)


def test_minmax_scaler_maps_to_unit_interval():
    z = MinMaxScaler().fit(X).transform(X)
    assert z.min() == 0.0 and z.max() == 1.0


def test_robust_scaler_resists_outliers():
    y = X.copy()
    y[0, 0] = 1e6
    assert abs(np.median(RobustScaler().fit(y).transform(y)[:, 0])) < 1e-12


def test_constant_column_does_not_divide_by_zero():
    assert np.isfinite(StandardScaler().fit([[1.0], [1.0]]).transform([[1.0]])).all()
