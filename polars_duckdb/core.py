"""Forecast error variance — error aggregates via DuckDB."""

from pathlib import Path
from typing import Any

import duckdb
import matplotlib.pyplot as plt
import numpy as np
import polars as pl


def calculate_error_metrics(errors: pl.Series, alpha: float = 0.2) -> dict[str, float]:
    pl.DataFrame({"e": errors})
    row = (
        duckdb.sql(f"""
        SELECT
            AVG(e) AS mean_error,
            AVG(ABS(e)) AS mad,
            AVG(ABS(e)) * SQRT(pi() / 2.0) AS sigma_approx,
            VAR_SAMP(e) AS sample_variance
        FROM df
    """)
        .pl()
        .row(0, named=True)
    )
    return {k: float(v) for k, v in row.items()}


def calculate_multi_step_variance(
    c1: float, c_tau: float, mad: float, alpha: float = 0.2
) -> float:
    sigma_e_approx = mad * np.sqrt(np.pi / 2)
    var_one_step = sigma_e_approx**2 * (2 - alpha) / 2
    return float(c_tau * var_one_step)


def plot_forecast_analysis(
    actual: pl.Series,
    fitted: pl.Series,
    errors: pl.Series,
    title: str,
    output_path: Path,
    plot: bool = False,
) -> None:
    if not plot:
        return
    fig, axes = plt.subplots(2, 1, figsize=(10, 8), sharex=True)
    axes[0].plot(actual.to_list(), label="Actual", color="#4A90A4", linewidth=1.2)
    axes[0].plot(fitted.to_list(), label="Fitted", color="#D4A574", linewidth=1.2, linestyle="--")
    axes[0].legend(loc="best")
    axes[1].plot(errors.to_list(), color="#8B6F9E", linewidth=1.2)
    axes[1].axhline(0, color="black", linewidth=0.5, alpha=0.3)
    plt.savefig(output_path, dpi=100, bbox_inches="tight")
    plt.close()
