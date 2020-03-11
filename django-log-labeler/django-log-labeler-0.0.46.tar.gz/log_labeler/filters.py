import logging

class HeaderToLabelFilter(logging.Filter):
    def filter(self, record):
        return True
