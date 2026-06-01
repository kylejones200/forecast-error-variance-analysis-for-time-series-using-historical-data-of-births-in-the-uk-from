//! Forecast error metrics: MSE, MAPE, RMSE.

pub fn forecast_error_metrics(actual: &[f64], forecast: &[f64]) -> (f64, f64, f64) {
    assert_eq!(actual.len(), forecast.len());
    let n = actual.len().max(1) as f64;
    let mut se = 0.0;
    let mut ape = 0.0;
    for (&a, &f) in actual.iter().zip(forecast) {
        let e = a - f;
        se += e * e;
        if a.abs() > 1e-12 {
            ape += (e / a).abs();
        }
    }
    let mse = se / n;
    (mse, ape / n, mse.sqrt())
}
