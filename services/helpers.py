from pathlib import Path
from datetime import datetime

def root_dir():
    return Path(__file__).parent.parent


def this_time() -> str:
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")