import os
import psycopg2

from src.engine import get_db_connection
from config import POSTGRES_HOST, POSTGRES_USER, POSTGRES_PASSWORD, POSTGRES_DB, POSTGRES_PORT


def before_all(context):
    """
    Runs once before all tests.
    """
    with get_db_connection(user=POSTGRES_USER,
                           password=POSTGRES_PASSWORD,
                           host=POSTGRES_HOST,
                           port=POSTGRES_PORT,
                           database=POSTGRES_DB) as conn:
        context.conn = conn
