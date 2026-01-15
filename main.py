"""
ETL Pipeline Main Module
This module orchestrates the extraction, transformation, and loading (ETL) of data.
"""

from uuid import uuid4
from datetime import datetime

from src.load import load_data
from src.extract import extract_dataset
from src.metadata import save_run_metadata
from src.models import RunMetadata
from src.transform import transform_data
from src.engine import get_db_connection
from config import POSTGRES_HOST, POSTGRES_USER, POSTGRES_PASSWORD, POSTGRES_DB, POSTGRES_PORT


def run_pipeline():
    """Runs the ETL pipeline."""
    metadata = RunMetadata(
        run_id=uuid4(),
        dataset_provider="alanjo/cpu-benchmarks",
        dataset_name="CPU_benchmark_v4.csv",
        status="Running",
        start_time=datetime.now()
    )
    
    transformed_dataset_file_path = f"./data/{metadata.dataset_name}"

    with get_db_connection(user=POSTGRES_USER,
                           password=POSTGRES_PASSWORD,
                           host=POSTGRES_HOST,
                           port=POSTGRES_PORT,
                           database=POSTGRES_DB) as conn:
        try:
            conn.cursor().execute("TRUNCATE TABLE cpu_benchmark;")
            conn.commit()

            raw_dataset_file_path = extract_dataset(handle=metadata.dataset_provider,
                                                    path=metadata.dataset_name)

            transform_data(file_path=raw_dataset_file_path,
                           output_path=transformed_dataset_file_path)
            
            load_data(db_conn=conn,
                      file_path=transformed_dataset_file_path)
            
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