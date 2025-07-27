from forecasting import forecast_metric
from reporting import run_gam_report
from data_cleaning import clean_gam_dataframe
import matplotlib.pyplot as plt

# Step 1: Get raw data
raw_df = run_gam_report(
    start_date={"year": 2024, "month": 7, "day": 1},
    end_date={"year": 2024, "month": 7, "day": 31}
)

# Step 2: Clean the data
clean_df = clean_gam_dataframe(raw_df)

# Step 3: Forecast impressions and revenue
forecast_impressions = forecast_metric(clean_df, "impressions", periods=30)
forecast_revenue = forecast_metric(clean_df, "revenue", periods=30)

# Step 4: Plot forecasts
forecast_impressions[['ds', 'yhat']].plot(title="Impressions Forecast")
plt.show()

forecast_revenue[['ds', 'yhat']].plot(title="Revenue Forecast")
plt.show()
