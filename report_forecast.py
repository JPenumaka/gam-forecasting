from forecasting import forecast_metric
from reporting import run_gam_report
from data_cleaning import clean_gam_dataframe
import matplotlib.pyplot as plt

# Step 1: Pull and clean the data
raw_df = run_gam_report(
    start_date={"year": 2024, "month": 7, "day": 1},
    end_date={"year": 2024, "month": 7, "day": 31}
)

print("Raw DataFrame Columns:")
print(raw_df.columns)
print("Sample Data:")
print(raw_df.head())

clean_df = clean_gam_dataframe(raw_df)

# Step 2: Forecast 30 days for both impressions and revenue
forecast_impressions = forecast_metric(clean_df, metric="impressions", periods=30)
forecast_revenue = forecast_metric(clean_df, metric="revenue", periods=30)

# Optional: Export to CSV
forecast_impressions.to_csv("forecast_impressions.csv", index=False)
forecast_revenue.to_csv("forecast_revenue.csv", index=False)

# Step 3: Plot impressions forecast
plt.figure(figsize=(10, 5))
plt.plot(forecast_impressions['ds'], forecast_impressions['yhat'], label='Forecast')
plt.title('Impressions Forecast')
plt.xlabel('Date')
plt.ylabel('Impressions')
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.show()

# Step 4: Plot revenue forecast
plt.figure(figsize=(10, 5))
plt.plot(forecast_revenue['ds'], forecast_revenue['yhat'], label='Forecast', color='green')
plt.title('Revenue Forecast')
plt.xlabel('Date')
plt.ylabel('Revenue')
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.show()
