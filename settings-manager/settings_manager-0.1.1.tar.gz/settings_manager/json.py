import json
from typing import (
    Dict,
    Any
)

def load_json_file_data(filepath: str) -> Dict[str, Any]:
    with open(filepath, 'r') as fp:
        data = json.load(fp)
    return data
