"""
Metadata management for ETL pipeline.
"""
from src.models import RunMetadata

def save_run_metadata(db_conn, metadata: RunMetadata) -> None:
    """Log status of the pipeline run."""
    if metadata.status not in ["Success", "Failed"] or metadata.start_time > metadata.end_time:
        raise ValueError("Invalid run metadata.")
    
    db_conn.cursor().execute(
        """
        INSERT INTO metadata (run_id, dataset_provider, dataset_name, status, start_time, end_time, errors)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """,
        (metadata.run_id, metadata.dataset_provider, metadata.dataset_name,
         metadata.status, metadata.start_time, metadata.end_time, metadata.errors)
    )
    db_conn.commit()
