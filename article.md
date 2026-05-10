# Forecast Error Variance Analysis for Time Series using Historical Data of Births in the UK from... Forecasting is never about being exactly right. It is about
understanding where and why errors occur --- and using that information to...

### Forecast Error Variance Analysis for Time Series using Historical Data of Births in the UK from 1837--1983 with Python
Forecasting is never about being exactly right. It is about understanding where and why errors occur --- and using that information to improve.

This article uses UK births, beginning in 1837, to show how forecast error analysis works in practice. The framework follows Montgomery and Johnson's classic structure from *Forecasting and Time Series Analysis*. We are focused on the analysis of errors, not the forecasting method here.

We fit a seasonal Exponential Smoothing model (additive seasonality and trend) to generate one-step-ahead forecasts. Every forecast uses only data available at the time. Errors are then calculated as:


where:

- xT+τx\_{T+\\tau} is the actual birth count
- x\^T+τ(T) is the forecast made at time T for time T+τ

### Visualizing Actual vs Forecast
The plot below shows actual births in black and the model's one-step-ahead forecasts in red dashed lines.


Forecasts track the broad seasonal pattern but miss finer details. That is expected. No model can capture every fluctuation in birth rates over nearly two centuries.

### Measuring Forecast Errors
The forecast error series is plotted below:


Most errors stay within a reasonable band, but there are periods where the model consistently over- or under-predicts. These patterns matter. They tell us whether the model assumptions hold over time.

### Estimating Expected Error
Montgomery and Johnson describe three simple ways to estimate expected forecast error.

**Simple Average**: The average forecast error across all periods was about **−113** births. This suggests a slight downward bias but close to neutral overall.


**Moving Average**: Using only the most recent 20 quarters, the moving average error rises to about **+805**. Recent forecasts have been slightly too low compared to actual births.


**Exponentially Smoothed Errors**: Applying exponential smoothing with α=0.2 highlights recent error trends more sharply.


The chart below shows how the moving average and the exponentially smoothed errors evolve.


Notice how exponential smoothing responds more quickly to changes compared to a simple moving average.

### Measuring Error Variability
It is not enough to know the average error. We need to know how variable the errors are.

Using the last 20 quarters: The sample variance of errors is approximately 26,255,770. The mean absolute deviation (MAD) is about 5,135 births.

Assuming normality, the standard deviation can be approximated by scaling MAD:


This gives a practical sense of how much actual births can deviate from forecasts, even when the model is unbiased.

### Forecasting Multi-Step Errors
Forecast errors compound when forecasting farther ahead. Using standard approximations:

- The 3-step ahead error variance is about 93,208,872.
- The 6-step ahead error variance rises to 167,775,969.
- The 12-step ahead error variance climbs to 298,268,389.

This pattern is plotted here:


Errors grow roughly proportionally to the forecast horizon --- a common result for time series models with persistent seasonality and trend.

A model can have zero average error over a long horizon and still be wrong today. Moving averages and exponential smoothing allow you to detect drift **before** it compounds into major forecast failure.

Without simple average error, you miss long-term bias. Without moving average error, you miss model drift. Without exponential smoothing, you miss rapid shifts.

Using all three together provides a simple but robust system for keeping forecasts honest.

For the UK births forecast:

- Long-term bias is low (simple average ≈ −113).
- Recent forecasts are underestimating births (moving average ≈ +805).
- Recent shifts are visible and accelerating when viewed through exponentially smoothed errors.

If this pattern continued, it would suggest revisiting the model choice, re-estimating parameters, or considering regime change models.

### Why This Matters
No forecast is complete without error analysis. A good forecast model minimizes bias, limits error variability, and makes uncertainty explicit for users.

By working through simple averages, moving averages, smoothing, and variance estimates, we built a full picture of how the model performs --- not just on point predictions but on the errors that follow.

Forecast error analysis is practical. It can be done with basic techniques and provides powerful insights. Whether you are forecasting birth rates, sales, or industrial output, the tools are the same --- and they start by recognizing that every forecast is a compromise between simplicity and reality.

### Measuring Forecast Error Variability
Knowing the average forecast error is a start. You also need to know how much that error fluctuates to understand how uncertain your forecasts really are.

