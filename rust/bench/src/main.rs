use forecast_error_variance_analysis_for_time_series_using_historical_data_of_births_in_the_uk_from_core::forecast_error_metrics;

fn main() {
    let n = 2000usize;
    let actual: Vec<f64> = (0..n).map(|i| 1000.0 + (i as f64 * 0.1).sin() * 50.0).collect();
    let forecast: Vec<f64> = actual.iter().map(|&a| a + 5.0).collect();
    for _ in 0..10000 {
        let _ = forecast_error_metrics(&actual, &forecast);
    }
}
