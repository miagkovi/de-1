"""
Metadata management for ETL pipeline.
"""

def save_run_metadata(db_conn, run_id, run_start, run_end, run_status, run_errors=None) -> None:
    """Log status of the pipeline run."""
    if run_status not in ["Success", "Failed"] or run_start > run_end:
        raise ValueError("Invalid run metadata.")
    db_conn.cursor().execute(
        """
        INSERT INTO metadata (run_id, run_status, run_start, run_end, run_errors)
        VALUES (%s, %s, %s, %s, %s)
        """,
        (run_id, run_status, run_start, run_end, run_errors)
    )
    db_conn.commit()
