"""
Main entry point. Steps order.
1. Pipeline start
2. Extract data
3. Transform data
4. Load data
5. Pipeline end (success or failure)
"""
from extract.kaggle import extract_dataset
from metadata.repository import pipeline_start, pipeline_end
from uuid import uuid4

def run_pipeline():
    try:
        run_id = uuid4()
        dataset_name = "alanjo/cpu-benchmarks"
        pipeline_start(run_id=run_id, dataset_name=dataset_name)
        extract_dataset(dataset_name=dataset_name, download_path="./data/raw")
        data = extract_data()
        transformed_data = transform_data(data)
        load_data(transformed_data)
        pipeline_end(run_id=run_id, status="success")
    except Exception as e:
        print(f"Pipeline failed: {e}")
        pipeline_end(run_id=run_id, status="failure", error_message=str(e))

if __name__ == "__main__":
    run_pipeline()