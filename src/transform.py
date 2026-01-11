"""
Data transformations with pandas DataFrames.
"""
import pandas as pd


def transform_data(file_path: str, output_path: str) -> None:
    """
    Transforms the dataset by applying necessary data cleaning and formatting.
    Args:
        file_path (str): The path to the input CSV file.
        output_path (str): The path to save the transformed CSV file.
    """
    if not file_path.endswith(".csv"):
        raise ValueError("Only CSV files are supported for transformation.")
    df = pd.read_csv(file_path)
    print("Dataframe rows before transformation: ", len(df))
    df = df.dropna() # Drop rows with missing values
    df = df.drop_duplicates() # Remove duplicate rows
    print("Dataframe rows after transformation: ", len(df))
    df.to_csv(output_path, index=False)
    return output_path