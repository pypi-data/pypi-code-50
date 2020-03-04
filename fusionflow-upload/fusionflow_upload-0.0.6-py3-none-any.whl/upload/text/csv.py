from ..table import Table

class CSVTable(Table):
    """parse csv files
    """
    def __init__(self, path, *, include_header=True, headers=None, **kwargs):
        super().__init__(**kwargs)