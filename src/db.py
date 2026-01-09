"""
Database connection module.
"""

import psycopg2
from contextlib import contextmanager

@contextmanager
def get_db_connection(db_config):
    """
    Context manager for database connection.
    
    Args:
        db_config (dict): Database configuration parameters.
    """
    conn = None
    try:
        conn = psycopg2.connect(**db_config)
        yield conn
    finally:
        if conn:
            conn.close()
