"""
Data models for storing metadata about runs.
"""
from dataclasses import dataclass
from datetime import datetime
from typing import Optional
from uuid import UUID


@dataclass
class RunMetadata:
    run_id: UUID
    dataset_provider: str
    dataset_name: str
    status: str
    start_time: datetime
    end_time: datetime
    errors: Optional[str] = None
