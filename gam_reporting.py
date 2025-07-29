# gam_reporting.py

from googleads import ad_manager
import pandas as pd
import time
from config import API_VERSION

def get_client():
    return ad_manager.AdManagerClient.LoadFromStorage("googleads.yaml")

def run_report(start_date: dict, end_date: dict, dimensions: list, metrics: list):
    client = get_client()
    report_service = client.GetService("ReportService", version=API_VERSION)

    report_job = {
        "reportQuery": {
            "dimensions": dimensions,
            "columns": metrics,
            "dateRangeType": "CUSTOM_DATE",
            "startDate": start_date,
            "endDate": end_date
        }
    }

    report_job_id = report_service.runReportJob(report_job)
    print(f"Report job started with ID: {report_job_id}")

    # Wait for the job to complete
    status = report_service.getReportJobStatus(report_job_id)
    while status != "COMPLETED":
        if status == "FAILED":
            raise Exception("Report job failed")
        print("Waiting for report to finish...")
        time.sleep(5)
        status = report_service.getReportJobStatus(report_job_id)

    return report_job_id

def download_report_to_df(report_job_id):
    client = get_client()
    report_downloader = client.GetDataDownloader(version=API_VERSION)

    report_file = "report.csv"
    with open(report_file, "wb") as f:
        report_downloader.DownloadReportToFile(
            report_job_id,
            "CSV_DUMP",
            f,
            include_report_properties=True
        )

    df = pd.read_csv(report_file)
    return df
