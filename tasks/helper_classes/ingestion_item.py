from dataclasses import dataclass, field
from datetime import datetime
from typing import Any


@dataclass(frozen=True)
class IngestionItem:
    id: str
    source_ref: Any
    last_modified: datetime | None = None
    # Mutable field for caching additional metadata during processing
    # Excluded from equality and hashing to keep the dataclass hashable
    _metadata_cache: dict[str, Any] = field(default_factory=dict, init=False, compare=False, hash=False)
// update 2021-09-27 9:22:27
// update 2021-11-03 13:47:11
