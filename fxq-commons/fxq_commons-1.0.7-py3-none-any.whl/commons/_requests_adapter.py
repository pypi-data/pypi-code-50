from http import HTTPStatus
from typing import Dict

import requests


def _do_get_json(url, params) -> Dict:
    r = requests.get(url, params=params)
    if r.status_code != HTTPStatus.OK:
        raise Exception(f"Exception requesting JSON from {url} with params {params}")
    return r.json()
