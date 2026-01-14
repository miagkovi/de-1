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
    status: str
    start_time: datetime
    end_time: Optional[datetime] = None
    errors: Optional[str] = None