import pandas as pd


def clean_gam_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    """
    Cleans and standardizes a GAM DataFrame for forecasting.

    Expected raw GAM columns:
        - 'Dimension.DATE'
        - 'Column.AD_SERVER_IMPRESSIONS'
        - (optional) 'Column.AD_SERVER_CLICKS'
        - (optional) 'Column.TOTAL_REVENUE' — not always present

    Returns a DataFrame with:
        - 'date': datetime
        - 'impressions': int
        - 'revenue': float
    """

    # Rename columns to standard internal names
    df = df.rename(columns={
        "Dimension.DATE": "date",
        "Column.AD_SERVER_IMPRESSIONS": "impressions",
        "Column.AD_SERVER_CLICKS": "clicks",  # optional
        "Column.TOTAL_REVENUE": "revenue"     # optional
    })

    # Ensure required columns exist or initialize fallback values
    if "revenue" not in df.columns:
        df["revenue"] = 0.0

    # Drop rows with missing dates or impressions
    df = df.dropna(subset=["date", "impressions"])

    # Parse dates and convert numerics
    df["date"] = pd.to_datetime(df["date"], errors="coerce")
    df["impressions"] = pd.to_numeric(df["impressions"], errors="coerce")
    df["revenue"] = pd.to_numeric(df["revenue"], errors="coerce").fillna(0.0)

    # Final check: must include date, impressions, revenue
    required_cols = {"date", "impressions", "revenue"}
    if not required_cols.issubset(df.columns):
        raise ValueError("DataFrame must include 'date', 'impressions', and 'revenue' columns")

    return df
