"""
ETL Pipeline Main Module
This module orchestrates the extraction, transformation, and loading (ETL) of data.
"""

from load import load_data
from uuid import uuid4
from datetime import datetime

from extract import extract_dataset
from metadata import save_run_metadata
from models import RunMetadata
from transform import transform_data
from engine import get_db_connection
from config import POSTGRES_HOST, POSTGRES_USER, POSTGRES_PASSWORD, POSTGRES_DB, POSTGRES_PORT


def run_pipeline():
    """Runs the ETL pipeline."""
    metadata = RunMetadata(
        run_id=uuid4(),
        status="Running",
        start_time=datetime.now()
    )
    dataset_provider = "alanjo/cpu-benchmarks"
    dataset_name = "CPU_benchmark_v4.csv"
    data_path = f"./data/{dataset_name}"

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
                      file_path=data_path)
            
            metadata.status = "Success"
            metadata.end_time = datetime.now()

            save_run_metadata(db_conn=conn,
                              metadata=metadata)

        except Exception as e:
            metadata.status = "Failed"
            metadata.end_time = datetime.now()
            metadata.errors = str(e)

            save_run_metadata(db_conn=conn,
                              metadata=metadata)

if __name__ == "__main__":
    run_pipeline()