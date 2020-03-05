__author__ = 'v.denisov'

from dataclasses import dataclass

@dataclass
class TestsToSwagger:
    method: str = None
    path: str = None
    text: str = None

# [
#   { "method": "POST", "path": "/v1/file", "text": "5" },
#   {"method": "GET", "path": "/system/health", "text": "2" }
# ]