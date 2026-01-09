"""
Dataset extraction module using kagglehub.
"""

import kagglehub

def extract_dataset(handle: str, path: str) -> str:
    """
    Extracts a dataset from Kaggle using kagglehub.
    """
    return kagglehub.dataset_download(handle=handle,
                                      path=path,
                                      force_download=True)
