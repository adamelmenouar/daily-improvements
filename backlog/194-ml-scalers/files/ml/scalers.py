"""Normalisations : ajuster sur l'échantillon d'entraînement, appliquer au test (jamais l'inverse)."""
import numpy as np


class StandardScaler:
    def fit(self, X):
        X = np.asarray(X, dtype=float)
        self.mean_, self.std_ = X.mean(axis=0), X.std(axis=0, ddof=0)
        self.std_ = np.where(self.std_ == 0, 1.0, self.std_)
        return self

    def transform(self, X):
        return (np.asarray(X, dtype=float) - self.mean_) / self.std_


class MinMaxScaler:
    def fit(self, X):
        X = np.asarray(X, dtype=float)
        self.lo_, self.hi_ = X.min(axis=0), X.max(axis=0)
        self.rng_ = np.where(self.hi_ == self.lo_, 1.0, self.hi_ - self.lo_)
        return self

    def transform(self, X):
        return (np.asarray(X, dtype=float) - self.lo_) / self.rng_


class RobustScaler:
    def fit(self, X):
        X = np.asarray(X, dtype=float)
        self.med_ = np.median(X, axis=0)
        q75, q25 = np.percentile(X, [75, 25], axis=0)
        self.iqr_ = np.where(q75 == q25, 1.0, q75 - q25)
        return self

    def transform(self, X):
        return (np.asarray(X, dtype=float) - self.med_) / self.iqr_
