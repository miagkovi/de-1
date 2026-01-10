"""
Metadata logging functions for the ETL pipeline.
"""

def save_run_metadata(db_conn, run_id, run_start, run_end, run_status, run_errors=None) -> None:
    """Log status of the pipeline run."""
    if run_status in ["Success", "Failed"] and run_start <= run_end:
        db_conn.cursor().execute(
            """
            INSERT INTO metadata (run_id, run_status, run_start, run_end, run_errors)
            VALUES (%s, %s, %s, %s, %s)
            """,
            (run_id, run_status, run_start, run_end, run_errors)
        )
        db_conn.commit()
    else:
        raise ValueError("Invalid run metadata.")
