"""
Database connection module.
"""

import psycopg2
from contextlib import contextmanager

@contextmanager
def get_db_connection(user, password, host, port=5432, database=None):
    """
    Context manager for database connection.
    
    Args:
        user (str): Database user.
        password (str): Database password.
        host (str): Database host.
        port (int): Database port.
        database (str): Database name.
    """
    conn = None
    try:
        conn = psycopg2.connect(
            user=user,
            password=password,
            host=host,
            port=port,
            database=database
        )
        yield conn
    finally:
        if conn:
            conn.close()
