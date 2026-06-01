use forecast_error_variance_analysis_for_time_series_using_historical_data_of_births_in_the_uk_from_core::forecast_error_metrics;
use numpy::PyReadonlyArray1;
use pyo3::prelude::*;

#[pyfunction]
fn forecast_error_metrics_py(
    actual: PyReadonlyArray1<f64>,
    forecast: PyReadonlyArray1<f64>,
) -> PyResult<(f64, f64, f64)> {
    Ok(forecast_error_metrics(actual.as_slice()?, forecast.as_slice()?))
}

#[pyfunction]
#[pyo3(signature = (actual, forecast, iterations=10_000))]
fn bench_kernel_py(
    actual: PyReadonlyArray1<f64>,
    forecast: PyReadonlyArray1<f64>,
    iterations: usize,
) -> PyResult<f64> {
    let a = actual.as_slice()?.to_vec();
    let f = forecast.as_slice()?.to_vec();
    let start = std::time::Instant::now();
    for _ in 0..iterations {
        let _ = forecast_error_metrics(&a, &f);
    }
    Ok(start.elapsed().as_secs_f64())
}

#[pymodule]
fn forecast_error_variance_analysis_for_time_series_using_historical_data_of_births_in_the_uk_from_rs(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(forecast_error_metrics_py, m)?)?;
    m.add_function(wrap_pyfunction!(bench_kernel_py, m)?)?;
    Ok(())
}
