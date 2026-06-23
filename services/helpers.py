import json

from pathlib import Path
from datetime import datetime

def root_dir():
    return Path(__file__).parent.parent


def this_time() -> str:
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def json_serializer(obj):
    if isinstance(obj, datetime):
        return obj.isoformat()

    raise TypeError(f"Object of type {type(obj)} is not JSON serializable")