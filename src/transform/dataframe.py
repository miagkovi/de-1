"""
Data transformations with pandas DataFrames.
"""
import pandas as pd

def load_dataset_to_dataframe(file_path: str) -> pd.DataFrame:
    """
    Loads a dataset from a CSV file into a pandas DataFrame.
    Args:
        file_path (str): The path to the CSV file.
    """
    df = pd.read_csv(file_path)
    return df