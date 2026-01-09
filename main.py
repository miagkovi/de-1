"""
ETL Pipeline Main Module
This module orchestrates the extraction, transformation, and loading (ETL) of data.
"""

from load import load_data
from uuid import uuid4
from datetime import datetime

from extract import extract_dataset
from metadata import log_status
from transform import transform_data
from db import get_db_connection


dataset_provider = "alanjo/cpu-benchmarks"
dataset_name = "CPU_benchmark_v4.csv"
processed_data_path = f"./data/processed/{dataset_name}"

def run_pipeline():
    """Runs the ETL pipeline."""
    start_time = datetime.now()
    run_id = uuid4()

    with get_db_connection() as conn:
        try:
            raw_data_path = extract_dataset(handle=dataset_provider,
                                            path=dataset_name)

            transform_data(file_path=raw_data_path,
                           output_path=processed_data_path)
            
            load_data(processed_data_path)

            log_status(run_id=run_id,
                        db=conn, 
                        dataset_name=dataset_name,
                        start_time=start_time,
                        end_time=datetime.now())

        except Exception as e:
            log_status(run_id=run_id,
                        db=conn,
                        dataset_name=dataset_name,
                        start_time=start_time,
                        end_time=datetime.now(),
                        error_message=str(e))

if __name__ == "__main__":
    run_pipeline()