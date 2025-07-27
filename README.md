# GAM Forecasting

This project fetches Google Ad Manager (GAM) report data, cleans it, and applies time series forecasting using Facebook Prophet to predict future impressions and revenue.

## Features

- ✅ Pulls GAM data via the Google Ads API
- 🧹 Cleans and normalizes raw DataFrames
- 📈 Forecasts future ad impressions and revenue using Prophet
- 📊 Optional Plotly/Matplotlib visualizations

## Project Structure

```
.
├── config.py               # API version and constants
├── credentials.json        # Your GAM service account credentials (ignored)
├── data_cleaning.py        # Cleans GAM raw report output
├── forecasting.py          # Forecasting logic using Prophet
├── reporting.py            # GAM API report runner
├── report_forecast.py      # End-to-end execution script
├── requirements.txt        # Python package dependencies
├── .gitignore              # Ignore sensitive files
└── README.md               # Project overview
```

## Notes

- Forecasts are generated using Prophet.
- Plotly is optional but provides interactive charts.
