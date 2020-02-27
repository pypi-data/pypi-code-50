import os
from typing import Optional

from dotenv import load_dotenv


def init() -> None:
    load_dotenv()


def get(key: str, default = None) -> Optional[str]:
    return os.getenv(key, default)


# Shortcut variables for Framework.
PIPELINE_DATABASE_URL = get('PIPELINE_DATABASE_URL')
PIPELINE_READ_ONLY_DATABASE_URL = get('PIPELINE_READ_ONLY_DATABASE_URL')
GOOGLE_STORAGE_BUCKET = get('GOOGLE_STORAGE_BUCKET')
GRPC_MAX_WORKERS = int(get('GRPC_MAX_WORKERS', 10))