We calculated that the simple average error is close to zero. Now we look deeper at how much errors move around.

### Step 1: Sample Variance of Forecast Errors
The first metric is the sample variance:


Using the most recent 20 quarters of forecast errors:

- The **sample variance** is approximately **26,255,770**.

This tells us that errors are spread out, even though their average might be close to zero.

### Step 2: Mean Absolute Deviation (MAD)
Another practical measure of variability is the **mean absolute deviation (MAD)**:


For the UK births forecasts:

- The MAD is about 5,135 births.

MAD is easier to interpret intuitively than variance. It tells you the typical size of an error, regardless of whether it was positive or negative.

### Step 3: Approximate Standard Deviation from MAD
Assuming normally distributed errors, Montgomery and Johnson show that:


Applying that:

- Estimated standard deviation ≈ **6,436** births.

This provides a quick way to move from MAD to an estimated spread without recalculating variance directly.

Forecast models can be unbiased but still wildly uncertain. Variance and MAD are your tools for catching that.

- Variance shows how much total fluctuation exists.
- MAD gives a simpler, more robust measure that is less sensitive to extreme values.
- Approximate standard deviation lets you set practical prediction intervals quickly.

Without these metrics, you risk presenting forecasts with false confidence.

### Practical Outcomes for UK Birth Forecasts
For UK births:

- Forecast errors fluctuate strongly across time.
- The model performs well on average, but variability remains high.
- Forecasts for individual quarters can easily miss by 5,000--6,000 births either way.

This level of uncertainty must be communicated alongside any forecast-driven decisions.

Measuring error variability is the foundation for responsible forecasting.\ It is not just about knowing the expected error. It is about knowing the expected unpredictability.

Variance, MAD, and approximate standard deviation provide fast, powerful ways to quantify this uncertainty in any forecasting project.

### Predicting Future Error with Multi-Period Forecast Errors
Forecasting one step ahead is one thing. Forecasting three, six, or twelve steps ahead is something else entirely. Errors accumulate, and uncertainty grows.

Forecast error variance grows over time because each new forecast compounds earlier uncertainties.

In a simple model, the τ-period-ahead forecast error variance can be approximated as:


where:

- cτ is a multiplier based on model structure
- σe² is the variance of one-step-ahead errors

Cumulative forecast error over multiple steps adds up as:


where qL depends on how many periods ahead you are forecasting.

### Applying This to UK Births
Using the results from our error variability analysis and standard approximations:

- 1-step ahead error variance ≈ 26,255,770
- Estimated standard deviation from MAD ≈ 6,436

Applying typical values for cτ (derived from model structure and empirical studies):


This pattern shows that forecast error variance grows quickly with the forecast horizon.

### Cumulative Forecast Error Variance
When considering cumulative forecasts (e.g., predicting total births over the next 12 quarters), the error variance becomes even larger.

For UK births:

- The cumulative forecast error variance over 12 quarters is approximately 559,253,230.

Large cumulative variance reinforces that aggregated forecasts can have even higher uncertainty, especially when model errors are correlated over time.

Forecasts lose sharpness the further out you go. Error variance estimates make that clear.

- Short-term forecasts can be trusted within a tighter band.
- Longer-term forecasts need wider prediction intervals to be credible.
- Cumulative forecasts (total births, total revenue, total demand) require even greater caution.

Understanding forecast error variance growth prevents overconfidence and avoids costly decisions based on point forecasts alone.

### Practical Outcomes for UK Birth Forecasts
For UK births:

- Forecasting one quarter ahead is relatively precise.
- Forecasting three to twelve quarters ahead results in much larger uncertainty bands.
- Any strategic decisions based on long-term birth forecasts must account for this growing variance.

Without adjusting for forecast horizon, decision makers risk underestimating risks and planning for outcomes that are far less certain than they appear.

### Summary
Forecast error is not static. It grows as the forecast horizon expands.\ Estimating and visualizing multi-step forecast error variance is essential for building forecasts that are honest about what they can and cannot guarantee.

Knowing the number is important. Seeing the curve is even more important.
