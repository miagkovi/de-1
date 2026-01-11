"""
Logic for loading data into Postgres database.
"""

def load_data(db_conn, data_path: str):
    """
    Load data from CSV file into Postgres database.
    Args:
        db_conn: Active database connection.
        data_path (str): Path to the CSV file containing the data.
    """
    try:
        with open(data_path, 'r', encoding='utf-8') as file:
            # Using COPY command for efficient bulk loading
            sql = f"""
            COPY cpu_benchmark FROM STDIN WITH CSV HEADER DELIMITER AS ',';
            """
            db_conn.cursor().copy_expert(sql, file)
        db_conn.commit()
    except Exception as e:
        db_conn.rollback()
        raise e
