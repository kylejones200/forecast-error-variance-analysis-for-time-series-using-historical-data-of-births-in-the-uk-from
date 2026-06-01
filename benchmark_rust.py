#!/usr/bin/env python3
"""Python vs Rust kernel benchmark."""

from __future__ import annotations

import time
import sys
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / "src"))
from compute_kernel import forecast_error_metrics  # noqa: E402

def main() -> None:
    n = 2000
    actual = np.ascontiguousarray(1000.0 + np.sin(np.arange(n) * 0.1) * 50.0)
    forecast = actual + 5.0
    t0 = time.perf_counter()
    for _ in range(200):
        forecast_error_metrics(actual, forecast)
    py_s = time.perf_counter() - t0
    try:
        import forecast_error_variance_analysis_for_time_series_using_historical_data_of_births_in_the_uk_from_rs as rs
    except ImportError:
        print("Build: maturin develop --release -m rust/py/Cargo.toml")
        print(f"Python {py_s:.3f}s")
        return
    rs_s = rs.bench_kernel_py(actual, forecast, 10000)
    print(f"Python {py_s:.3f}s Rust {rs_s:.3f}s speedup {py_s / max(rs_s, 1e-9):.1f}x")
    py = forecast_error_metrics(actual, forecast)
    rs_m = rs.forecast_error_metrics_py(actual, forecast)
    for i in range(3):
        np.testing.assert_allclose(py[i], rs_m[i], rtol=1e-10)
    print("Correctness: OK")

if __name__ == "__main__":
    main()
