# Forecast Error Variance Analysis for Time Series Using UK Births Data

This project demonstrates forecast error variance analysis for time series forecasting.

## Business context

Forecasting is never about being exactly right. It is about understanding where and why errors occur --- and using that information to improve.

This article uses UK births, beginning in 1837, to show how forecast error analysis works in practice. The framework follows Montgomery and Johnson's classic structure from *Forecasting and Time Series Analysis*. We are focused on the analysis of errors, not the forecasting method here.

We fit a seasonal Exponential Smoothing model (additive seasonality and trend) to generate one-step-ahead forecasts. Every forecast uses only data available at the time. Errors are then calculated as:

## Article

Medium article: [Forecast Error Variance Analysis for Time Series Using UK Births Data](https://medium.com/@kylejones_47003/forecast-error-variance-analysis-for-time-series-using-historical-data-of-births-in-the-uk-from-a527646a134c)

## Project Structure

```
.
├── README.md           # This file
├── main.py            # Main entry point
├── config.yaml        # Configuration file
├── requirements.txt   # Python dependencies
├── src/               # Core functions
│   ├── core.py        # Forecast error variance functions
│   └── plotting.py    # Tufte-style plotting utilities
├── tests/             # Unit tests
├── data/              # Data files
├── images/            # Generated plots and figures
├── rust/                   # Rust port (core + PyO3 + CLI bench)
├── benchmark_rust.py       # Python vs Rust benchmark
├── src/compute_kernel.py   # Python/numpy reference kernel
```

## Configuration

Edit `config.yaml` to customize:
- Data source (URL, file path, or synthetic generation)
- Model parameters (seasonal periods, alpha)
- Multi-step variance coefficients
- Output settings

## Forecast Error Variance

Analysis includes:
- Exponential Smoothing: Fitted model
- Error Metrics: MAD, variance, sigma approximation
- Multi-step Variance: Forecast error variance growth
- Smoothed Errors: Moving average and exponential smoothing

## Caveats

- By default, generates synthetic UK births data.
- Requires Excel file format for original data.
- Multi-step variance coefficients depend on model assumptions.

## Rust performance port

Side-by-side **Python vs Rust** implementation of the numeric hot loop — MSE / MAPE / RMSE metrics. Reference PyO3 benchmark: **see `benchmark_rust.py`** on a release build (local machine; run `benchmark_rust.py` to reproduce).

| Path | Role |
|------|------|
| `src/compute_kernel.py` | Python/numpy reference kernel |
| `rust/core/` | Pure Rust library |
| `rust/py/` | PyO3 bindings |
| `rust/bench/` | Standalone CLI benchmark |
| `benchmark_rust.py` | Python vs Rust timing + correctness check |

```bash
# Rust-only CLI benchmark
cd rust && cargo run --release -p forecast_error_variance_analysis_for_time_series_using_historical_data_of_births_in_the_uk_from_bench

# Python vs Rust (PyO3)
pip install maturin numpy
maturin develop --release -m rust/py/Cargo.toml
python benchmark_rust.py
```

Python ML training, solvers, and orchestration stay in Python; Rust targets the numeric hot loops. Stochastic generators validate output shapes; deterministic kernels match at tight floating-point tolerance.


## Disclaimer

Educational/demo code only. Not financial, safety, or engineering advice. Use at your own risk. Verify results independently before any production or operational use.

## License

MIT — see [LICENSE](LICENSE).