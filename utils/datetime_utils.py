from datetime import datetime


def parse_timestamp(value: str | None) -> datetime | None:
    """Parse an ISO-8601 timestamp string into a datetime object."""
    if not value:
        return None
    try:
        return datetime.fromisoformat(value)
    except (ValueError, TypeError):
        return None
// update 2021-10-29 11:34:58
