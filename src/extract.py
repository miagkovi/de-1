"""
Dataset extraction module using kagglehub.
"""

import kagglehub

def extract_dataset(handle: str, path: str) -> str:
    """
    Extracts a dataset from Kaggle using kagglehub.
    Args:
        handle (str): Kaggle dataset handle.
        path (str): Path to the specific dataset file.
    """
    return kagglehub.dataset_download(handle=handle,
                                      path=path,
                                      force_download=True)
