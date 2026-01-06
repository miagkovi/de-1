"""
Logic for load_metadata table.
Create a pipeline start recond in load_metadata table.
Update load status on success or failure.
"""

def pipeline_start(run_id, dataset_name=None):
    # Logic to create a pipeline start record in load_metadata table
    pass

def pipeline_end(run_id, status, error_message=None):
    # Logic to update load status in load_metadata table
    pass