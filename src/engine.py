"""
Database connection module.
"""

import psycopg2
import psycopg2.extras
from contextlib import contextmanager

@contextmanager
def get_db_connection(user: str,
                      password: str,
                      host: str,
                      port: int = 5432,
                      database: str = None):
    """
    Context manager for database connection.
    
    Args:
        user (str): Database user.
        password (str): Database password.
        host (str): Database host.
        port (int): Database port.
        database (str): Database name.
    """

    psycopg2.extras.register_uuid() # Enable UUID support

    conn = None
    try:
        conn = psycopg2.connect(user=user,
                                password=password,
                                host=host,
                                port=port,
                                database=database)
        yield conn
    finally:
        if conn:
            conn.close()
