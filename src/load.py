"""
Logic for loading data into Postgres database.
"""
from pathlib import Path


def load_data(db_conn, file_path: str) -> None:
    """
    Load data from CSV file into Postgres database.
    Args:
        db_conn: Active database connection.
        file_path (str): Path to the CSV file containing the data.
    """
    file_path = Path(file_path)
    if not file_path.exists() or file_path.suffix != ".csv":
        raise ValueError("Invalid file path or format. Please provide a valid CSV file.")
    
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            # Using COPY command for efficient bulk loading
            sql = f"""
            COPY cpu_benchmark(cpu_name, price, cpu_mark, cpu_value, thread_mark, thread_value, tdp, power_perf, cores, test_date, socket, category)
            FROM STDIN WITH CSV HEADER DELIMITER AS ',';
            """
            db_conn.cursor().copy_expert(sql, file)
        db_conn.commit()
    except Exception as e:
        db_conn.rollback()
        raise e
