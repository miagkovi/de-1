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

def save_dataframe_to_csv(df: pd.DataFrame, output_path: str) -> None:
    """
    Saves the DataFrame to a CSV file.
    Args:
        df (pd.DataFrame): The DataFrame to save.
        output_path (str): The path to save the CSV file.
    """
    df.to_csv(output_path, index=False)
    return output_path

def transform_data(file_path: str, output_path: str) -> None:
    """
    Transforms the dataset by applying necessary data cleaning and formatting.
    Args:
        file_path (str): The path to the input CSV file.
        output_path (str): The path to save the transformed CSV file.
    """
    # Example transformation: Drop rows with any missing values
    df = load_dataset_to_dataframe(file_path)
    transformed_df = df.dropna()
    return save_dataframe_to_csv(transformed_df, output_path)