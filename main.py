"""
Main entry point. Steps order.
1. Pipeline start
2. Extract data
3. Transform data
4. Load data
5. Pipeline end (success or failure)
"""

from load import load_data
from uuid import uuid4

from extract import extract_dataset
from metadata import log_start, log_end
from transform import transform_data
from db import get_db_connection

def run_pipeline():
    with get_db_connection() as conn:
        try:
            run_id = uuid4()
            dataset_name = "alanjo/cpu-benchmarks"
            log_start(run_id=run_id, db=conn, dataset_name=dataset_name)
            raw_data = extract_dataset(dataset_name=dataset_name)
            transformed_data = transform_data(file_path=raw_data, output_path="./data/processed/transformed_data.csv")
            load_data(transformed_data)
            log_end(run_id=run_id, db=conn, status="success")
        except Exception as e:
            log_end(run_id=run_id, db=conn, status="failure", error_message=str(e))

if __name__ == "__main__":
    run_pipeline()