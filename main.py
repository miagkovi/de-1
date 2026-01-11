"""
ETL Pipeline Main Module
This module orchestrates the extraction, transformation, and loading (ETL) of data.
"""

from load import load_data
from uuid import uuid4
from datetime import datetime

from extract import extract_dataset
from metadata import save_run_metadata
from transform import transform_data
from db import get_db_connection
from config import POSTGRES_HOST, POSTGRES_USER, POSTGRES_PASSWORD, POSTGRES_DB, POSTGRES_PORT


def run_pipeline():
    """Runs the ETL pipeline."""
    dataset_provider = "alanjo/cpu-benchmarks"
    dataset_name = "CPU_benchmark_v4.csv"
    data_path = f"./data/{dataset_name}"
    run_start = datetime.now()
    run_id = uuid4()

    with get_db_connection(user=POSTGRES_USER,
                           password=POSTGRES_PASSWORD,
                           host=POSTGRES_HOST,
                           port=POSTGRES_PORT,
                           database=POSTGRES_DB) as conn:
        try:
            raw_data_path = extract_dataset(handle=dataset_provider,
                                            path=dataset_name)

            transform_data(file_path=raw_data_path,
                           output_path=data_path)
            
            load_data(db_conn=conn,
                      data_path=data_path)

            save_run_metadata(db_conn=conn,
                              run_id=run_id,
                              run_start=run_start,
                              run_end=datetime.now(),
                              run_status="Success")

        except Exception as e:
            save_run_metadata(db_conn=conn,
                              run_id=run_id,
                              run_start=run_start,
                              run_end=datetime.now(),
                              run_status="Failed",
                              run_errors=str(e))
if __name__ == "__main__":
    run_pipeline()