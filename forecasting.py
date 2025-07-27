from prophet import Prophet
import pandas as pd

def forecast_metric(df: pd.DataFrame, metric: str, periods: int = 30) -> pd.DataFrame:
    """
    Forecasts the specified metric using Prophet.

    Args:
        df (pd.DataFrame): Cleaned DataFrame with 'date' and the metric column.
        metric (str): Column name to forecast (e.g., 'impressions', 'revenue').
        periods (int): Number of future days to forecast.

    Returns:
        pd.DataFrame: Forecast DataFrame with 'ds', 'yhat', 'yhat_lower', 'yhat_upper'.
    """
    df_prophet = df[['date', metric]].rename(columns={'date': 'ds', metric: 'y'})
    model = Prophet()
    model.fit(df_prophet)
    future = model.make_future_dataframe(periods=periods)
    forecast = model.predict(future)
    return forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']]
