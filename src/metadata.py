"""
Logic for load_metadata table.
Create a pipeline start recond in load_metadata table.
Update load status on success or failure.
"""

def log_start(run_id, db, dataset_name=None):
    # Logic to create a pipeline start record in load_metadata table
    print(f"Logging start of pipeline run {run_id} for dataset {dataset_name}")

def log_end(run_id, status, db, error_message=None):
    # Logic to update load status in load_metadata table
    print(f"Logging end of pipeline run {run_id}: {status}", f"Error: {error_message}" if error_message else "")