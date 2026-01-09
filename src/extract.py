"""
Data extraction from Kaggle.
W/o transformations.
"""

import kagglehub

def extract_dataset(dataset_name: str) -> None:
    """
    Extracts a dataset from Kaggle using kagglehub.
    """
    return kagglehub.dataset_download(dataset_name,
                                      path="CPU_benchmark_v4.csv",
                                      force_download=True)
