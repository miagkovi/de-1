"""
Metadata logging functions for the ETL pipeline.
"""

def log_status(run_id, db, dataset_name, start_time, end_time, error_message=None) -> None:
    """Log status of the pipeline run."""
    print(f"Logging status of pipeline run {run_id} for dataset {dataset_name}",
          f"Error: {error_message}" if error_message else "Success")
