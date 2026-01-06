"""
Data extraction from Kaggle.
W/o transformations.
"""

import kagglehub

def extract_dataset(dataset_name: str, download_path: str) -> None:
    """
    Extracts a dataset from Kaggle and saves it to the specified download path.

    Args:
        dataset_name (str): The name of the Kaggle dataset to download (e.g., 'username/dataset-name').
        download_path (str): The local path where the dataset will be saved.
    """
    kagglehub.download_dataset(dataset_name, download_path)
    return f"{download_path}/{dataset_name.split('/')[-1]}.csv"
