import logging
from .utils import Utils

class HeaderToLabelFilter(logging.Filter):
    def filter(self, record):
        if isinstance(record.msg, dict) and "data" in record.msg:
            record.msg["data"] = Utils.obfuscate_body(record.msg["data"])
            record.msg["data"] = Utils.obfuscate_response(record.msg["data"])
        return True
