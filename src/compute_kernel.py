"""Forecast error metrics: MSE, MAPE, RMSE."""

from __future__ import annotations

import numpy as np


def forecast_error_metrics(
    actual: np.ndarray, forecast: np.ndarray
) -> tuple[float, float, float]:
    a = np.asarray(actual, dtype=float)
    f = np.asarray(forecast, dtype=float)
    n = max(len(a), 1)
    se = 0.0
    ape = 0.0
    for ai, fi in zip(a, f):
        e = ai - fi
        se += e * e
        if abs(ai) > 1e-12:
            ape += abs(e / ai)
    mse = se / n
    return mse, ape / n, mse**0.5
