"""
Data transformations with pandas DataFrames.
"""
import pandas as pd
from pathlib import Path


def transform_data(file_path: str, output_path: str) -> int:
    """
    Transforms the dataset by applying necessary data cleaning and formatting.
    Args:
        file_path (str): The path to the input CSV file.
        output_path (str): The path to save the transformed CSV file.
    Returns:
        int: Number of rows in the transformed dataset.
    """
    file_path = Path(file_path)
    if not file_path.exists() or file_path.suffix != ".csv":
        raise ValueError("Invalid file path or format. Please provide a valid CSV file.")
    
    if not Path(output_path).parent.exists():
        raise ValueError("Output directory does not exist.")
    
    df = pd.read_csv(file_path)
    
    if not len(df):
        raise ValueError("Input CSV file is empty.")
    
    df = df.dropna() # Drop rows with missing values
    df = df.drop_duplicates() # Remove duplicate rows
    
    df.to_csv(output_path, index=False)
    return len(df)