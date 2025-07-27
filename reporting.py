# reporting.py

import gzip
import tempfile
import pandas as pd
import time
from googleads import ad_manager
from config import API_VERSION


def get_client():
    return ad_manager.AdManagerClient.LoadFromStorage("googleads.yaml")


def run_gam_report(start_date: dict, end_date: dict) -> pd.DataFrame:
    """
    Runs a basic GAM report (e.g., daily impressions) and returns a DataFrame.

    Args:
        start_date (dict): {"year": 2024, "month": 7, "day": 1}
        end_date (dict):   {"year": 2024, "month": 7, "day": 31}

    Returns:
        pd.DataFrame: Parsed GAM report data
    """
    client = get_client()
    report_service = client.GetService("ReportService", version=API_VERSION)

    report_job = {
    "reportQuery": {
        "dimensions": ["DATE", "AD_UNIT_ID"],
        "columns": ["AD_SERVER_IMPRESSIONS", "AD_SERVER_CLICKS", "AD_SERVER_CPM_REVENUE"],
        "dateRangeType": "CUSTOM_DATE",
        "startDate": start_date,
        "endDate": end_date
    }
}
    # Run the report
    report_job = report_service.runReportJob(report_job)

    # Poll until the report is ready
    status = report_service.getReportJobStatus(report_job["id"])
    while status != "COMPLETED":
        if status == "FAILED":
            raise Exception("Report job failed")
        time.sleep(5)
        status = report_service.getReportJobStatus(report_job["id"])

    # Download the report to a temp file
    report_downloader = client.GetDataDownloader(version=API_VERSION)
    with tempfile.NamedTemporaryFile(delete=False, suffix=".csv") as report_file:
        report_downloader.DownloadReportToFile(
        report_job["id"],
        "CSV_DUMP",
        report_file
    )

        report_file_path = report_file.name

# GAM always returns CSV_DUMP as GZIP-compressed, even if filename doesn't say so
    with gzip.open(report_file_path, mode="rt", encoding="utf-8") as f:
        df = pd.read_csv(f)
    
    return df
